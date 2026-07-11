from pathlib import Path


def get_latest_segment():

    segment_dir = Path(
        "/opt/dartreplay/camera-segments"
    )

    segments = sorted(
        segment_dir.glob("*.mp4")
    )

    if not segments:
        return None

    return str(segments[-1])


if __name__ == "__main__":

    print(
        get_latest_segment()
    )
