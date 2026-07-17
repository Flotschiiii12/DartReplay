import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime

from timeline_video_builder import build_video_jobs
from buffer_offset_calculator import calculate_buffer_offset


def find_ts_file(timestamp, prefix):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S.%f"
    )

    files = sorted(
        Path(f"/opt/dartreplay/ts_ring/{prefix}").glob(
            f"{prefix}_*.mp4"
        )
    )

    best_match = None
    best_offset = None

    for file in files:

        try:
            file_time = datetime.strptime(
                file.stem.replace(
                    f"{prefix}_",
                    ""
                ),
                "%Y%m%d_%H%M%S"
            )
        except Exception:
            continue

        if file_time > target:
            continue

        offset = (
            target - file_time
        ).total_seconds()

        if offset > 62.5:
            continue

        probe = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                str(file)
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if probe.returncode != 0:
            print(f"[SKIP INVALID] {file}")
            continue

        if best_offset is None or offset < best_offset:
            best_offset = offset
            best_match = {
                "file": str(file),
                "timestamp": file_time
            }

    if best_match:
        print(
            f"[FIND] target={target} "
            f"file={best_match['file']} "
            f"offset={best_offset}"
        )
        return best_match

    return None

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

    for job in jobs:

        event = job["event"]


        ts = job["timestamp"]

        print("JOB_TIMESTAMP=", job["timestamp"])


        camera = job["camera"]

        match = find_ts_file(ts, camera)

        if not match:
            print(f"Kein {camera}-TS gefunden")
            continue

        offset = calculate_buffer_offset(
            ts,
            match["timestamp"]
        )

        print(
            f"EVENT={event} "
            f"TS={ts} "
            f"BASE_OFFSET={offset}"
        )

        offset = max(0, offset)

#        if camera == "board" and offset % 2 == 1:
#            offset -= 1

        if offset + job["duration"] >= 65:

            files = sorted(
                Path(
                    f"/opt/dartreplay/ts_ring/{camera}"
                ).glob(
                    f"{camera}_*.mp4"
                )
            )

            current = Path(match["file"])

            names = [str(f) for f in files]

            try:
                idx = names.index(str(current))

                if idx + 1 < len(names):
                    match["file"] = names[idx + 1]
                    offset = 0

            except Exception:
                pass

        output = job["output"]

        print(
            f"Render {camera} "
            f"{match['file']} "
            f"offset={offset}"
        )

        print(
            f"[DEBUG] camera={camera} event={event} target={ts} segment={match['file']} segment_time={match['timestamp']} offset={offset} duration={job['duration']}"
        )

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-ss",
                str(offset),
                "-i",
                match["file"],
                "-t",
                str(job["duration"]),
                "-c:v",
                "libx264",
                "-preset",
                "ultrafast",
                "-pix_fmt",
                "yuv420p",
                "-an",
                output
            ]
        )

    print("✅ TS Timeline erstellt")


if __name__ == "__main__":
    execute_jobs()
