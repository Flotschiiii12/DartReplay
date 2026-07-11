import subprocess

from multicam_segment_matcher import get_segments

timestamp = "2026-07-11 20:40:00"

segments = get_segments(timestamp)

board_output = "/opt/dartreplay/replays/board_clip.mp4"
player_output = "/opt/dartreplay/replays/player_clip.mp4"

subprocess.run([
    "ffmpeg",
    "-y",
    "-i",
    segments["board"]["file"],
    "-ss",
    "5",
    "-t",
    "20",
    "-c",
    "copy",
    board_output
])

subprocess.run([
    "ffmpeg",
    "-y",
    "-i",
    segments["player"]["file"],
    "-ss",
    "5",
    "-t",
    "20",
    "-c",
    "copy",
    player_output
])

print("✅ Board Clip erstellt")
print("✅ Player Clip erstellt")
