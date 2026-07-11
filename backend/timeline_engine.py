from datetime import datetime, timedelta
from sqlalchemy import text
from database import engine


def parse_time(value):
    value = str(value)
    value = value.split("+")[0].strip()

    if "." in value:
        value = value[:26]

    parsed = datetime.strptime(
        value,
        "%Y-%m-%d %H:%M:%S.%f"
    )

    return parsed + timedelta(hours=2)


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

        throw_1 = parse_time(throws[2].detection_time)
        throw_2 = parse_time(throws[1].detection_time)
        throw_3 = parse_time(throws[0].detection_time)

        delta_1 = (throw_2 - throw_1).total_seconds()
        delta_2 = (throw_3 - throw_2).total_seconds()
        visit_duration = (throw_3 - throw_1).total_seconds()

        return {
            "throw_1": str(throw_1),
            "throw_2": str(throw_2),
            "throw_3": str(throw_3),
            "sector_1": throws[2].sector,
            "sector_2": throws[1].sector,
            "sector_3": throws[0].sector,
            "delta_1": delta_1,
            "delta_2": delta_2,
            "visit_duration": visit_duration,
            "clip_start": str(
                throw_1 - timedelta(seconds=15)
            ),
            "clip_end": str(
                throw_3 + timedelta(seconds=10)
            )
        }


def get_latest_180_throws():

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

        return {
            "throw_1": str(parse_time(throws[2].detection_time)),
            "throw_2": str(parse_time(throws[1].detection_time)),
            "throw_3": str(parse_time(throws[0].detection_time)),
            "sector_1": throws[2].sector,
            "sector_2": throws[1].sector,
            "sector_3": throws[0].sector
        }


if __name__ == "__main__":
    print(get_latest_180_timeline())
