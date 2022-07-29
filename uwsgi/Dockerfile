FROM python:latest
RUN pip3 install pipenv virtualenv wheel setuptools
RUN apt-get update && apt-get install -y libjansson-dev
RUN pipenv run pip uninstall uwsgi
RUN pipenv run pip install uwsgi
COPY test_handler.py /root
COPY uwsgi.conf /root
WORKDIR /root
ENTRYPOINT [ "pipenv", "run", "uwsgi","--json","uwsgi.conf:PoC" ]