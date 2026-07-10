# 🎯 DartReplay Architecture

## System Overview

```text
Data Provider
     │
     ▼
FastAPI Backend
     │
     ▼
PostgreSQL
     │
     ├── Dashboard
     ├── Discord Bot
     └── Replay Engine
                │
                ▼
            FFmpeg
                │
                ▼
        Highlight Videos
                │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
 Dashboard   Discord    TikTok
```

## Components

### Backend
- FastAPI
- Business Logic
- API Integration

### Database
- PostgreSQL
- Match Data
- Statistics
- Highlights

### Replay Engine
- Ring Buffer
- Camera Processing
- Video Generation

### Output Channels
- Dashboard
- Discord
- WhatsApp (planned)
- TikTok Ready Exports
