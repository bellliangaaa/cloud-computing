FROM python:3.9.10
COPY 7940group.py /
COPY requirements.txt /
COPY config.ini /
ENV ACCESS_TOKEN =5251254508:AAG0K1ff3RTlXkdvpms64I7_Yl0ldE5Fvxg
RUN pip install pip update
RUN pip install PyMySQL
RUN pip install -r requirements.txt
RUN pip install python-telegram-bot --upgrade
CMD ["/7940group.py"]
ENTRYPOINT ["python"]