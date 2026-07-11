from pathlib import Path

from tv_renderer import build_render_plan


def build_video_jobs():

    plan = build_render_plan()

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
                "duration": clip["duration"]
            }
        )

    return jobs


if __name__ == "__main__":

    jobs = build_video_jobs()

    for job in jobs:
        print(job)
