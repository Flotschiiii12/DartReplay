import json
import subprocess
from pathlib import Path

from sqlalchemy import text

from database import engine
from replay_metadata import get_highlight_metadata


with engine.connect() as connection:

    result = connection.execute(
        text("""
            SELECT *
            FROM replay_queue
            WHERE status = 'PENDING'
            ORDER BY id ASC
            LIMIT 1
        """)
    )

    replay = result.fetchone()

    if replay:

        connection.execute(
            text("""
                UPDATE replay_queue
                SET status = 'PROCESSING'
                WHERE id = :id
            """),
            {"id": replay.id}
        )

        connection.commit()

        metadata = get_highlight_metadata(
            replay.trigger_id
        )

        Path("/opt/dartreplay/replays").mkdir(
            parents=True,
            exist_ok=True
        )

        video_file = f"replay_{replay.id}.mp4"

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "lavfi",
                "-i",
                "color=c=black:s=1280x720:d=3",
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                f"/opt/dartreplay/replays/{video_file}"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        output = {
            "replay_id": replay.id,
            "trigger_id": replay.trigger_id,
            "status": "COMPLETED",
            "video_status": "CREATED",
            "video_file": video_file,
            "highlight": metadata
        }

        with open(
            f"/opt/dartreplay/replays/replay_{replay.id}.json",
            "w"
        ) as file:
            json.dump(
                output,
                file,
                indent=4,
                default=str
            )

        connection.execute(
            text("""
                UPDATE replay_queue
                SET status = 'COMPLETED'
                WHERE id = :id
            """),
            {"id": replay.id}
        )

        connection.commit()

        print(
            f"✅ Replay {replay.id} abgeschlossen"
        )

    else:
        print("Keine offenen Replays")
