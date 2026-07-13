# 🎯 DartReplay Architecture

## System Overview

```text
                    ┌─────────────────┐
                    │      SCOLIA     │
                    │ Throw Detection │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Replay Trigger  │
                    │ Event Processing│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Replay Queue   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Timeline Engine │
                    └────────┬────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌────────────────┐     ┌────────────────┐
        │  Player Camera │     │  Board Camera  │
        └────────┬───────┘     └────────┬───────┘
                 │                      │
                 ▼                      ▼
        ┌────────────────┐     ┌────────────────┐
        │ RTSP Mainstream│     │ RTSP Mainstream│
        └────────┬───────┘     └────────┬───────┘
                 │                      │
                 ▼                      ▼
        ┌───────────────────────────────────────┐
        │      Ringbuffer Recording System      │
        │      60s Buffer Segments              │
        │      1280x720 Replay Buffer           │
        └────────────────┬──────────────────────┘
                         │
                         ▼
               ┌────────────────────┐
               │ Buffer File Matcher│
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
               │ Replay Concatenator│
               └─────────┬──────────┘
                         │
                         ▼
                  TV Replay Output
```

---

# Core Components

## SCOLIA Integration

### Aktuell verfügbar

- THROW_DETECTED Events
- Wurfzeitpunkte
- Sektorinformationen
- Trefferkoordinaten
- Bounceout Informationen

### Einschränkung

SCOLIA liefert aktuell keine automatischen Spieler- oder Matchdaten.

Für zukünftige Statistiken werden eigene Datenmodelle benötigt.

---

## Replay Engine

### Bereits umgesetzt

- Replay Queue
- Timeline Engine
- Timeline Builder
- Buffer File Matching
- Buffer Offset Berechnung
- Clip Erstellung
- Replay Rendering
- Zwei-Kamera Logik
- TV Replay Ausgabe

### Replay Workflow

```text
SCOLIA Event
↓
Replay Queue
↓
Timeline Builder
↓
Buffer Matcher
↓
Player Clip
↓
Board Clip
↓
Timeline Renderer
↓
Replay Export
```

---

## Camera System

### Board Camera

```text
Reolink
↓
RTSP Mainstream
↓
FFmpeg
↓
1280x720 Buffer
```

### Player Camera

```text
Reolink
↓
RTSP Mainstream
↓
FFmpeg
↓
1280x720 Buffer
```

### Eigenschaften

- Mainstream Aufnahme
- Audioaufzeichnung
- Ringbuffer
- 60 Sekunden Segmente
- Automatische Segmentrotation

---

## Recording Pipeline

### Aufnahme

```text
RTSP Mainstream
2560x1440 @ 30 FPS
↓
FFmpeg Transcoding
↓
1280x720 Buffer Recording
↓
Replay Engine
```

### Buffer System

```text
player_YYYYMMDD_HHMMSS.mp4
board_YYYYMMDD_HHMMSS.mp4
```

- Segmentlänge: 60 Sekunden
- Automatische Rotation
- Mainstream Quelle
- Replay optimierte Speicherung

---

## Backend

### Technologien

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- WebSockets

### Aufgaben

- Replay Steuerung
- Event Verarbeitung
- Queue Verwaltung
- API Bereitstellung
- Datenverarbeitung

---

## Database

### Aktueller Stand

- PostgreSQL eingerichtet
- SQLAlchemy integriert
- Datenbankanbindung vorhanden

### Geplante Inhalte

- Spieler
- Matches
- Statistiken
- Highlights
- Replay Metadaten

---

## Output Systems

### Bereits umgesetzt

- TV Replay Videos
- MP4 Export

### Geplant

- Dashboard
- Discord Bot
- Highlight Bibliothek
- WhatsApp Integration
- TikTok Export
- YouTube Shorts Export

---

# Current Project Status

## Fertig

- ✅ Infrastruktur
- ✅ Kamerasystem
- ✅ Ringbuffer
- ✅ Replay Queue
- ✅ Replay Engine
- ✅ Mainstream Recording
- ✅ Mainstream Replay Rendering
- ✅ TV Replay Export

## In Arbeit

- 🚧 Replay Timing Feintuning
- 🚧 Kamera-Regie Optimierung
- 🚧 Celebration Clips

## Geplant

- ⏳ Highlight Engine
- ⏳ Dashboard
- ⏳ Discord Bot
- ⏳ Social Media Export
- ⏳ Statistiksystem
