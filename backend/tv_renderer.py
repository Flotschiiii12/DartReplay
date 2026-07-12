from timeline_clip_generator import generate_clip_plan


def build_render_plan():

    clips = generate_clip_plan()

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


if __name__ == "__main__":

    plan = build_render_plan()

    for step in plan:
        print(step)
