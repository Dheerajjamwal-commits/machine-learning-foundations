# Exercise 1: Write a function that takes a list and returns only even numbers using list comprehension 
def evlist(l):
    return [i for i in l if i%2==0]

a=list(map(int,input("Enter NUmbers: ").split(" ")))
print(evlist(a))

# Exercise 2: Write a function that takes a dictionary and returns a new dict with values doubled

def ddic(d):
    return {key : value *2 for (key,value) in d.items()}
dictionary={"A":10,"B":35,"C":50,"D":90}
print(ddic(dictionary))

# Exercise 3: Use map and filter together filter even numbers then square them 
sample=[1,2,3,4,5,6,7,9,0,44]
out=list(map(lambda x:x**2,filter(lambda x : x % 2 == 0,sample)))
print(out)

