import numpy as np

def magnitude(vector):
    squqred_sum = np.sum(vector ** 2)
    return np.sqrt(squqred_sum)

def vector_projection(a, b):
    # b project on a
    scale_projection = (a.dot(b)) / magnitude(a)
    return scale_projection * (a / magnitude(a))

def GramSchmidt(vectors):
    basis = []
    for vector in vectors:
        v = vector
        v -= np.sum(vector_projection(b, vector) for b in basis)
        v /= magnitude(v)
        basis.append(v)
    return np.array(basis)







