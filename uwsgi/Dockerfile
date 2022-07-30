FROM python:latest
WORKDIR /root
RUN apt-get update && apt-get install -y libjansson-dev
RUN pip3 install pipenv virtualenv wheel setuptools uwsgi
COPY test_handler.py /root
COPY uwsgi.conf /root
ENTRYPOINT [ "pipenv", "run", "uwsgi","--json","uwsgi.conf:PoC" ]