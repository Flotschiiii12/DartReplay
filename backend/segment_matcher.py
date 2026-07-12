from datetime import datetime
from pathlib import Path


def find_segment_for_timestamp(
    timestamp,
    segment_directory
):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    segments = sorted(
        Path(segment_directory).glob("*.mp4")
    )

    best_match = None

    for segment in segments:

        segment_time = datetime.strptime(
            segment.stem.replace(
                "segment_",
                ""
            ),
            "%Y%m%d_%H%M%S"
        )

        if segment_time <= target:
            best_match = {
                "file": str(segment),
                "timestamp": segment_time.strftime(
                    "%Y%m%d_%H%M%S"
                )
            }

    return best_match


def find_previous_segment(
    timestamp,
    segment_directory
):

    current = find_segment_for_timestamp(
        timestamp,
        segment_directory
    )

    if not current:
        return None

    segments = sorted(
        Path(segment_directory).glob("*.mp4")
    )

    current_file = current["file"]

    previous = None

    for segment in segments:

        if str(segment) == current_file:
            return previous

        previous = {
            "file": str(segment),
            "timestamp": segment.stem.replace(
                "segment_",
                ""
            )
        }

    return None
