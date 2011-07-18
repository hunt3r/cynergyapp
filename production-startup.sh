#!/bin/bash

nohup gunicorn -c gunicorn.conf deploy:app &
