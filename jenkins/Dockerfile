FROM jenkinsci/blueocean

USER root

RUN apk add python py-pip; pip install awscli
RUN wget https://releases.hashicorp.com/terraform/0.12.26/terraform_0.12.26_linux_amd64.zip; unzip terraform_0.12.26_linux_amd64.zip -d /bin; rm terraform_0.12.26_linux_amd64.zip

USER jenkins