import numpy as np
from GramSchmidtProcess import *

vectors = np.array([[0, 3, 4],
                    [1, 0, 1],
                    [1, 1, 3],], dtype = float)

print(GramSchmidt(vectors))