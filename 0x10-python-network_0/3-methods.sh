#!/bin/bash
# Show all the methods for an HTTP request
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
