#!/bin/bash
rm build -r
mkdir build
cd build
cmake ..
make
