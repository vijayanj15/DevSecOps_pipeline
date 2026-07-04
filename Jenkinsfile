pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('DevSecOps: SAST Scan') {
            steps {
                echo 'Running Bandit Security Scanner...'
                bat 'python -m bandit -r Flask_App.py'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                bat 'python -m pytest'
            }
        }
        
        stage('Containerize (Mock)') {
            steps {
                echo 'Building Docker Image...'
                // In a fully configured Jenkins environment with Docker installed, you would run:
                // bat 'docker build -t devsecops-app:latest .'
                echo 'Dockerfile is present and ready for containerization!'
            }
        }
    }
}