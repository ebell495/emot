FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /EMOT
WORKDIR /EMOT
RUN python3 -m pip install . && chmod +x fuzz/emoji-parse-fuzz.py