# Microshop – Docker & Kubernetes Project

## Project Goal
This project demonstrates practical skills in:
- Docker & Docker Hub
- Kubernetes (Minikube)
- Microservices architecture

## Architecture
The application consists of three components:
- **Database:** PostgreSQL
- **Backend:** Python (Flask API)
- **Frontend:** HTML/JavaScript with Nginx

Frontend → Backend → Database

## Technologies Used
- Docker
- Docker Hub
- Kubernetes
- Python (Flask)
- PostgreSQL
- Nginx

## Docker Images
- `your-dockerhub-username/microshop-backend:v1`
- `your-dockerhub-username/microshop-frontend:v1`

## Kubernetes Deployment
```bash
kubectl apply -f k8s/
