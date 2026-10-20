#!/bin/bash

file=$1

if [ -f "$file" ]; then
    echo "File exists: $file"
    exit 0
else
    echo "ERROR: File not found: $file"
    exit 1
fi