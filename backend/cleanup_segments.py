from pathlib import Path

SEGMENT_DIR = Path(
    "/opt/dartreplay/camera-segments"
)

MAX_SEGMENTS = 30

files = sorted(
    SEGMENT_DIR.glob("*.mp4"),
    key=lambda f: f.stat().st_mtime
)

while len(files) > MAX_SEGMENTS:

    oldest = files.pop(0)

    print(
        f"Lösche: {oldest.name}"
    )

    oldest.unlink()

print(
    f"Aktuelle Segmente: {len(files)}"
)
