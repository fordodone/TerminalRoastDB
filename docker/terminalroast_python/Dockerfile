FROM debian:9

RUN apt-get update \
      && apt-get install -y \
        python3 \
        python3-pip \
        default-libmysqlclient-dev \
        sudo

COPY . /app 

RUN cd /app \
      && pip3 install -r requirements.txt \
      && sed -i 's/sh/sh\nsleep 20s/' TerminalRoastDB.sh \
      && sed -i 's/python3/python3 -u/' TerminalRoastDB.sh \
      && sed -i '/self.db/s/localhost/terminalroast_mysql/' recipe.py

WORKDIR /app

CMD [ "./TerminalRoastDB.sh" ]
