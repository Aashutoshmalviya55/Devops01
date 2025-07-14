# Devops01 : First project
This project demonstrates a complete DevOps pipeline that automates the process of building and deploying a simple **Python Flask web application** using **Docker** and **Jenkins Trigger**, integrated with **GitHub**.

## Tech Stack

- 🐍 Python Flask — Lightweight web application framework
- 🐳 Docker — Containerization platform
- 🔧 Jenkins — CI/CD automation server
- 🧠 Git & GitHub — Version control and remote repo hosting


CI/CD Flow (How it Works)
Push to GitHub triggers Jenkins via webhook.

Jenkins pulls the latest code and runs the pipeline.

Jenkins builds a Docker image and runs the container.

Flask app is deployed and accessible at http://localhost:5000.

