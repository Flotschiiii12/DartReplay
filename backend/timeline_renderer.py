from datetime import datetime

from timeline_engine import get_latest_180_timeline


def get_replay_duration():

    timeline = get_latest_180_timeline()

    if not timeline:
        return None

    start = datetime.strptime(
        timeline["clip_start"],
        "%Y-%m-%d %H:%M:%S.%f"
    )

    end = datetime.strptime(
        timeline["clip_end"],
        "%Y-%m-%d %H:%M:%S.%f"
    )

    return int(
        (end - start).total_seconds()
    )


if __name__ == "__main__":
    print(
        get_replay_duration()
    )
