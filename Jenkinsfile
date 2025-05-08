pipeline {
    agent any

    stages {
        stage("Clone Git Repository") {
            steps {
                git branch: 'main', url: 'https://github.com/Oren1984/jenkins-hello-python.git'
            }
        }

        stage("Run Hello Python") {
            steps {
                sh "python hello.py"
            }
        }
    }
}
