#!/bin/bash

echo "numpy" >> results.txt
perf stat -r 10 python matrix-multiplication-numpy.py >> results.txt 2>&1

echo "theano" >> results.txt
perf stat -r 10 python matrix-multiplication-theano.py >> results.txt 2>&1
