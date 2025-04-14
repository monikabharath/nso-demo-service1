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
                sh 'pip3 install -r requirements.txt'

            }
        }

        // stage('Lint YANG') {
        //     steps {
        //         sh 'pyang service-yang-model.yang'
        //     }
        // }

        // stage('Lint Python') {
        //     steps {
        //         sh 'python3 -m py_compile package/python/*.py'
        //     }
        // }

        stage('Test') {
            steps {
                sh 'pytest tests/'
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
