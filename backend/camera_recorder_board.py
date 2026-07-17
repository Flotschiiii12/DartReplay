import subprocess
import threading
import time
from pathlib import Path
import time

while True:
    try:
        subprocess.run([
            "ffmpeg",
            "-y",
            "-rtsp_transport", "tcp",
            "-fflags", "+genpts",
            "-i", "rtsp://admin:florian123!@192.168.2.179:554/h264Preview_01_main",
            "-vf", "scale=1280:720,fps=20",

            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "23",

            "-an",
            "-f", "segment",
            "-segment_time", "60",
            "-reset_timestamps", "1",
            "-strftime", "1",

            "/opt/dartreplay/ts_ring/board/board_%Y%m%d_%H%M%S.mp4"
        ])
    except Exception as e:
        print("BOARD ERROR:", e)

    time.sleep(5)


def cleanup_ringbuffer():
    while True:
        try:
            files = sorted(
                Path("/opt/dartreplay/ts_ring/board").glob("*.mp4"),
                key=lambda p: p.stat().st_mtime,
                reverse=True
            )

            for old_file in files[30:]:
                old_file.unlink(missing_ok=True)

        except Exception as e:
            print(f"Cleanup-Fehler: {e}")

        time.sleep(60)

threading.Thread(
    target=cleanup_ringbuffer,
    daemon=True
).start()
