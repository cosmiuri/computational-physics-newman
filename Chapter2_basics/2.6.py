import numpy as np

def madelung_constant(distance, number):

    e = -1.602176634e-19 # electron chanrge on coulomb
    e_0 = 8.8541878128e-12 # permittivity of the vacuum
    V_total = 0 # total electric potential
    a = distance
    L = number

    for i in range (-L,L+1):
        for j in range (-L,L+1):
            for k in range (-L,L+1):

                if i ==0 and j ==0 and k ==0:
                    continue
                elif abs(i+j+k)%2==0:
                    V_total += e / (4*np.pi*e_0*a*np.sqrt(i**2+j**2+k**2))
                else:
                    V_total -= e / (4*np.pi*e_0*a*np.sqrt(i**2+j**2+k**2))

    M = (V_total*4*np.pi*e_0*a) / e

    return M

#print(madelung_constant(0.005,10))

a = madelung_constant(0.005,10)

print(a)

