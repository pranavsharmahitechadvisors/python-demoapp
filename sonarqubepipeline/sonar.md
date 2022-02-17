# On Demand Sonarqube Scanning

This pipeline template will enable user to run a sonar-scanning on a pre-configured sonarqube server on GCP. Server is stopped after the scan and started on the trigger.

 # Triggers

Configured to run on as a manual trigger.

 # Prerequisites

1) Create a VM on GCP and configure sonarqube server using docker https://docs.sonarqube.org/latest/setup/get-started-2-minutes/

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
 Google-Cloud-Compute-Engine,TextEditor, Command Line, Git, Docker, Slack

# Pipeline Design

