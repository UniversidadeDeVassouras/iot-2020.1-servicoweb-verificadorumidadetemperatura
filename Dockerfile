FROM python:3.8.3-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]