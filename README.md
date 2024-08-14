# Media Cell API

This is a simple FastAPI application that allows querying actions based on codewords. The app is Dockerized for easy deployment.

## Features

- Query actions by codeword.
- Query codewords by action ID.
- Dockerized for easy deployment.

## Requirements

- Docker
- Docker Compose (optional)

## Setup and Usage

### Build the Docker Image

To build the Docker image, run:

```bash
docker build -t media_cell_api .
```

### Run the Docker Container

To run the container on port 3000:

```bash
docker run -d -p 3000:3000 --name media_cell_container media_cell_api
```

### API Endpoints

- **Get Action ID by Codeword**

  ```
  GET /action/{codeword}
  ```

  Example:

  ```bash
  curl http://localhost:3000/action/5001
  ```

  Response:

  ```json
  {
    "codeword": 5001,
    "id": "alert"
  }
  ```

- **Get Codewords by Action ID**

  ```
  GET /codewords/{action_id}
  ```

  Example:

  ```bash
  curl http://localhost:3000/codewords/alert
  ```

  Response:

  ```json
  {
    "action_id": "alert",
    "codewords": [5001, 5003]
  }
  ```

### Stop and Remove the Container

To stop and remove the Docker container:

```bash
docker stop media_cell_container
docker rm media_cell_container
```

### Using Docker Compose

If you prefer using Docker Compose, you can start the application with:

```bash
docker-compose up --build
```

To stop the application:

```bash
docker-compose down
```

### Interactive API Documentation

FastAPI provides interactive API documentation available at:

- **Swagger UI**: `http://localhost:3000/docs`
- **ReDoc**: `http://localhost:3000/redoc`

These can be accessed once the application is running.
