#!/bin/bash

input="incoming/customers.csv"
raw="raw/customers.csv"
output="processed/active-customers.csv"
log="logs/pipeline.log"

echo "Pipeline started" >> "$log"

if [ ! -f "$input" ]; then
    echo "ERROR: customers.csv not found" >> "$log"
    exit 1
fi

cp "$input" "$raw"

head -n 1 "$raw" > "$output"
grep ",active" "$raw" >> "$output"

count=$(grep -c ",active" "$raw")

echo "Processed active customers: $count" >> "$log"

mv "$input" archive/customers.csv

echo "Pipeline completed successfully" >> "$log"

exit 0