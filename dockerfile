FROM python:3.8

# Ddding trusting keys to apt for repositories:
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    # use shell cmd to add the chrome url to repos
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    # download the repo
    && apt-get -y update \
    #install the repo
    && apt-get install -y google-chrome-stable \
    # download the zipfile containing the latest chromedriver release
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    # download something to unzip it
    && apt-get install -yqq unzip \
    #unzip it
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#copy files from local app dir to docker dir
COPY app/. .

RUN pip install -r requirements.txt 


CMD ["python3", "main.py"]

