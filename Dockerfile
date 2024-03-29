FROM python:3.7

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "api_server1.py"]