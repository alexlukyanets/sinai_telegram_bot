FROM python:3.11-slim

LABEL Author="YuzkoBot"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#directory to store app source code
RUN mkdir /sinai_bot

#switch to /app directory so that everything runs from here
WORKDIR /sinai_bot

#copy the app code to image working directory
COPY . /sinai_bot

#let pip install required packages
RUN pip install --upgrade pip
RUN pip install -r requirements_docker.txt