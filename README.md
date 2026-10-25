# LabTrack — Student Lab & Assignment Tracker

LabTrack is a Flask-based web application for tracking student lab work and assignments. This project was used to demonstrate a Continuous Integration and Continuous Deployment (CI/CD) pipeline for the Cloud Computing and DevOps CCA2 assignment.

## Project Overview

The application provides a dashboard for viewing assignment information and tracking completion status. It also exposes a health endpoint to verify that the application is running.

## Technology Stack

- **Application:** Python and Flask
- **Version Control:** Git and GitHub
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Container Registry:** Docker Hub
- **Orchestration:** Kubernetes using Minikube
- **Infrastructure:** AWS EC2
- **Testing:** Python unittest

## Repository Structure

```text
CCA2-StudentApp/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── tests/
│   └── test_app.py
├── templates/
│   └── index.html
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

## CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. **Checkout:** Retrieves the latest source code from the GitHub `main` branch.
2. **Build and Test:** Installs the required dependencies and runs the application tests.
3. **Docker Build:** Builds a container image for LabTrack.
4. **Push Image:** Publishes the image to Docker Hub using credentials stored securely in Jenkins.
5. **Minikube Deployment:** Applies the Kubernetes Deployment and Service manifests and deploys the updated image.
6. **Verification:** Checks the deployment, pods, services, and application health endpoint.

## Deployment Configuration

- **Jenkins Job:** `labtrack-pipeline`
- **Container Registry:** Docker Hub
- **Image Repository:** `arushsinha/labtrack`
- **Kubernetes Deployment:** `labtrack`
- **Kubernetes Service:** `labtrack`
- **Service Type:** NodePort
- **Container Port:** `5000`
- **NodePort:** `30080`
- **Cluster:** Minikube hosted on AWS EC2

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/arushsinha896-cmd/CCA2-StudentApp.git
cd CCA2-StudentApp
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### 5. Run the tests

```bash
python -m unittest discover -s tests -v
```

## Health Check

The application provides a health endpoint:

```text
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "version": "2"
}
```

The version shown by the endpoint can change when a new application version is deployed.

## Demonstration of CI/CD

The pipeline was tested by making a source-code change, committing it to GitHub, and running the Jenkins pipeline again. The updated application was deployed to Kubernetes and verified through the health endpoint.

The project demonstrated source-code management, automated testing, Docker image creation and publication, Kubernetes deployment, and post-deployment verification.

## Cleanup

The AWS EC2 infrastructure used for the demonstration was terminated after testing. The repository contains the source code and configuration files needed to review the project and reproduce the deployment with suitable infrastructure and credentials.

## Author

**Arush Sinha**

B.Tech Computer Science and Engineering  
MIT World Peace University, Pune
