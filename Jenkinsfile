pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/YOUR-USERNAME/jenkins-pipeline-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building project..."'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
