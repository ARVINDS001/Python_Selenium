pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat '''
                if not exist %VENV% (
                    python -m venv %VENV%
                )
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
}
