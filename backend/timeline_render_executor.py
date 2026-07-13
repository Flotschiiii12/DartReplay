import json
import sys
import subprocess

from timeline_video_builder import build_video_jobs

from buffer_file_matcher import find_buffer_file
from buffer_offset_calculator import calculate_buffer_offset


def load_timeline():

    if len(sys.argv) > 1:

        with open(sys.argv[1], "r") as f:
            return json.load(f)

    return None


def execute_jobs():

    timeline = load_timeline()

    if not timeline:
        print("Keine Timeline gefunden")
        return

    jobs = build_video_jobs(timeline)

    if not jobs:
        print("Keine Jobs gefunden")
        return

    for job in jobs:

        event = job["event"]

        if event == "pre_throw_1":
            ts = timeline["throw_1"].split(".")[0]

        elif event == "throw_1":
            ts = timeline["throw_1"].split(".")[0]

        elif event == "pre_throw_2":
            ts = timeline["throw_2"].split(".")[0]

        elif event == "throw_2":
            ts = timeline["throw_2"].split(".")[0]

        elif event == "throw_3":
            ts = timeline["throw_3"].split(".")[0]

        else:
            continue

        if job["camera"] == "player":

            match = find_buffer_file(
                ts,
                "player"
            )

            if not match:
                print("Kein Player-Buffer gefunden")
                continue

            source = match["file"]

            offset = calculate_buffer_offset(
                ts,
                match["timestamp"]
            )

            offset = max(
                0,
                offset + 3.0
            )

        else:

            match = find_buffer_file(
                ts,
                "board"
            )

            if not match:
                print("Kein Board-Buffer gefunden")
                continue

            source = match["file"]

            offset = calculate_buffer_offset(
                ts,
                match["timestamp"]
            )

            offset = max(
                0,
                offset - 0.5
            )

        print(
            f"Render {event} "
            f"{job['camera']} "
            f"{source} "
            f"offset={offset}"
        )

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-ss",
                str(offset),
                "-i",
                source,
                "-t",
                str(job["duration"]),
                "-vf",
                "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
                "-r",
                "30",
                "-c:v",
                "libx264",
                "-preset",
                "ultrafast",
                "-crf",
                "23",
                "-c:a",
                "aac",
                job["output"]
            ]
        )

    print("✅ Timeline erstellt")


if __name__ == "__main__":
    execute_jobs()
