t11 = [14.27,22.98,13.40,39.35,33.57,32.22,23.96,19.83,16.07]
t12 = [60.90,89.70,59.55,39.32,33.54,32.26,79.00,59.65,51.54]
t21 = [19.47,29.66,61.43,25.30,20.94,20.31,28.31,22.99,18.73]
m1 = [213.19,212.84,210.35]
m2 = [112.31,111.99,109.55]

def energy(t, m):
    v = 1.03 * 10 / t
    energy = 0.5 * m * v ** 2 * 0.001
    return energy

def momentum(t, m):
    v = 1.03 * 10 / t
    momentum = v * m * 0.001
    return momentum

for i in [1,2,3]:
    print("第",i,"次")
    for j in [1,2,3]:
        print("Number:",j)
        E1 = energy(t21[(i-1)*3+j-1], m1[i-1])
        E2 = energy(t12[(i-1)*3+j-1], m1[i-1]) + energy(t11[(i-1)*3+j-1], m2[i-1])
        print("E1 = ",  E1 )
        print("E2 = ",  E2 )
        print("能量损失率：",(E1 - E2)/E1)
        P1 = momentum(t21[(i-1)*3+j-1], m1[i-1])
        P2 = momentum(t12[(i-1)*3+j-1], m1[i-1]) + momentum(t11[(i-1)*3+j-1], m2[i-1])
        print("P1 = ",  P1 )
        print("P2 = ",  P2)
        print("动量损失率",(P1-P2)/P1)
        print("Number:",j)
        print()
    print("************")
