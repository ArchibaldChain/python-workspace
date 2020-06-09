# %%
import itertools
import random
import csv

relation = []
with open(r'I:\Programming\Python\python-workspace\GenerticAlgorithm\relation.csv', 'r') as r:
    temp = csv.reader(r)
    for row in temp:
        vec = []
        for num in row:
            vec.append(int(num))
        relation.append(vec)

# %%


def deg_relation(type1, type2):
    return reltaion[type1][type2]

# %%


def gen_1():
    newone = {}
    case = random.randint(1, 5)
    w300 = {1: 1, 2: 5, 3: 7, 4: 8, 5: 15, 6: 16}
    w400 = {1: 6, 2: 9, 3: 14}
    w600 = {1: 10, 2: 12}
    w500 = {1: 2, 2: 4, 3: 13}
    if (case <= 3):
        nothere = random.randint(1, 3)
        if(nothere == 1):
            a1 = 4
            a2 = 13
            a3 = 2
        if(nothere == 2):
            a1 = 2
            a2 = 13
            a3 = 4
        if(nothere == 3):
            a1 = 2
            a2 = 4
            a3 = 13
        s3 = []
        s4 = []
        s6 = []
        while(len(s3) < 6):
            x = random.randint(1, 6)
            if x not in s3:
                s3.append(x)
        while(len(s4) < 3):
            x = random.randint(1, 3)
            if x not in s4:
                s4.append(x)
        while(len(s6) < 2):
            x = random.randint(1, 2)
            if x not in s6:
                s6.append(x)
        newone[a1] = 1
        newone[a2] = 2
        if(case == 1):
            newone[11] = 3
            newone[w300[s3[0]]] = 3
            newone[3] = 4
            newone[w400[s4[0]]] = 4
            newone[w300[s3[1]]] = 5
            newone[w400[s4[1]]] = 5
            newone[w300[s3[2]]] = 6
            newone[w300[s3[3]]] = 6
            newone[w300[s3[4]]] = 7
            newone[w600[s6[0]]] = 7
            newone[w300[s3[5]]] = 8
            newone[w600[s6[1]]] = 8
            newone[w400[s4[2]]] = 9
            newone[a3] = 9
        if(case == 2):
            newone[11] = 3
            newone[3] = 3
            newone[w300[s3[0]]] = 4
            newone[w300[s3[1]]] = 4
            newone[w300[s3[2]]] = 5
            newone[w400[s4[0]]] = 5
            newone[w300[s3[3]]] = 6
            newone[w400[s4[1]]] = 6
            newone[w300[s3[4]]] = 7
            newone[w600[s6[0]]] = 7
            newone[w300[s3[5]]] = 8
            newone[w600[s6[1]]] = 8
            newone[w400[s4[2]]] = 9
            newone[a3] = 9
        if(case == 3):
            newone[11] = 3
            newone[w400[s4[0]]] = 3
            newone[w300[s3[0]]] = 4
            newone[w300[s3[1]]] = 4
            newone[3] = 5
            newone[w400[s4[1]]] = 5
            newone[w300[s3[2]]] = 6
            newone[w300[s3[3]]] = 6
            newone[w300[s3[4]]] = 7
            newone[w600[s6[0]]] = 7
            newone[w300[s3[5]]] = 8
            newone[w600[s6[1]]] = 8
            newone[w400[s4[2]]] = 9
            newone[a3] = 9
    ss5 = []
    while(len(ss5) < 3):
        x = random.randint(1, 3)
        if x not in ss5:
            ss5.append(x)
    ss3 = []
    while(len(ss3) < 6):
        x = random.randint(1, 6)
        if x not in ss3:
            ss3.append(x)
    ss4 = []
    while(len(ss4) < 3):
        x = random.randint(1, 3)
        if x not in ss4:
            ss4.append(x)
    ss6 = []
    while(len(ss6) < 2):
        x = random.randint(1, 2)
        if x not in ss6:
            ss6.append(x)
    if(case == 4):
        newone[w500[ss5[0]]] = 1
        newone[w600[ss6[0]]] = 2
        newone[11] = 3
        newone[3] = 3
        newone[w400[ss4[0]]] = 4
        newone[w300[ss3[0]]] = 4
        newone[w300[ss3[1]]] = 5
        newone[w300[ss3[2]]] = 5
        newone[w300[ss3[3]]] = 6
        newone[w300[ss3[4]]] = 6
        newone[w300[ss3[5]]] = 7
        newone[w600[ss6[1]]] = 7
        newone[w400[ss4[1]]] = 8
        newone[w500[ss5[1]]] = 8
        newone[w400[ss4[2]]] = 9
        newone[w500[ss5[2]]] = 9
    if(case == 5):
        newone[w500[ss5[0]]] = 1
        newone[w600[ss6[0]]] = 2
        newone[11] = 3
        newone[w300[ss3[0]]] = 3
        newone[w400[ss4[0]]] = 4
        newone[3] = 4
        newone[w300[ss3[1]]] = 5
        newone[w300[ss3[2]]] = 5
        newone[w300[ss3[3]]] = 6
        newone[w300[ss3[4]]] = 6
        newone[w300[ss3[5]]] = 7
        newone[w600[ss6[1]]] = 7
        newone[w400[ss4[1]]] = 8
        newone[w500[ss5[1]]] = 8
        newone[w400[ss4[2]]] = 9
        newone[w500[ss5[2]]] = 9
    here1 = []
    for num in range(1, 16):
        here1.append(newone[num])
    return here1

