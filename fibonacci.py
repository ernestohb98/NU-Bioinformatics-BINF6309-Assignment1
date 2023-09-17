import sys

def population(n = int ,k = int ):
    population = [0] * (n + 1)
    population[0] = 1
    for i in range(1, n + 1):
        population[i] = population[i - 1] * (1 + k)

    return population[n]

if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(population(n,k))