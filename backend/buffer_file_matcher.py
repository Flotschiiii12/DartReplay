from datetime import datetime
from pathlib import Path


def find_buffer_file(
    timestamp,
    prefix
):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    files = sorted(
        Path("/opt/dartreplay/buffer").glob(
            f"{prefix}_*.mp4"
        )
    )

    best_match = None

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

        if file_time <= target:

            best_match = {
                "file": str(file),
                "timestamp": file_time
            }

    return best_match
