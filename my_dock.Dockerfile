FROM python:3.8

RUN apt-get update && apt-get install -y libsndfile1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "--server.port", "8501", "--server.enableCORS", "false", "str.py"]

