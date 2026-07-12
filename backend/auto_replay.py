import time
import subprocess
from pathlib import Path

from timeline_engine import get_latest_180_timeline

last_throw = None

while True:

    try:

        timeline = get_latest_180_timeline()

        if timeline:

            current_throw = timeline["throw_3"]

            if current_throw != last_throw:

                last_throw = current_throw

                print("🎯 Neuer Visit erkannt")

                print("⏳ Warte 70 Sekunden auf fertige Segmente...")
                time.sleep(70)

                for file in Path(
                    "/opt/dartreplay/temp/timeline"
                ).glob("clip_*.mp4"):
                    file.unlink(missing_ok=True)

                concat_file = Path(
                    "/opt/dartreplay/temp/timeline/concat.txt"
                )

                concat_file.unlink(
                    missing_ok=True
                )

                subprocess.run(
                    [
                        "python3",
                        "/opt/dartreplay/backend/timeline_render_executor.py"
                    ]
                )

                subprocess.run(
                    [
                        "python3",
                        "/opt/dartreplay/backend/timeline_concat_renderer.py"
                    ]
                )

                print("✅ Replay erstellt")

    except Exception as e:
        print(e)

    time.sleep(5)
