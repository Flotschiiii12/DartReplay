import json
import time
from pathlib import Path
from datetime import datetime

from timeline_engine import get_latest_180_timeline

QUEUE_DIR = Path("/opt/dartreplay/replay_queue")

last_throw = None

while True:

    try:

        timeline = get_latest_180_timeline()

        if not timeline:
            time.sleep(2)
            continue

        current_throw = timeline["throw_3"]

        if current_throw == last_throw:
            time.sleep(2)
            continue

        last_throw = current_throw

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

        print(f"✅ Queue gespeichert: {queue_file}")

    except Exception as e:
        print(e)

    time.sleep(2)
