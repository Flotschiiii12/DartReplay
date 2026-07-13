import subprocess
import time
from datetime import datetime

RTSP_URL = "rtsp://admin:florian123!@192.168.2.178:554/h264Preview_01_main"

while True:

    filename = datetime.now().strftime(
        "/opt/dartreplay/buffer/player_%Y%m%d_%H%M%S.mp4"
    )

    try:

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-rtsp_transport", "tcp",
                "-i", RTSP_URL,
                "-t", "60",
                "-vf", "scale=1280:720",
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-c:a", "aac",
                filename
            ],
            timeout=75
        )

    except subprocess.TimeoutExpired:
        print("Player timeout")

    time.sleep(1)
