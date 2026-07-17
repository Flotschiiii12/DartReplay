# 🎯 DartReplay

**Replay every great moment.**

DartReplay ist eine Plattform zur automatischen Erstellung von Dart-Replays auf Basis von SCOLIA-Daten und einem Multi-Kamera-System.

Ziel des Projekts ist eine vollautomatische Replay- und Highlight-Plattform für Dartspieler – inklusive TV-ähnlicher Regie, Highlight-Erkennung, Statistiksystem und zukünftiger Social-Media-Integration.

---

# 🚀 Features

## 🎬 Replay Engine

### Bereits umgesetzt

- ✅ Automatische Replay-Erstellung
- ✅ SCOLIA-basierte Wurferkennung
- ✅ Replay-Trigger aus SCOLIA Events
- ✅ Datenbankbasierte Replay Queue
- ✅ Zwei-Kamera-System (Player + Board)
- ✅ Mainstream-Aufzeichnung
- ✅ Audioaufzeichnung
- ✅ TS-Ringbuffer-System
- ✅ Segmentierte Videoaufnahme
- ✅ Automatisches Buffer-Matching
- ✅ Offset-basierte Segmentzuordnung
- ✅ Timeline-basierte Replay-Regie
- ✅ Automatische Clip-Erstellung
- ✅ Automatische Kameraumschaltung
- ✅ TV-Style Replay-Ausgabe
- ✅ FFmpeg Rendering Pipeline
- ✅ Mainstream Replay Pipeline
- ✅ 1280x720 Replay-Aufzeichnung
- ✅ Automatische Replay-Erstellung nach Takeouts
- ✅ Stabile Verarbeitung mehrerer schneller Visits
- ✅ Best-Match Segmentauswahl für überlappende Buffer-Dateien

### Geplante Erweiterungen

- ⏳ Celebration-Cam
- ⏳ Slow Motion Replays
- ⏳ Dynamische Replay-Regie
- ⏳ Mehrere Kameraperspektiven
- ⏳ TV-Style Übergänge
- ⏳ Automatische Highlight-Zusammenschnitte

---

## 📊 Analytics

### Geplant

- Average
- First 9 Average
- Checkout %
- High Finishes
- Legs & Sets
- Matchhistorie
- Rekorde
- Spielerstatistiken
- Persönliche Leistungsanalyse

### Hinweis

SCOLIA liefert aktuell keine automatischen Spieler- oder Matchdaten.

Für zukünftige Analytics-Funktionen wird daher eine eigene Matchengine mit eigener Datenhaltung und Statistikberechnung verwendet.

---

## 🤖 Integrationen

### Geplant

- Discord Bot
- Replay Benachrichtigungen
- Highlight Meldungen
- Replay Abruf per Slash Command
- WhatsApp Integration

---

## 📱 Social Media

### Geplant

- TikTok Export
- YouTube Shorts Export
- Automatische Highlight Videos
- Thumbnail Erstellung
- Hashtag Generierung
- Caption Generierung

---

# 🏗️ Technologie

## Backend

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- WebSockets

## Video

- FFmpeg
- RTSP Streams
- TS-Ringbuffer
- Timeline-basierte Replay-Regie
- Multi-Kamera Rendering

## Infrastruktur

- Linux VPS
- Docker
- GitHub

---

# 📂 Systemarchitektur

```text
SCOLIA
   │
   ▼
Event Verarbeitung
   │
   ▼
Replay Queue
   │
   ▼
Timeline Engine
   │
   ▼
Segment Matching
   │
   ▼
Clip Rendering
   │
   ▼
Replay Renderer
   │
   ▼
TV Replay Ausgabe
```

---

# 🚧 Projektstatus

## Infrastruktur

- ✅ VPS eingerichtet
- ✅ Ubuntu Server installiert
- ✅ Docker eingerichtet
- ✅ PostgreSQL eingerichtet
- ✅ GitHub Integration

## SCOLIA Integration

- ✅ Verbindung zu SCOLIA
- ✅ WebSocket Kommunikation
- ✅ Wurferkennung
- ✅ Wurfzeitpunkte
- ✅ Replay Trigger
- ✅ Takeout Verarbeitung

## Kamerasystem

- ✅ Board Kamera
- ✅ Player Kamera
- ✅ RTSP Streams
- ✅ Mainstream Recording
- ✅ Audioaufzeichnung
- ✅ TS-Ringbuffer
- ✅ Segmentierte Buffer-Dateien
- ✅ Automatisches Ringbuffer Cleanup

## Replay Engine

- ✅ Replay Queue
- ✅ Visit Queue System
- ✅ Timeline Engine
- ✅ Buffer Matcher
- ✅ Offset Berechnung
- ✅ Segment Matching
- ✅ Clip Erstellung
- ✅ Replay Rendering
- ✅ TV Replay Ausgabe
- ✅ Mainstream Replay Pipeline
- ✅ Automatische Replay Erstellung
- ✅ Mehrfach-Visit Verarbeitung
- ✅ Replay Stabilisierung

---

# ✅ Aktuelle Erfolge

### Replay Engine Stabilisierung

- Replay Queue erfolgreich implementiert
- Segment-Matching Fehler behoben
- Überlappende TS-Segmente korrekt aufgelöst
- Mehrfach-Visit Replay Bug behoben
- Replay Rendering Pipeline stabilisiert
- Drei schnelle Test-Visits erfolgreich als Replays verarbeitet

### Ringbuffer System

- TS-Ringbuffer Architektur eingeführt
- Automatisches Cleanup integriert
- Ringbuffer auf 30 Segmente pro Kamera begrenzt
- Speicherverbrauch deutlich reduziert

---

# 🎯 Aktueller Fokus

## Replay Fine Tuning

- Player Timing perfektionieren
- Board Timing perfektionieren
- Dartflug optimieren
- Einschlag optimieren
- Celebration-Clip nach Dart 3
- Jubel-Kamera integrieren

## Nächste Meilensteine

1. Highlight Detection Engine
2. Dashboard
3. Discord Bot
4. Highlight Bibliothek
5. Social Media Export

---

# 📡 Aktuell genutzte SCOLIA-Daten

- Sektor (S1–S20, T1–T20, D1–D20)
- X/Y Koordinaten
- Horizontaler Winkel
- Vertikaler Winkel
- Bounceout Status
- Zeitstempel
- Sektorvorschläge

---

# 🎯 Vision

DartReplay soll Dartspielern ermöglichen:

- Replays automatisch zu erzeugen
- Highlights automatisch zu erkennen
- Besondere Momente dauerhaft festzuhalten
- Spiele professionell aufzubereiten
- Persönliche Statistiken auszuwerten
- Highlight-Bibliotheken aufzubauen
- Social-Media-Inhalte automatisch zu generieren

**Replay every great moment.**
