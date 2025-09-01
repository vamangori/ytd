<h1 align="center"> PYTHONE </h1>

<h1 align="center">
  Ultimate YouTube Downloader 🐍
</h1>

<p align="center">
  A powerful, self-sufficient command-line tool to download YouTube videos, audio, and playlists in any quality without ads or sketchy websites.
</p>

<p align="center">
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.7+-blue.svg">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green.svg">
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
</p>

> The definitive, ad-free solution for downloading YouTube content with full control and a modern, user-friendly interface.



---

## ✨ Key Features

This script is packed with features designed for a seamless and powerful user experience.

| Feature                      | Description                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **🤖 Automatic FFmpeg Setup** | On first run, it detects if FFmpeg is missing and **installs it for you**, unlocking all high-quality formats automatically.               |
| **🎞️ Full Quality Control** | Fetches and displays all available resolutions (up to 8K) for any video, allowing you to choose the exact quality you want.          |
| **🎵 Audio Quality Selection** | Lets you choose the desired audio quality (Best, Good, etc.) to balance file size and fidelity. Saves as `.mp3` with FFmpeg.      |
| **📚 Smart Playlist Handling** | Automatically detects playlists, asks for a max quality, and saves all files into a **named folder** or a single **ZIP archive**.    |
| **💅 Modern & Intuitive CLI** | Built with `rich` for a beautiful interface with clear prompts, colors, and progress indicators that make it a pleasure to use.      |
| **🛡️ Safe & Reliable Engine** | Powered by `yt-dlp`, the industry-standard tool for video downloading, ensuring maximum compatibility and reliability.                 |

---

## 🛠️ Installation & Setup

Getting started is simple. You just need to have **Python 3.7+** installed.

#### **1. Clone the Repository**
Open your terminal and clone this repository to your local machine.

1. Clone the Repository
Open your terminal and clone this repository to your local machine.

Bash

# Make sure the repository name matches the folder name
git clone https://github.com/your-username/ultimate-youtube-downloader.git
cd ultimate-youtube-downloader
2. Install Dependencies
This project's dependencies are listed in requirements.txt. Install them in one go using pip.

Bash

pip install -r requirements.txt
<details>
<summary><b>Click to see requirements.txt content</b></summary>

Plaintext

# requirements.txt
yt-dlp
rich
requests
py7zr
</details>

🚀 How to Use
Once the setup is complete, running the script is straightforward.

1. Run the Script
Bash

# Using a standard name like 'main.py' or 'downloader.py' is a good practice
python main.py
2. First-Time FFmpeg Setup
If it's your first time, the script will check for FFmpeg. If it's not found, it will ask for your permission to download and install it automatically. It's highly recommended to press y (yes) to unlock all quality features.

3. Follow the On-Screen Prompts
The script will guide you through a simple, step-by-step process:

Step 1: Paste the YouTube URL (for a single video or a playlist).

Step 2: Choose whether you want to download Video or Audio.

Step 3: Select your desired quality from the generated list.

All downloaded files will be saved into a Downloads folder created in the same directory as the script.






