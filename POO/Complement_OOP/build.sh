#!/bin/sh
g++ -std=c++17 -c cellule.cpp
g++ -std=c++17 -c test_old.cpp
g++ -std=c++17 test_old.o cellule.o -o test
test
