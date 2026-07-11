import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

board_output = f"/opt/dartreplay/captures/board/{timestamp}.jpg"
player_output = f"/opt/dartreplay/captures/player/{timestamp}.jpg"

os.system(
    f"ffmpeg -loglevel error -rtsp_transport tcp "
    f"-i 'rtsp://admin:florian123!@192.168.2.179:554/h264Preview_01_main' "
    f"-frames:v 1 {board_output}"
)

os.system(
    f"ffmpeg -loglevel error -rtsp_transport tcp "
    f"-i 'rtsp://admin:florian123!@192.168.2.178:554/h264Preview_01_main' "
    f"-frames:v 1 {player_output}"
)

print("Snapshots erstellt")
print(board_output)
print(player_output)
