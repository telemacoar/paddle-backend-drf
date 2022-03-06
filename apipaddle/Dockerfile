FROM python:3.8.12-buster
COPY . /
RUN pip install -r requirements.txt
EXPOSE 7890:7890
CMD ./start_server.sh