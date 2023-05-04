# FROM python:3.9

# WORKDIR /usr/src/app

# COPY requirements.txt .

# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # streamlit-specific commands
# RUN mkdir -p /root/.streamlit
# RUN bash -c 'echo -e "\
# [general]\n\
# email = \"\"\n\
# " > /root/.streamlit/credentials.toml'
# RUN bash -c 'echo -e "\
# [server]\n\
# enableCORS = false\n\
# " > /root/.streamlit/config.toml'

# # exposing default port for streamlit
# EXPOSE 8501

# COPY . .

# CMD [ "streamlit", "run", "sed.py"]

# -------------------

FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg2

# Install Google Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install chromedriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/bin && \
    rm /tmp/chromedriver.zip

# Install streamlit
RUN pip install streamlit

# Install selenium
RUN pip install selenium

# Install nodejs and npm for webdriver-manager
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g webdriver-manager

CMD ["bash", "sed.py"]
