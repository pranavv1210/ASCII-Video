ASCII-Video

---

Play videos in your terminal as live ASCII art — a small, fun Python utility for experimenting with character-based rendering.

---

This project converts video frames into ASCII characters and plays them in your terminal. It supports forcing a 16:9 output ratio, using the video's native FPS (normal speed), and a configurable character set so you can tweak the visual style.

---

Features

- Render any video file into ASCII frames and play them in the terminal
- Defaults to 16:9 output and uses the video's FPS for normal-speed playback
- Configurable terminal width, FPS override, aspect ratio, and character set
- Works on Windows (PowerShell) and other platforms (uses `cls` / `clear` internally)

---

Requirements

- Python 3.8+
- OpenCV for Python

---

Install

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install opencv-python
```


---

Quick start — interactive

Run the script and follow the prompts:

```powershell
python .\index.py
```

Prompts you'll see:
- Enter path to video (e.g. `C:\path\to\video.mp4`)
- Enter terminal width (default 80)
- Enter FPS (default: use video FPS)
- Enter target aspect ratio (W:H) (default 16:9)
- Enter ASCII characters to use (leave blank for default '@%#*+=-:. ')


---

Quick start — non-interactive (example)

You can import and call the helper directly (useful for quick tests or scripts):

```powershell
python -c "import sys; sys.path.insert(0, r'C:\Users\Pranav\Desktop\assci-art'); import index; index.play(r'C:\Users\Pranav\Desktop\assci-art\vid.mp4', width=100, fps=0, target_ratio=(16,9))"
```


---

Notes and tips

- Default charset: `@%#*+=-:. ` (darker characters map to brighter pixels). Try different sets for other looks:
  - ` .:-=+*#%@` (lighter first)
  - `@#WMBRXVYIti+=;:,. ` (very dense)
  - emojis or letters (results vary across terminals)
- Terminals use rectangular character cells. The script applies an aspect correction so the rendered output looks closer to the original aspect.
- Press Ctrl+C to stop playback early.


---

Troubleshooting

- If `cv2` is missing, install OpenCV: `pip install opencv-python`.
- On Windows, if terminal output looks clipped, increase the `width` prompt value or resize the console window.
- If pushing to your GitHub repo fails with permissions, either switch the remote to your fork/HTTPS URL or configure SSH keys (see Git/GitHub docs).


---

Want more?

- I can add command-line flags (argparse) so you can pass width/fps/ratio/charset without prompts.
- I can add a small `requirements.txt` and a test that writes a few ASCII frames to text files for quick previews.

---

License

- MIT (feel free to adapt)

Enjoy — have fun experimenting with different character sets and sizes!