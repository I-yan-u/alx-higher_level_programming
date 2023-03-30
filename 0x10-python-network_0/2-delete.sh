#!/bin/bash
# Script that connects to a url, sends a
# DLETE request and print out ther response
curl -sXL DELETE "$1"
