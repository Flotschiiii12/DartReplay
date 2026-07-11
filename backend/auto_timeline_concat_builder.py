from pathlib import Path


def build_concat_file():

    clips = sorted(
        Path("/opt/dartreplay/temp/timeline").glob(
            "clip_*.mp4"
        )
    )

    concat_file = (
        "/opt/dartreplay/temp/timeline/auto_concat.txt"
    )

    with open(concat_file, "w") as file:

        for clip in clips:

            file.write(
                f"file '{clip}'\n"
            )

    return concat_file


if __name__ == "__main__":

    print(
        build_concat_file()
    )
