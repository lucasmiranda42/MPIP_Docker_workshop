FROM continuumio/anaconda3
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD echo "I'm running!"
CMD [ "/bin/bash" ]
