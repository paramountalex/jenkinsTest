pipeline{
    agent { label "mac" }
    stages{
        stage('Docker Build') {
            steps {
      	        sh 'docker build -t test .'
            }
        }
        stage('Docker Run'){
            steps{
                sh 'docker run --rm test'
            }
        }
    }
}