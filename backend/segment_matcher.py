from datetime import datetime

from segment_index import get_segments


def find_segment_for_timestamp(timestamp):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    best_match = None

    for segment in get_segments():

        segment_time = datetime.strptime(
            segment["timestamp"],
            "%Y%m%d_%H%M%S"
        )

        if segment_time <= target:
            best_match = segment

    return best_match


if __name__ == "__main__":

    test_time = input(
        "Timestamp (YYYY-MM-DD HH:MM:SS): "
    )

    print(
        find_segment_for_timestamp(
            test_time
        )
    )
