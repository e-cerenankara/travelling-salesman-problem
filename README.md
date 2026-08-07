# Traveling Salesman Problem with a Genetic Algorithm

A Python implementation that solves the Traveling Salesman Problem using a genetic algorithm.

## What is the Traveling Salesman Problem?

Given a set of cities and the distances between them, the objective is to find the shortest route that visits every city exactly once before returning to the starting point. As the number of cities increases, the number of possible routes grows exponentially, making it computationally infeasible to evaluate every combination. For this reason, TSP is classified as an NP-hard problem.

## What is a Genetic Algorithm?

A genetic algorithm is a search method inspired by natural selection. Instead of checking every possible route, it keeps a population of candidate routes and improves them over many generations. Shorter routes are more fit and more likely to survive. Surviving routes are combined through crossover to produce new routes. Mutations keep the population diverse and help avoid getting stuck on a bad solution.

## Algorithm

1. Generate an initial population of random routes, all starting at city 0.
2. Calculate the total distance of each route.
3. Select survivors by pairing up routes randomly and keeping the shorter one from each pair.
4. Cross over the selected routes to produce new offspring routes.
5. Mutate some routes by swapping two cities.
6. Repeat steps 2 to 5 for a number of generations, keeping track of the best route found.

## Requirements

Python 3, standard library only.

## Installation

```bash
git clone https://github.com/e-cerenankara/traveling-salesman-problem.git
cd traveling-salesman-problem
```

## Usage

```bash
python tsp.py --population 1000 --generations 100 --mutation-rate 0.25
```

## Example

```bash
python tsp.py --population 200 --generations 30
```

Output

```
Generation 0: Best distance = 462.39
Generation 1: Best distance = 462.39
...
Generation 29: Best distance = 294.821

Best route found: [0, 9, 7, 2, 5, 10, 14, 12, 4, 11, 6, 8, 13, 3, 1]
Best distance: 294.821
```
