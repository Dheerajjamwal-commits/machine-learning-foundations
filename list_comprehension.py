def evlist(l):
    return [i for i in l if i%2==0]

a=list(map(int,input("Enter NUmbers: ").split(" ")))
print(evlist(a))