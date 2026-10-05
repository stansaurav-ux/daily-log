FROM python:3.12-slim
WORKDIR /app
COPY log.py .
RUN mkdir /data
ENV DB_PATH=/data/notes.db
ENTRYPOINT ["python", "log.py"]
