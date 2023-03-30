#!/bin/bash
# a header with a variable will be sent along with the GET request.
curl -H "X-School-User-Id: 98" -sLX GET "$1"
