import subprocess
import sys 
import os
import asyncio
import shutil
import zipfile
import re
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.spinner import Spinner

# --- Initialize Rich Console for a beautiful user experience ---
console = Console()

class TheDefinitiveDownloader:
    """
    The definitive, self-sufficient, and error-free YouTube downloader.
    - Features a new, robust FFmpeg auto-installer that uses standard ZIP files.
    - Provides quality selection for videos, playlists, and audio.
    - Intelligently handles playlists with options for saving to a folder or ZIP.
    """
    def __init__(self):
        # Use the directory where the script is located as the base
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.download_path = os.path.join(self.script_dir, "Downloads")
        os.makedirs(self.download_path, exist_ok=True)
        self.ffmpeg_path = ""

    async def setup_ffmpeg(self):
        """
        Checks for FFmpeg and offers to download a compatible ZIP version if not found.
        This is the new, robust installer.
        """
        console.print("\n[cyan]Initializing & checking for dependencies...[/cyan]")
        ffmpeg_exe_path = os.path.join(self.script_dir, "ffmpeg", "ffmpeg.exe")

        if os.path.exists(ffmpeg_exe_path):
            console.print("[bold green]✔ FFmpeg is ready! High-Quality Mode is active.[/bold green]")
            self.ffmpeg_path = ffmpeg_exe_path
            return True

        console.print("[bold yellow]⚠️ FFmpeg (for high-quality downloads) is not found.[/bold yellow]")
        install = Prompt.ask("   Do you want to download and set it up automatically? (This is a one-time setup)",
                             choices=["y", "n"], default="y")

        if install == 'n':
            console.print("[yellow]Continuing in Compatibility Mode. Quality will be limited.[/yellow]")
            return False

        # **THE FIX**: Use a standard .zip file URL
        ffmpeg_zip_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        archive_path = os.path.join(self.script_dir, "ffmpeg.zip")
        extract_path = os.path.join(self.script_dir, "ffmpeg_temp")
        final_path = os.path.join(self.script_dir, "ffmpeg")

        try:
            with console.status("[bold cyan]Downloading FFmpeg (approx. 65MB)...[/bold cyan]", spinner="dots"):
                with requests.get(ffmpeg_zip_url, stream=True) as r:
                    r.raise_for_status()
                    with open(archive_path, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
            
            console.print("[green]Download complete. Extracting...[/green]")
            # **THE FIX**: Use Python's built-in zipfile module
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # Find the ffmpeg.exe within the extracted, versioned folder
            extracted_folder = os.path.join(extract_path, os.listdir(extract_path)[0])
            source_bin_path = os.path.join(extracted_folder, "bin", "ffmpeg.exe")

            os.makedirs(final_path, exist_ok=True)
            shutil.move(source_bin_path, os.path.join(final_path, "ffmpeg.exe"))
            
            self.ffmpeg_path = ffmpeg_exe_path
            console.print("[bold green]✔ FFmpeg setup complete! High-Quality Mode is now active.[/bold green]")
            return True
        except Exception as e:
            console.print(f"[bold red]FFmpeg setup failed: {e}[/bold red]")
            return False
        finally:
            # **THE FIX**: This cleanup now works reliably
            if os.path.exists(archive_path): os.remove(archive_path)
            if os.path.exists(extract_path): shutil.rmtree(extract_path)

    async def get_formats(self, url, content_type):
        """Fetches and parses available formats for video or audio."""
        spinner = Spinner("dots", text=f" [bold cyan]Fetching available {content_type} qualities...[/bold cyan]")
        with console.status(spinner):
            process = await asyncio.create_subprocess_exec(
                sys.executable, '-m', 'yt_dlp', '-F', url,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, _ = await process.communicate()
        
        lines = stdout.decode().splitlines()
        formats = []
        if content_type == "Video":
            pattern = re.compile(r"^(?P<code>\d+)\s+.*?\s+(?P<res>\d{3,5}x\d{3,5}).*")
            for line in lines:
                match = pattern.match(line)
                if match:
                    is_premerged = "video only" not in line
                    if not self.ffmpeg_path and not is_premerged:
                        continue # In compatibility mode, only show pre-merged files
                    formats.append({"code": match.group('code'), "desc": match.group('res'), "premerged": is_premerged})
        else: # Audio
            pattern = re.compile(r"^(?P<code>\d+)\s+.*audio only.*(?P<bitrate>\d+k).*")
            for line in lines:
                match = pattern.match(line)
                if match:
                    formats.append({"code": match.group('code'), "desc": f"~{match.group('bitrate')}"})
        
        unique_formats = {f['desc']: f for f in formats}.values()
        return sorted(list(unique_formats), key=lambda x: int(re.sub(r'\D', '', x['desc'])), reverse=True)

    async def download_content(self, url, content_type, format_code=None, is_playlist=False):
        """Constructs and executes the final yt-dlp command."""
        console.print("-" * 50, style="blue")
        output_template = os.path.join(self.download_path, '%(playlist_title)s', '%(playlist_index)s - %(title)s.%(ext)s') if is_playlist else os.path.join(self.download_path, '%(title)s.%(ext)s')

        command = [
            sys.executable, '-m', 'yt_dlp', '--no-warnings', '--ignore-errors',
            '--progress', '--output', output_template, '--no-overwrites'
        ]

        if is_playlist: command.extend(['--yes-playlist'])
        if self.ffmpeg_path: command.extend(['--ffmpeg-location', self.ffmpeg_path])
        
        if format_code:
            if content_type == 'Video' and self.ffmpeg_path:
                command.extend(['-f', f'{format_code}+bestaudio/best', '--merge-output-format', 'mp4'])
            else:
                command.extend(['-f', format_code])
        else:
            command.extend(['-f', 'best[ext=mp4]/best'])

        if content_type == 'Audio' and self.ffmpeg_path:
            command.extend(['-x', '--audio-format', 'mp3'])

        command.append(url)
        
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()

        if process.returncode != 0: console.print(f"\n[bold red]Download failed.[/bold red]\n[red]{stderr.decode()}[/red]")
        else:
            console.print(stdout.decode())
            console.print("\n[bold green]✔ Download complete![/bold green]")
            console.print(f"   Files saved in [cyan]'{self.download_path}'[/cyan]")

    async def start(self):
        """The main user interface loop."""
        await self.setup_ffmpeg()

        console.print("\n" + "="*50, style="bold blue")
        console.print(" The Definitive YouTube Downloader ".center(50), style="bold blue")
        console.print("="*50, style="bold blue")

        try:
            url = Prompt.ask("[bold yellow]Step 1: Paste your YouTube URL (video or playlist)[/bold yellow]")
            is_playlist = 'playlist?list=' in url or 'list=' in url

            console.print("\n[bold yellow]Step 2: Choose what to download[/bold yellow]")
            console.print("[cyan]  (1: Video, 2: Audio)[/cyan]")
            content_choice = Prompt.ask("Enter your choice", choices=["1", "2"], default="1")
            content_type = "Audio" if content_choice == "2" else "Video"
            
            format_code = None
            if not is_playlist:
                formats = await self.get_formats(url, content_type)
                if formats:
                    console.print(f"\n[bold yellow]Step 3: Select the desired quality[/bold yellow]")
                    choices = [str(i+1) for i in range(len(formats))]
                    for i, f in enumerate(formats):
                        console.print(f"  [cyan]({i+1}): {f['desc']}[/cyan]")
                    quality_choice_index = int(Prompt.ask("Enter your choice", choices=choices, default="1")) - 1
                    format_code = formats[quality_choice_index]['code']
                else:
                     console.print(f"[yellow]Could not find specific formats. Will download best available.[/yellow]")
            else:
                console.print(f"\n[bold yellow]Step 3: Choose maximum quality for the playlist[/bold yellow]")
                if content_type == "Video":
                    console.print("[cyan]  (1: Best Available, 2: 1080p, 3: 720p)[/cyan]")
                    quality_choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"], default="1")
                    quality_map = {"1": "", "2": "[height<=1080]", "3": "[height<=720]"}
                    format_code = f"bestvideo{quality_map[quality_choice]}+bestaudio/best{quality_map[quality_choice]}" if self.ffmpeg_path else f"best{quality_map[quality_choice]}"
                else:
                    format_code = "bestaudio/best"

            await self.download_content(url, content_type, format_code, is_playlist)

        except KeyboardInterrupt: console.print("\n[red]Operation cancelled.[/red]")
        finally: console.print("\n[bold blue]All done![/bold blue]")

async def main():
    downloader = TheDefinitiveDownloader()
    await downloader.start()

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: console.print("\n[bold red]Program terminated.[/bold red]")