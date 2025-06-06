#!/bin/bash 

cat mess | grep -o [a-zA-Z] | tr -d '\n'