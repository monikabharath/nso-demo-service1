pipeline {
    agent any

    environment {
        NSO_HOST = "localhost"
        NSO_PORT = "8081"
        NSO_USER = "admin"
        NSO_PASS = "admin"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/monikabharath/nso-demo-service1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
             # Create a virtual environment (if not already created)
                python3 -m venv venv
                # Activate the virtual environment
                source venv/bin/activate
                # Upgrade pip to the latest version
                python3 -m pip install --upgrade pip
                # Install dependencies from requirements.txt
                pip install -r requirements.txt
                '''
            }
        }

        stage('Lint YANG') {
            steps {
                sh '''
                source venv/bin/activate
                pyang service-yang-model.yang/
                '''
            }
        }

        stage('Lint Python') {
            steps {
                sh '''
                source venv/bin/activate
                python3 -m py_compile package/python/*.py/
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                source venv/bin/activate
                pytest tests/
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Successfully logged in to NSO and pipeline completed!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
