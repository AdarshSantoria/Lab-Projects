R = "ABCDE"
F = {'A':'B', 'B':'C', 'C':'D'}
def all_subsets(string):
    n = len(string)
    subsets = set()
    for i in range(2 ** n):
        subset = ""
        for j in range(n):
            if i & (1 << j):
                subset += string[j]
        if(len(subset) != 0): 
            subsets.add(subset)
    return subsets
subsets = all_subsets(R)
def closure(X):
    X_plus = set(X)
    addition = True
    while addition:
        addition = False
        for key, value in F.items():
            if set(key).issubset(X_plus):
              for i in value:
                if i not in X_plus:
                    X_plus.add(i)
                    addition = True        
    return X_plus
for attribute in subsets:
    print(f"{attribute} -> {closure(attribute)}")
