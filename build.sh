#!/bin/sh
python3 /usr/local/bin/dumppdf.py --extract-toc "$1" > toc.toc
python3 format-toc.py toc.toc > toc.txt