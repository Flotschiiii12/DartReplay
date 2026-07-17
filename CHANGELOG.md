# Changelog

---

# v0.1.0 – Projektplanung

## Planung

- Projektname festgelegt
- VPS Architektur definiert
- Replay-Konzept erstellt
- Kamerakonzept erstellt
- Produktvision definiert
- Roadmap erstellt
- VPS als Hauptplattform festgelegt
- 2x Reolink E1 Pro Kameras beschafft

---

# v0.2.0 – Infrastruktur Foundation

## Infrastruktur

- Ubuntu Server eingerichtet
- Docker installiert
- Docker Compose eingerichtet
- PostgreSQL Container erstellt
- Python 3 installiert
- FastAPI installiert
- Erste API Route erstellt

---

# v0.2.1 – Produktivbetrieb

## Deployment

- GitHub Repository mit VPS verbunden
- Automatische Deployment-Struktur aufgebaut
- FastAPI Backend produktiv eingerichtet
- PostgreSQL produktiv eingerichtet

---

# v0.2.2 – Datenbankanbindung

## Datenbank

- SQLAlchemy installiert
- PostgreSQL erfolgreich mit FastAPI verbunden
- Datenbankverbindung getestet

## Backend

- Datenbank-Engine zentralisiert
- Verbindungstest implementiert

---

# v0.2.3 – Datenmodell

## Datenbank

- Datenbankschema erstellt
- Players-Tabelle angelegt
- Matches-Tabelle angelegt

## Backend

- SQLAlchemy Models erstellt
- Automatische Tabellenerstellung implementiert

---

# v0.2.4 – Player API

## API

- GET /players implementiert
- POST /players implementiert
- Swagger UI erfolgreich getestet

## Datenbank

- Erste Testdaten gespeichert
- Schreibzugriffe getestet
- Lesezugriffe getestet

---

# v0.2.5 – Match API

## API

- GET /matches implementiert
- POST /matches implementiert

## Datenbank

- Erste Matchdaten gespeichert
- Verknüpfung zwischen Spielern und Matches getestet

---

# v0.2.6 – Statistik Foundation

## Statistics API

- Statistik-Endpunkt erstellt
- SQL JOINs implementiert
- Spieler- und Matchdaten verknüpft
- Erste Statistiken erzeugt

## Backend

- Erweiterte Datenabfragen implementiert
- Grundlage für SCOLIA vorbereitet

---

# v0.2.7 – SCOLIA Foundation

## SCOLIA Integration

- Throws-Tabelle erstellt
- Datenmodell für Wurfdaten eingeführt
- SCOLIA Ordnerstruktur erstellt
- Erster WebSocket Client implementiert
- Authentifizierung implementiert
- Verbindung zum SCOLIA Board hergestellt
- HELLO_CLIENT erfolgreich empfangen
- Erster THROW_DETECTED Event empfangen

---

# v0.2.8 – Throw Persistence

## SCOLIA

- THROW_DETECTED Events automatisch gespeichert
- Erste echte Würfe in PostgreSQL gespeichert
- Live-WebSocket-Daten erfolgreich persistiert

---

# v0.2.9 – Throw API & Highlight Foundation

## Throw API

- GET /throws implementiert
- Echte SCOLIA-Würfe per API abrufbar

## Highlight Foundation

- GET /highlights implementiert
- Erste Highlight-Erkennung vorbereitet
- 180-Erkennung vorbereitet

---

# v0.3.0 – Kamera Integration

## Kamera Infrastruktur

- Tailscale Subnet Routing eingerichtet
- Zugriff auf lokales Kameranetz ermöglicht
- Reolink BoardCam angebunden
- Reolink PlayerCam angebunden
- RTSP Streaming integriert
- Erste Kamerabilder auf VPS gespeichert

---

# v0.4.0 – Mainstream Replay Milestone

## Replay Engine

- Replay-Synchronisation verbessert
- Player-/Board-Schnitt optimiert
- Timeline Rendering stabilisiert
- Fehlerhafte Buffer-Zuordnung behoben
- Unterstützung für 60-Sekunden Buffersegmente implementiert

## Recording

- Mainstream-Kameras integriert
- Aufnahme direkt auf 1280x720 normalisiert
- Gültige MP4-Erstellung stabilisiert
- Segmentwechsel-Probleme behoben

## Replay Quality

- Deutlich verbesserte Bildqualität
- 30 FPS Mainstream Pipeline aktiviert

---

# v0.5.0 – TV Replay Engine

## Replay System

- Zwei-Kamera Replay System entwickelt
- TV-Style Replay-Ausgabe eingeführt
- Automatische Kameraumschaltung implementiert
- Timeline-basierte Replay-Regie eingeführt
- FFmpeg Rendering Pipeline aufgebaut

## Buffer System

- Segmentierte Ringbuffer eingeführt
- Automatisches Buffer Matching implementiert
- Offset-Berechnung integriert
- Clip-Erstellung automatisiert

---

# v0.6.0 – Replay Automation

## Automatisierung

- Automatische Replay-Erstellung eingeführt
- Replay Queue System aufgebaut
- Replay Rendering End-to-End automatisiert
- SCOLIA Trigger mit Replay Engine verbunden

## Datenverarbeitung

- Wurfzeitpunkte automatisch ausgewertet
- Replay Trigger aus SCOLIA Events erzeugt

---

# v0.7.0 – Visit Replay Engine

## Replay Queue 2.0

- Datenbankbasierte Replay Queue eingeführt
- Replay Takeout Verarbeitung implementiert
- Visit Queue System entwickelt
- Mehrere Replay-Jobs hintereinander unterstützt

## Timeline System

- Timeline Builder erweitert
- Replay Timeline stabilisiert
- TS-Segment Matching integriert

---

# v0.7.1 – Replay Stabilization Update

## Replay Engine

- Fehler bei schnellen Folge-Visits analysiert
- Überlappende TS-Ringbuffer-Segmente identifiziert
- Segmentauswahl vollständig überarbeitet
- Best-Match Segmentauswahl eingeführt

## Bug Fixes

### Replay Segment Selection

Behoben:

- Falsche Segmentauswahl bei überlappenden Ringbuffer-Dateien
- Fehlerhafte Replays bei mehreren schnellen Visits
- Instabile Segmentwechsel innerhalb einer Visit

Neue Logik:

- Auswahl des Segments mit dem kleinsten Offset zum Zielzeitpunkt
- Deutlich stabilere Replay-Erstellung bei schnellen Folge-Visits

Verifikation:

- Drei schnelle Test-Visits erfolgreich verarbeitet
- Drei korrekte Replays erzeugt

## Ringbuffer

Behoben:

- Cleanup-System zeigte noch auf das alte Verzeichnis `/camera-segments`
- TS-Ringbuffer wurde nicht bereinigt

Verbessert:

- Cleanup auf `/ts_ring/player` umgestellt
- Cleanup auf `/ts_ring/board` umgestellt
- Automatische Begrenzung auf 30 Segmente pro Kamera wiederhergestellt

Ergebnis:

- Ringbuffer von über 550 Segmenten auf ~30 Segmente pro Kamera reduziert
- Speicherverbrauch deutlich reduziert
- Langzeitstabilität verbessert
