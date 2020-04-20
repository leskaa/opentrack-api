FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /opentrack_dir
WORKDIR /opentrack_dir
ADD requirements.txt /opentrack_dir
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /opentrack_dir
