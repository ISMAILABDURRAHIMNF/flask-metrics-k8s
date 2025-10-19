FROM python:3.11.12-slim

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
