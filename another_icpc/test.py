def wow(*n):
    new = " ".join(list(map(str,n)))
    print(f"wow in {new}")



a = lambda func,*a : (print("a"),func(*a))
b = lambda func,*b : (print("b"),func(*b))
c = lambda func,*c : (print("c"),func(*c))
d = lambda func,*d : (print("d"),func(*d))
e = lambda func,*e : (print("e"),func(*e))
f = lambda func,*f : (print("f"),func(*f))
g = lambda func,*g : (print("g"),func(*g))
h = lambda func,*h : (print("h"),func(*h))
i = lambda func,*i : (print("i"),func(*i))
j = lambda func,*j : (print("j"),func(*j))
k = lambda func,*k : (print("k"),func(*k))
l = lambda func,*l : (print("l"),func(*l))
m = lambda func,*m : (print("m"),func(*m))
n = lambda func,*n : (print("n"),func(*n))
o = lambda func,*o : (print("o"),func(*o))
p = lambda func,*p : (print("p"),func(*p))
q = lambda func,*q : (print("q"),func(*q))
r = lambda func,*r : (print("r"),func(*r))
s = lambda func,*s : (print("s"),func(*s))
t = lambda func,*t : (print("t"),func(*t))
u = lambda func,*u : (print("u"),func(*u))
v = lambda func,*v : (print("v"),func(*v))
w = lambda func,*w : (print("w"),func(*w))
x = lambda func,*x : (print("x"),func(*x))
y = lambda func,*y : (print("y"),func(*y))
z = lambda func,*z : (print("z"),func(*z))

z(
    y,x,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a,wow,90,80,70,60,50,40,30,20,10
)
