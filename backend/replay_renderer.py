import subprocess

from segment_finder import get_latest_segment


def render_replay(replay_id):

    segment = get_latest_segment()

    if not segment:
        print("Kein Segment gefunden")
        return None

    output = (
        f"/opt/dartreplay/replays/replay_{replay_id}.mp4"
    )

    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            segment,
            "-ss",
            "5",
            "-t",
            "15",
            "-c",
            "copy",
            output
        ]
    )

    return output


if __name__ == "__main__":
    print(
        render_replay(999)
    )
