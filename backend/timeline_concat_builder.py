from pathlib import Path


def build_concat_file():

    clips = sorted(
        Path(
            "/opt/dartreplay/temp/timeline"
        ).glob("clip_*.mp4")
    )

    output = (
        "/opt/dartreplay/temp/timeline/concat.txt"
    )

    with open(output, "w") as file:

        for clip in clips:

            file.write(
                f"file '{clip}'\n"
            )

    return output


if __name__ == "__main__":

    print(
        build_concat_file()
    )
