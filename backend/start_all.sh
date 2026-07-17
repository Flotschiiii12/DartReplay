#!/bin/bash

cd /opt/dartreplay/backend

pkill -f auto_replay.py
pkill -f scolia/client.py
pkill -f camera_recorder_board.py
pkill -f camera_recorder_player.py
pkill -f ringbuffer_manager.py

pkill -f "h264Preview_01_main"
pkill -f "/opt/dartreplay/ts_ring"
pkill -f "/opt/dartreplay/buffer"

sleep 3

nohup python3 scolia/client.py > /tmp/scolia.log 2>&1 &
nohup python3 camera_recorder_board.py > /tmp/board.log 2>&1 &
nohup python3 camera_recorder_player.py > /tmp/player.log 2>&1 &
nohup python3 ringbuffer_manager.py > /tmp/ringbuffer.log 2>&1 &
nohup python3 auto_replay.py > /tmp/auto_replay.log 2>&1 &

echo "✅ Alles gestartet"
