# visit-tracker-api

This is a simple FastAPI project with two endpoints:

- `POST /visit`: Increments and returns the total visit count.
- `GET /stats`: Returns system uptime, total visits, and current server time.

## 🚀 Run with Docker

```bash
make run
# or
docker-compose up --build
