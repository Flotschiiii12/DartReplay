import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: create_replay.py <timeline.json>")
    sys.exit(1)

timeline_file = sys.argv[1]

print("🎯 Erstelle Timeline...")

result = subprocess.run([
    "python3",
    "/opt/dartreplay/backend/timeline_render_executor_ts.py",
    timeline_file
])

if result.returncode != 0:
    print("❌ Timeline fehlgeschlagen")
    sys.exit(1)

print("🎬 Erstelle Replay...")

result = subprocess.run([
    "python3",
    "/opt/dartreplay/backend/timeline_concat_renderer.py"
])

if result.returncode != 0:
    print("❌ Replay fehlgeschlagen")
    sys.exit(1)

print()
print("✅ Replay fertig")
