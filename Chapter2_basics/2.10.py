#A = mass_number
#Z = atomic_number
#B = binding_energy
import numpy as np



def a_5 (mass_number,atomic_number):
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    A = mass_number
    Z = atomic_number
    if A%2 != 0:
        a5 = 0
    elif A%2 == 0 and Z%2 ==0:
        a5 = 12
    elif A%2 == 0 and Z%2 != 0:
        a5 = -12

    B = a1*A - a2*A**(2/3) - a3*(Z**2)/A**(1 / 3) - a4*(A-2*Z)**2 / A + a5 / A**(1/2)

    B_per_nucleon = B/A
    return B, B_per_nucleon

print(a_5(58,28))


def a_5 (atomic_number):
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    Z = atomic_number

    A_list = list(range(Z,3*Z+1))
    binding_energies = []
    binding_per_nuce = []

    for a in A_list:

        if A%2 != 0:
            a5 = 0
        elif A%2 == 0 and Z%2 ==0:
            a5 = 12
        elif A%2 == 0 and Z%2 != 0:
            a5 = -12

        B = a1*A - a2*A**(2/3) - a3*(Z**2)/A**(1 / 3) - a4*(A-2*Z)**2 / A + a5 / A**(1/2)
        binding_energies.append(B)
        B_per_nucleai.append(B / A)

    most_stable = max(bin_per_nucleai)
    A_of_most_stable = A_list[binding_energies.index(max(binding_energies))]

    return most_stable, A_of_most_stable, binding_energies


    B_per_nucleon = B/A
    return B, B_per_nucleon






