FROM python:3.10.1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY . /usr/src/app/
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--reload"]