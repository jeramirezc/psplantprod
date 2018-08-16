# psplantprod
This software is an attempt to simulate the propagation process of specific microorganisms over plantations with two varieties of plants based on percolation theory. It requires six modifiable variables:

p density of plants (occupation probability)

l size of the square matrix

rep runs for statistics

perc percentage of inoculated soil (the portion of entries with microbial charge)

Xa pathogen susceptibility of A variety plant

Xb pathogen susceptibility of B variety plant

This version starts on p=0.05 (editable) and stops on p=0.95 (editable changing the number of iterations), with increments of 
0.05 (editable). Also, the software scans the values of M in the same range as p.

The unique difference between versions 2N and 3N is the coordination number of square lattices, 4 (nearest neighbors) and 8 (next-nearest neighbors), respectively.

Usage

This software is functional in Python 2.x. Run in a console with the following command:

python prod-xN.py l perc Xa Xb

The file 'prod-xN-l-perc.dat' will be created as an output. It contains information about the production yield as a function of p and M under the given conditions of perc, Xa, and Xb.
