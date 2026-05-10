# Sentence Corrector Chatbot

A simple chatbot application for correcting sentences using a backend API and a Streamlit frontend, containerized with Docker.

## Project Structure

- `backend/`: Flask API for sentence correction
- `frontend/`: Streamlit web app
- `nginx/`: Reverse proxy configuration
- `docker-compose.yml`: Docker Compose setup
- `Makefile`: Build and run commands

## Getting Started

1. Ensure Docker and Docker Compose are installed.

2. Clone the repository.

3. Run `make build` to build the images.

4. Run `make run` to start the services.

5. Access the app at http://localhost

## Usage

Enter a sentence in the frontend, and it will be corrected by the backend.