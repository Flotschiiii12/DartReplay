from datetime import datetime, timedelta
from pathlib import Path
import subprocess


def valid_mp4(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def find_buffer_file(timestamp, prefix):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    files = sorted(
        Path("/opt/dartreplay/buffer").glob(
            f"{prefix}_*.mp4"
        ),
        reverse=True
    )

    candidates = []

    for file in files:

        try:
            file_time = datetime.strptime(
                file.stem.replace(
                    f"{prefix}_",
                    ""
                ),
                "%Y%m%d_%H%M%S"
            )

        except Exception:
            continue

        file_end = file_time + timedelta(seconds=75)

        if file_time <= target < file_end:
            candidates.append(
                (file, file_time)
            )

    for file, file_time in candidates:

        if valid_mp4(file):
            return {
                "file": str(file),
                "timestamp": file_time
            }

    return None
