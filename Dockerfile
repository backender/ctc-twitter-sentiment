FROM python:3

WORKDIR .

COPY * ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python main.py
