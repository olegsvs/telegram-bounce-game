#!/usr/bin/sh
pkill -f game:app
pkill -f bounce.py
sleep 2
nohup gunicorn game:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8103 > game_server.log &
nohup python3.10 bounce.py > bot.log &
