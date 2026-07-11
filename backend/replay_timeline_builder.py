from timeline_engine import get_latest_180_timeline


def build_timeline():

    timeline_data = get_latest_180_timeline()

    if not timeline_data:
        return None

    delta_1 = timeline_data["delta_1"]
    delta_2 = timeline_data["delta_2"]

    return [
        {
            "camera": "player",
            "event": "pre_throw_1",
            "duration": max(2, delta_1)
        },

        {
            "camera": "board",
            "event": "throw_1",
            "timestamp": timeline_data["throw_1"],
            "duration": 2
        },

        {
            "camera": "player",
            "event": "pre_throw_2",
            "duration": max(2, delta_2)
        },

        {
            "camera": "board",
            "event": "throw_2",
            "timestamp": timeline_data["throw_2"],
            "duration": 2
        },

        {
            "camera": "player",
            "event": "pre_throw_3",
            "duration": 3
        },

        {
            "camera": "board",
            "event": "throw_3",
            "timestamp": timeline_data["throw_3"],
            "duration": 4
        },

        {
            "camera": "player",
            "event": "reaction",
            "duration": 8
        }
    ]


if __name__ == "__main__":
    print(build_timeline())
