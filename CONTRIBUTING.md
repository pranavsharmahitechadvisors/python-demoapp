# Python CI Pipeline

This CI pipeline will automate CI for a container-based python application.In this pipeline, an image will be released to docker hub after the automated tests pass at different stages.

 # Triggers

Configured to run on a Github Push Trigger

 # Prerequisites

1) Generate Github personal access token and add to Kaholo Vault
2) Setup Slack webhook for you slack channel to send notifications

# Pipeline Steps

Below are the different steps in this pipeline. The pipeline is mix of parallel and sequential steps.

1) Package Install - Install any custom linux packages using command Line - eg  apt-get install -y python3-venv python3-virtualenv python3-dev
2) Docker Cleanup - In parallel to step 1 this will stop and remove any running docker containers to have a clean start
3) Code Checkout - Here we configure the github repository using github plugin and providing the git hub credentials through Vault
4) Code Styling - This step will enforce the coding style by running linting tools such as flake8
5) Build - Here we build the docker image from the source code
6) Run - Run the locally built docker image 
7) Unit/Intergration/E2E Tests - Run the tests in parallel
8) Release - If the tests are successfull , tag and release the image to docker hub
9) Slack - Configured for notifications at various stages


# Plugins
Command Line, Github, Docker, Slack