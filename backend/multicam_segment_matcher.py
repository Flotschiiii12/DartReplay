from datetime import datetime, timedelta

from segment_matcher import find_segment_for_timestamp


PLAYER_SEGMENT_DELAY = 0


def get_segments(timestamp):

    board = find_segment_for_timestamp(
        timestamp,
        "/opt/dartreplay/camera-segments-board"
    )

    corrected_player_time = (
        datetime.strptime(
            timestamp,
            "%Y-%m-%d %H:%M:%S"
        )
        - timedelta(seconds=PLAYER_SEGMENT_DELAY)
    )

    player = find_segment_for_timestamp(
        corrected_player_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "/opt/dartreplay/camera-segments-player"
    )

    return {
        "board": board,
        "player": player
    }


if __name__ == "__main__":

    timestamp = input("Timestamp: ")

    print(
        get_segments(timestamp)
    )
