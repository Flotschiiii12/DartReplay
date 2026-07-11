import subprocess

from segment_finder import get_latest_segment


segment = get_latest_segment()

if not segment:
    print("Kein Segment gefunden")
    exit()

output = "/opt/dartreplay/replays/auto_replay.mp4"

subprocess.run([
    "ffmpeg",
    "-y",
    "-i",
    segment,
    "-ss",
    "5",
    "-t",
    "15",
    "-c",
    "copy",
    output
])

print("✅ Auto Replay erstellt")
