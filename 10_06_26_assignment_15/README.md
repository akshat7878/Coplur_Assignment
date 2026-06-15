# Dockerized Python Version Application

## Objective

This project demonstrates how to create a Dockerized Python application using the `python:3.12-slim` base image.

The application prints:

- Current Python Version
- Current Date and Time

---

## Project Structure

```text
python-version-app/
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Build Docker Image

```bash
docker build -t python-version-app .
```

---

## Run Docker Container

```bash
docker run --rm python-version-app
```

---

## Sample Output

```bash

Python Version : 3.12.11 (main, Jun  3 2025, ...)
Current Date & Time : 2026-06-15 12:05:30.123456

```

---

## Verify Image

```bash
docker images
```

---

## Verify Running Container

```bash
docker ps
```

---

## Remove Image

```bash
docker rmi python-version-app
```

---

## Author

Akshat Kumawat