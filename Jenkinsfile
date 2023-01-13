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
                script {
                    def num1 = 2
                    def num2 = 0
                    sh 'python3 calculador.py ${num1} ${num2}'
                }

            }
        }
    }
}
