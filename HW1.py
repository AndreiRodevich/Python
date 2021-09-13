name = "Andrei"
age = 27
weight = 75.5
height = bytes([180, 181, 182])
x = [1, 2, 3]
y = ('a', )
z = {1, 2, 3}
f= frozenset([1, 2, 3])
d = {"MINSK":"BELARUS"}

print(name,(type(name)))
print(age,(type(age)))
print(weight,(type(weight)))
print(height,(type(height)))
print(x,(type(x)))
print(y,(type(y)))
print(z,(type(z)))
print(f,(type(f)))
print(d,(type(d)))

name1 = "Julia"
name2 = "Daniel"
name3 = name1 + name2
print(name3)

age1 = 27
age2 = 3
age3 = age1 + age2
print(age3)

age4 = age1 / age2
print(age4)

age5 = age1 * age2
print(age5)

age6 = age1 % age2
print(age6)

