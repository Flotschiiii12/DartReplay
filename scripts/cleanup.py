from pathlib import Path

MAX_FILES = 20

directories = [
    "/opt/dartreplay/recordings/board",
    "/opt/dartreplay/recordings/player"
]

for directory in directories:
    files = sorted(
        Path(directory).glob("*.mp4"),
        key=lambda f: f.stat().st_mtime
    )

    while len(files) > MAX_FILES:
        oldest = files.pop(0)
        print(f"Lösche: {oldest}")
        oldest.unlink()
