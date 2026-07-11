import subprocess

from multicam_segment_matcher import get_segments


def extract_clips(timestamp):

    segments = get_segments(timestamp)

    if not segments:
        return None

    board_clip = (
        "/opt/dartreplay/temp/timeline/board_test.mp4"
    )

    player_clip = (
        "/opt/dartreplay/temp/timeline/player_test.mp4"
    )

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        segments["board"]["file"],
        "-ss",
        "5",
        "-t",
        "5",
        "-c",
        "copy",
        board_clip
    ])

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i",
        segments["player"]["file"],
        "-ss",
        "5",
        "-t",
        "5",
        "-c",
        "copy",
        player_clip
    ])

    return {
        "board": board_clip,
        "player": player_clip
    }


if __name__ == "__main__":

    result = extract_clips(
        "2026-07-11 20:40:00"
    )

    print(result)
