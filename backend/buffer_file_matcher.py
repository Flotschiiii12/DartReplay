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

    if len(files) > 1:
        files = files[:-1]

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

        from datetime import timedelta

        file_end = file_time + timedelta(seconds=60)

        if file_time <= target < file_end:

            best_match = {
                "file": str(file),
                "timestamp": file_time
            }

    return best_match
