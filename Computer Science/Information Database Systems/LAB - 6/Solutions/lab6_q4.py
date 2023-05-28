R = [ {'A' , 'B' ,'C'}  , {'A' , 'D' , 'E'} , {'B' , 'F'} , {'F' , 'G' ,'H'} ,  {'D' , 'I' ,'J'}]
def checkdp( myset):
      for r in R:
        if r == myset:
          return True 
          break
      return False 
FDs = {"AB":"C" , "A" : "DE" , "B":"F" , "F":"GH" , "D":"IJ"}
check = []
for keys,values in FDs.items():
  myset = set()
  for j in keys:
    myset.add(j)
  for j in values:
    myset.add(j)
  if checkdp(myset) :
    check.append(1)
print(check)
lenoffd = len(FDs)
if len(check) == lenoffd:
  print("yes !  , dependecny preserving")
def is_proper_subset(subset, superset):
    return set(subset).issubset(set(superset)) and set(subset) != set(superset)
Attributes = [ 'A', 'B' ,'C' , 'D' ,'E','F','G','H','I','J']
def in_2nf(fds , r):
  cand_key = set()
  Non_prime = set()
  for key in fds:
    for keys in key:
      cand_key.add(keys)
  for i in Attributes:
    if (i not in cand_key) and (i in r):
      Non_prime.add(i)
  flag2nf = 1 
  for keys , values in fds.items():
    flag = 1 
    for sepval in values:
      if sepval not in Non_prime:
        flag = 0 
    if flag == 1:
      myset = set()
      for char in keys:
        myset.add(char)
      if is_proper_subset(myset , cand_key):
        print(" partial dependecny for ")
        print( keys , "->> " , values)
        flag2nf =0
  atset = set() 
  for rr in r:
    atset.add(rr)
  if flag2nf == 1:
    print("Given Relation r with attributes " , atset , " is in 2NF with key as " , cand_key , " and non prime attributes as  " , Non_prime)
    print()
for r in R:
  fds = {}
  for i , j  in FDs.items():
    tempset = set()
    for key in i:
      tempset.add(key)
    for val in j:
      tempset.add(val)
    if(tempset.issubset(r)):
      fds[i] = j 
  in_2nf(fds , r)
Attributes = [ 'A', 'B' ,'C' , 'D' ,'E','F','G','H','I','J']
def in_3nf(fds , r):
  cand_key = set()
  Non_prime = set()
  prime = set()
  for key in fds:
    for keys in key:
      cand_key.add(keys)
  for i in Attributes:
    if (i not in cand_key) and (i in r):
      Non_prime.add(i)
    else:
      prime.add(i)
  flag3nf = 0 
  for keys , values in fds.items():
    keyset = set()
    valset = set()
    for key in keys:
      keyset.add(key)
    for val in values:
      valset.add(val)
    if cand_key.issubset(keyset) or valset.issubset(prime): 
      flag3nf = 1; 
  atset = set()
  for rr in r:
    atset.add(rr)
  if flag3nf == 1:
    print("Given Relation r with attributes " , atset , " is in 3NF with key as " , cand_key )
    print()
for r in R:
  fds = {}
  for i , j  in FDs.items():
    tempset = set()
    for key in i:
      tempset.add(key)
    for val in j:
      tempset.add(val)
    if(tempset.issubset(r)):
      fds[i] = j 
  in_3nf(fds , r)
Attributes = [ 'A', 'B' ,'C' , 'D' ,'E','F','G','H','I','J']
def in_BCNF(fds , r):
  cand_key = set()
  Non_prime = set()
  prime = set()
  for key in fds:
    for keys in key:
      cand_key.add(keys)
  for i in Attributes:
    if (i not in cand_key) and (i in r):
      Non_prime.add(i)
    else:
      prime.add(i)
  flag3nf = 0 
  for keys , values in fds.items():
    keyset = set()
    valset = set()
    for key in keys:
      keyset.add(key)
    for val in values:
      valset.add(val)
    if cand_key.issubset(keyset): 
      flag3nf = 1; 
  atset = set()
  for rr in r:
    atset.add(rr)
  if flag3nf == 1:
    print("Given Relation r with attributes " , atset , " is in BCNF with key as " , cand_key )
    print()
  else:
    print("it is not in bcnf ")
for r in R:
  fds = {}
  for i , j  in FDs.items():
    tempset = set()
    for key in i:
      tempset.add(key)
    for val in j:
      tempset.add(val)
    if(tempset.issubset(r)):
      fds[i] = j 
  in_BCNF(fds , r)