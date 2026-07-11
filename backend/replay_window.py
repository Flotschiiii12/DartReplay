from sqlalchemy import text

from database import engine


def get_latest_180_window():

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

        return {
            "first_throw_time": throws[2].detection_time,
            "last_throw_time": throws[0].detection_time
        }


if __name__ == "__main__":
    print(
        get_latest_180_window()
    )
