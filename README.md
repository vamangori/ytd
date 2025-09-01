Ultimate YouTube Downloader 🐍
A powerful, user-friendly command-line tool built with Python to download YouTube videos, audio, and entire playlists with full control over quality. This script is designed to be a safe, ad-free, and reliable alternative to sketchy websites, featuring a modern CLI and an automatic setup process for all its dependencies.

Why This Project?
The internet is flooded with YouTube downloader websites that are often slow, filled with intrusive ads and pop-ups, and limit your download quality. This project was born out of the need for a clean, powerful, and reliable solution that puts the user in control.

This script solves the biggest problems with online downloaders:

No Ads or Sketchy Redirects: A clean, safe experience directly in your terminal.

No Quality Limitations: Download videos in their original quality, up to 4K/8K.

No Hassle with Dependencies: The script automatically handles the installation of FFmpeg, the most critical (and often trickiest) dependency for high-quality downloads.

✨ Key Features
Automatic FFmpeg Installer: On its first run, the script detects if FFmpeg is missing, asks for permission, and automatically downloads and sets it up for you. This unlocks high-quality downloads without any manual setup.

Full Video Quality Selection: For any single video, the script fetches a list of all available resolutions (e.g., 480p, 720p, 1080p, 4K) and lets you choose your preferred quality.

Smart Playlist Handling:

Automatically detects playlist URLs.

Asks for your desired maximum quality (e.g., 1080p) to apply to all videos.

Downloads and neatly organizes all files into a folder named after the playlist.

Audio Quality Selection: Choose your desired audio quality (Best, Good, Standard) to balance file size and fidelity. When FFmpeg is available, audio is saved in the universal .mp3 format.

Modern & Intuitive CLI: Built with the rich library for a beautiful, user-friendly interface with clear prompts, colors, and progress indicators.

Safe & Reliable Engine: Powered by yt-dlp, the industry-standard tool for video downloading, ensuring maximum compatibility and reliability.

🛠️ Installation & Setup
Getting started is simple. You just need to have Python 3.7+ installed on your system.

1. Clone the Repository
Open your terminal and clone this repository to your local machine.

Bash

git clone https://github.com/your-username/git-name.git
cd ultimate-youtube-downloader
2. Install Dependencies
This project's dependencies are listed in the requirements.txt file. Install them using pip:

Bash

pip install -r requirements.txt
(You will need to create a requirements.txt file with the content below.)

requirements.txt
yt-dlp
rich
requests
py7zr
🚀 How to Use
Once the setup is complete, you can run the script from your terminal.

1. Run the Script

Bash

python youtube_d.py


2. First-Time FFmpeg Setup
If you're running the script for the first time, it will check for FFmpeg. If it's not found, it will ask for your permission to download and install it automatically. It's highly recommended to press y (yes) to unlock all quality features.

3. Follow the On-Screen Prompts
The script will guide you through a simple, step-by-step process:

Step 1: Paste the YouTube URL (for a single video or a playlist).

Step 2: Choose whether you want to download Video or Audio.

Step 3: Select your desired quality from the list of available formats.



All downloaded files will be saved into a Downloads folder created in the same directory as the script.

⚙️ Tech Stack
Core Language: Python

Download Engine: yt-dlp (A feature-rich fork of youtube-dl)

CLI Interface: Rich (For beautiful and user-friendly terminal UIs)

HTTP Requests: Requests (Used for the automatic FFmpeg downloader)

Decompression: py7zr & zipfile (Used to extract the FFmpeg archive)

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

⚠️ Disclaimer
This tool is intended for personal and educational use only. Users are responsible for ensuring they comply with YouTube's terms of service and all applicable copyright laws. The developers of this tool do not condone piracy and are not responsible for any misuse of this software. Please respect the intellectual property of content creators.







