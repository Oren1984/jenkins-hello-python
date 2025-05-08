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
                sh "python3 hello.py"
            }
        }
    }
}
// This Jenkinsfile defines a simple pipeline that clones a Git repository and runs a Python script.
// The pipeline consists of two stages:
// 1. **Clone Git Repository**: This stage uses the `git` command to clone the specified branch of the repository.
// 2. **Run Hello Python**: This stage  executes a shell command to run the `hello.py` Python script.
// The pipeline is set to run on any available agent.
// The `git` command is used to clone the repository from GitHub, and the `sh` command is used to execute the Python script.
// The `python3` command is used to run the script, assuming Python 3 is installed on the agent.
// The pipeline is defined using the declarative syntax of Jenkins Pipeline DSL.
// The `pipeline` block defines the entire pipeline, and the `stages` block contains the individual stages.
// The `steps` block within each stage contains the commands to be executed.
// This Jenkinsfile is a simple example of how to automate the process of cloning a Git repository and running a Python script using Jenkins.
// The pipeline is defined using the declarative syntax of Jenkins Pipeline DSL.
// The `pipeline` block defines the entire pipeline, and the `stages` block contains the individual stages.