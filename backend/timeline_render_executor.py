import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime

from timeline_video_builder import build_video_jobs
from buffer_file_matcher import find_buffer_file
from buffer_offset_calculator import calculate_buffer_offset


def load_timeline():

    if len(sys.argv) > 1:

        with open(sys.argv[1], "r") as f:
            return json.load(f)

    return None


def get_next_buffer_file(current_file):

    current = Path(current_file)

    if current.name.startswith("player_"):
        prefix = "player"
    else:
        prefix = "board"

    files = sorted(
        Path("/opt/dartreplay/buffer").glob(
            f"{prefix}_*.mp4"
        )
    )

    files = [str(f) for f in files]

    try:
        idx = files.index(str(current))
    except ValueError:
        return current_file

    if idx + 1 < len(files):
        return files[idx + 1]

    return current_file


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

        if event in ["pre_throw_1", "throw_1"]:
            ts = timeline["throw_1"].split(".")[0]

        elif event in ["pre_throw_2", "throw_2"]:
            ts = timeline["throw_2"].split(".")[0]

        elif event == "throw_3":
            ts = timeline["throw_3"].split(".")[0]

        else:
            continue

        if job["camera"] == "player":

            match = find_buffer_file(ts, "player")

            if not match:
                print("Kein Player-Buffer gefunden")
                continue

            source = match["file"]

            offset = calculate_buffer_offset(
                ts,
                match["timestamp"]
            )

            offset = max(0, offset + 3.0)

        else:

            match = find_buffer_file(ts, "board")

            if not match:
                print("Kein Board-Buffer gefunden")
                continue

            source = match["file"]

            offset = calculate_buffer_offset(
                ts,
                match["timestamp"]
            )

            offset = max(0, offset - 0.5)

        if offset + job["duration"] > 60:

            source = get_next_buffer_file(source)
            offset = 0

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
                "-i",
                "-ss",
                str(offset),
                source,
                "-t",
                str(job["duration"]),
                "-c",
                "copy",
                job["output"]
            ],
        )

    print("✅ Timeline erstellt")


if __name__ == "__main__":
    execute_jobs()
