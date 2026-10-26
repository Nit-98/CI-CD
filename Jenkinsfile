pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-2'
        ECR_REPO = '201971881499.dkr.ecr.ap-south-2.amazonaws.com/myapp'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:v1 .'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION |
                    docker login --username AWS --password-stdin 201971881499.dkr.ecr.ap-south-2.amazonaws.com

                    docker tag myapp:v1 $ECR_REPO:v1
                    docker push $ECR_REPO:v1
                '''
            }
        }
    }
}
