# 🎯 DartReplay Architecture

                  Data Provider
                        │
                        ▼
                  FastAPI Backend
                        │
                        ▼
                   PostgreSQL
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Dashboard      Discord Bot     WhatsApp
                        │
                        ▼
                 Replay Engine
                        │ 
              ┌─────────┴─────────┐
              ▼                   ▼
         Board Cam          Player Cam
                        │
                        ▼
                     FFmpeg
                        │
                        ▼
                 Highlight Video
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      Dashboard     Discord       TikTok
