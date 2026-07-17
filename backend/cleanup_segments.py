from pathlib import Path

MAX_SEGMENTS = 30

for segment_dir in [
    Path("/opt/dartreplay/ts_ring/player"),
    Path("/opt/dartreplay/ts_ring/board")
]:

    files = sorted(
        segment_dir.glob("*.mp4"),
        key=lambda f: f.stat().st_mtime
    )

    original_count = len(files)

    while len(files) > MAX_SEGMENTS:
        oldest = files.pop(0)

        print(
            f"Lösche: {oldest}"
        )

        oldest.unlink()

    print(
        f"{segment_dir.name}: "
        f"{original_count} -> {len(files)}"
    )
