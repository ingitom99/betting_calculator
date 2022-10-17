import numpy as np

def betting(B, Ma, P):
    Ia = (P + B)/Ma
    Ib = B - Ia
    Mb = B/Ib
    return np.array([Mb, Ia, Ib])
