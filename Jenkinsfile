pipeline {
    agent any

    environment {
        DOCKER_USER = 'konankipranavi'
        REPO_NAME   = 'employee-system'
    }

    stages {
        stage('Checkout') {
            steps {
                // Fixed: Explicitly points directly to your exact GitHub repository path
                git branch: 'main', url: 'https://github.com/KonankiPranavi/Employee-System.git'
                echo 'Employee System source code checked out successfully.'
            }
        }

        stage('Check Project Files') {
            steps {
                // Lists files on your Windows machine to verify the folder context
                bat 'dir'
                echo 'Project files verified successfully.'
            }
        }

        stage('Build & Push All Versions') {
            steps {
                echo 'Building and Pushing Docker Image Version 1...'
                bat "docker build -f Dockerfile1 -t ${DOCKER_USER}/${REPO_NAME}:v1 ."
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v1"

                echo 'Building and Pushing Docker Image Version 2...'
                bat "docker build -f Dockerfile -t ${DOCKER_USER}/${REPO_NAME}:v2 ."
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v2"

                echo 'Building and Pushing Docker Image Version 3...'
                bat "docker build -f Dockerfile3 -t ${DOCKER_USER}/${REPO_NAME}:v3 ."
                bat "docker push ${DOCKER_USER}/${REPO_NAME}:v3"
            }
        }
    }
}

