FROM python:3.9-bullseye

WORKDIR /app

RUN apt update

RUN apt install git

RUN git clone https://github.com/nicholascomuni/Spam-Classifier

WORKDIR ./Spam-Classifier

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV development

CMD ["flask","run"]
