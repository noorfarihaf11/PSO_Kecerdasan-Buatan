import random
import matplotlib.pyplot as plt

def pso(fitness_func, min_bound, max_bound, num_particles, num_iterations, w, c1, c2):
    random.seed(42)  # Optional: make results reproducible
    particles = [random.uniform(min_bound, max_bound) for _ in range(num_particles)]
    velocities = [0.0 for _ in range(num_particles)]

    particles_pbest = particles.copy()
    pbest_fitness = [fitness_func(p) for p in particles_pbest]
    particles_gbest = particles_pbest[pbest_fitness.index(min(pbest_fitness))]

    best_fitness_per_iteration = []

    for i in range(num_iterations):
        for j in range(num_particles):
            fitness = fitness_func(particles[j])
            if fitness < pbest_fitness[j]:
                particles_pbest[j] = particles[j]
                pbest_fitness[j] = fitness

        current_gbest = particles_pbest[pbest_fitness.index(min(pbest_fitness))]
        if fitness_func(current_gbest) < fitness_func(particles_gbest):
            particles_gbest = current_gbest

        for j in range(num_particles):
            velocities[j] = (
                w * velocities[j] +
                c1 * random.random() * (particles_pbest[j] - particles[j]) +
                c2 * random.random() * (particles_gbest - particles[j])
            )
            particles[j] += velocities[j]
            particles[j] = max(min_bound, min(particles[j], max_bound))  # clamp

        best_fitness_per_iteration.append(fitness_func(particles_gbest))

    return particles_gbest, fitness_func(particles_gbest), best_fitness_per_iteration


# Objective function
def tugas(x):
    return x**2


particles_gbest, fitness_gbest, best_fitness_per_iteration = pso(
    tugas, -10, 10, 10, 50, 0.5, 1.5, 1.5
)

print("Nilai Minimum:", fitness_gbest)
print("X terbaik:", particles_gbest)

plt.figure(figsize=(8, 5))
plt.plot(best_fitness_per_iteration, linestyle='-')
plt.title("Best Fitness per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.plot(best_fitness_per_iteration, linestyle='-')
plt.title("Best Fitness per Iteration (Log)")
plt.xlabel("Iteration")
plt.ylabel("Best Fitness")
plt.yscale('log')
plt.grid(True)
plt.tight_layout()
plt.show()