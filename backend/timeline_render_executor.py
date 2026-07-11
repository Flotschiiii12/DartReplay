import subprocess

from timeline_video_builder import build_video_jobs
from multicam_segment_matcher import get_segments
from timeline_engine import get_latest_180_timeline


def execute_jobs():

    timeline = get_latest_180_timeline()

    if not timeline:
        print("Keine Timeline gefunden")
        return

    timestamp = timeline["throw_1"].split(".")[0]

    jobs = build_video_jobs()

    if not jobs:
        print("Keine Jobs gefunden")
        return

    segments = get_segments(timestamp)

    if not segments:
        print("Keine Segmente gefunden")
        return

    for job in jobs:

        source = (
            segments["player"]["file"]
            if job["camera"] == "player"
            else segments["board"]["file"]
        )

        print(
            f"Render {job['camera']} -> {job['output']}"
        )

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                source,
                "-ss",
                "5",
                "-t",
                str(job["duration"]),
                "-c",
                "copy",
                job["output"]
            ]
        )

    print("✅ Timeline Clips erstellt")


if __name__ == "__main__":
    execute_jobs()
