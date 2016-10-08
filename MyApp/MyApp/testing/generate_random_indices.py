import random
import os.path


def GenerateRandomIndices(count):
    fname = os.path.join(os.path.dirname(__file__),
                         '../data/random_indices.txt')
    with open(fname, 'w') as f:
        rlist=' '.join([str(i) for i in
                          random.sample(range(0, 568454-1), count)])
        f.write(rlist)
        
