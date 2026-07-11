from sqlalchemy import text

from database import engine


def get_highlight_metadata(trigger_id):

    with engine.connect() as connection:

        result = connection.execute(
            text("""
                SELECT
                    rt.id AS trigger_id,
                    h.highlight_type,
                    h.created_at
                FROM replay_triggers rt
                JOIN highlights h
                    ON h.id = rt.highlight_id
                WHERE rt.id = :trigger_id
            """),
            {"trigger_id": trigger_id}
        )

        row = result.fetchone()

        if not row:
            return None

        return {
            "trigger_id": row.trigger_id,
            "highlight_type": row.highlight_type,
            "created_at": row.created_at
        }
