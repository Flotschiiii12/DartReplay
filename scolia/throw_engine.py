from datetime import datetime

current_visit = []

while True:
    dart = input("Dartwert: ")

    try:
        dart = int(dart)
    except ValueError:
        continue

    current_visit.append(dart)

    print(f"Wurf gespeichert: {dart}")

    if len(current_visit) == 3:
        visit_total = sum(current_visit)

        print(f"Visit Total: {visit_total}")

        if visit_total == 180:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("🔥 180 erkannt!")
            print(f"Zeitpunkt: {timestamp}")

        current_visit = []
