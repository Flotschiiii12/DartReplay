def build_timeline(timeline_data):

    if not timeline_data:
        return None

    return [

        {
            "camera": "player",
            "event": "throw_1",
            "timestamp": timeline_data["throw_1"],
            "duration": 1.0
        },

        {
            "camera": "board",
            "event": "throw_1",
            "timestamp": timeline_data["throw_1"],
            "duration": 3.0
        },

        {
            "camera": "player",
            "event": "throw_2",
            "timestamp": timeline_data["throw_2"],
            "duration": 1.0
        },

        {
            "camera": "board",
            "event": "throw_2",
            "timestamp": timeline_data["throw_2"],
            "duration": 3.0
        },

        {
            "camera": "player",
            "event": "throw_3",
            "timestamp": timeline_data["throw_3"],
            "duration": 1.0
        },

        {
            "camera": "board",
            "event": "throw_3",
            "timestamp": timeline_data["throw_3"],
            "duration": 3.0
        }

    ]
