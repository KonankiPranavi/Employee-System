pipeline {
    agent any

    environment {
        DOCKER_USER = 'konankipranavi'
        REPO_NAME   = 'employee-system'
    }

    stages {
        stage('Checkout') {
            steps {
                // Fixed: Added your full repository URL link here
                git branch: 'main', url: 'https://github.com/KonankiPranavi/Employee-System.git'
                echo 'Employee System source code checked out successfully.'
            }
        }

        stage('Check Project Files') {
            steps {
                // Lists folder contents on your Windows local system environment
                bat 'dir'
                echo 'Project files verified successfully.'
            }
        }

        stage('Build & Push V1') {
            steps {
                echo 'Building Docker Image Version 1...'
                bat "docker build -f Dockerfile1 -t ${DOCKER_USER}/${REPO_NAME}:v1 ."
                echo 'Pushing Docker Image Version 1...'
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v1"
            }
        }

        stage('Build & Push V2') {
            steps {
                echo 'Building Docker Image Version 2...'
                bat "docker build -f Dockerfile.v2 -t ${DOCKER_USER}/${REPO_NAME}:v2 ."
                echo 'Pushing Docker Image Version 2...'
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v2"
            }
        }

        stage('Build & Push V3') {
            steps {
                echo 'Building Docker Image Version 3...'
                bat "docker build -f Dockerfile3 -t ${DOCKER_USER}/${REPO_NAME}:v3 ."
                echo 'Pushing Docker Image Version 3...'
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v3"
            }
        }
    }
}
