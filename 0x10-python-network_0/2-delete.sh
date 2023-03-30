#!/bin/bash
# Script that connects to a url, sends a DLETE request and print out ther response
curl -sX DELETE "$1"
