# IPython notebooks for A Practical Introduction to the Simulation of Molecular Systems

IPython notebooks for examples of [A Practical Introduction to the Simulation of Molecular Systems, by Martin J. Field](http://www.cambridge.org/br/academic/subjects/chemistry/chemistry-general-interest/practical-introduction-simulation-molecular-systems-2nd-edition)

All the examples use the [pDynamo](https://sites.google.com/site/pdynamomodeling/) library. pDynamo is an open source program library that has been designed for the simulation of molecular systems using quantum chemical (QC), molecular mechanical (MM) and hybrid QC/MM potential energy functions.

## Using the web viewer ([nbviewer](http://nbviewer.ipython.org/))

### Examples

* [Example 1](http://nbviewer.ipython.org/github/mchelem/simulation-of-molecular-systems/blob/master/example1.ipynb)
* [Example 2](http://nbviewer.ipython.org/github/mchelem/simulation-of-molecular-systems/blob/master/example2.ipynb)

### Exercises
* [Exercise 2](http://nbviewer.ipython.org/github/mchelem/simulation-of-molecular-systems/blob/master/exercise2.ipynb)

## Running locally

### Install dependencies

If you run the examples in your machine, you can install the dependencies by running:

```bash
make install
```

This will install IPython notebook, rdkit (for the molecule drawings) and pDynamo.

### Running the examples

There is a convenience script that runs IPython notebook with pDynamo loaded:

```bash
./run_examples.sh
```
