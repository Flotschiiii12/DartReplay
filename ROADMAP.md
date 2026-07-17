# 🎯 DartReplay Roadmap

## Phase 0 – Planung

- [x] Vision
- [x] Roadmap
- [x] VPS Entscheidung
- [x] Kamerakonzept
- [x] Reolink Kameras beschafft

---

## Phase 1 – Infrastruktur

- [x] VPS aufsetzen
- [x] Ubuntu Server installieren
- [x] Docker installieren
- [x] PostgreSQL einrichten
- [x] FastAPI Projekt starten

---

## Phase 2 – Kamerasystem

- [x] Board Cam
- [x] Player Cam
- [x] RTSP Integration
- [x] Ringpuffer
- [x] Audioaufzeichnung
- [x] Segmentierte Buffer-Dateien
- [x] Mainstream Integration
- [x] Mainstream → 720p Transcoding
- [x] Automatischer Recorder Start
- [x] TS-Ringbuffer System
- [x] Automatisches TS-Ringbuffer Cleanup

---

## Phase 3 – Replay Engine

- [x] FFmpeg Integration
- [x] Replay Queue
- [x] Buffer Matching
- [x] Buffer Offset Berechnung
- [x] Clip Erstellung
- [x] Timeline Builder
- [x] Timeline Renderer
- [x] Replay Renderer
- [x] Zwei-Kamera Replay System
- [x] TV Replay Ausgabe
- [x] Mainstream Replay Pipeline
- [x] Automatische Replay Erstellung
- [x] Replay Rendering End-to-End
- [x] Replay Visit Queue System
- [x] Datenbankbasierte Replay Trigger
- [x] TS Segment Matching
- [x] Segmentauswahl mit Best-Match Logik

---

## Phase 4 – Replay Fine Tuning

### Bereits erledigt

- [x] Grundlegende Synchronisation
- [x] Mainstream Replay erfolgreich
- [x] Segment-Matching Fehler behoben
- [x] Mainstream Buffer stabilisiert
- [x] Replay Queue Stabilisierung
- [x] Mehrfach-Visit Replay Bug behoben
- [x] Überlappende TS-Segmente korrekt aufgelöst
- [x] Replay Rendering für schnelle Folge-Visits stabilisiert

### Offen

- [ ] Player Timing perfektionieren
- [ ] Board Timing perfektionieren
- [ ] Dartflug Feintuning
- [ ] Einschlag Feintuning
- [ ] Celebration Clip nach Dart 3
- [ ] Jubel Kamera
- [ ] Slow Motion Replays
- [ ] TV-Regie Übergänge
- [ ] Dynamische Clip-Längen

---

## Phase 5 – Daten & Events

### Bereits erledigt

- [x] SCOLIA Event Verarbeitung
- [x] Wurfzeitpunkte extrahieren
- [x] Replay Trigger aus SCOLIA Daten
- [x] Automatische Visit-Erkennung
- [x] Replay Queue Speicherung

### Offen

- [ ] Eigene Matchdatenbank
- [ ] Eigene Spielerverwaltung
- [ ] Eigene Statistikberechnung
- [ ] Event Mapping erweitern

### Hinweis

SCOLIA liefert aktuell keine automatischen Spieler- oder Matchdaten.

---

## Phase 6 – Highlight Engine

- [ ] Highlight Typen definieren
- [ ] Highlight Datenbank
- [ ] Highlight API
- [ ] Highlight Detection Engine
- [ ] 180 Erkennung
- [ ] Checkout Erkennung
- [ ] High Finish Erkennung
- [ ] Rekord Erkennung

---

## Phase 7 – Dashboard

- [ ] Spielerübersicht
- [ ] Matchhistorie
- [ ] Statistiken
- [ ] Rekorde
- [ ] Replay Übersicht
- [ ] Highlight Übersicht

---

## Phase 8 – Discord Bot

- [ ] Discord Application
- [ ] Slash Commands
- [ ] Replay Abruf
- [ ] Highlight Meldungen
- [ ] Replay Benachrichtigungen
- [ ] Statistiken

---

## Phase 9 – Highlight Bibliothek

- [ ] Replay Archiv
- [ ] Suche
- [ ] Filter
- [ ] Kategorien
- [ ] Spielerfilter

---

## Phase 10 – Animationen

- [ ] 180 Animation
- [ ] Checkout Animation
- [ ] High Finish Animation
- [ ] Rekord Animation
- [ ] Automatische Zooms

---

## Phase 11 – Social Media

- [ ] TikTok Export
- [ ] YouTube Shorts Export
- [ ] Thumbnail Generator
- [ ] Caption Generator
- [ ] Hashtag Generator

---

## Phase 12 – WhatsApp

- [ ] Benachrichtigungen
- [ ] Replay Versand
- [ ] Highlight Versand

---

## Phase 13 – Monatsrückblick

- [ ] Monatsstatistiken
- [ ] Highlight Video
- [ ] Best Of
- [ ] Automatische Zusammenfassung

---

# 🎯 Version 1.0

## Bereits erreicht

- [x] Zwei Kameras
- [x] Ringpuffer
- [x] Replay Queue
- [x] Replay Engine
- [x] Automatische Replay Erstellung
- [x] TV Replay Ausgabe
- [x] Mainstream Recording
- [x] Mainstream Replay Pipeline
- [x] Datenbankbasierte Replay Trigger
- [x] TS-Ringbuffer Architektur
- [x] Stabile Mehrfach-Visit Replays

## Für Version 1.0 noch offen

- [ ] Replay Fine Tuning
- [ ] Highlight Engine
- [ ] Dashboard
- [ ] Discord Bot
- [ ] Highlight Bibliothek

---

# 🔥 Aktueller Fokus

1. Replay Timing perfektionieren
2. Celebration Clip nach Dart 3
3. Slow Motion Replays
4. Highlight Detection
5. Dashboard
6. Discord Bot

---

# ✅ Letzte große Erfolge (17.07.2026)

- Replay Queue System vollständig stabilisiert
- Bug bei mehreren schnellen Visits behoben
- TS-Segmentauswahl auf Best-Match Logik umgestellt
- Automatisches TS-Ringbuffer Cleanup repariert
- Ringbuffer von über 550 Segmenten zurück auf ~30 Segmente pro Kamera reduziert
- Drei schnelle Test-Visits erfolgreich und fehlerfrei als Replay erzeugt
