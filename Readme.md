# Setup

## Environment Variables

```
DB_TBL=""
DB_HOST=""
DB_USER=""
DB_PASS=""
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_TOKEN_KEY=""
TWITTER_TOKEN_SECRET=""
```

## Docker setup

This step is optional and explains how to run the service within a docker container.

```
NAME="ctc-twitter-sentiment"
docker build -t $NAME .
docker run -d -e CTC_TWITTER_DB=$DB_TBL -e CTC_TWITTER_HOST=$DB_HOST -e CTC_TWITTER_PORT=3306 -e CTC_TWITTER_USER=$DB_USER -e CTC_TWITTER_PASSWORD=$DB_PASS -e TWITTER_CONSUMER_KEY=$TWITTER_CONSUMER_KEY -e TWITTER_CONSUMER_SECRET=$TWITTER_CONSUMER_SECRET -e TWITTER_TOKEN_KEY=$TWITTER_TOKEN_KEY -e TWITTER_TOKEN_SECRET=$TWITTER_TOKEN_SECRET -t $NAME
```

## Run

In order to run the code locally, just execute the main function after installing dependencies.

```
pip install --no-cache-dir -r requirements.txt
python main.py
```
