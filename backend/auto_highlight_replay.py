from replay_window import get_latest_180_window
from replay_renderer import render_replay


def process_latest_highlight():

    highlight = get_latest_180_window()

    if not highlight:
        print("Kein Highlight gefunden")
        return

    print("Highlight erkannt")
    print(highlight)

    render_replay(180)

    print("✅ Replay erzeugt")


if __name__ == "__main__":
    process_latest_highlight()
