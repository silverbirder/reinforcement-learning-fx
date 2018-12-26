# selected os
FROM ubuntu

# mainte user
MAINTAINER pampkin_boy
RUN apt-get update

# auto_order needs tools
RUN apt-get install -y python python3 python3-pip
RUN pip3 install mongo pymongo gym pyyaml keras tensorflow
RUN apt-get install -y git
RUN pip3 install git+https://github.com/oanda/oandapy.git

# mainte tools
RUN apt-get install -y vim

# login user
RUN groupadd -g 1000 fx_group && \
    useradd -g fx_group -G sudo -m -s /bin/bash fx_trader && \
    echo 'fx_trader:pass' | chpasswd
USER fx_trader

# deploy
RUN mkdir /home/fx_trader/fxTrade
COPY fxTrade /home/fx_trader/fxTrade/

CMD echo "successfully auto order container!!"
