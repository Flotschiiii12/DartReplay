from datetime import datetime


def calculate_buffer_offset(
    timestamp,
    buffer_timestamp
):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S.%f"
    )

    return (
        target - buffer_timestamp
    ).total_seconds()
