pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo "Code already cloned by Jenkins"
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                docker compose build
                '''
            }
        }

        stage('Deploy Containers') {
            steps {
                sh '''
                docker compose down
                docker compose up -d
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                sleep 5
                curl http://localhost:5000
                curl http://localhost:8082
                '''
            }
        }
    }
}
