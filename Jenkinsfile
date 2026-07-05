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
        
        stage('Containerize') {
        steps {
            echo 'Building Docker Image...'
            bat 'docker build -t devsecops-app:latest .'
            
            echo 'Verifying the built image...'
            bat 'docker images devsecops-app'
        }
    }
    }
}