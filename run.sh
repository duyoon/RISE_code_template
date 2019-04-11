#!/usr/bin/env bash

python main.py
python main.py -nn 32 64 128
python main.py -nn 32 32 -lr 0.01
python main.py -b 128