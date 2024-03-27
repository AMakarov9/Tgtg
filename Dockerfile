FROM python:3.11.8

ADD telegram.py . 
ADD get_client.py . 
ADD db.db .

RUN pip install aiogram==2.23.1
RUN pip install tgtg

CMD ["python", "./telegram.py"]