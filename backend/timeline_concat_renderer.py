import subprocess

from datetime import datetime

from timeline_concat_builder import build_concat_file


def render_tv_replay():

    concat_file = build_concat_file()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    output = (
        f"/opt/dartreplay/replays/"
        f"tv_replay_{timestamp}.mp4"
    )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            concat_file,
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "23",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            output
        ]
    )

    print("✅ TV Replay erstellt")
    print(output)


if __name__ == "__main__":
    render_tv_replay()
