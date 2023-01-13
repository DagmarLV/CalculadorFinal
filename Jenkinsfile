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
                def num1 = 5
                def num2 = 7
                sh 'python3 calculador.py ${num1} ${num2}'

            }
        }
    }
}
