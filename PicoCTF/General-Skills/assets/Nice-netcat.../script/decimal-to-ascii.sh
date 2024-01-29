#!/bin/bash
decimal=$(nc mercury.picoctf.net 7449)
# Convert numbers into characters using awk
flag=$(echo "$decimal" | awk '{printf "%c", $0}')
# Print flag and delete all new lines
echo "Flag: $(echo $flag | tr -d $'\n')"
