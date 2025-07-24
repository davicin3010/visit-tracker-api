# 🚀 visit-tracker-api

Una API ligera y dockerizada construida con FastAPI que rastrea visitas de usuarios y reporta estadísticas del sistema.  
Ideal para demostrar fundamentos de backend: endpoints, concurrencia, contenedores y rendimiento.

---

## 📦 Funcionalidades

- `POST /visit`: Incrementa y devuelve el número total de visitas  
- `GET /stats`: Devuelve el tiempo activo del servidor, el número de visitas y la hora actual  
- Contador seguro para múltiples hilos usando `threading.Lock` de Python  
- Dockerizado y expuesto en el puerto `8080`  
- Documentación Swagger generada automáticamente (`/docs`)  

---

## 🛠 Cómo ejecutar (Docker)

### Opción 1: Con Docker Compose

```bash
docker compose up --build
```

### Opción 2: Manualmente con Docker

```bash
docker build -t visit-tracker-api .
docker run -p 8080:8080 visit-tracker-api
```

Luego abre:  
👉 http://localhost:8080/docs para ver la interfaz de Swagger

---

## 🔁 Endpoints de la API

### `POST /visit`

Incrementa y devuelve el número de visitas.

**Ejemplo de respuesta:**

```json
{
  "visits": 5
}
```

---

### `GET /stats`

Devuelve estadísticas del servidor incluyendo tiempo activo, hora actual y visitas totales.

**Ejemplo de respuesta:**

```json
{
  "uptime_seconds": 120.5,
  "total_visits": 5,
  "current_time": "2025-07-22T01:00:00.123Z"
}
```

---

## 🧵 Estrategia de Concurrencia

Esta API maneja solicitudes concurrentes usando `threading.Lock`, asegurando que múltiples llamadas a `/visit` no generen condiciones de carrera al incrementar el contador.  
Elegimos locks en lugar de variables atómicas o colas asíncronas por su simplicidad y seguridad en servidores multihilo como Uvicorn.

---

## 📈 Pruebas de Rendimiento

Prueba de estrés ejecutada usando `concurrent.futures.ThreadPoolExecutor` de Python para simular solicitudes POST concurrentes a `/visit`.

**Configuración:**
- Solicitudes totales: 1000  
- Hilos concurrentes: 100  
- Máquina: Localhost (Windows, Docker Desktop)  
- Modo de API: FastAPI dockerizado corriendo sobre Uvicorn (puerto 8080)  

**Resultados:**

| Métrica                | Valor         |
|------------------------|---------------|
| ✅ Solicitudes totales  | 1000          |
| ✅ Respuestas exitosas  | 1000          |
| ❌ Respuestas fallidas  | 0             |
| ⏱️ Tiempo total         | 4.40 segundos |
| ⚡ Promedio req/seg     | ~227.3 req/s  |

Estos resultados confirman que la API maneja tráfico concurrente de forma confiable, sin pérdida de datos y con mínima latencia, gracias a la lógica segura del contador.

---

## 🚀 Preparación para Producción

Para desplegar esta API en un entorno de producción:

- Agregar logs (por ejemplo: `loguru`, `structlog`)  
- Validación de solicitudes y manejo de errores  
- Usar un proxy inverso (como Nginx o Traefik)  
- Asegurar con HTTPS (por ejemplo, certificados de Let's Encrypt)  
- Opcionalmente, persistir el contador en Redis o una base de datos  
- Desplegar en Render, Railway, AWS EC2 o GCP  

---

## 📁 Estructura del Proyecto

```
visit-tracker-api/
│
├── app/
│   ├── main.py          # Aplicación FastAPI con endpoints
│   ├── counter.py       # Contador de visitas seguro para múltiples hilos
│   └── utils.py         # Utilidades para estadísticas del sistema
│
├── tests/               # Carpeta de tests (opcional)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
├── README.md
└── .gitignore
```

---

## 👤 Autor

**David Pedemonte**  
🧪 Stack tecnológico: FastAPI · Docker · Python 3.11 · Git · REST  
🔗 GitHub: [@davicin3010](https://github.com/davicin3010)
