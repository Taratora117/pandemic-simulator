from matplotlib import pyplot as plt
from random import random
from math import floor

# vars
population = 2000   # simulation population
spread_rate = 2.8   # R - number of infections per case
spread_time = 14    # active case
death_rate = 0.045  # % of death cases
days = 90           # simulation duration in days

# data generator
people = []


class Person:
    def __init__(self):
        # 0 - unaffected
        # 1-st - infected
        # st+1 - recovered
        # -1 - dead
        self.condition = 0


# init people
for i in range(population):
    people.append(Person())


# simulation init
people[floor(random() * len(people))].condition = 1
result = {
    'unaffected': [population - 1],
    'infected': [1],
    'recovered': [0],
    'dead': [0],
}


def update(infected, recovered, dead):
    result['unaffected'].append(result['unaffected'][-1] - infected)
    result['infected'].append(result['infected'][-1] + infected - (recovered + dead))
    result['recovered'].append(result['recovered'][-1] + recovered)
    result['dead'].append(result['dead'][-1] + dead)


# simulation
for i in range(days):
    newly_infected = 0
    newly_recovered = 0
    newly_dead = 0

    for person in people:
        if 1 <= person.condition <= spread_time:
            for random_person in people:
                if random() <= ((spread_rate / spread_time) / len(people)) and random_person.condition == 0:
                    random_person.condition = 1
                    newly_infected += 1

            person.condition += 1

            if person.condition == spread_time + 1:
                if random() <= death_rate:
                    person.condition = -1
                    newly_dead += 1
                else:
                    newly_recovered += 1

    update(newly_infected, newly_recovered, newly_dead)


# draw
fig, a = plt.subplots()
a.stackplot(range(days + 1), result.values(), labels=result.keys(), alpha=0.8)
a.legend()
a.set_title('Pandemic')
a.set_xlabel('days')
a.set_ylabel('population')

plt.show()
