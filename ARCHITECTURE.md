# 🎯 DartReplay Architecture

## System Overview


                    ┌─────────────────────┐
                    │       SCOLIA        │
                    │  THROW_DETECTED     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Event Processing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Replay Takeouts    │
                    │    PostgreSQL       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Auto Replay      │
                    │     Visit Queue     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Replay Queue     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Timeline Engine   │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼

        ┌────────────────┐         ┌────────────────┐
        │ Player Camera  │         │ Board Camera   │
        └───────┬────────┘         └───────┬────────┘
                │                          │
                ▼                          ▼

        ┌────────────────┐         ┌────────────────┐
        │ RTSP Mainstream│         │ RTSP Mainstream│
        └───────┬────────┘         └───────┬────────┘
                │                          │
                ▼                          ▼

        ┌─────────────────────────────────────────┐
        │        TS Ringbuffer Recording          │
        │     1280x720 Replay Segments            │
        └─────────────────┬───────────────────────┘
                          │
                          ▼

               ┌────────────────────┐
               │ Segment Selection  │
               │   Best Match       │
               └─────────┬──────────┘
                         │
                         ▼

               ┌────────────────────┐
               │ Offset Calculator  │
               └─────────┬──────────┘
                         │
                         ▼

               ┌────────────────────┐
               │ Clip Extraction    │
               └─────────┬──────────┘
                         │
                         ▼

               ┌────────────────────┐
               │ Timeline Renderer  │
               └─────────┬──────────┘
                         │
                         ▼

               ┌────────────────────┐
               │ Replay Renderer    │
               └─────────┬──────────┘
                         │
                         ▼

                  🎬 TV Replay Output
```

---

# Core Components

## SCOLIA Integration

### Verfügbar

- THROW_DETECTED Events
- Wurfzeitpunkte
- Sektorinformationen
- Trefferkoordinaten
- Bounceout Informationen
- Winkelinformationen
- Replay Trigger

### Einschränkungen

SCOLIA liefert aktuell keine:

- Spielerinformationen
- Matchinformationen
- Leg-/Set-Daten
- Statistiken

Für spätere Analytics-Funktionen wird eine eigene Match-Engine benötigt.

---

## Replay Engine

### Bereits umgesetzt

- Replay Takeouts
- Replay Queue
- Visit Queue
- Timeline Engine
- Segment Matching
- Best-Match Segmentauswahl
- Offset Berechnung
- Clip Rendering
- Timeline Rendering
- Replay Rendering
- TV Replay Export

### Replay Workflow


SCOLIA Event
↓
Replay Takeout
↓
Replay Queue
↓
Timeline Builder
↓
Segment Matching
↓
Best Match Selection
↓
Offset Calculation
↓
Player Clip
↓
Board Clip
↓
Timeline Rendering
↓
Replay Export


---

## Best-Match Segment Selection

### Problem

TS-Ringbuffer-Dateien überlappen sich bewusst.

Beispiel:

```text
player_194723.mp4
player_194756.mp4
player_194817.mp4
```

Ein einzelner Zeitpunkt kann gleichzeitig in mehreren Segmenten vorhanden sein.

### Lösung

```text
Timestamp
↓
Alle passenden Segmente finden
↓
Offset berechnen
↓
Segment mit kleinstem Offset auswählen
↓
Replay rendern
```

Dadurch bleiben auch mehrere schnelle Visits stabil und korrekt synchronisiert.

---

## Camera System

### Board Camera

```text
Reolink E1 Pro
↓
RTSP Mainstream
↓
FFmpeg Recorder
↓
TS Ringbuffer
```

### Player Camera


Reolink E1 Pro
↓
RTSP Mainstream
↓
FFmpeg Recorder
↓
TS Ringbuffer
```

### Eigenschaften

- Mainstream Recording
- Audioaufzeichnung
- TS Ringbuffer
- Automatische Segmentrotation
- Automatisches Cleanup
- Replay optimierte Speicherung

---

## Recording Pipeline

```text
RTSP Mainstream
2560x1440 @ 30 FPS
↓
FFmpeg Transcoding
↓
1280x720 Recording
↓
TS Ringbuffer
↓
Replay Engine
```

### Buffer Format

```text
player_YYYYMMDD_HHMMSS.mp4
board_YYYYMMDD_HHMMSS.mp4
```

### Eigenschaften

- Segmentdauer ~60 Sekunden
- Überlappende Segmente
- Automatische Rotation
- Automatisches Cleanup
- Maximal ~30 Segmente pro Kamera

---

## Backend

### Technologien

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- WebSockets
- FFmpeg

### Aufgaben

- Replay Steuerung
- Queue Verwaltung
- Event Verarbeitung
- API Bereitstellung
- Datenverarbeitung
- SCOLIA Kommunikation

---

## Database

### Bereits umgesetzt

- players
- matches
- throws
- replay_takeouts

### Geplant

- Highlight Datenbank
- Replay Metadaten
- Eigene Matchengine
- Statistiksystem

---

## Output Systems

### Bereits umgesetzt

- TV Replay Videos
- MP4 Export
- Replay Archiv
- Automatische Replay Erstellung

### Geplant

- Dashboard
- Discord Bot
- Highlight Bibliothek
- WhatsApp Integration
- TikTok Export
- YouTube Shorts Export

---

# Current Project Status

## ✅ Fertig

### Infrastruktur

- VPS
- Docker
- PostgreSQL
- GitHub Integration

### Kamerasystem

- Board Kamera
- Player Kamera
- RTSP Integration
- TS Ringbuffer
- Mainstream Recording
- Audioaufzeichnung
- Automatisches Cleanup

### Replay Engine

- Replay Queue
- Visit Queue
- Timeline Engine
- Segment Matching
- Offset Berechnung
- Clip Erstellung
- Replay Rendering
- TV Replay Ausgabe
- Multi-Visit Replay Verarbeitung

---

## 🚧 In Arbeit

### Replay Fine Tuning

- Player Timing
- Board Timing
- Dartflug Optimierung
- Einschlag Optimierung
- Celebration Clip
- Jubel Kamera

---

## ⏳ Geplant

### Highlight System

- 180 Detection
- Checkout Detection
- High Finish Detection
- Rekord Detection

### Plattform

- Dashboard
- Discord Bot
- Highlight Bibliothek
- Social Media Export

---

# Wichtige Architekturentscheidungen

## Warum TS-Ringbuffer?

- Niedrige Latenz
- Dauerhafte Aufnahme
- Schnelle Replay-Erstellung
- Entkopplung von Aufnahme und Replay-Rendering

## Warum Replay Queue?

- Replays blockieren die Aufnahme nicht
- Mehrere Replays hintereinander möglich
- Stabil bei schnellen Folge-Visits

## Warum Best-Match Segment Selection?

- Segmente überlappen sich
- Mehrere Dateien können denselben Zeitpunkt enthalten
- Höhere Replay-Genauigkeit
- Stabilere Synchronisation
