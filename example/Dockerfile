FROM cszubert/awscli-python:latest
EXPOSE 5000
ENV FLASK_APP=secret.py
ADD ./app/secret.py .
RUN pip install flask
RUN apt-get install jq
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
