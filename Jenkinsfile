/* STREAMING_CHUNK:Initializing the pipeline... */
pipeline {
agent any

stages {
    /* STREAMING_CHUNK:Configuring the Build stage... */
    stage('Install Dependencies') {
        steps {
            echo 'Installing Python dependencies...'
            bat 'pip install -r requirements.txt'
        }
    }
    
    /* STREAMING_CHUNK:Configuring the Security stage... */
    stage('DevSecOps: SAST Scan') {
        steps {
            echo 'Running Bandit Security Scanner...'
            // This scans app.py for security vulnerabilities.
            // If it finds a hardcoded password, it returns a non-zero exit code and fails the build!
            bat 'bandit -r app.py' 
        }
    }
    
    /* STREAMING_CHUNK:Configuring the Test stage... */
    stage('Test') {
        steps {
            echo 'Running automated tests with pytest...'
            bat 'pytest test_app.py'
        }
    }
    
    /* STREAMING_CHUNK:Configuring the Containerization stage... */
    stage('Containerize (Mock)') {
        steps {
            echo 'Building Docker Image...'
            // In a fully configured Jenkins environment with Docker installed, you would run:
            // sh 'docker build -t devsecops-app:latest .'
            echo 'Dockerfile is present and ready for containerization!'
        }
    }
}


}