x = "32"
y = "31"

z = 27
a = 26
s = 25
f = 3

g = 20.5
h = 3.5
j = 27.5

if z < a :
    print(z)
else:
    print(a)

if z > a :
    print(z)
else:
    print(a)

if z <= a :
    print(z)
else:
    print(a)

if z >= a :
    print(z)
else:
    print(a)

if z != a :
    print(z)
else:
    print(a)

if s < f :
    print(s)
elif s != f :
    print(s)
else:
    print(f)

if s < f :
    print(s)
elif s > f :
    print(s)
else:
    print(f)

if s < f :
    print(s)
elif s != f :
    print(s)
else:
    print(f)

if a < f :
    print(a)
elif f > a :
    print(a)
else:
    print(f)

if a < s :
    print(a)
elif a != s :
    print(a)
else:
    print(s)

if z < f :
    print(z)
elif z != f :
    print(z)
else:
    print(f)


if z > a :
    print(z)
elif z != a :
    print(z)
else:
    print(a)

if z != f :
    print(z)
elif z < f :
    print(z)
else:
    print(f)

if z < s :
    print(z)
elif z != s :
    print(z)
else:
    print(s)

if a < f :
    print(a)
elif a > f :
    print(a)
else:
    print(f)


if g < h :
    print(g)
else:
    print(h)

if g > h :
    print(g)
else:
    print(h)

if g <= h :
    print(g)
else:
    print(h)

if g >= h :
    print(g)
else:
    print(h)

if x != y :
    print(h)
else:
    print(g)

if g < h :
    print(g)
elif g != h :
    print(g)
else:
    print(h)

if g != h :
    print(g)
elif x < y :
    print(g)
else:
    print(h)

if g < h :
    print(g)
elif g != h:
    print(g)
else:
    print(h)

if g < h :
    print(g)
elif g > h :
    print(g)
else:
    print(h)


if (z>0 or a>0) :
    print(z,a)
else:
    print(s,f)

if (z>a and s>f) :
    print(z,s)
else:
    print(a,f)

if not (z>a and s>f) :
    print(a,f)
else:
    print(z,s)

if (z>(s+30) or a>(f+30)) :
    print(z,a)
else:
    print(s,f)

if (z!=a and s!=f) :
    print(z,s)
else:
    print(a,f)

if not (z<-a and s<-f) :
    print(z,s)
else:
    print(a,f)

if (z>(s+f) or a>(f+s)) :
    print(z,a)
else:
    print(s,f)

if (z<=a and s<=f) :
    print(z,s)
else:
    print(a,f)

if not (z>=a and s>=f) :
    print(z,s)
else:
    print(a,f)

if not (z>a and s>f) :
    print(z,s)
elif (z!=a and s!=f) :
    print(z, s)
else:
    print(a,f)

age = int(input("Введите свой возрост: "))
if age < 30 :
    print(age)
else:
    pass

age = int(input("Введите свой возрост: "))
if age > 30 :
    print(age)
else:
    pass

age = int(input("Введите свой возрост: "))
if age == 30 :
    print(age)
else:
    pass

A = int(input("Введите свой возрост: "))
import random
V = random.randint(1, 100)
if A < V :
    print("Вы ввели число =", A, "которое <", V)
elif A > V :
    print("Вы ввели число =", A, "которое >", V)
elif A == V :
    print("Вы ввели число =", A, "которое =", V)
else :
    pass

A = int(input("Введите свой возрост: "))
import random
V = random.randint(1, 100)
W = random.randint(1, 100)
if A < V and A < W:
    print("Вы ввели число =", A, "которое <", V, "и <", W)
else :
    pass
if A < V and A == W:
    print("Вы ввели число =", A, "которое <", V, "и =", W)
else :
    pass
if A < V and A > W:
    print("Вы ввели число =", A, "которое <", V, "и >", W)
else :
    pass
if A > V and A < W:
    print("Вы ввели число =", A, "которое >", V, "и <", W)
else :
    pass
if A > V and A == W:
    print("Вы ввели число =", A, "которое >", V, "и =", W)
else :
    pass
if A > V and A > W:
    print("Вы ввели число =", A, "которое >", V, "и >", W)
else :
    pass
if A == V and A < W:
    print("Вы ввели число =", A, "которое =", V, "и <", W)
else :
    pass
if A == V and A == W:
    print("Вы ввели число =", A, "которое =", V, "и =", W)
else :
    pass
if A == V and A > W:
    print("Вы ввели число =", A, "которое =", V, "и >", W)
else :
    pass




