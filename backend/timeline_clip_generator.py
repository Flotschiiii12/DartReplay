from replay_timeline_builder import build_timeline


def generate_clip_plan(timeline_data):

    timeline = build_timeline(timeline_data)

    if not timeline:
        return None

    clips = []

    counter = 1

    for item in timeline:

        clips.append(
            {
                "clip_id": counter,
                "camera": item["camera"],
                "event": item["event"],
                "duration": item["duration"],
                "timestamp": item.get("timestamp")
            }
        )

        counter += 1

    return clips
