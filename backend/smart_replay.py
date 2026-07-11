from replay_window import get_latest_180_window
from replay_renderer import render_replay


def create_latest_180_replay():

    window = get_latest_180_window()

    if not window:
        print("Kein 180 erkannt")
        return

    print("180 erkannt")
    print(window)

    render_replay(180)

    print("✅ Replay erstellt")


if __name__ == "__main__":
    create_latest_180_replay()
