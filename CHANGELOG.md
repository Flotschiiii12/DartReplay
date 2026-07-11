# Changelog

## v0.1.0

### Planung

- Projektname festgelegt
- VPS Architektur definiert
- Replay Konzept erstellt
- Kamerakonzept erstellt
- Roadmap erstellt
- VPS festgelegt
- 2 Reolink E1 Pro Kameras beschafft

## v0.2.0

### Infrastruktur

- Ubuntu Server eingerichtet
- Docker installiert
- Docker Compose eingerichtet
- PostgreSQL Container erstellt
- Python 3 installiert
- FastAPI installiert
- Erste API Route erstellt

## v0.2.1

- GitHub Repository mit VPS verbunden
- Infrastruktur auf GitHub veröffentlicht
- FastAPI Backend produktiv eingerichtet
- PostgreSQL Datenbank produktiv eingerichtet

- ## v0.2.2

### Datenbank

- SQLAlchemy installiert
- PostgreSQL erfolgreich mit FastAPI verbunden
- Datenbankverbindung erfolgreich getestet

### Backend

- Datenbank-Engine zentralisiert
- Testskript für Verbindungsprüfung erstellt

- ## v0.2.3

### Datenbank

- Datenbankschema erstellt
- Players-Tabelle angelegt
- Matches-Tabelle angelegt

### Backend

- SQLAlchemy-Models erstellt
- Automatische Tabellenerstellung implementiert

`
## v0.2.4

### Player API

- GET /players implementiert
- POST /players implementiert
- Swagger UI erfolgreich verwendet

### Datenbank

- Erste Testdaten gespeichert
- PostgreSQL-Schreibzugriffe getestet
- PostgreSQL-Lesezugriffe getestet

### DartReplay

- Erster Spieler erfolgreich gespeichert
- Erste Daten erfolgreich aus PostgreSQL abgerufen

- ## v0.2.5

### Match API

- GET /matches implementiert
- POST /matches implementiert
- Erste Matchdaten gespeichert
- Matchdaten erfolgreich aus PostgreSQL abrufbar

### Datenbank

- Matches-Tabelle produktiv genutzt
- Verknüpfung zwischen Spielern und Matches getestet

- ## v0.2.6

### Statistics API

- Statistik-Endpunkt (/stats) erstellt
- SQL JOIN zwischen Players und Matches implementiert
- Player- und Matchdaten erfolgreich verknüpft
- Erste Statistiken erfolgreich erzeugt und ausgegeben

### Backend

- Erweiterte Datenabfragen implementiert
- Grundlage für SCOLIA-Import vorbereitet

- ## v0.2.7

### SCOLIA Integration Foundation

- Throws-Tabelle erstellt
- Datenmodell für Wurfdaten vorbereitet
- SCOLIA-Ordnerstruktur erstellt
- Erster WebSocket-Client implementiert
- Authentifizierung über Serial Number und Access Token erfolgreich
- Verbindung zum SCOLIA Board hergestellt
- HELLO_CLIENT erfolgreich empfangen
- Ersten echten THROW_DETECTED Event empfangen
- Live-Kommunikation mit dem Board erfolgreich getestet

- ## v0.2.8

### Throw Persistence

- THROW_DETECTED Events automatisch gespeichert
- Erste echte SCOLIA-Würfe in PostgreSQL gespeichert
- Live-WebSocket-Daten erfolgreich persistiert
