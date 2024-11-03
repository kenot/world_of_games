pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "tdinkov"
        DOCKER_IMAGE = "world_of_games-flask_app"
        DOCKER_TAG = "latest"
        APP_PORT = 5000
        HOST_PORT = 8777
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    docker.build("${DOCKER_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container with mounted dummy scores.txt
                    sh '''
                    mkdir -p /tmp/dummy_scores
                    echo "0" > /tmp/dummy_scores/scores.txt

                    docker run -d --name ${DOCKER_IMAGE} \
                        -p ${HOST_PORT}:${APP_PORT} \
                        -v /tmp/dummy_scores/scores.txt:/scores.txt \
                        ${DOCKER_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                // Run the e2e.py test script using Python
                script {
                    def test_result = sh(script: 'python3 e2e.py http://localhost:${HOST_PORT}', returnStatus: true)
                    if (test_result != 0) {
                        error("Tests failed. Failing pipeline.")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the container after tests
                    sh 'docker stop ${DOCKER_IMAGE}'
                    sh 'docker rm ${DOCKER_IMAGE}'

                    // Log in to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USER --password-stdin"
                    }

                    // Push the Docker image to Docker Hub
                    sh "docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        cleanup {
            // Clean up by stopping and removing any leftover containers
            sh '''
            docker stop ${DOCKER_IMAGE} || true
            docker rm ${DOCKER_IMAGE} || true
            '''
        }
    }
}
