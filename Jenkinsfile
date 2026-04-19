pipeline {
    agent any

    environment {
        APP_ENV = "dev"
    }

    parameters {
        string(name: 'NAME', defaultValue: 'DevOps', description: 'Your name')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Pradeepreddy405/Jenkins_Exp.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building in $APP_ENV environment'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
            }
        }

        stage('Parallel Jobs') {
            parallel {
                stage('Lint') {
                    steps {
                        sh 'echo Linting code...'
                    }
                }
                stage('Security Scan') {
                    steps {
                        sh 'echo Scanning security...'
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                expression { params.NAME == 'DevOps' }
            }
            steps {
                sh 'echo Deploying application...'
            }
        }
    }
}
