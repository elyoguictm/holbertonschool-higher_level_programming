#!/bin/bash
# cURL POST parameters
curl -s -X POST "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
