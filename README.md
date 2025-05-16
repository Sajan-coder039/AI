# 🩺 Health Checkup App


A web application built with FastAPI that assesses vital signs such as heart rate, temperature, blood pressure, and respiration rate. It provides real-time feedback based on user input and is designed for easy development and deployment with modern tools.


---


## 🚀 Features


- User-friendly web interface for inputting vital signs (heart rate, temperature, blood pressure, respiration rate).
- FastAPI backend with HTML templates rendered via Jinja2.
- Clear, responsive UI styled with CSS.
- Dockerized for consistent deployment environments.
- Pre-configured testing setup with pytest.
- Code quality checks enforced via pre-commit hooks.
- Continuous Integration setup using GitHub Actions.


---


## 📦 Getting Started


### 🔧 Requirements


- Docker and Docker Compose (for containerized runs)
- Python 3.11+
- `pre-commit` CLI (for code quality hooks)


---


### 🐳 Running the App with Docker


Build and run the app using Docker:


```bash
docker-compose up --build
```


---
### 🧪 Running Locally (Without Docker)




Install dependencies and start the server:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9999
```
## 🧬 Project Structure
```bash
health_checkup_project/
├── app/
│   ├── __init__.py          # Marks app as a Python package
│   ├── main.py              # FastAPI app: routes, request handling
│   ├── vital.py             # Functions to evaluate vital signs
│   └── config.py            # App configuration & environment settings
│
├── templates/
│   ├── pro.html             # HTML form for user input
│   └── results.html         # HTML page showing results
│
├── static/
│   └── look.css             # CSS styling for pages
│
├── tests/
│   ├── __init__.py          # Marks tests as a Python package
│   └── test_app.py          # Unit/integration tests for FastAPI app
│
├── .env                     # Environment variables (e.g., secrets)
├── requirements.txt         # Python dependencies list
├── Dockerfile               # Docker image build instructions
├── docker-compose.yml       # Docker Compose config for multi-container setups
├── .pre-commit-config.yml   # Git pre-commit hooks config (linting, formatting)
├── .gitignore               # Files/folders for Git to ignore
└── README.md                # Project overview & usage instructions
```




### 🔑 Environment Configuration
Create a .env file with your environment variables
Add environment variables here
```bash
PORT =9999
```


### 🧪 Running Tests
Execute tests with:


```bash
pytest
```
### ✅ Code Quality with Pre-commit Hooks
Install and run pre-commit hooks to maintain code quality:


```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```


### ⚙️ Continuous Integration with GitHub Actions


CI is configured to:


- Set up Python environment 
- Install dependencies 
- Run tests with `pytest` 
- Run `pre-commit` checks 
- Trigger on pushes and pull requests to the `main` branch




### 🐳 Docker Overview
Dockerfile: Builds the app container image using Python and FastAPI.
```bash
docker build -t web .
docker run -d web
```


docker-compose.yml: Simplifies running containers and environment configuration.
```bash
docker compose up        # Run all services
docker compose down      # Stop and remove services
```
