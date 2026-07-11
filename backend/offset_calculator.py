from datetime import datetime

from segment_matcher import find_segment_for_timestamp


def calculate_offset(
    timestamp,
    segment_directory
):

    segment = find_segment_for_timestamp(
        timestamp,
        segment_directory
    )

    if not segment:
        return None

    segment_time = datetime.strptime(
        segment["timestamp"],
        "%Y%m%d_%H%M%S"
    )

    target_time = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    offset = (
        target_time - segment_time
    ).total_seconds()

    return {
        "segment": segment["file"],
        "offset": offset
    }


if __name__ == "__main__":

    timestamp = input(
        "Timestamp (YYYY-MM-DD HH:MM:SS): "
    )

    print(
        calculate_offset(
            timestamp,
            "/opt/dartreplay/camera-segments-board"
        )
    )
