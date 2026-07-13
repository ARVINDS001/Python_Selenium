pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
    }

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat '''
                if exist %VENV% rmdir /S /Q %VENV%
                "%PYTHON%" -m venv %VENV%
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automation') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python Data_Driven_Excel\\Data_Driven_openpyxl.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished.'
        }
    }
}
