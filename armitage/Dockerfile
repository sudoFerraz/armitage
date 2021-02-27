FROM python:3

LABEL maintainer="Gabriel Ferraz sudoferraz@gmail.com"

COPY ./requirements.txt ./armitageApp/requirements.txt

ENV FLASK_APP "flaskMathApp"
ENV FLASK_ENV "development"
WORKDIR /armitageApp

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]