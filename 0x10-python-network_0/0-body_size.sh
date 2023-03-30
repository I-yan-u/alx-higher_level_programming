#!/bin/bash
# Displays the size of the HTTP body of the response
curl -s "$1" | wc -c
