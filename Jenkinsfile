pipeline {
    agent any

    environment {
        NSO_HOST = "localhost"
        NSO_PORT = "8080"
        NSO_USER = "admin"
        NSO_PASS = "admin"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/monikabharath/nso-demo-service1.git/'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Lint YANG') {
            steps {
                sh 'pyang service-yang-model.yang'
            }
        }

        stage('Lint Python') {
            steps {
                sh 'python3 -m py_compile package/python/*.py'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Deploy to NSO') {
            steps {
                sh '''
                    curl -u $NSO_USER:$NSO_PASS \
                         -X POST http://$NSO_HOST:$NSO_PORT/api/running/services/my-service \
                         -H "Content-Type: application/vnd.yang.data+json" \
                         -d @sample-payload.json
                '''
            }
        }
    }
}
