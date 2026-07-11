from datetime import datetime, timedelta

from sqlalchemy import text

from database import engine


def parse_time(value):

    value = str(value)

    value = value.split("+")[0].strip()

    if "." in value:
        value = value[:26]

    return datetime.strptime(
        value,
        "%Y-%m-%d %H:%M:%S.%f"
    )


def get_latest_180_timeline():

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT *
                FROM throws
                ORDER BY id DESC
                LIMIT 3
            """)
        )

        throws = list(result)

        if len(throws) < 3:
            return None

        sectors = [
            throws[0].sector,
            throws[1].sector,
            throws[2].sector
        ]

        if sectors != ["T20", "T20", "T20"]:
            return None

        first_throw = parse_time(
            throws[2].detection_time
        )

        last_throw = parse_time(
            throws[0].detection_time
        )

        return {
            "first_throw": str(first_throw),
            "last_throw": str(last_throw),
            "clip_start": str(
                first_throw - timedelta(seconds=10)
            ),
            "clip_end": str(
                last_throw + timedelta(seconds=5)
            )
        }


if __name__ == "__main__":
    print(
        get_latest_180_timeline()
    )
