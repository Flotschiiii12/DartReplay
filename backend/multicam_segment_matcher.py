from segment_matcher import find_segment_for_timestamp


def get_segments(timestamp):

    board = find_segment_for_timestamp(
        timestamp,
        "/opt/dartreplay/camera-segments-board"
    )

    player = find_segment_for_timestamp(
        timestamp,
        "/opt/dartreplay/camera-segments-player"
    )

    return {
        "board": board,
        "player": player
    }


if __name__ == "__main__":

    timestamp = input(
        "Timestamp: "
    )

    print(
        get_segments(timestamp)
    )
