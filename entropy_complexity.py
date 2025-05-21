import numpy as np
from itertools import permutations

#Shannon's entropy
def entropy(P):
  P = P[P != 0]
  return - np.sum(P * np.log(P))

#Normalized Shannon's entropy
def normalized_entropy(P):
  N = len(P)
  P_e = np.ones(N) / N

  S_max = entropy(P_e)
  S = entropy(P)
  return S / S_max


 #Jensen-Shannon divergence
def divergence(P_1, P_2, Q_0):
  return Q_0 * (
                entropy((P_1 + P_2) / 2) -
                entropy(P_1) / 2 -
                entropy(P_2) / 2
                )

#Normalizing constant
def Q_0(dist):
  #len(dist) = D!

  return 1 / (np.log(2 * len(dist)) +
              (len(dist) + 1) * np.log(1 / (len(dist) + 1)) /  len(dist) / 2  -
              np.log(len(dist)) / 2)

#Complexity
def complexity(P):
  H_S = normalized_entropy(P)

  N = len(P)
  P_e = np.ones(N) / N


  Q_J = divergence(P, P_e, Q_0(P))

  return Q_J * H_S




## This is the function to get the distribution from time series ##
def get_distribution(time_series, D=3):
  M = len(time_series)

  #Get the permutation variants and get the indices for them
  perms = list(permutations(range(D)))
  perms_to_idx = dict(zip(perms, range(len(perms))))

  #Preare the array for distribution
  distribution = np.zeros(len(perms_to_idx))

  #For every z-vector add 1 to the permutation count
  for i in range(M - D + 1):
    z_vector = time_series[i:i+D]
    permut = tuple(np.argsort(z_vector))
    distribution[perms_to_idx[permut]] += 1

  #Normalize
  distribution /= (M - D + 1)
  return distribution

## Compute entropy-complexity for a given t.s. ##
def entropy_complexity_time_series(time_series, D):
  P = get_distribution(time_series, D=D)
  return normalized_entropy(P), complexity(P)
