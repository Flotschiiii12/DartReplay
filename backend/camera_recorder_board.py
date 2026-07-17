import subprocess
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
