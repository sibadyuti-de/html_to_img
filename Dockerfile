FROM ubuntu

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update &&\
    apt-get install git -y &&\
    apt-get install python3 pip -y &&\
    apt-get install xvfb -y &&\
    pip install imgkit &&\
    apt-get install wget -y &&\
    apt-get install nano -y &&\
    apt-get install wkhtmltopdf -y &&\
    apt-get autoremove -y &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

CMD /bin/bash
