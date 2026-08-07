import argparse
import math
import random

cities = [
    (10, 20), (80, 90), (30, 70), (90, 30), (50, 50),
    (20, 80), (70, 20), (40, 60), (60, 10), (15, 45),
    (25, 85), (75, 35), (45, 55), (85, 15), (35, 75),
]


def generate_initial_population(num_cities, population_size):
    # Creates a starting population of random routes, all starting at city 0.
    population = []
    for _ in range(population_size):
        route = list(range(1, num_cities))
        random.shuffle(route)
        route = [0] + route
        population.append(route)
    return population


def route_distance(cities, route):
    # Total distance of visiting the cities in the given order.
    total = 0
    for i in range(len(route) - 1):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[i + 1]]
        dx = x2 - x1
        dy = y2 - y1
        total += math.sqrt(dx * dx + dy * dy)
    return total


def select_survivors(cities, generation):
    # Pairs routes up and keeps the shorter one.
    population = generation[:]
    random.shuffle(population)
    mid = len(population) // 2

    selected = []
    for i in range(mid):
        route_a = population[i]
        route_b = population[i + mid]
        if route_distance(cities, route_a) < route_distance(cities, route_b):
            selected.append(route_a)
        else:
            selected.append(route_b)
    return selected


def crossover_pair(parent1, parent2):
    # Takes a slice from parent1, fills the rest with parent2's order, skipping cities already taken from parent1.
    start = random.randint(1, len(parent1) - 1)
    finish = random.randint(start, len(parent1))

    from_parent1 = parent1[start:finish]
    from_parent2 = [city for city in parent2 if city not in from_parent1]

    child = []
    parent2_index = 0
    for i in range(len(parent1)):
        if start <= i < finish:
            child.append(from_parent1[i - start])
        else:
            child.append(from_parent2[parent2_index])
            parent2_index += 1
    return child


def crossover_generation(selected):
    # Pairs up the selected routes and produces offspring from each pair.
    offsprings = []
    mid = len(selected) // 2
    for i in range(mid):
        parent1 = selected[i]
        parent2 = selected[i + mid]
        for _ in range(2):
            offsprings.append(crossover_pair(parent1, parent2))
            offsprings.append(crossover_pair(parent2, parent1))
    return offsprings


def mutate_generation(generation, mutation_rate):
    # Swaps two random cities in a route with the given probability.
    mutated = []
    for route in generation:
        route = route[:]
        if random.random() < mutation_rate:
            i = random.randint(1, len(route) - 1)
            j = random.randint(1, len(route) - 1)
            route[i], route[j] = route[j], route[i]
        mutated.append(route)
    return mutated


def next_generation(cities, generation, mutation_rate):
    selected = select_survivors(cities, generation)
    offsprings = crossover_generation(selected)
    return mutate_generation(offsprings, mutation_rate)


def run_ga(cities, population_size, generations, mutation_rate):
    # Runs the genetic algorithm and returns the best route found, its distance, and the best distance seen in every generation.
    population = generate_initial_population(len(cities), population_size)
    history = []
    best_route, best_distance = None, None

    for gen in range(generations):
        distances = [route_distance(cities, route) for route in population]
        best_idx = distances.index(min(distances))
        gen_best_route = population[best_idx]
        gen_best_distance = distances[best_idx]
        history.append(gen_best_distance)

        if best_distance is None or gen_best_distance < best_distance:
            best_distance = gen_best_distance
            best_route = gen_best_route[:]

        population = next_generation(cities, population, mutation_rate)

    return best_route, best_distance, history


def main():
    parser = argparse.ArgumentParser(description="Solve the TSP with a genetic algorithm.")
    parser.add_argument("--population", type=int, default=1000, help="Population size")
    parser.add_argument("--generations", type=int, default=100, help="Number of generations")
    parser.add_argument("--mutation-rate", type=float, default=0.25, help="Mutation probability (0-1)")
    args = parser.parse_args()

    best_route, best_distance, history = run_ga(
        cities, args.population, args.generations, args.mutation_rate
    )

    for gen, dist in enumerate(history):
        print(f"Generation {gen}: Best distance = {round(dist, 3)}")

    print()
    print(f"Best route found: {best_route}")
    print(f"Best distance: {round(best_distance, 3)}")


if __name__ == "__main__":
    main()