from math import sqrt

if __name__ == "__main__":
    multiset = map(int, open('/home/sulab/Downloads/rosalind_pdpl.txt').read().strip().split())
    n = int(0.5 + 0.5 * sqrt(8.0 * len(multiset) + 1))
    print 'nval' 
    print n
    x = [0]
    x.append(max(multiset))
    multiset.remove(x[1])
    deltaSet = set(multiset)
    for candidate in deltaSet:
                if sum([(abs(candidate-member) in multiset) for member in x])  == len(x):
                    for member in x:
                          multiset.remove(abs(candidate-member))
                    x.append(candidate)
                    if len(x) == n: break
    x.sort()
    print ' '.join(map(str, x))
