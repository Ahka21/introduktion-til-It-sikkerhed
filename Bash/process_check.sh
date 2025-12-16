#!/bin/bash

echo "Kører sleep-processer:" > sleep_processer.txt
ps aux | grep sleep | grep -v grep >> sleep_processer.txt
