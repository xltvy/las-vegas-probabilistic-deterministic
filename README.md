# las-vegas-probabilistic-deterministic

Bogazici University

Computer Engineering Department

Fall 2021

CMPE 300 - Analysis of Algorithms

Project 3

Altay Acar & Engin Oguzhan Senol

***

An algorithm based study on deterministic and probabilistic approaches on Las Vegas Algorithm and their results regarding the complexity analysis.

Two algorithms written in main.py: first one is a Las Vegas algorithm for the n-queens problem and the second one is a modified version of the first one hat places a number k (k<n) of queens on the board in a random way and then uses backtracking (the deterministic algorithm) to place the remaining queens (without changing the positions of the queens that were placed randomly). That is, after the k queens are fixed, the deterministic algorithm begins from the (k+1)th queen and backtracks when necessary.

Both algorithms run countless times and the results are stored into an output file to compare both approaches to the same problem.

The results of our analysis are provided via cmpe300-project3-report.pdf file.
