from datetime import datetime, timedelta

FMT = "%Y-%m-%d %H:%M:%S.%f"

def shift(ts, seconds):
    return (
        datetime.strptime(ts, FMT)
        - timedelta(seconds=seconds)
    ).strftime(FMT)

def build_timeline(timeline_data):

    if not timeline_data:
        return None

    return [

        {
            "camera": "player",
            "event": "throw_1",
            "timestamp": shift(timeline_data["throw_1"], 0.5),
            "duration": 3.0
        },

        {
            "camera": "board",
            "event": "throw_1",
            "timestamp": shift(timeline_data["throw_1"], 0.5),
            "duration": 3.0
        },

        {
            "camera": "player",
            "event": "throw_2",
            "timestamp": shift(timeline_data["throw_2"], 0.5),
            "duration": 3.0
        },

        {
            "camera": "board",
            "event": "throw_2",
            "timestamp": shift(timeline_data["throw_2"], 0.5),
            "duration": 3.0
        },

        {
            "camera": "player",
            "event": "throw_3",
            "timestamp": shift(timeline_data["throw_3"], 0.5),
            "duration": 3.0
        },

        {
            "camera": "board",
            "event": "throw_3",
            "timestamp": shift(timeline_data["throw_3"], 0.5),
            "duration": 3.0
        }

    ]
