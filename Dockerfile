FROM joyzoursky/python-chromedriver:3.8

COPY . /selenium_classic_framework

WORKDIR /selenium_classic_framework

RUN apt-get update
RUN apt-get install -y locales

RUN pip3 install pipenv
RUN pipenv install --system
