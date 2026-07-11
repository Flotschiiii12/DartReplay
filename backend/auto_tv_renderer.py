import subprocess

from auto_timeline_concat_builder import (
    build_concat_file
)

concat_file = build_concat_file()

output = (
    "/opt/dartreplay/replays/auto_tv_replay.mp4"
)

subprocess.run([
    "ffmpeg",
    "-y",
    "-f",
    "concat",
    "-safe",
    "0",
    "-i",
    concat_file,
    "-c",
    "copy",
    output
])

print("✅ Auto TV Replay erstellt")
