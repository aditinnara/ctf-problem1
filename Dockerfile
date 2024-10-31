FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV FLAG_FILE=/challenge/flag.txt

RUN useradd -ms /bin/bash ctfuser
RUN mkdir -p /challenge

COPY challenge.py /home/ctfuser/challenge.py
COPY cheese_list.txt /home/ctfuser/cheese_list.txt
COPY flag.txt ${FLAG_FILE}

RUN chown -R root:root /home/ctfuser/challenge.py /home/ctfuser/cheese_list.txt ${FLAG_FILE} && \
    chmod 700 /home/ctfuser/challenge.py && \
    chmod 600 ${FLAG_FILE} && \
    chmod 600 /home/ctfuser/cheese_list.txt

RUN echo "{\"flag\":\"$(cat ${FLAG_FILE})\"}" > /challenge/metadata.json

USER ctfuser
WORKDIR /home/ctfuser
CMD ["python3", "./challenge.py"]

