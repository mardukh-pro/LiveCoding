FROM python:3.11

#update apk repo
RUN echo "dl-4.alpinelinux.org" >> /etc/apk/repositories && \
echo "dl-4.alpinelinux.org" >> /etc/apk/repositories

#install chromedriver
RUN apk update
RUN apk add --no-cache chromium chromium-chromedriver tzdata

#Get all the prereqs
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub alpine-pkgs.sgerrand.com
RUN wget github.com
RUN wget github.com
RUN apk update && \
apk add openjdk11-jre curl tar && \
curl -o allure-2.13.8.tgz -Ls repo.maven.apache.org && \
tar -zxvf allure-2.13.8.tgz -C /opt/ && \
ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
rm allure-2.13.8.tgz

WORKDIR /usr/workspace

# Copy the dependencies file to the working directory
COPY ./requirements.txt /usr/workspace

#Install Python dependencies
RUN pip3 install -r requirements.txt