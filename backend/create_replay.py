import subprocess

print("🎯 Erstelle Timeline...")
subprocess.run(
    [
        "python3",
        "/opt/dartreplay/backend/timeline_render_executor.py"
    ]
)

print("🎬 Erstelle Replay...")
subprocess.run(
    [
        "python3",
        "/opt/dartreplay/backend/timeline_concat_renderer.py"
    ]
)

print()
print("✅ Replay fertig")
print("/opt/dartreplay/replays/tv_replay.mp4")
