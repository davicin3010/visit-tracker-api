run:
	docker build -t visit-tracker-api .
	docker run -p 8080:8080 visit-tracker-api

compose:
	docker-compose up --build
