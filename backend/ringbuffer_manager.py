import time
import subprocess

while True:

    subprocess.run(
        [
            "python3",
            "/opt/dartreplay/backend/cleanup_segments.py"
        ]
    )

    time.sleep(60)
