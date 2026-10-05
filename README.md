# daily-log

A tiny CLI note logger built with Python and SQLite, packaged in Docker.

## Run locally

```
python log.py "my note"   # save a note
python log.py             # list notes
```

## Run with Docker

```
docker build -t daily-log .
docker run -v daily-log-data:/data daily-log "my note"
docker run -v daily-log-data:/data daily-log
```

## What I learned

Containers lose their files when they stop. A Docker volume keeps the database alive between runs.
