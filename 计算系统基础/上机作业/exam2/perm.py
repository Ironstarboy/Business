print(*map(lambda x:' '.join(map(lambda y:str(y),x)),sorted(set((__import__("itertools")).permutations([int( i) for i in [input(),input().split(' ')][1]])))),sep='\n')