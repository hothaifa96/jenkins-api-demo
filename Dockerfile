from python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py main.py

EXPOSE 5005

CMD [ "python3","main.py" ]