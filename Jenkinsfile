pipeline{
    agent{ label "linux"}
    stages{
        stage("build"){
            steps{
                sh """
                    docker build -t test .
                """
            }
        }
        stage("run"){
            steps{
                sh """
                    docker run --rm test
                """
            }
        }
    }
}