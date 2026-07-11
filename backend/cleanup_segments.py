from pathlib import Path

segment_dir = Path("/opt/dartreplay/camera-segments")

files = sorted(
    segment_dir.glob("*.mp4"),
    key=lambda f: f.stat().st_mtime
)

keep = 30

if len(files) > keep:

    for file in files[:-keep]:
        file.unlink()
        print(f"Gelöscht: {file.name}")

else:
    print("Nichts zu löschen")
