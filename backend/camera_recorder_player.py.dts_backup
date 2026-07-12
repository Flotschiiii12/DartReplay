import subprocess

RTSP_URL = "rtsp://admin:florian123!@192.168.2.178:554/h264Preview_01_main"

subprocess.run([
    "ffmpeg",
    "-rtsp_transport",
    "tcp",
    "-i",
    RTSP_URL,
    "-c",
    "copy",
    "-f",
    "segment",
    "-segment_time",
    "60",
    "-strftime",
    "1",
    "/opt/dartreplay/camera-segments-player/segment_%Y%m%d_%H%M%S.mp4"
])
