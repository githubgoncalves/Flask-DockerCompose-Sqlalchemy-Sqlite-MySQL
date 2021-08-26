FROM ubuntu:latest

LABEL maintainer="danielgoncalves.info@gmail.com"

CMD tail -f /dev/null

RUN apt-get update -y && apt-get install -y python3-pip python-dev

COPY ./requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT [ "python3" ]
CMD ["app.py" ]


