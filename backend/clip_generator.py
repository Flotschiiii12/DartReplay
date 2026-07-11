import subprocess

SOURCE_FILE = "/opt/dartreplay/camera-segments/segment_20260711_193644.mp4"

OUTPUT_FILE = "/opt/dartreplay/replays/manual_replay.mp4"

subprocess.run(
    [
        "ffmpeg",
        "-y",
        "-i",
        SOURCE_FILE,
        "-ss",
        "10",
        "-t",
        "15",
        "-c",
        "copy",
        OUTPUT_FILE
    ]
)

print("✅ Replay erstellt")
