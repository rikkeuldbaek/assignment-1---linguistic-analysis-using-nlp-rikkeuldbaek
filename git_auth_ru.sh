#!/usr/bin/env bash
git config --global user.email "rikke_uldbaek@hotmail.com"
git config --global user.name "rikkeuldbaek"

#install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_sm