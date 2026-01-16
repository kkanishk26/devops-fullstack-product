pipeline {
    agent any

    stages {

        stage('Pull Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kkanishk26/devops-fullstack-product.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                docker compose down
                docker compose build
                docker compose up -d
                '''
            }
        }
    }
}
