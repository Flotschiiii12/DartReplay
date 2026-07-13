# 🛠️ DartReplay Setup

## Server

### Host System

- Ubuntu Server 22.04 LTS
- Linux VPS
- SSH Zugriff eingerichtet
- GitHub Repository angebunden

### Infrastruktur

- Docker installiert
- Docker Compose installiert
- PostgreSQL eingerichtet
- Python 3 installiert
- FastAPI eingerichtet

---

# 📦 Installierte Komponenten

## Basis

- Git
- Python 3
- pip
- FFmpeg

## Container

- Docker
- Docker Compose

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- WebSockets

---

# 🗄️ Datenbank

## PostgreSQL

Status:

- ✅ PostgreSQL installiert
- ✅ PostgreSQL in Docker
- ✅ Datenbankverbindung erfolgreich
- ✅ SQLAlchemy integriert
- ✅ FastAPI erfolgreich angebunden

---

# 📡 SCOLIA Integration

## Aktueller Stand

- ✅ SCOLIA Verbindung erfolgreich
- ✅ WebSocket Client implementiert
- ✅ Access Token Authentifizierung
- ✅ Empfang von THROW_DETECTED Events
- ✅ Verarbeitung von Wurfzeitpunkten
- ✅ Replay Trigger vorbereitet

### Verfügbare Daten

- Sektor
- X/Y Koordinaten
- Horizontaler Winkel
- Vertikaler Winkel
- Bounceout Status
- Zeitstempel
- Sektorvorschläge

### Einschränkung

SCOLIA liefert aktuell keine automatischen Spieler- oder Matchdaten.

Eigene Match- und Statistikdaten müssen zukünftig separat gespeichert werden.

---

# 🎥 Kamerasystem

## Hardware

### Board Kamera

- Reolink Kamera
- RTSP Stream
- Mainstream aktiv

### Player Kamera

- Reolink Kamera
- RTSP Stream
- Mainstream aktiv

---

## Recording

### Aktueller Stand

- ✅ Zwei-Kamera-System
- ✅ Ringbuffer Recording
- ✅ Segmentierte 60-Sekunden-Dateien
- ✅ Audioaufzeichnung
- ✅ Mainstream Aufnahme
- ✅ Automatisches Transcoding
- ✅ 1280x720 Replay Buffer

### Replay Recording Pipeline

```text
Reolink Mainstream
↓
2560x1440 @ 30 FPS
↓
FFmpeg Transcoding
↓
1280x720 Replay Buffer
↓
Replay Engine
```

---

# 🎬 Replay Engine

## Aktueller Stand

- ✅ Replay Queue
- ✅ Buffer Matching
- ✅ Buffer Offset Berechnung
- ✅ Timeline Engine
- ✅ Timeline Builder
- ✅ Automatische Clip Erstellung
- ✅ Zwei-Kamera Replay System
- ✅ TV Replay Rendering
- ✅ Mainstream Replay Pipeline

### Rendering Pipeline

```text
SCOLIA Event
↓
Replay Queue
↓
Buffer Matcher
↓
Clip Erstellung
↓
Timeline Builder
↓
Timeline Rendering
↓
TV Replay Export
```

---

# 🌐 API

## Erste API

### Request

```http
GET /
```

### Antwort

```json
{
  "message": "Welcome to DartReplay"
}
```

### Dokumentation

```text
/docs
```

(Swagger UI)

---

# ✅ Infrastrukturstatus

## Server

- ✅ VPS eingerichtet
- ✅ Ubuntu installiert
- ✅ SSH Zugriff aktiv

## Software

- ✅ Git aktiv
- ✅ Docker aktiv
- ✅ Docker Compose aktiv
- ✅ Python aktiv
- ✅ FFmpeg aktiv

## Backend

- ✅ FastAPI aktiv
- ✅ API erreichbar
- ✅ Swagger verfügbar

## Datenbank

- ✅ PostgreSQL aktiv
- ✅ Verbindung erfolgreich

## Replay System

- ✅ Zwei Kameras aktiv
- ✅ Ringbuffer aktiv
- ✅ Replay Queue aktiv
- ✅ Replay Rendering aktiv
- ✅ Mainstream Recording aktiv

## Repository

- ✅ GitHub Synchronisierung aktiv
