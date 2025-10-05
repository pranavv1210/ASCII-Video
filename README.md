ASCII-Video — play videos in the terminal as ASCII art

A small, fun Python project that renders video frames as ASCII characters and plays them in your terminal. The script supports forcing a 16:9 output ratio, using the video's native FPS (normal speed), and a configurable character set so you can experiment with different visual styles.

Features
- Render any video file into ASCII frames and play them in the terminal
- Defaults to 16:9 output and uses the video's FPS for normal-speed playback
- Configurable terminal width, FPS override, aspect ratio, and character set
- Works on Windows (PowerShell) and other platforms (uses `cls` / `clear` internally)

Requirements
- Python 3.8+
- OpenCV for Python

Install
1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install OpenCV:

```powershell
pip install opencv-python
```

Quick start — interactive

Run the script and follow prompts:

```powershell
python .\index.py
```

Prompts you'll see:
- Enter path to video:  (e.g. `C:\path\to\video.mp4`)
- Enter terminal width (default 80):
- Enter FPS (default: use video FPS):
- Enter target aspect ratio (W:H) (default 16:9):
- Enter ASCII characters to use (leave blank for default '@%#*+=-:. '):

Quick start — non-interactive (example)

You can also import and call the helper directly (useful for quick tests):

```powershell
python -c "import sys; sys.path.insert(0, r'C:\Users\Pranav\Desktop\assci-art'); import index; index.play(r'C:\Users\Pranav\Desktop\assci-art\vid.mp4', width=100, fps=0, target_ratio=(16,9))"
```

Notes and tips
- The default character set is `@%#*+=-:. ` (darker chars first). Try other sets for different looks, for example:
  - ` .:-=+*#%@` (lighter-to-dark mapping)
  - `@#WMBRXVYIti+=;:,. ` (very dense)
  - emojis or letters (might not look consistent across terminals)
- Terminal characters are not square. The script compensates with a character-aspect correction to preserve the intended visual ratio.
- Press Ctrl+C to stop playback early.

Want more?
- I can add command-line flags (argparse) so you can pass width/fps/ratio/charset without prompts.
- I can add a small `requirements.txt` and a test that writes a few ASCII frames to text files for quick previews.

License
- MIT (feel free to adapt)

Enjoy — have fun experimenting with different character sets and sizes!