# daily-log

A tiny CLI note logger built with Python and SQLite, packaged in Docker.

## Run locally

```
python log.py "my note"        # save a note
python log.py                  # list notes
python log.py search docker    # find notes containing a word
```

## Run with Docker

```
docker build -t daily-log .
docker run -v daily-log-data:/data daily-log "my note"
docker run -v daily-log-data:/data daily-log
docker run -v daily-log-data:/data daily-log search docker
```

## What I learned

Containers lose their files when they stop. A Docker volume keeps the database alive between runs.

Search uses a SQL `LIKE` query with a `?` placeholder, so the number of placeholders must match the number of values passed in.
