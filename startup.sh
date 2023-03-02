docker compose down
docker build . -f docker/flask.Dockerfile -t flasky
docker compose up -d