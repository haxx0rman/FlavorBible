import json
import time

import numpy as np
def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return int(distance[row][col])

def find(s, data):
    high = 99
    best_guess = ""
    for item in data.keys():
        #print(item)
        dist = levenshtein_ratio_and_distance(s, item)
        if dist < high:
            best_guess = item
            high = dist
            #print("Best Guess: " + best_guess)
            #print("Distance: " + str(dist))
    return best_guess

def mutuals(l1, l2):
        mutuals = []
        for i in l1:
            if i in l2:
                mutuals.append(i)
        return mutuals


with open('data.json') as f:
    data = json.load(f)

while True:
    time.sleep(.01)

    inp = input("Type in a flavor: ")
    for x in range(0, 50):
        print("\n")
    if ", " in inp:
        inp = inp.split(", ")
        #print(inp)
        print("Searching for:")
        for i in range(0, len(inp)):
            inp[i] = find(inp[i], data)
            print(inp[i])

        muts = data[inp[0]]

        for x in range(0, 2):
            print("\n")
        print("Finding pairings...")
        for i in inp:
            muts = mutuals(muts, data[i])
            print(i)

        for i in muts:
            print(i)
    else:
        inp = find(inp, data)
        print("Searching for:")
        print(inp)
        for i in data[inp]:
            print(i)
