"""
bunch of alg and functions for validate parentheses , the number of valid parentheses
or generating the valid parentheses


"""
def gen(n):
	ans=[]
	res=[]
	def solve(o,c):
		if o==c==n:
			res.append("".join(ans))
			return
		if o<n:
			ans.append("(")
			solve(o+1,c)
			ans.pop()
		if c<o:
			ans.append(")")
			solve(o,c+1)
			ans.pop()
	solve(0,0)
	return res

fact = lambda x : 1 if x < 2 else x*fact(x-1)
def count(n):
	upper=fact(2*n)
	lower=fact(n)*fact(n+1)
	return upper//lower

def is_pair(l,r):
	if l=="(" and r==")":
		return True
	return False
def check(n):
	stack=[]
	for t in n:
		if stack and is_pair(stack[-1],t):
			stack.pop()
		else:
			stack.append(t)
	if len(stack) == 0:
		print(f"{n} is True")
	else:
		print(f"{n} is False")


if __name__ == "__main__":
   n=int(input("Num : "))
    print(count(n))
    res=gen(n)
    print(res)
    print(len(res))

    for word in res:
        check(word)


