from pathlib import Path


def get_segments():

    segment_dir = Path(
        "/opt/dartreplay/camera-segments"
    )

    segments = sorted(
        segment_dir.glob("*.mp4")
    )

    result = []

    for segment in segments:

        name = segment.stem.replace(
            "segment_",
            ""
        )

        result.append(
            {
                "file": str(segment),
                "timestamp": name
            }
        )

    return result


if __name__ == "__main__":

    for segment in get_segments():
        print(segment)
