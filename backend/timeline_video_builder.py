from tv_renderer import build_render_plan


def build_video_jobs(timeline_data):

    plan = build_render_plan(timeline_data)

    if not plan:
        return None

    jobs = []

    for index, clip in enumerate(plan, start=1):

        output = (
            f"/opt/dartreplay/temp/timeline/"
            f"clip_{index:03d}.mp4"
        )

        jobs.append(
            {
                "output": output,
                "camera": clip["source_camera"],
                "event": clip["event"],
                "duration": clip["duration"],
                "timestamp": clip.get("timestamp")
            }
        )

    return jobs
