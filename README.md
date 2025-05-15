📝 Text Summarizer App
This is a web application built with FastAPI that uses Hugging Face Transformers to generate summaries from long pieces of text. The app includes everything you need for development and deployment: Docker support, CI/CD with GitHub Actions, automated testing using pytest, and code quality checks via pre-commit hooks.

🚀 Features
Automatically summarizes lengthy text using the facebook/bart-large-cnn model.

FastAPI-based backend, with HTML templates rendered using Jinja2.

Clean and responsive front-end styled with CSS.

Fully containerized using Docker for easy deployment.

CI pipeline integrated with GitHub Actions for continuous testing and linting.

Code quality enforced through pre-commit hooks.

Unit tests written with pytest to ensure app functionality.

📦 Getting Started
🔧 Requirements
Before you begin, make sure you have the following installed:

Docker and Docker Compose

Python 3.10 or higher

pre-commit CLI tool

🐳 Running the App with Docker
To start the application using Docker Compose:

bash
Copy
Edit
docker-compose up --build
Then, open your browser and go to: http://localhost:8000

🧪 Running the App Locally (Without Docker)
If you prefer to run it without Docker:

bash
Copy
Edit
pip install -r requirements.txt
uvicorn app.main:app --reload
🧬 Project Structure
bash
Copy
Edit
health_checkup_project/
├── app/
│   ├── __init__.py           # Marks app as a Python package
│   ├── main.py               # FastAPI app: routes, request handling
│   ├── vital.py              # Functions to evaluate vital signs
│   └── config.py             # App configuration & environment settings
│
├── templates/
│   ├── pro.html              # HTML form for user input
│   └── results.html          # HTML page showing results
│
├── static/
│   └── look.css              # CSS styling for pages
│
├── tests/
│   ├── __init__.py           # Marks tests as a Python package
│   └── test_app.py           # Unit/integration tests for FastAPI app
│
├── .env                      # Environment variables (e.g., secrets)
├── requirements.txt          # Python dependencies list
├── Dockerfile                # Docker image build instructions
├── docker-compose.yml        # Docker Compose config for multi-container setups
├── .pre-commit-config.yml    # Git pre-commit hooks config (linting, formatting)
├── .gitignore                # Files/folders for Git to ignore
└── README.md                 # Project overview & usage instructions

🔑 Environment Configuration
Your .env file should include:

ini
Copy
Edit
MODEL_NAME=facebook/bart-large-cnn
🧪 Running Tests
To execute the tests, simply run:

bash
Copy
Edit
pytest
Tests cover:

Loading the homepage correctly

Producing a summary when given a long input text

✅ Using Pre-commit Hooks
To ensure code quality, use pre-commit:

bash
Copy
Edit
pip install pre-commit
pre-commit install
pre-commit run --all-files
These hooks include:

Auto-formatting with Black

Linting with Flake8

Removing unnecessary whitespace

⚙️ Continuous Integration with GitHub Actions
The CI pipeline is defined in .github/workflows/ci.yml.

It runs automatically when code is pushed or a pull request is opened on the main branch. It performs the following steps:

Sets up a Python environment

Installs dependencies

Runs tests with pytest

Executes pre-commit checks

🐳 Docker Overview
Dockerfile: Builds the app using Python and FastAPI.

docker-compose.yml: Manages the container, reads the .env file, and simplifies running everything with one command.
