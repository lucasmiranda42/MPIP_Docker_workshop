FROM continuumio/anaconda3
COPY requirements.txt .
COPY *.py ./
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]
