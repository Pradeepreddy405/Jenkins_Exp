pipeline {

    agent any 
    // Run this pipeline on any available Jenkins agent (node)

    environment {
        APP_ENV = "dev"
        // Global environment variable accessible in all stages
    }

    parameters {
        string(name: 'NAME', defaultValue: 'DevOps', description: 'Your name')
        // User input parameter shown in Jenkins UI before running the job
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Pradeepreddy405/Jenkins_Exp.git'
                // Pulls code from GitHub repo (main branch) into workspace
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building in $APP_ENV environment'
                // Simulates build process using environment variable
                // In real projects → compile, package, docker build, etc.
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
                // Placeholder for executing unit/integration tests
            }
        }

        stage('Parallel Jobs') {
            parallel {

                stage('Lint') {
                    steps {
                        sh 'echo Linting code...'
                        // Code quality check (style, syntax issues)
                        // Example tools: eslint, flake8, checkstyle
                    }
                }

                stage('Security Scan') {
                    steps {
                        sh 'echo Scanning security...'
                        // Security scanning stage
                        // Example tools: Snyk, Trivy, OWASP Dependency Check
                    }
                }
            }
            // Both stages run simultaneously → saves time
        }

        stage('Deploy') {
            when {
                expression { params.NAME == 'DevOps' }
                // Deploy ONLY if user input NAME = "DevOps"
                // Otherwise this stage is skipped
            }
            steps {
                sh 'echo Deploying application...'
                // Placeholder for deployment logic
                // Real case → Kubernetes, EC2, Docker, etc.
            }
        }
    }
}
