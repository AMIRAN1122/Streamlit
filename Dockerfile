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

FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install webdriver-manager

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

RUN apt-get update && \
    apt-get install -y wget unzip xvfb libxi6 libgconf-2-4 && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    wget https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chown root:root /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver

# exposing default port for streamlit
EXPOSE 8501

COPY . .

CMD ["bash", "-c", "Xvfb :99 -screen 0 1024x768x24 >/dev/null 2>&1 & export DISPLAY=:99 && streamlit run --server.port 8501 --server.enableCORS false --browser.serverAddress 0.0.0.0 --server.headless true sed.py"]
