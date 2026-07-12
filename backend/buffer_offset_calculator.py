from datetime import datetime


def calculate_buffer_offset(
    timestamp,
    buffer_timestamp
):

    target = datetime.strptime(
        timestamp,
        "%Y-%m-%d %H:%M:%S"
    )

    return (
        target - buffer_timestamp
    ).total_seconds()
