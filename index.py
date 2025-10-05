import cv2
import os
import time

def frame_to_ascii(frame, width=80, target_ratio=(16, 9), ascii_chars=None):
    """Return an ASCII-art string for `frame`.

    width: number of characters across
    target_ratio: tuple (W,H) to force output aspect (default 16:9)
    """

    # default charset: darker characters first for higher brightness mapping
    if ascii_chars is None:
        ascii_chars = "@%#*+=-:. "
    # Character cells are usually taller than they are wide; compensate
    char_aspect = 2.0

    tw, th = target_ratio
    height = max(1, int(width * (th / tw) / char_aspect))

    resized = cv2.resize(frame, (width, height))
    if resized.ndim > 2:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    else:
        gray = resized

    norm = gray / 255.0
    # build lines with comprehension for a more compact look
    lines = [
        ''.join(ascii_chars[int(px * (len(ascii_chars) - 1))] for px in row)
        for row in norm
    ]

    return '\n'.join(lines) + '\n'

def play(video_path, width=80, fps=30, target_ratio=(16, 9), ascii_chars=None):
    """Play the given video as ASCII in the terminal.

    Defaults: use video's FPS when fps==0 (normal speed), and 16:9 output.
    """
    if not os.path.exists(video_path):
        print("Error: video not found ->", video_path)
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    # prefer the video's FPS when user passes 0
    chosen_fps = video_fps if (fps == 0 or fps is None) and video_fps > 0 else (fps if fps > 0 else video_fps)
    delay = 1.0 / chosen_fps if chosen_fps > 0 else 1.0 / 30.0

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            art = frame_to_ascii(frame, width, target_ratio, ascii_chars)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(art)
            time.sleep(delay)

    except KeyboardInterrupt:
        print('\nStopped.')

    finally:
        cap.release()

if __name__ == "__main__":

    video_path = input("Enter path to video: ").strip()
    
    try:
        width = int(input("Enter terminal width (default 80): ") or "80")
    except ValueError:
        width = 80

    try:
        fps = int(input("Enter FPS (default: use video FPS): ") or "0")
    except ValueError:
        fps = 0

    ratio_input = input("Enter target aspect ratio (W:H) (default 16:9): ").strip() or "16:9"
    try:
        w_str, h_str = ratio_input.split(":")
        target_ratio = (int(w_str), int(h_str))
    except Exception:
        target_ratio = (16, 9)

    # call the shorter name — my quick local patch
    # let user override the character set
    charset_input = input("Enter ASCII characters to use (leave blank for default '@%#*+=-:. '): ")
    user_charset = charset_input.strip() or None

    play(video_path, width, fps, target_ratio, user_charset)