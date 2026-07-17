import json
import subprocess
import time
from pathlib import Path
from datetime import datetime

from timeline_engine import get_latest_180_timeline

QUEUE_DIR = Path("/opt/dartreplay/replay_queue")

seen_throws = set()

while True:

    try:

        timeline = get_latest_180_timeline()

        if not timeline:
            time.sleep(2)
            continue

        throw_id = (
            timeline["throw_1"],
            timeline["throw_2"],
            timeline["throw_3"]
        )

        if throw_id not in seen_throws:

            seen_throws.add(throw_id)

            queue_file = QUEUE_DIR / (
                datetime.now().strftime(
                    "%Y%m%d_%H%M%S.json"
                )
            )

            with open(queue_file, "w") as f:
                json.dump(
                    timeline,
                    f,
                    indent=4
                )

            print(
                f"✅ Queue gespeichert: {queue_file}"
            )

            subprocess.Popen(
                [
                    "bash",
                    "-lc",
                    f"sleep 70 && python3 /opt/dartreplay/backend/create_replay.py {queue_file}"
                ]
            )

    except Exception as e:
        print(e)

    time.sleep(2)
