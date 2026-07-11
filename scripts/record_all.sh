#!/bin/bash

mkdir -p /opt/dartreplay/recordings/board
mkdir -p /opt/dartreplay/recordings/player

ffmpeg \
-rtsp_transport tcp \
-i 'rtsp://admin:florian123!@192.168.2.179:554/h264Preview_01_main' \
-c copy \
-f segment \
-segment_time 60 \
-reset_timestamps 1 \
/opt/dartreplay/recordings/board/board_%03d.mp4 &

BOARD_PID=$!

ffmpeg \
-rtsp_transport tcp \
-i 'rtsp://admin:florian123!@192.168.2.178:554/h264Preview_01_main' \
-c copy \
-f segment \
-segment_time 60 \
-reset_timestamps 1 \
/opt/dartreplay/recordings/player/player_%03d.mp4 &

PLAYER_PID=$!

wait $BOARD_PID
wait $PLAYER_PID
``
