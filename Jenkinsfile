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
                    def num1
                    def num2
                    withEnv(['num1=5','num2=7']) {
                        num1 = env.num1
                        num2 = env.num2
                    }
                    sh 'python3 calculadora.py ${num1} ${num2}'
                }
            }
        }
    }
}
