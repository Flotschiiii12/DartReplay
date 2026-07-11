import subprocess

from offset_calculator import calculate_offset
from timeline_renderer import get_replay_duration


def render_precise_replay(
    replay_id,
    timestamp
):

    data = calculate_offset(
        timestamp
    )

    if not data:
        print("Kein Segment gefunden")
        return None

    duration = get_replay_duration()

    if not duration:
        duration = 25

    output = (
        f"/opt/dartreplay/replays/precise_{replay_id}.mp4"
    )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            data["segment"],
            "-ss",
            str(max(0, int(data["offset"]) - 15)),
            "-t",
            str(duration),
            "-c",
            "copy",
            output
        ]
    )

    print(f"✅ {output}")

    return output


if __name__ == "__main__":

    render_precise_replay(
        999,
        "2026-07-11 19:38:40"
    )
