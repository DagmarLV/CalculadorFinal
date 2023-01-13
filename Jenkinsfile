pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Unit test") {
            steps {
                sh "python3 test_calculador.py"
            }
        }
        stage("Pipeline Broken"){
            steps {
                sh 'python3 calculador.py'

            }
        }
    }
}
