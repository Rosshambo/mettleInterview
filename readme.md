Anthony Teem - Mettle interview - 5/17/2023

Instructions provided: 
```
Write a function that takes in a series of numbers along with a map of numbers(A) to numbers(B), and returns the series of numbers where instances of A are replaced by their respective B  
    Ex: if the input is [1, 2, 3, 1, 5] and the map is {1: 10, 2: 33} then it should return [10, 33, 3, 10, 5]
```
To run using python 3.3+:
```commandline
usage: indexdisplay.py [-h] input_list input_map

positional arguments:
  input_list  Input list of indices you would like printed
  input_map   Input map of values for exercise

optional arguments:
  -h, --help  show this help message and exit
```
Assumptions:
1. The inputs will be provided from another system and passed via command line using arg parser.