Parallel processing benchmarks.

# Setup
You will need Theano and numpy installed to run the Python programs.
Easiest way of doing this is using something like pip or conda.

You can install pip and numpy dependencies on Ubuntu with
```
sudo apt-get install python-pip libblas-dev liblapack-dev libatlas-base-dev gfortran
```

To install numpy and Theano, go to the project directory and run
```
sudo pip install -r requirements.txt
```

# Running
There are two shell scripts which use perf-stat to run tests.
Use the commands `./benchmark_inverse.sh` or `./benchmark_multiplication.sh` to run the appropriate benchmark.

It runs 10 tests of each script and outputs the results to a file results.txt.
This will take a while.
