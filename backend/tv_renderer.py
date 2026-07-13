from timeline_clip_generator import generate_clip_plan


def build_render_plan(timeline_data):

    clips = generate_clip_plan(timeline_data)

    if not clips:
        return None

    render_plan = []

    for clip in clips:

        render_plan.append(
            {
                "source_camera": clip["camera"],
                "duration": clip["duration"],
                "event": clip["event"],
                "timestamp": clip.get("timestamp")
            }
        )

    return render_plan
