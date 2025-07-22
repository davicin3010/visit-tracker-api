# 🚀 visit-tracker-api

A lightweight, Dockerized API built with FastAPI that tracks user visits and reports system stats.  
Ideal for showcasing backend fundamentals: endpoints, concurrency, containerization, and performance.

---

## 📦 Features

- `POST /visit`: Increments and returns the number of total visits
- `GET /stats`: Returns server uptime, visit count, and current time
- Thread-safe counter using Python's `threading.Lock`
- Dockerized and exposed on port `8080`
- Auto-generated Swagger docs (`/docs`)

---

## 🛠 How to Run (Docker)

### Option 1: With Docker Compose

```bash
docker compose up --build
```

### Option 2: Manually with Docker

```bash
docker build -t visit-tracker-api .
docker run -p 8080:8080 visit-tracker-api
```

Then open:  
👉 http://localhost:8080/docs for the Swagger UI

---

## 🔁 API Endpoints

### `POST /visit`

Increments and returns the number of visits.

**Example response:**

```json
{
  "visits": 5
}
```

---

### `GET /stats`

Returns server statistics including uptime, current time, and total visits.

**Example response:**

```json
{
  "uptime_seconds": 120.5,
  "total_visits": 5,
  "current_time": "2025-07-22T01:00:00.123Z"
}
```

---

## 🧵 Concurrency Strategy

This API handles concurrent requests using `threading.Lock`, ensuring that multiple requests to `/visit` do not create race conditions when incrementing the counter.  
We chose locks over atomic variables or async queues for simplicity and thread safety in a multithreaded server like Uvicorn.

---

## 📈 Performance Benchmarks

Stress test executed using Python's `concurrent.futures.ThreadPoolExecutor` to simulate concurrent POST requests to `/visit`.

**Configuration:**
- Total requests: 1000
- Concurrent threads: 100
- Machine: Localhost (Windows, Docker Desktop)
- API mode: Dockerized FastAPI running on Uvicorn (port 8080)

**Results:**

| Metric                  | Value        |
|-------------------------|--------------|
| ✅ Total requests        | 1000         |
| ✅ Successful responses  | 1000         |
| ❌ Failed responses      | 0            |
| ⏱️ Time taken            | 4.40 seconds |
| ⚡ Avg req/sec (approx)  | ~227.3 req/s |

These results confirm that the API handles concurrent traffic reliably with no data loss and minimal latency, thanks to the thread-safe counter logic.

---

## 🚀 Production Readiness

To deploy this API in a production environment:

- Add logging (e.g. `loguru`, `structlog`)
- Add request validation, exception handling
- Use a reverse proxy (like Nginx or Traefik)
- Secure with HTTPS (e.g. Let's Encrypt certs)
- Optionally persist the counter in Redis or a database
- Deploy on Render, Railway, AWS EC2, or GCP

---

## 📁 Project Structure

```
visit-tracker-api/
│
├── app/
│   ├── main.py          # FastAPI app with endpoints
│   ├── counter.py       # Thread-safe visit counter
│   └── utils.py         # System stat helpers
│
├── tests/               # Test folder (optional)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
├── README.md
└── .gitignore
```

---

## 👤 Author

**David Pedemonte**  
🧪 Tech stack: FastAPI · Docker · Python 3.11 · Git · REST  
🔗 GitHub: [@davicin3010](https://github.com/davicin3010)