# %%


mess = [300,   500,   200,   500, 300,   400,  300,
        300,  400, 600,   100, 600,   500,  400,  300,  300]


class Individual(object):
    def __init__(self):
        self.arrange = self.generator()
        self.fitness = self.evaulate()

    def generator(self):
        return gen_1()

    def evaulate(self):
        individual = self.arrange
        sim = 0  # 亲缘度
        for furnace_id in range(1, 10):
            material_id_lst = [index for index,
                               v in enumerate(individual) if v == furnace_id]
            # 放入一个窖中的所有原料id

            # 包的重量符合加工窖的载重
            if len(material_id_lst) == 1:  # 独立成包的的亲缘度为10
                sim = sim + 10
            else:  # 组合成包的，亲缘度为两两组合的均值
                sim_tmp = 0
                sum_tmp = 0
                for row, col in itertools.combinations(material_id_lst, 2):
                    sim_tmp = sim_tmp + relation[row+1][col+1]
                    sum_tmp = sum_tmp + 1
                sim = sim + int(sim_tmp / sum_tmp)  # 亲缘度取整
        return sim

    def muted_gene(self):
        temp = self.arrange
        self.arrange = self.generator()

    def mate(self):
        room = []
        sum = 0
        index = []
        for i in range(1, 10):
            current_index = [j for j in self.arrange if i == j]
            index.append(current_index)
            for j in current_index:
                sum += mess[j]
            room.append(sum)
        for i in range(9):
            for j in range(i+1, 9):
                # print('i = ', i, 'j = ', j)
                if room[i] == room[j]:
                    temp = self.arrange
                    for ix in index[i]:
                        temp[ix+1] = j+1
                    for ix in index[j]:
                        temp[ix+1] = i+1
                    self.arragne = temp
                    break

# %%


Iter_num = 100
POPULATION_SIZE = 100
population = []

for _ in range(POPULATION_SIZE):
    ind = Individual()
    population.append(ind)

for i in range(Iter_num):
    population = sorted(population, key=lambda x: x.fitness, reverse=True)
    lst = [p.fitness for p in population]
    print(lst)

    s = int(10/10 * POPULATION_SIZE)

    for pop in population[:s]:
        pop.mate()

    for pop in population[10-s:]:
        # print('before: ', pop.arrange)
        pop.muted_gene()
        # print('after: ', pop.arrange)

    print('Generator: ', i, 'Fitness: ',
          population[0].fitness, '\n', 'Best Individual: ', population[0].arrange, '\n')


# %%
