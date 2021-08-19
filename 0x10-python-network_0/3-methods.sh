#!/bin/bash
# cURL only methods
curl -sI "$1" | grep "Allow: " | cut -b 8-
