import subprocess

RTSP_URL = "rtsp://admin:florian123!@192.168.2.179:554/h264Preview_01_main"

subprocess.run(
    [
        "ffmpeg",
        "-rtsp_transport",
        "tcp",
        "-i",
        RTSP_URL,

        "-f",
        "segment",

        "-segment_time",
        "60",

        "-reset_timestamps",
        "1",

        "-strftime",
        "1",

        "-c",
        "copy",

        "/opt/dartreplay/camera-segments/segment_%Y%m%d_%H%M%S.mp4"
    ]
)
