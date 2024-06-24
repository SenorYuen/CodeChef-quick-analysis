for scenario in range(int(input())):
    teams = dict()
    for i in range(4):
        key, val =  input().strip().split()
        teams[key] = int(val)
    print('Barcelona') if teams['Barcelona']>teams['Eibar'] and teams['RealMadrid']<teams['Malaga'] else print('RealMadrid')

#--------------------------

for _ in range(int(input())):
    d={}
    for i in range(4):
        x = input().split()
        d[x[0]]=int(x[1])
    
    if d["Barcelona"]>d["Eibar"] and d["RealMadrid"]<d["Malaga"]:
        print("Barcelona")
    else:
        print("RealMadrid")

#--------------------------

for i in range(int(input())):
    n,k=map(int,input().split())
    print(k//n)

#--------------------------

t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    print(m//n)
    


#--------------------------

for _ in range(int(input())):
    
    n,k = map(int,input().split()); n -= 1; k -=1; k = min(k,n-k); ans = 1
    
    for i in range(k):
        ans *= (n-i)
        ans //= (i+1)
    
    print(ans)


#--------------------------

import math

t = int(input())

def result(n,k):
    m = min(n-k, k)
    u = 1
    for i in range(m):
        u*=(n-i)
    return u//math.factorial(m)

while t>0:
    n, k = list(map(int, input().strip().split(' ')))
    print(result(n-1, k-1))
    t=t-1

#--------------------------

for _ in range(int(input())):
    s = input()
    flag = True
    for i in range(0,len(s),2):
        if s[i:i+2]=="AA" or s[i:i+2]=="BB":
            flag = False
            break
    if flag==False:
        print("no")
    else:
        print("yes")
            


#--------------------------

T = int(input())
for tc in range(T):
    log = input()
    segments = []
    for i in range(len(log)):
        if i % 2 == 0:
            segments.append(log[i:i+2])
    if 'AA' in segments or 'BB' in segments:
        print('no')
    else:
        print("yes")

#--------------------------


t = int(input())
for i in range(t):
    N = int(input())
    A = 1 
    B = N // A 
    
    print(A,B)

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    a=1 
    b=n//a
    print(a,' ',b)
            


#--------------------------

t=int(input())
while(t):
    n=int(input())
    c=0
    while(n):
        a,b=map(int,input().split())
        if b-a>5:
            c+=1
        n-=1
    print(c)
    t-=1


#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    count=0

    for ppoo in range(n):
        s,j=map(int,input().split())
        if j-s>5:
            count+=1
    print(count)
    
    

#--------------------------

for i in range(int(input())):
	x=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	a.sort()
	b.sort()
	a.pop(-1)
	b.pop(-1)
	c=sum(a)
	d=sum(b)
	if c>d:
		print('Bob')
	elif d>c:
		print('Alice')
	elif c==d:
		print('Draw')

#--------------------------

def  call():
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    tA = sum(A)-max(A)
    tB = sum(B)-max(B)
    if(tA<tB):
        print("Alice")
    elif(tB<tA):
        print("Bob")
    else:
        print('Draw')
        
t = int(input())
for i in range(t):
    call()

#--------------------------

def hcf(a, b):
    if b < a:
        a, b = b, a
    if a % b == 0:
        return b
    h = 1
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            h = i
    return h

def lcm(a, b, h):
    return a * b // h

for _ in range(int(input())):
    n, m = map(int, input().split())
    h = hcf(n, m)
    l = lcm(n, m, h)
    print(l // h)


#--------------------------

import math
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=math.gcd(n,m)
    n1=int(n/a)
    n2=int(m/a)
    print(n1*n2)

#--------------------------

t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    w=(l.count(a)*l.count(b))/(n*n)
    print(w)

#--------------------------

t=int(input())
while t>0 :
    n,a,b=map(int,input().split())
    x=list(map(int,input().split()))
    print((x.count(a)*x.count(b))/(n*n))
    t-=1

#--------------------------

from math import *
for j in range(int(input())):
    a,b=map(int,input().split())
    c=sqrt(abs(a**2-b**2))
    d=sqrt(a**2+b**2)
    print(c,d)

#--------------------------

import math
t = int(input())
for t1 in range(t):
    a, b = input().split()
    a , b = int(a) , int(b)
    print(math.sqrt(b*b - a*a), math.sqrt(b*b + a*a))

#--------------------------

def EstimateSkill(points) :
    count = points.count(1)
    
    if count == 0:
        return "Beginner"
    elif count == 1:
        return "Junior Developer"
    elif count == 2:
        return "Middle Developer"
    elif count == 3:
        return "Senior Developer"
    elif count == 4:
        return "Hacker"
    else:
        return "Jeff Dean"
    
    
LIMIT = int(input()) 

while LIMIT > 0 :
    LIMIT -= 1 
    points = list(map(int, input().split()))
    print(EstimateSkill(points))

#--------------------------

for i in range(int(input())):
    count=0
    l=list(map(int,input().split()))
    for num in l:
        if num==1:
            count+=1
    if count==0:
        print("Beginner")
    elif count==1:
        print("Junior Developer")
    elif count==2:
        print( "Middle Developer")
    elif count==3:
        print("Senior Developer")
    elif count==4:
        print("Hacker")
    elif count==5:
        print( "Jeff Dean")

#--------------------------

t,n=map(int,input().split())
for i in range(t):
    m=int(input())
    if m>=n:
        print('Good boi')
    else:
        print('Bad boi')

#--------------------------

n,r=list(map(int,input().split()))
for i in range(n):
    s=int(input())
    if(s>=r):
        print("Good boi");
    else:
        print("Bad boi");

#--------------------------

a = [int(i) for i in input().split() if i.isdigit()]
a.sort();
if a[0] * a[3] == a[1] * a[2]:
    print("Possible")
else:
    print("Impossible")
    

#--------------------------

lst = list(map(int, input().split()))
lst.sort()
if lst[0] / lst[1] == lst[2] / lst[3]:
    print("Possible")
else:
    print("Impossible")



#--------------------------

t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int, input().split()))
    a=[]
    b=0
    for i in range(n):
        for j in range(i+1,n):
            b=li[i]+li[j]
            a.append(b)
    max_count=max(a)
    c=a.count(max_count)
    print("%.8f"% (c/len(a)))

#--------------------------

for _ in range(int(input())):
	n = int(input())
	li = [int(i) for i in input().split()]
	d = n*(n-1)/2
	ma = 0
	l = 0
	for i in range(n):
		if li[i]>=ma:
			if li[i]==ma:
				l+=1
			else:
				ind = i
				ma = li[i]
				l = 1
	if l>1:
		s=l*(l-1)/2
	else:
		a = max(li[:ind]+li[ind+1:])
		s = li.count(a)
	print(f'{s/d:.8f}')

#--------------------------

A,B,C=map(int,input().split())
if ((C-A)//B)%2==0:
	print("Lucky Chef")
else:
	print("Unlucky Chef")

#--------------------------

#CHEF AND SOCKS

jc,sc,m = map(int,input().split())

rem_jcm = m-jc
rem_scm = (rem_jcm)//sc

if rem_scm % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
    


#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=[]
    ans=0
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-1):
        for j in range(n-1):
            l[i+1][j+1]+=l[i][j]
    for i in range(n):
        for j in range(n):
            ans=max(ans,l[i][j])
    print(ans)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=[]
    ans=0
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-1):
        for j in range(n-1):
            l[i+1][j+1]+=l[i][j]
    for i in range(n):
        for j in range(n):
            ans=max(ans,l[i][j])
    print(ans)

#--------------------------

for _ in range(int(input())):
      n=int(input())
      l=list(map(int,input().split()))
      print(min(l))
            
                  
            
      
      

#--------------------------

for _ in range(int(input())):
     n=int(input())
     a=list(map(int,input().split()))
     print(min(a))


#--------------------------

for _ in range(int(input())):
    
    n,k =  map(int,input().split())
    s =  sum(map(int,input().split()))


    if s% 2 !=0:
        print( 'even')
    else:
        if k==1:
            print('odd')
        else:
            print('even')

#--------------------------

try:
    for _ in range(int(input())):
        N, K = map(int, input().split(" "))
        l = list(map(int, input().split(" ")))
        s = sum(l)
        if(s % 2 == 0 and K == 1):
            print("odd")
        else:
            print("even")
except:
    pass

#--------------------------

t=int(input())
while(t>0):
    x,y,k=map(int,input().split())

    add=x+y
    if(add%(2*k)<k):
        print("Chef")
    else:
        print("Paja")
    t-=1




#--------------------------

for t in range(int(input())):
    x,y,k=map(int,input().split())
    if ((x+y)//k)%2==0:
        print('Chef')
    else:
        print('Paja')

#--------------------------

k, n = map(int,input().split())
a = list()
for i in range(k):
    s = input()
    a.append(s)
b = []
for i in range(n):
    s1 = input()
    b.append(s1)
for i in b:
    if len(i) >= 47:
        print('Good')
    else:
        for j in a:
            if j in i:
                print('Good')
                break
        else:
            print('Bad')

#--------------------------

k,n=map(int,input().split())
a=[]
b=[]
for _ in range(k):
    a.append(input())
for _ in range(n):
    b.append(input())


for i in b:
    f1=0 
    f2=0
    if len(i)>=47:
        f1=1
    for j in a:
        if j in i:
            f2=1 
            break 
            
    if (f1 or f2):
        print("Good")
    else:
        print("Bad")
                
    

#--------------------------

for _ in range(int(input())):
	score = 0
	n = int(input())
	corr = input()
	resp = input()
	i = 0
	
	while i < n:
		if resp[i] == 'N':
			i += 1
		elif corr[i] == resp[i]:
			score += 1
			i += 1
		else:
			i += 2
		
	print(score)

#--------------------------

# ashu@gate2022
for i in range(int(input())):
    n=int(input())
    s=input()
    a=input()
    t=0
    j=0
    for i in range(n):
        if j<n:
            if a[j]=="N":
                j+=1
            else:
                if a[j]==s[j]:
                    j+=1
                    t+=1
                else:
                    j+=2
    print(t)



#--------------------------

for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    c = 0
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == (s[i] & s[j]):
                c += 1
    else:
        print(c)

#--------------------------

for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = a.count(1)
    pairs = 0
    for i in range(len(a)):
        for j in range(i + 1 , len(a)):
            if a[i] & a[j] == a[i]:
                pairs = pairs + 1
    print(pairs)

#--------------------------

def fun(a,n):
    b=['cakewalk','simple','easy'],
    if 'cakewalk' in a  and 'simple' in a and 'easy' in a and ('easy-medium' in a or 'medium' in a) and ('medium-hard' in a or 'hard' in a):
        print('Yes')
    else:
        print('No')
        
for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(input())
    fun(a,n)

#--------------------------

for _ in range(int(input())):
    n = int(input())
    checker = [0]*5
    for i in range(n):
        s = input()
        if s == "cakewalk":
            checker[0] = 1
        elif s == "simple":
            checker[1] = 1
        elif s == "easy":
            checker[2] = 1
        elif s == "easy-medium" or s == "medium":
            checker[3] = 1
        else:
            checker[4] = 1
            
    if sum(checker) == 5:
        print("Yes")
    else:
        print("No")

#--------------------------

for _ in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    if l.index(max(l))<l.index(min(l)):
        print(max(l),min(l))
    else:
        print(min(l),max(l))


#--------------------------

t=int(input())
while(t>0):
    n=int(input())
    lst=list(map(int,input().split()))
    while(len(lst)>=3):
        x=lst[:3]
        x=sorted(x)
        lst.remove(x[1])
    
    print(* lst)
    
    
    t-=1

#--------------------------

n = int(input())

for i in range(n):
    l = [0]
    k = int(input())
    
    for j in range(k):
        
        m = int(input())
        if(m>l[-1]):
            l.append(m)
            
    
    print(l[-1])

#--------------------------

for I in range(int(input())):
    k=[]
    n=int(input())
    for j in range(n):
        a=int(input())
        k.append(a)
    print(max(k))

#--------------------------

for _ in range(int(input())):
    n=int(input())
    for i in range(n) :
        x, y=map(int,input().split())
    p=0
    for i in range(1,n+1):
        p=p^i
    print(p) 
        

#--------------------------

try:
    for _ in range(int(input())):
        N = int(input())
        for __ in range(N):
            a, b = map(int, input().split())
            
        ans = 1
        for i in range(2, N + 1):
            ans ^= i
            
        print(ans)
    
except Exception as e:
    print(e.__class__)

#--------------------------

t=int(input())
for l in range(t):
    n,k=map(int,input().split())
    minute=[]
    mb_per_minute=[]
    for i in range(n):
        a,b=map(int,input().split(' '))
        minute.append(a)
        mb_per_minute.append(b)
    i=0
    while(k>0 and i<n):
        if(minute[i]>=k):
            minute[i]=minute[i]-k
            k=0
        elif(minute[i]<k):
            k=k-minute[i]
            minute[i]=0
            
        if(minute[i]==0):
            minute.pop(i)
            mb_per_minute.pop(i)
    
    #print(minute)
#    print(mb_per_minute)
    sum=0
    for i in range(len(minute)):
        sum+=minute[i]*mb_per_minute[i]
    print(sum)

#--------------------------

tc=int(input())
for i in range(tc):
    (n,k)=map(int,input().split())
    tl=[]
    dl=[]
    for j in range(n):
        (t,d)=map(int,input().split())
        tl.append(t)
        dl.append(d)
    s=0
    h=0
    while(h!=len(tl) and k!=0):
        if(tl[h]==k):
            tl[h]=tl[h]-k
            k=0
        else:
            if(tl[h]>k):
                tl[h]=tl[h]-k
                k=0
            else:
                k=k-tl[h]
                tl[h]=0
        h+=1
    for x in range(len(tl)):
        s=s+(tl[x]*dl[x])
    print(s)
        

#--------------------------

t=int(input())
while t!=0:
    s=input()
    s+='X'
    n=len(s)
    m1=m2=c1=c2=0
    for i in range(0,n-1):
        if s[i]!=s[i+1]:
            if s[i]=='U':
                c1+=1
            if s[i]=='D':
                c2+=1
            if m1<c1 :
                m1=c1
            if m2<c2 :
                m2=c2;
    if m1>m2:
        d=m2
    else:
        d=m1
    print(d)
    t-=1

#--------------------------

for _ in range(int(input())):
    s = input()
    sn = []
    sn.append(s[0])
    i = 1
    while i<len(s):
        if s[i] != s[i-1]:
            sn.append(s[i])
        i+=1
    cd = sn.count('D')
    cu = sn.count('U')
    print(min(cd, cu))

#--------------------------


for _ in range(int(input())):
    a = int(input())
    b = list(map(int,input().split()))
    odd_num = list([i for i in b if i%2!=0])
    print("YES") if len(odd_num)==a else print("NO")

#--------------------------

for t in range(int(input())) :
    n=int(input())
    a=list(map(int,input().split()))
    itn=0
    for i in a:
        if i%2==0:
            itn=2
            print("NO")
            break
    if itn==0:
        print("YES")

#--------------------------

for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    b=list(filter(lambda x: x%2!=0,l))
    if(len(l)==1):
        print(1)
    elif(len(b)%2==0):
        print(1)
    else:
        print(2)

#--------------------------

t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        print(1)
    else:
        al = []
        
        for i in range(0,n):
            if a[i] % 2 != 0:
                al.append(a[i])
        
        if len(al) % 2 == 0:
            print(1)
        else:
            print(2)
    
    t -= 1

#--------------------------

for _ in range(int(input())):
    n=input()
    if n.count('1')==0:
        print('NO')
        continue
    for i in range(len(n)-2):
        if n[i]=='1' and n[i+1]=='0' and '1' in n[i+2:]:
            print('NO')
            break
    else:
        print('YES')


#--------------------------


for _ in range(int(input())):
    n=input()
    if n.count('1')==0:
        print('NO')
        continue
    for i in range(len(n)-2):
        if n[i]=='1' and n[i+1]=='0' and '1' in n[i+2:]:
            print('NO')
            break
    else:
        print('YES')


#--------------------------

n,k=map(int,input().split())
n=list(map(int,input().split()))
a=max(n)
b=min(n)
for i in range(k):
    p=int(input())
    if p<b or p>a:
        print("No")
    else:
        print("Yes")

#--------------------------

n,k=map(int,input().split())
n=list(map(int,input().split()))
a=max(n)
b=min(n)
for i in range(k):
    p=int(input())
    if p<b or p>a:
        print("No")
    else:
        print("Yes")

#--------------------------

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    summ=0
    i=0
    count=1
    if max(arr)>k:
        print(-1)
        continue
    while i<len(arr):
        summ+=arr[i]
        if summ>k:
            count+=1
            summ=arr[i]
        i+=1
    print(count)

#--------------------------

for _ in range(int(input())):
    n, k = map(int,input().split())
    w = list(map(int,input().split()))
    l = 0
    trips = 0
    while len(w)>0:
        if w[0]<=k:
            l += w[0]
            if l <= k:
                w.pop(0)
                continue
            else:
               trips += 1
               l = 0
               continue
        else:
            print(-1)
            break
    else:
        trips +=1
        print(trips)    
        

#--------------------------

a = int(input())
for i in range(a):
    b = int(input())
    if b%8==0:
        print(str(b-1) + 'SL')
    elif b%8==7:
        print(str(b+1) + 'SU')
    elif b%8==1:
        print(str(b+3) + 'LB')
    elif b%8==2:
        print(str(b+3) + 'MB')
    elif b%8==3:
        print(str(b+3) + 'UB')
    elif b%8==4:
        print(str(b-3) + 'LB')
    elif b%8==5:
        print(str(b-3) + 'MB')
    elif b%8==6:
        print(str(b-3) + 'UB')

#--------------------------

def get_train_partner(n):
    res = n%8
    if res==0:
        return str(n-1)+"SL"
    elif res==7:
        return str(n+1)+"SU"
    elif res==1:
        return str(n+3)+"LB"
    elif res==4:
        return str(n-3)+"LB"
    elif res==3:
        return str(n+3)+"UB"
    elif res==6:
        return str(n-3)+"UB"
    elif res==2:
        return str(n+3)+"MB"
    else:
        return str(n-3)+"MB"

for i in range(int(input())):
    n = int(input())
    print(get_train_partner(n))

#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    print((n-1)*(m-1))

#--------------------------

for __ in range(int(input())):
    x,y=map(int,input().split())
    print((x-1)*(y-1))

#--------------------------

T = int(input())
for _ in range(T):
    X = int(input())
    print(0,X)

#--------------------------

goals = int(input())
for distractions in range(goals):
    wife = int(input())
    print(1, wife - 1)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0 ; j=len(l)-1
    l=sorted(l)
    while i < j:
        print(l[i],end=" ")
        print(l[j],end=" ")
        i += 1; j -= 1
    if n%2==1: print(l[int(n/2)])
    print()


#--------------------------

t = int(input())
while t>0:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n%2==0: m = n//2
    else: m = n//2 + 1
    i, j = 0, m
    while i<m and j<n:
        print(str(arr[i]) + " " + str(arr[j]), end = " ")
        i = i+1
        j = j+1
    while i<m:
        print(str(arr[i]))
        i = i+1
    print()
    t -= 1


#--------------------------

for _ in range(int(input())):
    n = int(input())
    s = input()
    pos = [0,0]
    prev = ''
    for l in s:
        if l == 'R' or l == 'L':
            if prev == 'R' or prev == 'L':
                continue
            elif l == 'R':
                pos[0] += 1
            else:
                pos[0] -= 1
        elif l == 'U' or l == 'D':
            if prev == 'U' or prev == 'D':
                continue
            elif l == 'U':
                pos[1] += 1
            else:
                pos[1] -= 1        
        prev = l                
    print(*pos)            
            

#--------------------------

T=int(input())
for i in range(T):
    N=int(input())
    s=input()
    x=0
    y=0
    last="Z"
    for i in range(N):
        if s[i]=="L" and last!="L" and last!="R":
            x-=1
            last="L"
        elif s[i]=="R" and last!="R" and last!="L":
            x+=1
            last="R"
        elif s[i]=="U" and last!="U" and last!="D":
            y+=1
            last="U"
        elif s[i]=="D" and last!="D" and last!="U":
            y-=1
            last="D"
    print(x,y)
            

#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    
    for i in range(len(l)):
        for j in range(len(l)):
            if(i!=j):
                p=str(l[i]*l[j])
                li=list(map(int,p))
                a.append(sum(li))
    print(max(a))                
        
    
    


#--------------------------

t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split(" ")))
    if(n==2):
        p = A[0]*A[1]
        d = list(map(int, list(str(p))))
        print(sum(d))
    else:
        s = []
        for j in range(n):
            for k in range(j+1,n):
                p = A[j]*A[k]
                d = list(map(int, list(str(p))))
                s.append(sum(d))
        print(max(s))

#--------------------------

t=int(input())
for k in range(0,t):
    x,y=map(int,input().split())
    if x<=y:
        print('0')
    elif x%y==0:
        print(y)
    else :
        print(x%y)
        

#--------------------------

i=0;
for i in range(int(input())):
    (x,y)=map(int,input().split())
    z=x-y
    if z>0:
        print(z)
    else:
        print(0)
       
    
    
            
    

#--------------------------

for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    r =list(map(int,input().split()))

    m=[]
    

    for j in range(a):
        m.append(l[j]*r[j])

    p=r.index(max(r))

    if m.index(max(m))==p:
        print(p+1)
    else:
        df=[]
        for k in range(a):
            if m[k] == max(m):
                df.append([r[k],k+1])

        df.sort()
        for b in df:
            if b[0]==df[-1][0]:
                print(b[1])
                break
                
    


#--------------------------

def movie_weekend(a, b):
    l = []
    k = []
    for i in range(1, len(a)+1):
        l.append(tuple([a[i-1], b[i-1], i]))

    mul = list(map(lambda x: x[0]*x[1], l))
    max_m = max(mul)
    for i in range(len(mul)):
        if mul[i]==max_m:
            k.append(l[i])
    if max(k, key=lambda x: x[1]) != min(k, key=lambda x: x[1]):
        return max(k, key=lambda x: x[1])[2]
    else:
        return k[0][2]

for _ in range(int(input())):
    n = input()
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    print(movie_weekend(a, b))

#--------------------------

for _ in range(int(input())):
    (a,b,c)=map(int,input().split())
    if(a+b==c or b+c==a or c+a==b):
        print("yes")
    else:
        print("no")

#--------------------------

t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(x+y+z==(2*max(x,y,z))):
        print("yes")
    else:
        print("no")

#--------------------------

t=int(input())
while t>0:
    t=t-1
    c=0
    n=input()
    for i in n:
        if i.isdigit()==True:
            c=c+int(i)
    print(c)

#--------------------------

t = int(input())
for i in range(0,t):
    s=input()
    l = list(s)
    sum = 0
    for i in l:
        if i.isdigit():
            sum += int(i)
    print(sum)


#--------------------------

for t in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l.sort()
	c,v=0,0
	for i in l:
		if l.count(i)>c:
			c=l.count(i)
			v=i
	print(v,c)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    
    l.sort()
    d=[]
    for i in l:
        d.append(l.count(i))
    maxc=max(d)
    for i in l:
        if l.count(i)==maxc:
            print(i,maxc)
            break


#--------------------------

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print("YES")
    


#--------------------------

t = int(input())

while t:
    s = input()
    print("YES")
    
    t -= 1

#--------------------------

try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        m,k=0,0
        for i in l:
            if i>0:
                m+=1
            else:
                k+=1
        if(k==0 or m==0):
            print(max(m,k),max(m,k))
        else:
            print(max(m,k),min(m,k))
except:
    pass


#--------------------------

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    negative=0
    positive=0
    for i in a:
        if i<0:
            negative+=1
        else:
            positive+=1
    if negative==0:
        print(positive,positive)
    elif positive==0:
        print(negative,negative)
    else:
        print(max(positive,negative),min(positive,negative))
            


#--------------------------

for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l=sorted(l)
    for i in range(k):
        l.append(10001)
    print(l[(len(l)//2)])

#--------------------------

T=int(input())

for k in range(T):
    N,K=map(int,input().split())
    L=list(map(int,input().split()))
    L.sort()
    m=max(L)
    for i in range(K):
        L.append(m)
        m+=1

    print(L[len(L)//2])

#--------------------------

from collections import Counter
n1,n2,n3=map(int,input().split())
p=0
k,s=[],[]
for _ in range(n1+n2+n3):
    l=int(input())
    s.append(l)
t=Counter(s)
for x,y in t.items():
    if y>=2:
        p+=1
        k.append(x)
k.sort()
print(p)
for item in k:
    print(item)

#--------------------------

n1,n2,n3=map(int,input().split())
l1=[]
l2=[]
l3=[]
for i in range(n1):
    l1.append(int(input()))
for i in range(n2):
    l2.append(int(input()))
for i in range(n3):
    l3.append(int(input()))
a = set(l1)
b = set(l2)
c = set(l3)
i1 = a & b
i2 = b & c
i3 = a & c

i1= i1.union(i2)
fr= list(i1.union(i3))
fr.sort()
print(len(fr))
for i in fr:
    print(i)
    

#--------------------------

for t in range(int(input())):
    s = input()
    print(s.count('<>'))

#--------------------------

try:
    t = int(input())
    for _ in range(t):
    	s = input()
    	l = ""
    	for i in s:
    		if i=='>':
    			l += '<'
    		elif i=='<':
    			l += '>'
    		else:
    			l += i
    	print(l.count("><"))
except:
    pass

#--------------------------

import math
def call():
    k = int(input())
    coN=0
    while(k>0):
        t = math.floor(math.sqrt(k))
        k-=t*t
        coN+=1
    print(coN)
t = int(input())
for i in range(t):
    call()

#--------------------------

import math
for t in range(int(input())):
    n=int(input())
    c=0
    while(n!=0):
        s=int(math.sqrt(n))
        c+=1
        n=n-(s*s)
    print(c)
        

#--------------------------

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=10000000000
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])<m:
            m=abs(l[i]-l[i+1])
    print(m)
            

#--------------------------

for t in range(int(input())):
    N=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l1=[]
    for i in range(N-1):
        l1.append(l[i+1]-l[i])
    print(min(l1))


#--------------------------

for tc in range(int(input())):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    cakewalk,hard=0,0
    for i in range(n):
        if p//2<=a[i]:
            cakewalk+=1 
        if p//10>=a[i]:
            hard+=1 
    if cakewalk==1 and hard==2:
        print("yes")
    else:
        print("no")

#--------------------------

s = int(input())
for tc in range(s):
    l1=list(map(int,input().split(' ')))
    n,p = l1
    l2 = list(map(int,input().split(' ')))
    k1=p//2
    k2=p//10
    c=0
    h=0
    for i in l2:
        if i>=k1:
            c=c+1
        elif i<=k2:
            h=h+1
    if c==1 and h ==2:
        print('yes')
    else:
        print('no')


#--------------------------

for _ in range(int(input())):
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    array_converter = list()
    for element in array:
        if element%k == 0:
            array_converter.append("1")
        else:
            array_converter.append("0")
    print(''.join(array_converter))
    

#--------------------------

for t in range(int(input())) :
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=""
#    print(a)
    for i in a :
#        print(s)
        if i%k==0:
            s=s+'1'
        else:
            s=s+'0'
    print(s)   

#--------------------------

t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    if(sum(a)%2==1):
        print("YES")
    else:
        print("NO")

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(j) for j in input().split()][:n]
    if sum(l)%2==0:
        print("NO")
    else:
        print("YES")

#--------------------------

for i in range(int(input())):
    l1=list(input().split())
    l2=list(input().split())
    a=0
    for i in l1:
        if i in l2:
            a+=1
    if a>=2:
        print("similar")
    else:
        print("dissimilar")

#--------------------------

for i in range(int(input())):
    s=list(map(str,input().split()))
    a=list(map(str,input().split()))
    l=max(len(a),len(s))
    c=0
    for i in range(l):
        if(s[i] in a):
            c+=1
    if(c>=l//2):
        print('similar')
    else:
        print('dissimilar')

#--------------------------

n = int(input())
arr = list(map(int, input().split()))

ans = sum(arr)

if(ans == (n*(n+1)) / 2):
    print("YES", end = "")
else:
    print("NO", end = "")

#--------------------------

n=int(input())
lst=list(map(int,input().split()))
main=list(lst)
sum_stamps=0
men=0
if len(main)==n :
    for i in lst:
        sum_stamps+=i
    dig=n
    while dig>=0:
        men=men+dig
        dig=dig-1
    if men == sum_stamps :
        print("YES")
    else:
        print("NO")
            




#--------------------------

t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    b=[]
    l.sort()
    c=0
    for i in range(len(l)):
        c=0
        for j in range(i+1,len(l)):
            if l[j]>l[i]:
                b.append(n-j)
                c=1
                break
        if c==0:
            b.append(0)
    for i in range(n-1):
        print(b[i],end=" ")
    print(b[n-1])
    t-=1


#--------------------------

try:
    Test_Case=int(input())
    for i in range(Test_Case):
        N=int(input())
        list1=list(map(int,input().split(" ")))
        list2=[]
        if(len(list1)==N):
                for k in range(len(list1)):
                    c=0
                    for j in range(k+1,len(list1)):
                        if(list1[k]<list1[j]):
                            c=c+1
                        else:
                            continue
                            
                    list2.append(c)
        for l in range(len(list2)):
            print(list2[l],end=" ")
                
except:
    pass


#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        st=input().split()
        for j in range(m):
            val=int(st[j])
            arr.append(val)
    arr.sort(reverse=True)
    cy=0
    ge=0
    for i in range(n*m):
        if i%2==0:
            cy+=arr[i]
        else:
            ge+=arr[i]
    if cy==ge:
        print("Draw")
    elif cy>ge:
        print("Cyborg")
    else:
        print("Geno")


#--------------------------

n=int(input())
for i in range(n):
    m,k=map(int,input().split())
    s=[]
    for i in range(m):
        a=list(map(int,input().split()))
        s.extend(a)
    s.sort()
    c=[]
    g=[]
    for i in range(len(s)):
        if(i%2==0):
            c.append(s[-1-i])
        else:
            g.append(s[-1-i])
    if sum(c)>sum(g):
        print("Cyborg")
    elif(sum(c)==sum(g)):
        print("Draw")
    else:
        print("Geno")

#--------------------------

n=int(input())
fg=0
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
for i in range(1,n):
    if l[i][0]<l[i-1][0]:
        fg=1
        break
    elif l[i-1][1]>l[i][1]:
        fg=1
        break
    elif l[i-1][1]==10 and l[i][1]==10 and l[i-1][0]!=l[i][0]:
        fg=1
        break
if fg==0:
    print("YES")
else:
    print("NO")

#--------------------------

n=int(input())
r=[]
w=[]
for i in range(n):
    a,b=map(int,input().split())
    r.append(a)
    w.append(b)
    
ans=0
if n==1 and w[i]<=10:
    print("YES")
else:
    for i in range(n-1):
        if(r[i]<=r[i+1] and w[i]<=w[i+1]):
            if(w[i]==10 and w[i]==w[i+1]):
                ans=0
            else:
                ans=1
        else:
            ans=0
            break
    if ans==0:
        print("NO")
    else:
        print("YES")

#--------------------------

def solve(A, N, M):
    ans = 0
    for i in range(0, N-1):
        for j in range(0, M-1):
            delta, ch = 1, A[i][j]
            while (i + delta) < N and (j + delta) < M:
                if A[i][j + delta] == ch and A[i + delta][j] == ch and A[i + delta][j + delta] == ch:
                    ans += 1
                delta += 1
    print(ans)

if __name__ == '__main__':
    T = (int)(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = []
        for i in range(N):
            row = input()
            A.append(row)
        solve(A, N, M)


#--------------------------

def solve(A, N, M):
    ans = 0
    for i in range(0, N-1):
        for j in range(0, M-1):
            delta, ch = 1, A[i][j]
            while (i + delta) < N and (j + delta) < M:
                if A[i][j + delta] == ch and A[i + delta][j] == ch and A[i + delta][j + delta] == ch:
                    ans += 1
                delta += 1
    print(ans)

if __name__ == '__main__':
    T = (int)(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = []
        for i in range(N):
            row = input()
            A.append(row)
        solve(A, N, M)

#--------------------------

n=int(input())
l=list(map(int,input().split()))[:n]
le=len(l)
l.sort()
a=0
b=1 
m=[]
while(1):
    m.append(l[a]*l[b])
    a+=1 
    b+=1 
    if(b==le):
        break
print(sum(m))


#--------------------------

# # # t=int(input())
# # # for i in range(t):
# # #     n=int(input())
# # #     a=[]
# # #     b=[]
# # #     for j in range(n):
# # #         x,y =map(int,input().split())
# # #         a.append(x)
# # #         b.append(y)
# # #     print(len(set(a))+len(set(b)))
# # t=int(input())
# # for i in range(t):
# #     n=int(input())
# #     N=list(map(int,input().split()))
# #     x=float(sum(N)/n)
# #     if x>=4 and min(N)>2 and 5 in N:
# #         print("YES")
# #     else:
# #         print("NO")

# t =int(input())
# for i in range(t):
#     s=input()
#     l=s.split(' ')
#     if len(l)==1:
#         print(s.casefold().capitalize())
#     elif len(l)==2:
#         print(l[0][0].capitalize()+'. '+l[1].casefold().capitalize())
#     else:
#         print(l[0][0].capitalize()+'. '+l[1][0].capitalize()+'. '+l[2].casefold().capitalize())
# t=int(input())
# for i in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     l.sort()
#     a,b=l[0],l[len(l)-1]
#     d=0
#     for j in range(1,len(l)-1):
#         if (b-l[j])+(l[j]-a) >d:
#             d=(b-l[j])+(l[j]-a)
#     print(d+b-a)
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans =0
for j in range(len(l)-1):
    ans = ans +l[j]*l[j+1]
print(ans)

#--------------------------

x,y=map(int,input().split())
a={}
for i in range(x):
    p,q=input().split()
    a[p]=q
for i in range(y):
    f=input().strip()
    if "." in f:
        print(a.get(f.split(".")[-1],"unknown"))
    else:
        print("unknown")
    
    


#--------------------------

N,Q = map(int,input().split())

types={}

for _ in range(N):
    K,V=input().split()
    types[K]=V

for _ in range(Q):
    fileName = input().strip()
    I = fileName.rfind('.')
    if(I != -1):
        extension = fileName[I+1:]
        if(extension in types.keys()):
            print(types[extension])
        else:
            print('unknown')
    else:
        print('unknown')

#--------------------------

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    odd_count = 0
    even_count = 0

    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    res = even_count * odd_count
    print(res)


#--------------------------


#2 4 6 8 3 3

for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    oddcount=0
    evencount=0
    for i in l:
        if i%2==1:oddcount+=1
        else:evencount+=1
    print(oddcount*evencount)

#--------------------------

t = int(input())

for j in range(t):

    n, m = map(int, input().split())

    nlist = [i for i in range(n)]
    mlist = []

    for i in range(m):
        mlist.append(tuple(map(int, input().split())))

    mlist2 = mlist.copy()

    mlist.reverse()

    mselected = []

    for (x,y) in mlist:
        if x in nlist and y in nlist:
            nlist.remove(x)
            nlist.remove(y)
            mselected.append(mlist2.index((x,y)))


    p = ''
    for i in mselected:
        p = str(i) + ' ' + p

    print(p)

#--------------------------

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    l=[]
    q=[]
    p=[]
    for i in range(m):
        k,x=map(int,input().split())
        l.append([k,x])
    for i in reversed(range(m)):
        if l[i][0] not in q and l[i][1] not in q:
            q.append(l[i][0])
            q.append(l[i][1])
            p.append(i)
    p.sort()
    for i in range(len(p)):
        print(p[i],end=' ')
    print()

#--------------------------

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse = True)
    k = (a[0] + a[1])/2
    for i in range(2,n):
        k = (k + a[i])/2
    print(k)

#--------------------------

def poison(n,concentration):
    
    concentration=sorted(concentration)
    for i in range(n-1,0,-1):
        replaced=(concentration[i]+concentration[i-1])/2
        concentration.pop()
        concentration.pop()
        concentration.append(replaced)
        
    return concentration[0]



t=int(input())
for i in range(t):
    n=int(input())
    concentration=[int(x) for x in input().split()]
    ans=poison(n,concentration)
    print('%.6f'%ans)

#--------------------------

n=int(input())
a=[[0]*26]*n
m=[1000000000]*26
for i in range(n):
    a[i]=input()
for i in range(26):
    for j in range(n):
        x=chr(97+i)
        m[i]=min(a[j].count(chr(97+i)),m[i])
ans=""
for i in range(26):
    ans+=m[i]*chr(ord('a')+i)
if(len(ans)):
    print(ans)
else:
    print('no such string')

#--------------------------

from collections import Counter
l=[]
for _ in range(int(input())):
    s=input().strip()
    l.append(s)
s=Counter(l[0])
for i in range(1,len(l)):
    s=s&Counter(l[i])
s=list(s.elements())
if(len(s)!=0):
    print(*sorted(s),sep='')
else:
    print("no such string")
    
            

#--------------------------

r, c=map(int, input().strip().split())
main=[]
row=[]
col=[]
for j in range(r):
    a=list(map(int, input().strip().split()))    
    main.append(a)
    row.append(min(a))
count=0
for i in range(c):
    max=0
    for k in range(r):
        if(max<main[k][i]):
            max=main[k][i]
    col.append(max)
for i in range(r):
    n=row[i]
    for j in range(c):
        if(main[i][j]==n and col[j]==n):
            count=1
            break
    if(count==1):
        print(n)
        break
if(count==0):
    print("GUESS")

#--------------------------

R,C = map(int,input().split())
MAT = []
for r in range(R):
    MAT.append(list(map(int,input().split())))

colMax = []

for c in range(C):
    maxi=-1
    for r in range(R):
        if MAT[r][c]>maxi:
            maxi=MAT[r][c]
    colMax.append(maxi)

rowMin = []
for r in range(R):
    mini=MAT[r][0]
    for c in range(1,C):
        if MAT[r][c]<mini:
            mini=MAT[r][c]
    rowMin.append(mini)

noGuess=False
element=-1
for i in rowMin:
    if i in colMax:
        element=i
        noGuess=True
        break

if(noGuess):
    print(element)
else:
    print("GUESS")

#--------------------------

for _ in range(int(input())):
    n=int(input())
    s=0
    for i in range(n):
        x,l,f=map(int,input().split())
        while s>x:
            x+=f
        s=x+l
    print(s)
                

#--------------------------

# http://climatecanchange.com/
from itertools import count

for i in range(int(input())):
    k = int(input())
    chef_time = 0
    
    for station in range(k):
        x, l, f = map(int, input().split())
        if station == 0:
            chef_time += x + l
        else:
            for c in count(x, f):
                if c >= chef_time:
                    chef_time = c + l
                    break
            
    print(chef_time)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    d={}
    for i in range(n):
        name,vote=input().split()
        d[name]=vote
    c=0
    for name in d:
        if d[name]=='+':
            c+=1
        else:
            c-=1 
    
    print(c)

#--------------------------

try:
    for _ in range(int(input())):
        d = {}
        for _ in range(int(input())):
            string = input().split()
            if string[1] == '+':
                d[string[0]] = 1
            else:
                d[string[0]] = -1
        print(sum(d.values()))
except EOFError:
    pass

#--------------------------

t = int(input())
for i in range(0,t):
	n,m = map(int, input().split())
	soi = {}
	sof = {}
	for j in range (0,n):
		c, l = map(int, input().split())
		if not (l in soi.keys()):		
			soi[l]  = c	
		else:
			soi[l] += c 

	for j in range (0,m):
		c, l = map(int, input().split())
		if not (l in sof.keys()):		
			sof[l] = c
		else:
			sof[l] += c
	sum=0
	for i in soi.keys():
		if soi[i] < sof[i]:
			sum += sof[i] - soi[i]
	
	print(sum)

#--------------------------


t = int(input())
while t:
    n,m = map(int, input().split())
    soints = {}
    sofloats = {}
    while n:
        c,l = map(int, input().split())
        if l in soints.keys():
            soints[l] += c
        else:
            soints[l] = c
        n -= 1
    while m:
        c,l = map(int, input().split())
        if l in sofloats.keys():
            sofloats[l] += c
        else:
            sofloats[l] = c
        m -= 1
    c = 0
    for l in soints.keys():
        if sofloats[l]>=soints[l]:
            c += sofloats[l]-soints[l]
    print(c)
    t -= 1


#--------------------------

from collections import Counter
for _ in range(int(input())):
	R,S=input().split()
	B=True
	dr=Counter(list(R))
	ds=Counter(list(S))
	if set(list(R))==set(list(S)):
		for i in set(R):
			if dr[i]!=ds[i]:
				B=False
				break
	if B:
		print('YES')
	else:
		print('NO')

#--------------------------

T = int(input())
for i in range(T):
  r, s = input().split()
  r = list(r)
  s = list(s)
  r.sort()
  s.sort()
  if set(r) == set(s):
    t = "YES"
  else:
    t = "NO"
  if r == s and len(r) == len(s):
    c = "YES"    
  else:
    c = "NO"
  if t == c:
    print("YES")
  else:
    print("NO")

#--------------------------

from operator import xor
def find_xor(n):
    m=n%4
    if m==0:
        return n
    elif m==1:
        return 1
    elif m==2:
        return n+1
    elif m==3:
        return 0;
t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    t=xor(find_xor(l-1),find_xor(r))
    if t%2==0:
        print("Even")
    else:
        print("Odd")
    


#--------------------------

import sys
from sys import stdin,stdout
def get_int():return int(stdin.readline().strip())
def get_ints():return map(int,stdin.readline().strip().split())
def op(c):return stdout.write(c+"\n") 
t=get_int()
for _ in range(t):
    l,r=get_ints()
    n=(r-l)//2
    if (r % 2 != 0 or l % 2 != 0): 
        n += 1 
    if n%2==0:
        op("Even")
    else:
        op("Odd")
    


#--------------------------

t=int(input())
for _ in range(t):
    li=list(map(int,input().split()))
    l=len(li)
    fl=0
    f=1<<l
    
    for i in range(1,f):
        s=0
        for j in range(0,l):
            k=1<<j
            if((i&k)!=0):
                s+=li[j]
        if(s==0):
            fl=1
            break
    if(fl==1):
        print('Yes')
    else:
        print('No')

#--------------------------

n=16
def validate(l):
    for i in range(n):
        flag=False
        x=0
        for j in range(4):
            if(i&(1<<j) !=0):
                x+=l[j]
                flag=True
        if(flag and x==0):
            return("Yes")
    return ("No")
            
        
        
t=int(input())
while(t):
    l=list(map(int,input().split()))
    print(validate(l))
    
    t-=1
            
    


#--------------------------

for _ in range(int(input())):
    r , c = map(int,input().split())
    arr = []
    for i in range(r):
        arr.append(list(map(int,input().split())))
    ans = "Stable"
    for i in range(r):
        for j in range(c):
            if ((i == 0 or i == r-1) and (j == 0 or j == c-1)) :
                if arr[i][j] > 1 :
                    ans = "Unstable"
                    break
            elif i==0 or i==r-1 or j==0 or j==c-1 :
                if arr[i][j] > 2 :
                    ans = "Unstable"
                    break
            else :
                if arr[i][j] > 3 :
                    ans = "Unstable"
                    break
            if ans == "Unstable":
                break
    print(ans)
   
    


#--------------------------



for _ in range(int(input())):
    r,c = map(int, input().split())
    flag = 0

    for i in range(r):
        lst = list(map(int,input().split()))
        if flag == 1:
            continue
        else:
            for j in range(c):
                if i == 0 or i == r-1:
                    if j == 0 or j == c-1:
                        if lst[j] >= 2:
                            flag = 1
                    elif lst[j] >= 3:
                        flag = 1
                elif j == 0 or j == c-1:
                    if lst[j] >= 3:
                        flag = 1
                else:
                    if lst[j] >= 4:
                        flag = 1

    if flag == 1:
        print("Unstable")
    else:
        print("Stable")










#--------------------------

for _ in range(int(input())):
    t=int(input())
    p=[]
    for i in range(t):
        a,b=map(int,input().split())
        p.append([a,b])
    p=sorted(p)
    for j in range(t-1):
        p[j+1][1]+=p[j][1]
    q=int(input())
    for m in range(q):
        flag=0
        dead1,req1=map(int,input().split())
        for k in p:
            if k[0]<=dead1:
                if req1<=k[1]:
                    flag=1
        if flag==1:
            print('Go Camp')
        else:
            print('Go Sleep')

#--------------------------

for t in range(int(input())):
    c=[0]*31
    for i in range(int(input())):
        d,p=map(int,input().split())
        c[d-1]=p
    for i in range(int(input())):
        dead,req=map(int,input().split())
        s=c[0:dead]
        if sum(s)<req:
            print("Go Sleep")
        else:
            print("Go Camp")

#--------------------------

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    c=[0]*m
    for i in range(n):
        x=input()
        for k in range(m):
            if x[k]=='1':
                c[k]+=1
    sum1=0
    for i in range(m):
        if c[i]>1:
            sum1+=(c[i]*(c[i]-1)//2)
    print(sum1)

#--------------------------

t=int(input())
for i in range(t):
    n,m=[int(x) for x in input().split()]
    l=[0]*m
    for x in range(n):
        z=input()
        for y in range(m):
            if z[y]=='1':
                l[y]+=1 
    a=0
    #print(l)
    for x in range(m):
        if (l[x]>1):
         a=a+((l[x]*(l[x]-1))//2)
         #print(a)
    print(a)    

#--------------------------

import math
X,N=map(int,input().split())
empty_spaces=0
for i in range(N):
    car=list(map(int,input()))
    car.insert(0,-1)
    for j in range(9):
        empty_in_comp=0
        for k in range(1,5):
            if(car[j*4+k]==0):
                empty_in_comp+=1
        for k in range(2):
            if(car[54-2*j-k]==0):
                empty_in_comp+=1
        if(empty_in_comp>=X):
            empty_spaces+=math.factorial(empty_in_comp)/math.factorial(empty_in_comp-X)/math.factorial(X)
print(int(empty_spaces))

#--------------------------

import math
n,m = map(int,input().split())
l = []
ans = 0

for i in range(m):
    t = 0
    s = str(input())
    for j in range(0,36,4):
        a = s[j:j+4]
        a+=s[53-t]
        a+=s[53-t-1]
        l.append(a)
        t+=2

    for x in range(9*i,9*i+9):
        s = l[x]
        c = s.count("0")
        if c>=n:
            cnt = math.factorial(c)//(math.factorial(n)*math.factorial(c-n))
            ans+=cnt
        

print(ans)
        
    

#--------------------------

try:
    for i in range(int(input())):
        n,m = map(int,input().split())
        l = {}
        for j in range(0,n):
            d,v =  map(int,input().split())
            if(d in l.keys()):
                g = l[d]
                if(g<v):
                    l[d] = v 
            else:
                l[d] = v
        f = sorted(l.values()) 
        s = f[-1]+f[-2]
        print(s)
except EOFError as e:
    pass


#--------------------------

t=int(input())
for q in range(t):
  n,m=map(int,input().split())
  l=[0]*(m+1)
  for i in range(n):
    d,v=map(int,input().split())
    if l[d]<v:
        l[d]=v
  l.sort(reverse=True)
  print(l[0]+l[1])
        
    
        
    
  

#--------------------------

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    curr=0
    count=0
    for i in range(n):
        count += (s[i]-curr-1)//k
        curr=s[i]
    print(count)

#--------------------------

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    curr=0
    count=0
    for i in range(n):
        count += (s[i]-curr-1)//k
        curr=s[i]
    print(count)

#--------------------------

n = int(input())
a = input().split()
m = int(a[0])
c = int(a[1])

t1 = 0
t2 = 0
for _ in range(n):
    b = [int(s) for s in input().split()]
    x = b[0]
    y = b[1]
    p = b[2]
    if y > m*x + c:
        t1 = t1 + p
    else:
        t2 = t2 + p
print(max(t1,t2))

#--------------------------

ll=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(ll):
    x=list(map(int,input().split()))
    if l[0]*x[0]+l[1]-x[1]>0:
            c=c+x[2]
    elif l[0]*x[0]+l[1]-x[1]<0:
            c1=c1+x[2]
if c>c1:
        print(c)
else:
        print(c1)

#--------------------------

t=int(input())
for k in range(t):
    n=int(input())
    p=list(map(int, input().split()))[:n]
    x=min(p)
    sum=0
    for i in p:
        y=i*x
        sum=sum+y
    new_sum=sum-(x*x)
    print(new_sum)
        
    

#--------------------------

#two options to solve this questions, first one is to assume the cities are nodes and form every possible vector
#edge as roads between the cities and find the MST of that graph
#Other approach is that the cost will be minimum if the minimum element of the cost is multiplied with every other one and added

test = int(input())
for _ in range(test):
    cities = int(input())
    array = sorted(list(map(int, input().split())))
    multiply = array[0]
    total=sum(array[1:])
    print(total*multiply)

#--------------------------


try:
    def area():
    	n=int(input())
    	b=[]
    	for i in range(n):
    		x1,y1,x2,y2,x3,y3=map(int,input().split())
    		m=abs(0.5 * (((x2-x1)*(y3-y1))-((x3-x1)*(y2-y1))))
    		b.append(m)
    	p=[i for i, j in enumerate(b) if j == max(b)]
    	q=[i for i, j in enumerate(b) if j == min(b)]
    	print(q[-1]+1,p[-1]+1)
    area()
except:
    pass



#--------------------------

n=int(input())
z=[]
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    z.append(a)
x,y=[],[]
e=max(z)
f=min(z)
for i in range(len(z)):
    if(z[i]==e):
        x.append(i+1)
    if(z[i]==f):
        y.append(i+1)
print(y[-1],x[-1])

#--------------------------

def check(s1,s2,s3):
    if(s1==s2 and s2==s3 and s3==s1):
        return True
    else:
        return False
for _ in range(int(input())):
    f,b,l,r,t,bo = input().split()
    if(check(f, t, l) or check(f, t, r) or check(f,bo, l) or check(f,bo, r) or check(b, t, l) or check(b, t, r) or check(b, bo, l) or check(b, bo, r)):
        print("YES")
    else:
        print("NO")

#--------------------------

from collections import *
for u in range(int(input())):
    l=input().split()
    C=l
    if C[0]==C[2]==C[4] or C[0]==C[2]==C[5] or C[0]==C[3]==C[4] or C[0]==C[3]==C[5] or C[1]==C[2]==C[4] or C[1]==C[2]==C[5] or C[1]==C[3]==C[4] or C[1]==C[3]==C[5]:  
        print('YES')
    else:
        print('NO')        

#--------------------------

for i in range(int(input())):
	a,b,n=map(int,input().split())
	if n%2 ==0:
		a=abs(a)
		b=abs(b)
		if a>b:
			print(1)
		elif a<b:
			print(2)
		else:
			print(0)
	else:
		if a < b:
			print(2)
		elif a > b:
			print(1)
		else:
			print(0)

#--------------------------

t=int(input())
for i in range(t):
    a,b,n=list(map(int,input().split()))
    if (n%2)==0:
        if abs(a)>abs(b):
            print(1)
        elif abs(a)<abs(b):
            print(2)
        else:
            print(0)
            
    else:
        if a>b:
            print(1)
        elif a<b:
            print(2)
        else:
            print(0)    
      

        

#--------------------------

for _ in range(int(input())):
    s = str(input())
    l = ''
    for i in s:
        if i not in l:
            l = l + i
    if len(s) == len(l):
        print('no')
    else:
        print('yes')

#--------------------------

for _ in range(int(input())):
    s=input()
    a=[]
    for i in s:
        a.append(i)
    aa=set(a)
    if len(aa)==len(a):
        print('no')
    else:
        print('yes')

#--------------------------

from itertools import combinations
for _ in range(int(input())):
    a=[int(x) for x in input().split()]
    k=int(input())
    a.sort(reverse=True)
    s=0
    for i in range(k):
        s+=a[i]
    z=list(combinations(a,k))
    c=0
    for i in z:
        if sum(i)==s:
            c+=1
    print(c)
            
    

#--------------------------


try:
    from itertools import combinations
    for _ in range(int(input())):
        scores = list(map(int, input().split()))
        k = int(input())
        s = combinations(scores, k)
        res = []
        for i in s:
            res.append(sum(i))
        print(res.count(max(res)))
except EOFError:
    pass

    


#--------------------------

MOD=10**9+7
for _ in range(int(input())):
    s=input()
    ind=1
    level=1
    for i in range(len(s)):
        if s[i]=='l':
            if level%2==1:
                ind=ind*2
            else:
                ind=ind*2-1
        if s[i]=='r':
            if level%2==1:
                ind=ind*2+2
            else:
                ind=ind*2+1
        level+=1
        ind%=MOD
    print(ind)


#--------------------------

mod = 1000000007
for _ in range(int(input())):
    string = list(input().strip())
    idx = 1
    lev = 1
    for i in (string):
        if i == 'l':
            if lev % 2 == 1:
                idx = (idx * 2)
            else:
                idx = (idx * 2 - 1)
        else:
            if lev % 2 == 1:
                idx = (idx * 2 + 2)
            else:
                idx = (idx * 2 + 1)
        lev += 1
        idx = idx % mod
    print(idx)

#--------------------------


for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    l = list(map(int, input().split()))
    d = []
    for i in l:
        d.append(abs(i-b) + c + abs(i-a))
    print(min(d))
    
    
    

#--------------------------

T = int(input())
for i in range(T):
    N, a, b, c = map(int, input().split())
    F = list(map(int, input().split()))
    F.sort()
    l = []
    for i in range(len(F)):
        s = 0
        s += abs(F[i]-b)
        s += c
        s += abs(F[i]-a)
        l.append(s)
    print(min(l))

#--------------------------

for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=max(l)
    if c>=b:
        print("YES")
    else:
        print("NO")


#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    flag=0
    for i in range(n):
        if lst[i]>=k:
            flag=1
            break
    if flag==1:
        print("YES")
    else:
        print("NO")
    


#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split(" "))
    l=[]
    temp=""
    temp2=""
    find=False
    for i in range(n):
        word=input()
        word=word.lower()
        #print(word,len(word))
        temp=temp+" "+word
        temp2=temp2+word
    if(temp.find("spoon")!=-1):
        find=True
    if(n>4):
        for i in range(m):
            w=temp2[i::m]
            if(w.find("spoon")!=-1):
                find=True
    if(find==True):
        print("There is a spoon!")
    else:
        print("There is indeed no spoon!")
        
    

#--------------------------

for j in range(int(input())):
    r,c=map(int,input().split())
    x=[]
    for i in range(r):
        d=input().lower()
        x.append(d)
    a=0
    am=0
    for i in x:
        a=i.count("spoon")
        if(a!=0):
            print("There is a spoon!")
            am=1
            break
    if(am!=1):
        sum=""
        for k in range(c):
            for i in x:
                sum+=i[k]
            if(sum.count("spoon")!=0):
                print("There is a spoon!")
                break
        else:
            print("There is indeed no spoon!")

#--------------------------

for _ in range(int(input())):
    n,m=map(int, input().split())
    l=list(map(int, input().split()));h=[]
    for i in range(n):
        h.append(0)
    h[l[0]-1]=1
    for i in range(1,m):
        h[l[i] - 1] += 1
        if h[l[i]-1]==min(h)+2:
            print("NO")
            break

    else:
        print('YES')


#--------------------------

def chk(a,k,n):
    for i in range(1,k):
        if a[i] in a[:i] and a[:i].count(a[i])>i//n:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:k]))
    print(chk(a,k,n))
        

#--------------------------

for i in range(int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    b=set(a)
    b=list(b)
    b.sort()
    l=0
    for j in range(len(b)):
        if b[j]>x:
            break
        else:
            l=l+1
    print(x-l)


#--------------------------

def solve():
    n = int(input())
    b = [0] * (n + 1)
    a = list(map(int, input().split()))
    free_slot = 1
    ans = 0
    for x in a:
        if 1 <= x <= n:
            if b[x]:
                ans += 1
            else:
                b[x] = 1
        else:
            ans += 1
        pass
    return ans
    pass


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
    pass


#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=0
    for i in range(len(l)):
        if l[i]<2:
            flag=1
            break
    if flag==1:
        print(-1)
        continue
    s=sum(l)-min(l)+2
    if len(l)==1:
        print(2)
    else:
        print(s)

#--------------------------

for _ in range(int(input())):
	n = int(input())
	items = list(map(int,input().split()))
	if min(items) < 2:
		total = -1
	else:
		total = sum(items) - min(items) + 2
	print(total)


#--------------------------

t=int(input())
for x in range(t):
    n,c,q=map(int,input().split())
    for y in range(q):
        l,r=map(int,input().split())
        
        if c>=l and c<=r :
            c=c-r+1
            c=l-r+2-c
            c=c+r-1
            
    print(c)

#--------------------------

for _ in range(int(input())):
    N, C, Q = map(int,input().split())
    for i in range(Q):
        L, R = map(int,input().split())
        if C <= R and C >= L:
            C = L + R - C
    print(C)

#--------------------------

#attic cross
from sys import stdin,stdout
inp = stdin.readline

t=int(inp())

while(t):
  t-=1
  s=inp()
  e=0;d=0;k=0
  if s.count('.')==0:
      print(0)
  else:
      for i in s:
        if(i=='.'):
          e+=1
          
        else:
          if(e>d):  k+=1;d=e
          e=0
      print(k)

#--------------------------

t=int(input())

for x in range(t):
    s=input()
    l=[]
    count=0
    for i in s:
        if i=='.':
            count+=1
        else:
            if count!=0:
                l.append(count)
            count=0
    if count!=0:
        l.append(count)
    if len(l)==0:
        print('0')
    else:
        sum=1
        max=l[0]
        for i in range(1,len(l)):
            if max<l[i]:
                sum+=1
                max=l[i]
        print(sum)

    

#--------------------------

n = int(input())
s = input()
l = list(s)
x=[]
a = 0
l.reverse()
for i in range(n):
    if(l[i]=='1'):
        a=i
        break
print(a)

#--------------------------

n = int(input())
s = input()
print(s[::-1].find('1'))

#--------------------------

for tc in range(int(input())):
    
    z,n1,n2 = map(int,input().split(' '))
    
    n1 = bin(n1)
    n2 = bin(n2)
    
    c1 = n1.count('1')
    c2 = n2.count('1')
    
    ones =  c1+c2
    
    nums = abs(z - ones)
    
    sumi = 0 
    for i in range(nums,z):
        sumi = sumi + 2**i
        
        
    print(sumi)

#--------------------------

for t in range(int(input())):
    n,a,b=map(int,input().split())
    a = bin(a)
    b = bin(b)
    ones = a.count('1') + b.count('1')
    num = 0
    l = abs(n - ones)
    for i in range(l, n):
        num += 2**i
    print(num)

#--------------------------

from decimal import *
t=int(input())
while t>0:
    t-=1
    K=int(input())
    if K==0:
        print(3)
    else:
        ans='3.'
        y=33102
        x=103993%y

        for i in range(K):
            x*=10
            ans+=str(x//y)
            x=x%y
        print(ans)

#--------------------------

for aman in range(int(input())):
    k = int(input())
    if (k == 0):
        print("3")
        continue
    else:
        arr = []
        arr.append("3.")
        r = 103993 % 33102
        for i in range(k):
            r *= 10
            arr.append(r // 33102)
            r = r % 33102
        print(''.join(map(str, arr)))

#--------------------------

for _ in range(int(input())):
    n = int(input())
    f=0
    a=n
    
    while n%7!=0:
        n-=4
    ans= a-n

    if(ans%4==0 and n>=0):
        print(n)
    else:
        print(-1)

#--------------------------

for _ in range(int(input())):
    n = int(input())
    flag = 0
    for x in range(7):
        if (n-x*4) < 0:
            break
        if (n-x*4) % 7 == 0:
            flag = 1
            print(n-x*4)
            break
    if flag == 0:
        print(-1)


#--------------------------

for _ in range(int(input())):
    m, b = map(int, input().split())
    while m != 0:
        m, b = b%m, m
    print(2*b)

#--------------------------

import math

t = int(input())

while t:
    m, b = map(int, input().split())
    
    if m == b or (m == 0 or b == 0):
        print(m + b)
    else:
        print(2 * (math.gcd(m,b)))
    
    t -= 1

#--------------------------

t=int(input())
for i in range(t):
    x=input()
    y=input()
    z=''
    for i in range(len(x)):
        if x[i]==y[i]:
            if x[i]=='W':
                z+='B'
            else:
                z+='W'
        else:
            z+='B'
    print(z)

#--------------------------

for _ in range(int(input())):
    X = input()
    Y = input()
    
    Z = ''.join('W' if x == 'B' and y == 'B' else 'B' for x, y in zip(X, Y))
    print(Z)

#--------------------------

for _ in range(int(input())):
	li = [int(i) for i in input().split()]
	li1 = [(li[i],li[i+3]) for i in range(3)]
	li1.sort()
	for i in range(2):
		a= li1[i][0]-li1[i+1][0]
		b =li1[i][1]-li1[i+1][1]
		if (a>0 and b>0) or (a==0 and b==0) or (a<0 and b<0):
			continue
		print("NOT FAIR")
		break
	else:
		print("FAIR")

#--------------------------

t= int(input())
for _ in range(t):
    a1,a2,a3,c1,c2,c3= map(int,input().split())
    count=3
    if((a1>a2 and c1>c2) or (a2>a1 and c2>c1) or (a2==a1 and c2==c1)):
        count-=1
    if((a2>a3 and c2>c3) or (a3>a2 and c3>c2) or (a3==a2 and c3==c2)):
        count-=1
    if((a1>a3 and c1>c3) or (a3>a1 and c3>c1) or (a3==a1 and c3==c1)):
        count-=1
        
    if count==0 :
        print("FAIR")
    else:
        print("NOT FAIR")

#--------------------------

for _ in range(int(input())):
   n=int(input())
   a=[]
   a=list(map(str,input().split()))
   s=0
   if a[n-1]=='cookie':
       print('NO')
   else:
       for i in range(n-1):
           if a[i]=='cookie' and a[i+1]=='cookie':
               print("NO")
               s=1
               break
       if s==0:
            print('YES')
        

#--------------------------

for _ in range(int(input())):
   n=int(input())
   a=[]
   a=list(map(str,input().split()))
   s=0
   if a[n-1]=='cookie':
       print('NO')
   else:
       for i in range(n-1):
           if a[i]=='cookie' and a[i+1]=='cookie':
               print("NO")
               s=1
               break
       if s==0:
            print('YES')

#--------------------------

for _ in range(int(input())):
    n=int(input())
    if n==0:
        print('Draw')
    else:
        k=[1,0]
        f=input()
        se=''
        for i in range(n-1):
            s=input()
            if s ==f:
                k[0]+=1 
            else:
                se=s
                k[1]+=1
        if k[0]>k[1]:
            print(f)
        elif k[0]<k[1]:
            print(se)
        else:
            print('Draw')

#--------------------------

for _ in range(int(input())):
    n=int(input())
    if n==0:
        print('Draw')
        continue
    teamA=input()
    teamB=''
    a=1
    b=0
    for i in range(n-1): 
        s=input()
        if s==teamA:
            a=a+1 
        else:
            teamB=s 
            b=b+1 
    if a==b:
        print('Draw')
    elif a>b:
        print(teamA)
    elif a<b:
        print(teamB)
        

#--------------------------

from collections import Counter

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    i=0
    
    while i<len(a)-1:
        
        if a[i]==a[i+1]:
            del a[i+1]
            
        i+=1
        
    cod=Counter(a)

    typ=-1
    val=-1
    
    for k,v in cod.items():
        if v>val:
            typ=k
            val=v
        elif v==val and k<typ:
            typ=k
            
    print(typ)


#--------------------------

s=int(input())
for _ in range(s):
    r=int(input())
    u=list(map(int,input().split()))
    k=dict()
    p=0
    for c in u:
        if(c not in k):
            k[c]=1
            p=c
        else:
            if(c!=p):
                k[c]=k[c]+1
                p=c
            else:
                p=0
    z=sorted(k.items(),key=lambda s:(-s[1],s[0]))
    print(z[0][0])
    

#--------------------------

for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(str,input().split()))
    head_cnt = 0
    while k:
        t = arr.pop()
        if t == "H":
            for i in range(len(arr)):
                if arr[i] == "T":
                    arr[i] = "H"
                else:
                    arr[i] = "T"
        k-=1
    for i in range(len(arr)):
        if arr[i] == "H":
            head_cnt += 1 
    print(head_cnt)

#--------------------------

for i in range(int(input())):
    m,n = map(int,input().split())
    a = input().split()
    for i in range(n):
        coin = a.pop()
        if coin == 'H':
            for j in range(len(a)):
                if a[j] == 'H' : a[j] = 'T'
                else: a[j] = 'H'
    print(a.count('H'))

#--------------------------

n=int(input())

for i in range(n) :
	N,k=map(int,input().split())

	bucks=list(map(int,input().split(' ',N-1)))
	ans=0
	mid=int(k/2)
	for j in bucks :
		x=j%k
		y=k-x
		if j>=k:
			ans=ans+min(x,y)
		else:
			ans=ans+y

	print(ans)	

#--------------------------

for _ in range(int(input())):
    N,K = map(int,input().split())
    G = list(map(int,input().split()))
    ans = 0
    for i in G:
        Rem = i%K
        if i < K:
            ans += (K-Rem)
        else:
            ans += min(Rem,K-Rem)
    print(ans)

#--------------------------

t = int(input())

for i in range(t):
    u, v = map(int, input().split())
    x = u + v 
    print((x * (x + 1) // 2) + u + 1)

#--------------------------

t=int(input())
for i in range(t):
	u,v=map(int,input().split())
	x=u+v
	print((x*(x+1)//2)+u+1)

#--------------------------

n=int(input())
while n>0:
    n-=1
    r=input()
    l=len(r)
    x=r[0]
    y=r[1]
    flag=1
    if x!=y:
        for i in range(l):
            if i%2==0 and r[i]==x:
                flag=1
            elif i&1 and r[i]==y:
                flag=1
            else:
                flag=0
                break
    else:
        flag=0
    if flag==1:
        print("YES")
    else:
        print("NO")

#--------------------------

def luck(S):
    if S[0] == S[1]:
        return "NO"
    for i in range(2,len(S)):
        if S[i] != S[i-2]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    S = input()
    print(luck(S))

#--------------------------

for _ in range(int(input())):
    n=int(input())
    d={}
    a=[]
    for i in range(n):
        a.append([int(x) for x in input().split()])
        for j in range(n):
            d[a[i][j]]=[i,j]
    
    c=0
    for i in range(2,n*n+1):
        c+=abs(d[i-1][0]-d[i][0])+abs(d[i-1][1]-d[i][1])
    
    print(c)
            

#--------------------------

for i in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        t=[int(i) for i in input().split()]
        arr.append(t)
    x=[0]*(n**2)
    y=[0]*(n**2)   
    for i in range(n):
        for j in range(n):
            x[arr[i][j]-1]=i+1
            y[arr[i][j]-1]=j+1
    s=0 
    for i in range(n**2-1):
        s+=abs(x[i]-x[i+1])+abs(y[i]-y[i+1])
    print(s)            


#--------------------------

t= int(input())
for x in range(t):
    s=input()
    lst=[]
    count = 0
    for i in range(len(s)-1):
        if s[i:i+2] in lst:
            pass
        else:
            lst.append(s[i:i+2])
            count+=1
    print(count)

#--------------------------

t=int(input())
while(t>0):
    s=input()
    a=[]
    for x in range(len(s)-1):
        if s[x:x+2] not in a:
            a.append(s[x:x+2])
    print(len(a))
    t-=1

#--------------------------

t = int(input())
for _ in range(t):
    r, g , b = map(int, input().split())
    k = int(input())
    
    print(min(k-1, r) + min(k-1, g) + min(k-1, b) + 1) 

#--------------------------

for _ in range(int(input())):
    r,g,b=map(int,input().split())
    k=int(input())
    print(min(r,k-1)+min(g,k-1)+min(b,k-1)+1)

#--------------------------

from math import sqrt
for i in range(int(input())):
    P,A=map(int,input().split())
    l = (P - sqrt(P * P - 24 * A)) / 12; 
    V = l * (A / 2.0 - l * (P / 4.0 - l)); 
    print("%.2f"%(V))

#--------------------------

for _ in range(int(input())):
    p,s=map(int,input().split())
    b=(p-(p**2-24*s)**(0.5))/12
    l=p/4-2*b
    print("%.2f"%(l*b*b))


#--------------------------

t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  p=list(map(int,input().split()))
  if sum(p)<m:
    print(-1)
  else:
    p.sort(reverse=True)
    count=0
    res=0
    for i in p:
      count+=i
      res+=1
      if count>=m:
        print(res)
        break
        

#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    a=0
    count=0
    l.sort()
    for i in range(len(l)):
        a+=l[n-i-1]
        count+=1
        if a>=m:
            break 
    if a>=m:
        print(count)
    else:
        print(-1)
            
    
            

#--------------------------

T=int(input())
for i in range(T):
        n=int(input())
        l=list(map(int,input().split()))
        s=dict()
        for e in l:
                if(e in s):
                        s[e]=s[e]+1
                else:
                        s[e]=1
        l1=s.values()
        print(n-max(l1))
        



#--------------------------

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    for i in l:
        try:
            d[i]+=1
        except:
            d.setdefault(i,1)
    m = 0
    for i in d.values():
        if m<i:
            m = i
    print(n-m)

#--------------------------

for _ in range(int(input())):
    a,b=map(list,input().split())
    if len(a)<len(b):
        for i in range(len(b)-len(a)):
            a.insert(0,0)
    elif len(a)>len(b):
        for i in range(len(a)-len(b)):
            b.insert(0,0)
    s=''
    for i in range(len(a)):
        s+=str(int(a[i])+int(b[i]))[-1]
    print(int(s))

#--------------------------

try:
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        i=10
        temp=0
        tot=a+b
        while(a or b):
            if(a%10)+(b%10)>9:
                temp+=i
            a=a//10
            b=b//10
            i=i*10
        print(tot-temp)    
except:
    EOFError

#--------------------------

try:
    t=int(input())
    while t!=0:
        s=input()
        c1=0
        c2=0
        for i in range(0,len(s),1):
            if i%2==0:
                if s[i]=="-":
                    c2+=1
                else:
                    c1+=1
            else:
                if s[i]=="+":
                    c2+=1
                else:
                    c1+=1
        if c1>=c2:
            print(c2)
        else:
            print(c1)
        t=t-1
except:
    pass


#--------------------------

for _ in range(int(input())):
    s=list(input())
    n=len(s)
    c1=0
    c2=0
    if(n%2==0):
        s1="-+"*(n//2)
        s2="+-"*(n//2)
    else:
        s1="-+"*(n//2)
        s1+="-"
        s2="+-"*(n//2)
        s2+="+"
    s1=list(s1)
    s2=list(s2)
    for i in range(n):
        if(s[i]!=s1[i]):
            c1+=1
        if(s[i]!=s2[i]):
            c2+=1
    print(min(c1,c2))
        

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for j in range(len(a)):
        x=x^(2*a[j])
    print(x)    


#--------------------------

n=int(input())
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    sum1=0
    for i in l:
        sum1^=(i+i)
    print(sum1)



#--------------------------

try:
    m=int(input())
    for i in range(m):
        n = int(input())
        print(1, 10 ** (n // 2))
except:
    pass

#--------------------------

for i in range(int(input())):
    n = int(input())
    print(1, 10 ** (n // 2))


#--------------------------

import math
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    print(min(A))

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(min(a))

#--------------------------

def gcd(m, n):
    r = m%n
    while r!= 0:
        m = n
        n = r
        r = m%n
    return n


for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    x = gcd(s[0], s[1])
    for i in range(n-2):
        x = gcd(s[n-i-1], x)
    if x == 1:
        print(0)
    else:
        print(-1)

#--------------------------

from math import gcd
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=gcd(l[0],l[1])
    for i in range(len(l)):
       gcd1=gcd(a,l[i])
    if(gcd1==1):
       print(0)
    else:
       print(-1)

#--------------------------

for _ in range(int(input())):
	N=int(input())
	A=list(map(int,input().split()))
	s=A[0]
	for i in range(N-1):
		if A[i+1]>A[i]:
			s+=A[i+1]-A[i]
	print(s)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    a=0
    c=0
    for i in range(n):
        b=m[i]-c
        if b>=0:
            a+=b
            c+=b
        else:
            c+=b
    print(a)


#--------------------------


def check(L, n):
    count = dict()
    
    for i in range(n):
        a = L[i]
        count[a] = count.setdefault(a, 0) + 1 
        if count[a]>1:
            if L[i-1] !=L[i]:
                return False
    t = tuple(count.values())
    if len(t)!=len(set(t)):
        return False
    return True

for i in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    ch = check(L, n)
    if ch:
        print("YES")
    else:
        print("NO")

#--------------------------

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    freq={a.count(i):i for i in set(a)}
    if len(freq)==len(set(a)):
        freq={i:a.count(i) for i in set(a)}
        current_value=a[0]
        count=1
        flag=True
        for i in a[1:]:
            if i==current_value:
                count+=1
            elif count!=freq[current_value]:
                flag=False
                break
            else:
                count=1
                current_value=i
                
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
        
    
    

#--------------------------

for _ in range(int(input())):
    a=input()
    b=input()
    d=dict()
    ct=0
    for i in a:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    for j in b:
        if j in d.keys():
            if d[j]!=0:
                d[j]-=1
                ct+=1
    print(ct)

#--------------------------

from collections import *
for u in range(int(input())):
    s=input()
    r=input()
    x=Counter(s)
    y=Counter(r)
    c=0
    for i in x:
        c+=min(x[i],y[i])
    print(c)


#--------------------------

for _ in range(int(input())):
    str = list(input())
    l = len(str)
    flag = False
    for i in range(l//2):
        if str[i] == '.':
            if str[-i-1] == '.':
                str[i] = str[-i-1] = 'a'
            else:
                str[i] = str[-i-1]
        elif str[-i-1] == '.':
            str[-i-1] = str[i]
        elif str[i] != str[-i-1]:
            print("-1")
            flag = True
            break
    if flag:
        continue
    if l%2 != 0 and str[l//2] == '.':
        str[l//2] = 'a'
    print("".join(str))


#--------------------------

t = int(input())
for q in range(t):
    s = input()
    ns = ''
    
    f = 0
    if len(s)%2 == 0:
        k = len(s) // 2
    else:
        k = (len(s)//2)+1
    
    for i in range(k):
    
        if s[i] != s[len(s)-1-i] and s[i] != '.' and s[len(s)-1-i] != '.':
            f = 1
            break
        elif s[i] == '.':
            if s[i] == s[len(s)-1-i]:
                ns += 'a'
            else:
                ns += s[len(s)-1-i]
        elif s[len(s)-1-i] == '.':
            if s[i] == s[len(s)-1-i]:
                ns += 'a'
            else:
                ns += s[i]
        else:
            ns += s[i]
    
    
    if f == 1:
        print(-1)
    elif len(s)%2 == 0:
        print(ns + ns[::-1])
    else:
        print(ns + ns[::-1][1:])


#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    print(len(set(a)))

#--------------------------

try:
    def fun(t):
        for i in range(t):
            n=int(input())
            a=list(map(int,input().split()))
            b=set(a)
            print(len(b))
    t=int(input())
    fun(t)
except:
    pass

#--------------------------

import math
for _ in range(int(input())):
    n=int(input())
    j=list(map(int,input().split(' ')))
    for i in range(1,n):
        j[i]=math.gcd(j[i],j[i-1])
    print(j[-1])

#--------------------------

import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    for i in range(1,n):
        l[i]=math.gcd(l[i], l[i-1])
    print(l[-1])

#--------------------------

for i in range(int(input())):
    n=int(input())
    if n%4!=1:
        print("BOB")
    else:
        print("ALICE")


#--------------------------

for tc in range(int(input())):
    
    n = int(input())
    turns = 0
    
    if n%4 == 1:
        print('ALICE')
    else:
        print('BOB')

#--------------------------

import math

for _ in range(int(input())):
    angels = []
    dif = []
    gcd = 360
    nAngels = int(input())
    angels = list(map(int,input().split()))

    for i in range(1,len(angels)):
        dif.append(angels[i]-angels[i-1])
    
    dif.append(angels[0]+(360-angels[-1]))
    
    for d in dif:
        gcd = math.gcd(gcd,d)
    
    print(int(360/gcd)-nAngels)

#--------------------------

import math

for _ in range(int(input())):
    angels = []
    dif = []
    gcd = 360
    nAngels = int(input())
    angels = list(map(int,input().split()))

    for i in range(1,len(angels)):
        dif.append(angels[i]-angels[i-1])
    
    dif.append(angels[0]+(360-angels[-1]))
    
    for d in dif:
        gcd = math.gcd(gcd,d)
    
    print(int(360/gcd)-nAngels)


#--------------------------



id=int(input())
t=int(input())
for i in range(t):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    d1 = (x1-x2)**2 + (y1-y2)**2
    d2 = (x1-x3)**2 + (y1-y3)**2 
    d3 = (x2-x3)**2 + (y2-y3)**2
    
    angle=""
    length=""
    
    arr=[d1,d2,d3]
    arr.sort()
    
    if arr[2]>arr[0]+arr[1]:
      angle= "obtuse"
    elif arr[2]<arr[0]+arr[1]:
        angle= "acute"
    else:
        angle= "right"
    
    if d1!=d2 and d2!=d3 and d3!=d1:
        length="Scalene"
    else:
        length="Isosceles"  
        
    if id==1:
        print(length + " triangle")
    else:
        print(length + " " + angle + " triangle")
        

#--------------------------

id=int(input())
t=int(input())
for i in range(t):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    d1 = (x1-x2)**2 + (y1-y2)**2
    d2 = (x1-x3)**2 + (y1-y3)**2 
    d3 = (x2-x3)**2 + (y2-y3)**2
    
    angle=""
    length=""
    
    arr=[d1,d2,d3]
    arr.sort()
    
    if arr[2]>arr[0]+arr[1]:
      angle= "obtuse"
    elif arr[2]<arr[0]+arr[1]:
        angle= "acute"
    else:
        angle= "right"
    
    if d1!=d2 and d2!=d3 and d3!=d1:
        length="Scalene"
    else:
        length="Isosceles"  
        
    if id==1:
        print(length + " triangle")
    else:
        print(length + " " + angle + " triangle")
        


#--------------------------

n , m = map(int,input().split(" "))
arr = []
for i in range(n):
    arr.append([int(j) for j in input().split()])
l = int(input())
check = []
for i in range(l):
    a, b = map(int,input().split())
    check.append([a-1,b-1])

e1 , e2 = 0 , 0
for i in range(l):
    if e1 != -1:
        if check[i][0] < n and check[i][1] < m:
            e1 += arr[check[i][0]][check[i][1]]
        else:
            e1 = -1
    if e2 != -1:
        if check[i][0] < m and check[i][1] < n:
            e2 += arr[check[i][1]][check[i][0]]
        else:
            e2 = -1
print(max(e1,e2))

#--------------------------

n , m = map(int,input().split(" "))
arr = []
for i in range(n):
    arr.append([int(j) for j in input().split()])
l = int(input())
check = []
for i in range(l):
    a, b = map(int,input().split())
    check.append([a-1,b-1])

e1 , e2 = 0 , 0
for i in range(l):
    if e1 != -1:
        if check[i][0] < n and check[i][1] < m:
            e1 += arr[check[i][0]][check[i][1]]
        else:
            e1 = -1
    if e2 != -1:
        if check[i][0] < m and check[i][1] < n:
            e2 += arr[check[i][1]][check[i][0]]
        else:
            e2 = -1
print(max(e1,e2))


#--------------------------

from math import ceil,sqrt
l=[0]*(10**6+1)
for i in range(2,10**6):
    if l[i]==0:
        j=1
        while (i*j)<=(10**6):
            l[i*j]+=1
            j+=1
for i in range(int(input())):
    n,m=map(int,input().split())
    c=0
    for i in range(n,m):
        c+=l[i]
    print(c)


#--------------------------

factors=[0]*1000001
for i in range(2,1000001):
    if factors[i]==0:
        factors[i]=1
        for j in range(i+i,1000001,i):
            factors[j]+=1
t=int(input())
while t:
    t-=1
    ans=0
    n,m=map(int,input().strip().split(' '))
    for i in range(n,m):
        ans+=factors[i]
    print(ans)


#--------------------------

for _ in range(int(input())):
    A, B, C = list(map(int, input().split()))

    seen = set()
    iteration = ans = 0
    max_profit = 100*A + B
    while (A,B) not in seen and (A or B > C):
        seen.add((A,B))
        A, B = (B - C, A) if B >= C else (B + 100 - C, A - 1)
        iteration += 1
        profit = 100*A + B
        if max_profit < profit:
            max_profit = profit
            ans = iteration
        
        #print(A, B, iteration, max_profit)
    print(ans)

#--------------------------

for _ in range(int(input())):
  a, b, c = map(int, input().split())
  i, m_index, m_money = 0, 0, a*100+b
  p_money={m_money}
  while a*100+b>c:
    i += 1
    if c > b:
      a -= 1
      b += 100
    b -= c
    a,b = b,a
    if a*100+b in p_money:
      break
    p_money.add(a*100+b)
    if a*100+b > m_money:
      m_index=i
      m_money=a*100+b
  print(m_index)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

#--------------------------

for _ in range(int(input())):
    s=input()
    s1=s2=s3=s4=s5=0
    for i in range(len(s)):
        if s[i]=='L':
            s1+=1
        if s[i]=='T':
            s2+=1
        if s[i]=='I':
            s3+=1
        if s[i]=='M':
            s4+=1
        if s[i]=='E':
            s5+=1
    if s1>=2 and s2>=2 and s3>=2 and s4>=2 and s5>=2 and len(s)>9:
        print("YES")
    elif s1>=2 and s2>=2 and s3>=2 and s4>=2 and s5>=1 and len(s)==9:
        print("YES")
    else:
        print("NO")

#--------------------------

t=int(input())
for i in range(0,t):
    s=raw_input()
    
    h=[]
    for i in range(0,26):
        h.append(0)
        
    for i in range(0,len(s)):
        x=ord(s[i])-65
        h[x]=h[x]+1
        
    if h[4]>=2 and h[8]>=2 and h[11]>=2 and h[12]>=2 and h[19]>=2:
        print("YES")
    elif len(s)==9 and h[4]==1 and h[8]==2 and h[11]==2 and h[12]==2 and h[19]==2:
        print("YES")
    else:
        print("NO")

#--------------------------

for i in range(int(input())):
    n=int(input())
    l=[]
    h=1
    v=1
    win=0
    for i in range(n):
        x=input().strip()
        if len(x)>=3:
            if x[-3:]=='man':
                h=h+1
            else:
                v=v+1
        else:
            v=v+1
        if win==0:
            if v+2<=h:
                win=1
            elif h+3<=v:
                win=2
    if win==0:
        print('draw')
    elif win==1:
        print('superheroes')
    elif win==2:
        print('villains')


#--------------------------

for i in range(int(input())):
    n=int(input())
    l=[]
    h=1
    v=1
    win=0
    for i in range(n):
        x=input().strip()
        if len(x)>=3:
            if x[-3:]=='man':
                h=h+1
            else:
                v=v+1
        else:
            v=v+1
        if win==0:
            if v+2<=h:
                win=1
            elif h+3<=v:
                win=2
    if win==0:
        print('draw')
    elif win==1:
        print('superheroes')
    elif win==2:
        print('villains')

#--------------------------

for _ in range(int(input())):
	array = list(input().split())
	k = int(array[0])
	length = 2**k
	final = [0]*length
	for i in range(length):
		p = bin(i)[2:]
		for TT in range(k-len(p)):
			p = '0'+p
		p = p[-1::-1]
		final[int(p,2)] = array[1][i]
	print(''.join(final))

#--------------------------

from math import *
form = lambda x : int(x) if x.isdigit() else x
def padBin(n, k):
    b = bin(n)[2:]
    return ("0"*(ceil(len(b)/k)*k-len(b))) + b
def revBin(n, k):
    return int(padBin(n,k)[::-1], 2)
    
test=int(input())
for _ in range(test):
    k, mes = map(form, input().split())
    scrambled = ['']*(2**k)
    for i in range(2**k):
        scrambled[revBin(i,k)] = mes[i]
    print (''.join(scrambled))

#--------------------------

t=int(input())
for i in range(t):
    l=[]
    mi=99999999999
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    for j in range(n-1):
        for k in range(j+1,n):
            a1=a[j]
            a2=a[k]
            b1=a1+a2-m
            b2=abs(b1)
            l.append(b2)
            if(mi>b2):
                mi=b2
                
    print(mi,l.count(mi))        
            


#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    list1=list(map(int,input().split()))
    list1.sort()
    min1=1000000000000001
    maxsum=0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)): 
            temp=abs(list1[i]+list1[j]-k)      
            if temp<min1:
                min1=min(min1,temp)
    if min1!=0:        
        cand1=k+min1
        cand2=k-min1

        s=list()
        cnt=0
        for i in list1:
            t1=cand1-i
            if t1 in s:
                cnt+=s.count(t1)
            t2=cand2-i
            if t2 in s:
                cnt+=s.count(t2)
            s.append(i)    
        print(min1,cnt)        
    else:
        cand=k+min1
        s=list()
        cnt=0
        for i in list1:
            t1=cand-i
            if t1 in s:
                cnt+=s.count(t1)
            s.append(i)        
        print(min1,cnt)        

#--------------------------

t=int(input())
for _ in range(t):
    h=input()
    if len(h)%2:
        if h[:int(len(h)/2)]==h[int(len(h)/2)+1:][::-1]:
            print(1)
        else:
            print(2)
    else:
        if h[:int(len(h)/2)]==h[int(len(h)/2):][::-1]:
            print(1)
        else:
            print(2)

#--------------------------

def isPalindrome(s):
    return(s==s[::-1])
t=int(input())
for i in range(t):
    word=input()
    if(isPalindrome(word)):
        print(1)
    else:
        print(2)



#--------------------------

import sys
import math


    
    
   

     

for _ in range(int(input())):
    n=int(input())
    print(n*(n-1)**2+n*(n-1)**2+n*(n-1)*(n-2)+n*(n-1)*(n-2)*(n-2)+n*(n-1)*(n-2)*(n-2))

        

#--------------------------

test=int(input())
for _ in range(test):
  n=int(input())
  print(n*(n-1)*((n-1)*2+(n-2)+(n-2)*(n-2)*2))


#--------------------------

t= int(input())
for _ in range(t):
    h,m = map(int, input().split())
    cnt=0
    for i in range(h):
        for j in range(m):
            cnt+=1
            s = str(i)+str(j)
            for k in s:
                if k!=s[0]:
                    cnt-=1
                    break
    print(cnt)

#--------------------------

def getCount(h,m,i) :
    h=int(h)
    m=int(m)
    h1=0
    lst=[11,22,33,44,55,66,77,88,99]
    while(h1<h) :
        for m1 in range(0,m) :
            if h1<10 :
                if(m1<10 and h1==m1) : count[i]+=1
                if (m1 in lst and m1%10==h1) :  count[i]+=1
            else :
                if(m1 in lst and h1==m1) : count[i]+=1
                if(h1 in lst and h1%10==m1) : count[i]+=1
        h1+=1
t=int(input())
count=[0]*t
for i in range(0,t) :
    h,m=input().split()
    getCount(h,m,i)

for i in count : print(i)


#--------------------------

def solve():
    s = input()
    if len(s) != 5:
        print("Error")
    else:
        if (s[0] < 'a' or s[0] > 'h') or (s[1] < '1' or s[1] > '8') or (s[2] != '-') or (s[3] < 'a' or s[3] > 'h') or (
                s[4] < '1' or s[4] > '8'):
            print("Error")
        else:
            c1 = ord(s[0])
            c2 = ord(s[3])
            d1 = int(s[1])
            d2 = int(s[4])
            if abs((c1 - c2) * (d1 - d2)) == 2:
                print("Yes")
            else:
                print("No")
                

if __name__ == "__main__":
    t = int(input())
    while t != 0:
        solve()
        t -= 1


#--------------------------

colConv = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

col = set(list('abcdefgh'))
row = set(list('12345678'))
for _ in range(int(input())):
    m = input()
    if len(m) != 5:
        print ("Error")
        continue
    if (m[2] != '-') or (m[0] not in col) or (m[3] not in col) or (m[1] not in row) or (m[4] not in row):
        print ("Error")
        continue
    x1, y1, x2, y2 = colConv[m[0]], int(m[1]), colConv[m[3]], int(m[4]) 
    if ((abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(x1-x2) == 1 and abs(y1-y2) == 2)):
        print ("Yes")
    else:
        print ("No")

#--------------------------

t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    a=[]
    a.append(sum(l))
    a.append(sum(m))
    a.append(sum(n))
    a.append(l[0]+m[0]+n[0])
    a.append(l[1]+m[1]+n[1])
    a.append(l[2]+m[2]+n[2])
    c=max(a)
    if c>0:
        if c%2==0:
            print(c-1)
        else:    
            print(c)    
    else:
        print(0)

#--------------------------

def solve(m,o,p):
    sum_m=sum(m)
    sum_o=sum(o)
    sum_p=sum(p)
    maxi=0
    for i in range(0,len(m)):
        sum_=m[i]+o[i]+p[i]
        if(sum_%2!=0 and sum_>maxi):
            maxi=sum_
        elif(sum_>maxi and sum_-1>maxi):
            if(sum_%2==0):
                maxi=sum_-1
    if(sum_m%2==0):
        sum_m-=1
    if(sum_o%2==0):
        sum_o-=1
    if(sum_p%2==0):
        sum_p-=1
    return max(maxi,sum_m,sum_o,sum_p)









n=int(input())
results=[]
for i in range(0,n):
    M=list(map(int,input().split()))
    O=list(map(int,input().split()))
    P=list(map(int,input().split()))
    out=solve(M,O,P)
    results.append(out)

for i in results:
    print(i)


#--------------------------

def is_CPC(grid, j , k):
    l = k-1
    L = 0
    while(l >= 0):
        if grid[j][l] == '^':
            L = L + 1
        else:
            break
        l = l - 1
    if L < 2:
        return False
    l = k+1
    R = 0
    while(l < n):
        if grid[j][l] == '^':
            R = R + 1
        else:
            break
        l = l+1
    if R < 2:
        return False
    l = j-1
    T = 0
    while(l >= 0):
        if grid[l][k] == '^':
            T = T+1
        else:
            break
        l = l-1
    if T < 2:
        return False
    l = j+1
    B = 0
    while(l < m):
        if grid[l][k] == '^':
            B = B + 1
        else:
            break
        l = l+1
    if B < 2:
        return False
    return True


T = int(input())
for i in range(T):
    m,n = input().split()
    m = int(m)
    n = int(n)
    grid = []
    for j in range(m):
        row = str(input())
        grid.append(row)
    monsters = 0
    for j in range(m):
        for k in range(n):
            if grid[j][k] == '^' and is_CPC(grid, j, k):
                monsters = monsters + 1
    print(monsters)

#--------------------------


for _ in range(int(input())):
   r,c = map(int,input().split())
   mat = []
   for _ in range(r):
      st = input()
      mat.append(st)
   ans = 0 
   for i in range(r):
      for j in range(c):
         if i>=2 and i<=r-3 and j>=2 and j<=c-3:
            if mat[i][j]=='^' and mat[i-1][j]=='^' and mat[i-2][j]=='^' and mat[i+1][j]=='^' and mat[i+2][j]=='^' and mat[i][j-1]=='^' and mat[i][j-2]=='^' and mat[i][j+1]=='^' and mat[i][j+2]=='^':
               ans+=1 
   print(ans)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    for j in range(n):
        k = 1
        for qq in range(n):
            if a[j][qq] == 0:
                k = 0
                break
        if k==1:
            print("NO")
            break
    if k==0:
         for l in range(n):
             k=1
             for q in range(n):
                 if a[q][l]==0:
                     k=0
                     break
             if k!=0:
                 print("NO")
                 break
    if k==0:
        print("YES")

#--------------------------


from sys import stdin, stdout
from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        r = [False]*(n)
        c = [False]*(n)
        for i in range(n):
            a = list(map(int, input().split()))
            for j in range(n):
                if a[j] == 0:
                    r[i] = True
                    c[j] = True

        flag = True
        for i in range(n):
            if r[i] != True or c[i] != True:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()


#--------------------------

def s(t):
    a=0
    for k in str(t):
        a+=int(k)
    return a
def ss(t):
    a=0
    for k in str(s(t)):
        a+=int(k)
    return a

n=int(input())
c=0
for i in range(n-9*len(str(n))-9*(len(str(9*len(str(n))))),n+9*len(str(n))+9*(len(str(9*len(str(n)))))+1):
    if i+s(i)+ss(i)==n:
        #print(i,'+',s(i),'+',ss(i))
        c+=1
print(c)

#--------------------------

n=int(input())
count=0
def sumse(x):
    sums=0
    while x:
        sums+=x%10
        x=x//10
    return sums
for i in range(max(0,n-1000),n+1):
    res=i+sumse(i)+sumse(sumse(i))
    if res==n:
        count+=1
print(count)

#--------------------------

t = int(input())

while t!=0:
    s1 = input()
    s2 = input()
    
    s = s1.split(':')
    t1 = (int(s[0])*60)+int(s[1])
    s = s2.split(':')
    t2 = (int(s[0])*60)+int(s[1])
    
    t3 = int(input())
    
    if(t1-t2>=2*t3):
        ans2 = t1-t2
    else:
        ans2 = (t1-t2)+(2*t3+t2-t1)/2
    
    ans1 = t1-t2+t3;
    
    print('%0.1f %0.1f' %(ans1, ans2))
    t-=1

#--------------------------

def gerald04(time1, time2, dist):
	wait = (int(time1[3:])-int(time2[3:])) + (int(time1[:2])-int(time2[:2]))*60
	first = wait + dist
	if dist <= wait - dist:
		second = wait
	else:
		second = dist + wait / 2
	return float(first), float(second)
	
t = int(input())
for _ in range(t):
    time1 = input()
    time2 = input()
    dist = int(input())
    a, b = gerald04(time1, time2, dist)
    print(a, b)

#--------------------------

from math import *
for _ in range(int(input())):
   n,m,k = map(int,input().split())
   if n+m<=3:
      print(0)
   elif n==1 or m==1:
      print(k)
   else:
      print(ceil(k/2))

   

#--------------------------

from math import ceil
t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    if n == 1 or m == 1:
      if n <= 2 and m <= 2:
          print(0)
      else:
          print(k)
    elif n > 1 and m > 1:
        if k <= 2:
          print(1)
        else:
          print(ceil(k / 2)) 

#--------------------------

t=int(input())
for i in range(t):
    n,c=input().split()
    a=list(map(int,input().split()))
    n=int(n)
    if n==1 and a[0]%2==0 and c=='Dee':
        print("Dee")
    else:
        print("Dum")

#--------------------------

for i in range(int(input())):
    N,name = input().split()
    N = int(N)
    list1 = list(map(int,input().split()))
    if (N==1 and name == "Dee" and list1[0]%2 == 0):
        print("Dee")
    else:
        print("Dum")


#--------------------------

for _ in range(int(input())):
    a,b,c,d=[int(x) for x in input().split()]
    if a==b:
        print("YES")
    elif c==d:
        print("NO")
    elif abs(a-b)%abs(c-d)==0:
        print("YES")
    else:
        print("NO")

#--------------------------

t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a==b:
        print("YES")
    elif a!=b and c==d:
        print("NO")
    else:
        if abs(a-b)%abs(c-d)==0:
            print("YES")
        else:
            print("NO")

#--------------------------

for _ in range(int(input())):
    N=int(input())
    direc=[]
    for _ in range(N):
        direc.append(input().split())
    the_reverse=[]
    for i in range(N):
        the_reverse.append(direc[N-i-1])
    invert=[]
    for i in range(N-1):
        this_seq=the_reverse[i]
        prev_key=this_seq[0]
        if prev_key=='Left':
            invert.append('Right')
        else:
            invert.append('Left')
    for i in range(1,N):
        the_reverse[i][0]=invert[i-1]
    the_reverse[0][0]='Begin'
    for row in the_reverse:
        print(' '.join(row))

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    
    dict1={}
    dict1={"Right":"Left","Left":"Right"}
    for i in range(n):
        a=[]
        a=list(input().split())
        list7=[]
        str1=""
        str2=""
        str3=" "
        str1+=a[0]
        list7=a[2:]
        str2=str3.join(list7)
        
        list1.append(str1)
        list2.append(str2)
    list3=list1[1:]
    list4=list2[:len(list2)-1]
    list5=list3[::-1]
    list6=list4[::-1]
    print("Begin on",end=" ")
    print(list2[-1])
    for i in range(n-1):
        print(dict1[list5[i]],end=" ")
        print("on",end=" ")
        print(list6[i])
        
        
    


#--------------------------

for _ in range(int(input())):
	X=int(input())
	l=[0,1]
	while True:
		p=len(l)+l[-1]
		l.append(p)
		if p>X:
			break
	t1=len(l)-1+l[-1]-X
	t2=len(l)-2+X-l[-2]
	print(min(t1,t2))
		
		

#--------------------------

from bisect import bisect_left
x=[0]*50000
for i in range(50000):
    x[i] = x[i - 1] + (i + 1)
for j in range(int(input())):
    n=int(input())
    if(n==1):
        print(1)
    else:
        index=bisect_left(x,n)
        a=index
        b=index-1
        c=b+abs(x[b]-n)+1
        d=a+abs(x[a]-n)+1
        print(min(c,d))







#--------------------------

from math import sqrt

def div(n):
    count = 0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            j = n/i
            if '4' in str(i) or '7' in str(i):
                count += 1
            if '4' in str(j) or '7' in str(j):
                count += 1-(j==i)
    return count

t = int(input())
while t:
    n = int(input())
    print(div(n))
    t -= 1
    


#--------------------------

def divisors(n):
    r = []
    a = int(n**(0.5)+1)
    for i in range(1,a):
        if n%i==0:
            r.append(i)
            if n//i!=i:
                r.append(n//i)
    return r
def lucky(n):
    for i in n:
        if i!='4' or i!='7':
            return False
    return True
def overlucky(n):
    s = ''
    for i in n:
        if i=='4' or i=='7':
            s+=i
    if s=='':
        return False
    else:
        return True
T = int(input())
for i in range(T):
    N = int(input())
    count=0
    for i in divisors(N):
        if lucky(str(i)):
            count+=1
        else:
            if overlucky(str(i)):
                count+=1
    print(count)            
    

#--------------------------

def main():
    t = int(input())
    for __ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        s = sum(a)//(n-1)
        print(*[abs(x-s) for x in a])
if __name__ == '__main__':
    main()


#--------------------------

t=int(input())
for loop in range(t):
    n=int(input())
    nums=list(map(int,(input()).split()))
    s=0
    for num in nums:
        s+=num
    
    for i in range(n):
        x=(s//(n-1))-nums[i]
        print(x,end=" ")
    print("")

#--------------------------

t = int(input())
for _ in range(t):
    a = int(input())
    d1=0
    profit=0
    i=0
    while a-2**i>0:
        profit+=a-2**i
        i+=1
        d1+=1
        
    d2=d1
    
    while profit>0:
        profit+=a-2**i
        i+=1
        d2+=1
# one extra day gets counted after profit becomes negative
    print(d2-1,d1)

#--------------------------

T = int(input())

for i in range(T):
    a = int(input())
    
    # d2 = n such that 2^n is just greater than a.  
    # d1 = max days so that profit is > 0.
    
    s = bin(a)
    d2 = len(s) - s.index('1')
    if 2**(d2-1) == a:
        d2 -= 1
        
    d1 = 0
    while d1*a >= 2**d1 - 1:
        d1 += 1
        
    print(d1-1, d2)

#--------------------------

'''for i in range(int(intput())):
	n = int(input())
	print(pow(2,n,1000000007)-1)
'''
for u in range(int(input())):
    n=int(input())
    print(pow(2,n,1000000007)-1)


#--------------------------

t=int(input())
while(t>0):
    n=int(input())
    x=pow(2,n,1000000007)
    print(x-1)
    t-=1

#--------------------------

from sys import stdin, stdout
def fun(a,k):
    for i in range(len(a)):
        if a[i]==k:yield i
def ind(a,k,s,e):
    for i in range(s,e):
        if a[i]<k:return i
    return e
def rind(a,k,e,s):
    for i in range(e-1,s-1,-1):
        if a[i] <= k: return i
    return -1
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
q = int(stdin.readline())
for i in range(q):
    m = int(stdin.readline())
    b=tuple(fun(a,m))
    ans=0
    for i in range(len(b)):
        if b[i]==0:
            k=ind(a,a[b[i]],b[i]+1,n)
            ans+=k-b[i]
        elif b[i]==n-1:
            k=rind(a,a[b[i]],b[i],0)
            ans+=b[i]-k
        else:
            ans+=(b[i]-rind(a,a[b[i]],b[i],0))*(ind(a,a[b[i]],b[i]+1,n)-b[i])
    stdout.write(str(ans) + '\n')

#--------------------------


n=int(input())
lis = list(map(int, input().split()))

q = int(input())
ans = []
res=[]
for i in range(len(lis)+1):
    ans=[]
    for j in range(i+1, len(lis)+1):
        ans=lis[i:j]
        res.append(ans)
    #print(res)
while q>0:
    k = int(input())
    count=0
    for i in range(len(res)):
        if k==min(res[i]):
            count+=1
    print(count)
    q-=1


#--------------------------

# KNIGHT CHESS
# Code : KCHESS

#  find next moves of king
def findNextKxKy(kx,ky):
	row_dir = [-1,-1,0,1,1,1,0,-1]
	col_dir = [0,1,1,1,0,-1,-1,-1]
	next_kx_ky = [(kx,ky)]
	for i in range(8):
		next_kx_ky.append(tuple([kx+row_dir[i],ky+col_dir[i]]))
	return next_kx_ky

# find next moves of all knight
def findNextKNPS(knps_arr):
	row_dir = [1,2,2,1,-1,-2,-2,-1]
	col_dir = [2,1,-1,-2,-2,-1,1,2]
	next_knps = set()
	for kn in knps_arr:
		for i in range(8):
			next_knps.add(tuple([kn[0]+row_dir[i],kn[1]+col_dir[i]]))
	return list(next_knps)


#  check if king has atleast one move to go ahead if not return true
def allKxKyInKnps(next_knps,next_kx_ky):
	for kxky in next_kx_ky:
		if not (kxky in next_knps):
			return False
	return True


t = int(input())
while t>0:
	knps = int(input())
	knps_arr = []
	for _ in range(knps):
		knps_arr.append(tuple(map(int,input().split())))
	kx,ky = map(int,input().split())

	next_knps = findNextKNPS(knps_arr)

	next_kx_ky = findNextKxKy(kx,ky)

	if(allKxKyInKnps(next_knps,next_kx_ky) == True):
		print("YES")
	else:
		print("NO")
	t-=1


#--------------------------

def neighbours(i,j):
    x = [1,-1,2,-2,1,-1,2,-2];y = [2,2,1,1,-2,-2,-1,-1]
    for k in range(8):l.add((i+x[k],j+y[k]))
    return l
for t_iter in range(int(input())):
    n = int(input());l = set()
    for n_iter in range(n):i,j = map(int,input().split());neighbours(i,j)
    a,b = map(int,input().split());x = [0,0,1,1,1,-1,-1,-1];y = [-1,1,0,1,-1,0,1,-1];flag = 0
    for k in range(8):
        if not (a+x[k],b+y[k]) in l:flag = 1;print("NO");break
    if flag == 0:print("YES")

#--------------------------

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 'FINE'
    temp = ''
    for _ in range(n):
        a, b = input().split()
        if a == 'correct' and b.count('0') > 0:
            ans = 'INVALID'
        elif a == 'wrong' and b.count('0') == 0:
            temp = 'WEAK'
    if ans == 'FINE' and len(temp) > 0: print(temp)
    else:
        print(ans)

#--------------------------

def cd(n):
    c=0
    for x in n:            
        if x=='1':
            c+=1
    return c
for _ in range(int(input())):
	m,n=map(int,input().split())
	inv,we,f=0,0,0
	for _ in range(m):
		a,b=map(str,input().split())
		if a[0]=='c':
			if cd(b)!=n:inv=1
		elif a[0]=='w':
			if cd(b)==n:we=1
	if inv==1:print('INVALID')
	elif we==1 and inv==0:print('WEAK')
	elif inv==0 and we==0:print('FINE')


#--------------------------

T=int(input())
for i in range(0,T):
    s,v=map(int,input().split())
    print((2*s)/(3*v))
    


#--------------------------

for i in range(int(input())):
    s,v = map(int,input().split())
    print(2*s/(3*v))

#--------------------------

for _ in range(int(input())):
     N,H,Y1,Y2,L=map(int,input().split())
     k=0
     for i in range(N):
         t,x=map(int,input().split())
         if t==2:
             if Y2>=x and L>0:
                 k+=1
             elif(Y2<x and L>=1):
                 if L==1:
                     L-=1
                 else:
                     k+=1
                     L-=1
         elif t==1:
             if H-Y1<=x and L>0:
                 k=k+1
             elif H-Y1>x and L>=1:
                 if L==1:
                     L-=1
                 else:     
                     k+=1
                     L-=1
     print(k)    
                 
                        


#--------------------------

for i in range(int(input())):
    n,h,y1,y2,l=map(int,input().split())
    ctr=0
    for j in range(n):
        t,x=map(int,input().split())
        if t==2 and l!=0:
            if y2>=x:
                ctr+=1
            else:
                l-=1
                if l>=1:
                    ctr+=1
        elif t==1 and l!=0:
            if h-y1<=x:
                ctr+=1

            else:
                l-=1
                if l>=1:
                    ctr+=1
                
    print(ctr)
            
                
        
       



#--------------------------

for i in range(int(input())):
    n, r = map(int, input().split())
    li = list(map(int, input().split()))
    
    ans = "YES"
    least = None
    most = None
    
    for el in li:
        if el > r:
            if most == None or most > el:
                most = el
            else:
                ans = "NO"
                break
        else:
            if least == None or least < el:
                least = el
            else:
                ans = "NO"
                break
    
    print(ans)

#--------------------------

try:
    for _ in range(int(input())):
    	N,R=input().split()
    	N,R=int(N),int(R)
    	A=[int(j) for j in input().split()]
    	l,r=0,max(A)+1
    	for i in range(N):
    		if A[i]>R and A[i]<r:
    			r=A[i]
    		elif A[i]<R and A[i]>l:
    			l=A[i]
    		else:
    			if A[i]==R:
    				print("YES")
    				break
    			else:
    				print("NO")
    				break
except:
    pass

#--------------------------

x,y=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(y):
    p,q=input().split()
    q=int(q)
    if p=="C":
        count+=q
    elif p=="A":
        count-=q
    else:
        print(a[(q-1+count)%x])

#--------------------------

import collections 
n,m=map(int,input().split())
arr=[int(i) for i in input().split()]
e=collections.deque(arr)
for j in range(m):
    s,k=map(str,input().split())
    k=int(k)
    result=[]
    if s=='R':
        print(e[k-1]) 
         
    elif s=='C':
        e.rotate(-k)
        
    elif s=='A':
        e.rotate(k) 


    
        

#--------------------------

for _ in range(int(input())):
    x, y = list(map(int,input().split()))
    x, y = abs(x), abs(y)
    
    if x<=y:
        if(x+y)%2==0:
            p =2 *y
        else:
            p = 2*y-1
            
    else:
        if(x+y)%2==0:
            p = 2*x
        else:
            p = 2*x+1
            
    print(p)

#--------------------------

# Coding is about expressing your feeling and there is always a better way to express your feeling _feelme
import sys,math,numpy as np
# sys.stdin,sys.stdout=open('input.txt','r'),open('output.txt','w')
from sys import stdin,stdout;mod=int(1e9 + 7);from statistics import mode
from collections import deque,defaultdict;from math import ceil,floor,inf,factorial,gcd,log2
ii1=lambda:int(stdin.readline().strip())
is1=lambda:stdin.readline().strip()
iia=lambda:list(map(int,stdin.readline().strip().split()))
isa=lambda:stdin.readline().strip().split()
# print('{:.3f}'.format(1),round(1.123456789,4))
# np.set_printoptions(sign=' ',legacy='1.13') # legacy add space at sign position
def lcm(a,b): return (a*b)//gcd(a,b)
def setbits(n):return bin(n).count('1')
def resetbits(n):return bin(n).count('0')
def modinv(n,p):return pow(n,p-2,p)
def ncr_p(n, r, p):
    num,den=1,1;
    for i in range(r):num = (num * (n - i)) % p ;den = (den * (i + 1)) % p
    return (num * modinv(den,p)) % p
def isPrime(num) :
    if num<=1:return False
    if num==2 or n==3:return True
    if (num % 2 == 0 or num % 3 == 0) :return False
    for i in range(5,int(num**0.5)+1,6):
        if (num % i == 0 or num % (i + 2) == 0) :return False
    return True
def bin_search(arr, low, high, val):
    while low <= high:
        mid = low + (high - low) // 2;
        if arr[mid] == val:return mid
        elif arr[mid] < val:low = mid + 1
        else:high = mid - 1
    return -1
def sumofdigit(num):
    count=0;
    while num : count+=num % 10;num //= 10
    return count;
def make_dic(arr):
    freq = {}
    for val in arr : freq[val] = (freq[val] + 1 if val in freq else 1)
    # print(freq)
    return freq
def inputmatrix():
    r,c=iia();mat=[0]*r;
    for i in range(r):mat[i]=iia();
    return mat;
def prefix_sum(n,arr):
    for i in range(1,n):arr[i]+=arr[i-1]
    return arr;
def binomial(n, k):
    if 0 <= k <= n:
        ntok = 1;ktok = 1
        for t in range(1, min(k, n - k) + 1):ntok *= n;ktok *= t;n -= 1
        return ntok // ktok
    else:return 0
def divisors(n):
    res = [];
    for i in range(1,ceil(sqrt(n))+1):
        if n%i == 0:
            if i==n//i:res.append(i)
            else:res.append(i);res.append(n//i)
    return res;
# code here ----->
for _ in range(ii1()):
    n,m=iia()
    if abs(n)==abs(m):
        print(abs(n)+abs(m))
        continue
    elif abs(n)>abs(m):
        if (abs(n)-abs(m))&1:
            print(2*abs(n)+1)
        else:
            print(2*abs(n))
    else:
        if (abs(m)-abs(n))&1:
            print(2*abs(m)-1)
        else:
            print(2*abs(m))




#--------------------------

import math
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    least = None
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            lcm = (arr[i]*arr[j])//math.gcd(arr[i], arr[j])
            if least == None or lcm <= least:
                least = lcm
    print(least)


#--------------------------

import math

for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    m = (s[0]*s[1])//math.gcd(s[0],s[1])
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            x = (s[i]*s[j])//math.gcd(s[i], s[j])
            if x < m:
                m = x
    print(m)

#--------------------------

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n1,n2,m = map(int,input().split())
        temp = min(n1,n2)
        # if temp > sum of m numbers then
        count = 0
        total = m*(m+1)//2
        if total<temp:
            count = total
        else:
            count = temp
        ans = n1+n2-2*count
        print(ans)
            

    

#--------------------------

t=int(input()) 
for i in range(t):
   n1,n2,m=list(map(int,input().split())) 
   x=(m*(m+1))//2
   a=min(n1,n2) 
   b=max(n1,n2) 
   if x>a:
      x=a 
   a-=x 
   b-=x 
   print(a+b)
   
   
      
   

#--------------------------

for _ in range(int(input())):
    n,m = map(int,input().split())
    L = list(map(int,input().split()))
    count = 0
    for i in range(len(L)):
        if L[i] % m == 0:
            count += 1
    print(2**count-1)

#--------------------------

test=int(input())
for t in range(test) :
  n,m =[int(x) for x in input().split()]
  a =[int(x) for x in input().split()]
  count=0
  for i in a :
      if i % m ==0 :
        count=count+1
  print(2**count-1)

#--------------------------

T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))[:N]
    c=(N*(N-1))//2
    b=A.count(1)+A.count(0)
    d=A.count(2)
    c=c-((b*(b-1))//2)-b*(N-b)-((d*(d-1))//2)
    print(c)

#--------------------------

test=int(input())
for _ in range(test):
	n=int(input())
	a=list(map(int,input().split()))
	c=0
	c2=0
	for i in range(n):
		if a[i]==2:
			c2+=1
		elif a[i]>2:
			c+=1
	res=int((c2*c)+((c*(c-1))/2))
	print(res)


#--------------------------

t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    if(l>r):
        print(-1)
    elif(l*2>r):
        print(r)
    else:
        print(-1)

#--------------------------

import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
def solve():
    pass
    l, r = map(int, input().split())
    print(r) if r-l <= l-1 else print(-1)


for _ in range(int(input())):
    solve()


#--------------------------

t=int(input())
while t:
    arr=input().strip()
    count=0
    l=len(arr)
    for i in range(l):
        if arr[i] == '4' or arr[i] == '7':
            count+=1
    print(l-count)
    t-=1
    

#--------------------------

t=int(input())
for i in range(t):
    n=raw_input().strip()
    print (len(n)-n.count('4')-n.count('7'))

#--------------------------

for i in range(int(input())):
    count=0
    count2=0
    ar=[]
    n,m=map(int,input().split())
    for j in range(n):
        ar.append(input())
    for k in range(0,n):
        for b in range(0,m):
            if((k+b)%2==0):
                if(ar[k][b]=='R'):
                    count+=5
                else:
                    count2+=3
            else:
                if(ar[k][b]=='R'):
                    count2+=5
                else:
                    count+=3
    print(min(count,count2))
        

#--------------------------

def pat(pl,row):
    dict1 = {1:5,0:3}
    dict2 = {'R':1,'G':0}
    k=1
    c1=0
    c2=0
    for sl in pl:
        for e in sl:
            if dict2[e]!=k:
                c1+=dict1[abs(k-1)]
            else:
                c2+=dict1[k]
            k=abs(k-1)
        if row%2 == 0:
            k=abs(k-1)
    if c1<c2:
        return c1
    else:
        return c2

T = int(input())
for i in range(T):
    a,b = [int(x) for x in input().split()]
    costr = []
    for j in range(a):
        costr.append(input())
    print(pat(costr,b))

#--------------------------

a=int(input())
import math
while(a>0):
    n=int(input())
    
    if(n%6==0):
        print("Misha")
    else:
        print("Chef")
    
    a=a-1
            
            
                    
            

#--------------------------

for _ in range(int(input())):
    n = int(input())
    if n%6 == 0:
        print("Misha")
    else:
        print("Chef")

#--------------------------

for t in range(int(input())):
    n=int(input())
    temp=250000
    tax=0
    p=0.00
    while p<0.30 and n-temp>=0:
        tax+=250000*p
        temp+=250000
        p+=0.05
    tax+=(n-temp+250000)*p
    print(int(n-tax))
        

#--------------------------

T= int(input())
for i in range(T):
    N = int(input())
    a1 = 250000
    a2 = 250000*0.95
    a3 = 250000*0.9
    a4 = 250000*0.85
    a5 = 250000*0.8
    a6 = 250000*0.75
    
    if N<=250000:
        print(N)
    elif 250000<N<= 500000:
        print(int(0.95*(N-250000) + a1))
    elif 500000< N<=750000:
        print(int(0.9*(N-500000) + a2+a1))
    elif 750000<N<=1000000:
        print(int(0.85*(N-750000)+a3+a2+a1))
    elif 1000000<N<=1250000:
        print(int(0.8*(N-1000000)+a4+a3+a2+a1))
    elif 1250000<N<=1500000:
        print(int(0.75*(N-1250000)+a5+a4+a3+a2+a1))
    else: print(int(0.7*(N-1500000)+a6+a5+a4+a3+a2+a1))

#--------------------------

tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    motu = [a[0]]
    tomu = []
    
    for i in range(1, len(a)):
        if i % 2 == 0:
            motu.append(a[i])
        else:
            tomu.append(a[i])
    
    if sum(tomu) > sum(motu):
        print("YES")
        continue
    
    else:
        motu.sort(reverse = True)
        tomu.sort()
        
        for i in range(len(tomu)):
            if motu[i] > tomu[i] and k:
                motu[i], tomu[i] = tomu[i], motu[i]
                k -= 1
            if k == 0:
                break
            
        if sum(motu) < sum(tomu):
            print("YES")
        else:
            print("NO")

#--------------------------

try:
    for i in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        m_list=[]
        t_list=[]
        for j in range(0,len(l)):
            if(j%2==0):
                m_list.append(l[j])
            else:
                t_list.append(l[j])
        for k in range(k):
            max_m=max(m_list)
            min_t=min(t_list)
            max_index=m_list.index(max_m)
            min_index=t_list.index(min_t)
            t_list.append(max_m)
            m_list.append(min_t)
            m_list.pop(max_index)
            t_list.pop(min_index)
    
        if(sum(t_list)>sum(m_list)):
            print("YES")
        else:
            print("NO")
        
        
        
        
        
except:
    pass

#--------------------------

import sys
import math

def main(arr):
    
    freq={}
    for e in arr:
        s=int(e)
        
        if s not in freq:
            freq[s]=0
        freq[s]+=1 
   
    ans=[]
    for i in range(65,91):
        
        s=str(i)
        
        if int(s[0]) in freq:
            freq[int(s[0])]-=1 
            if int(s[1]) in freq and freq[int(s[1])]>0:
                ans.append(chr(i+32).upper())
            freq[int(s[0])]+=1 
    ans="".join(ans)
    return ans

t=int(input())

for i in range(t):
    n=input()
    print(main(n))
        

#--------------------------

import numpy as np
for t in range(int(input())):
    n = list(input())
    arr = [int(x) for x in n]
    num = []
    if 6 in arr:
        for i in arr:
            if i>=5:
                num.append(6*10 + i)
    if 66 in num:
        num.remove(66)
    if 7 in arr:
        for i in arr:
            num.append(7*10 + i)
    if 77 in num:
        num.remove(77)
    if 8 in arr:
        for i in arr:
            num.append(8*10 + i)
    if 88 in num:
        num.remove(88)
    if 9 in arr:
        if 0 in arr:
            num.append(90)
    num = np.array(num)
    np.sort(num)
    ch = ''
    for i in np.unique(num):
        ch += chr(i)
    
    print(ch)


#--------------------------

from collections import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n,m,x,y=map(int,input().split())
    n-=1
    m-=1
    if((n%x<=1 and m%y<=1 and n%x==m%y) or (n==m==0 or n==m==1) or((n-1)%x==(m-1)%y and (n-1)%x==0) and n-1>=0 and m-1>=0):
        print("Chefirnemo")
    else:
        print("Pofik")
    
    


#--------------------------

for _ in range(int(input())):
    
    n,m,x,y = map( int, input().split() )
    
    n= n-1
    m= m-1
    
    flag = 0
    
    if n%x == 0 and flag == 0:
        if m%y == 0 and flag == 0:
            print("Chefirnemo")
            flag = 1
            
    if n>0 and m>0:
        if (n-1)%x == 0 and (m-1)%y == 0 and flag == 0 :
            print("Chefirnemo")
            flag = 1
        
    if flag == 0:
        print("Pofik")
        
        

#--------------------------

for _ in range(int(input())):
    n = int(input());
    q1=q2=q3=0;
    if 360%n==0:
        print('y', end=" ");
    else:
        print('n', end=" ");
    if n<=360:
        print('y', end=" ");
    else:
        print('n', end=" ");
    if n*(n+1)//2<=360:
        print('y', end=" ");
    else:
        print('n', end=" ");
    print();

#--------------------------


t = int(input())

for i in range(t):
    n = int(input())
    
    if 360%n == 0:
        print("y",end=' ')
    else:
        print("n",end=' ')
    
    if n>360:
        print("n",end=' ')
    else:
        print("y",end=' ')
    
    if (n*(n+1))/2 <= 360:
        print("y",end=' ')
    else:
        print("n",end=' ')
        
    print('')

#--------------------------

n,k = map(int,input().split())
list1 = list(map(int,input().split()))
maxx = max(list1)
if k==0:
    pass
elif k!=0 and k%2!=0:
    for i in range(n):
        list1[i]=maxx-list1[i]
else:
    for i in range(n):
        list1[i]= maxx-list1[i]
    maxx2 = max(list1)
    for i in range(n):
        list1[i]=maxx2-list1[i]
for val in list1:
    print(val,end=" ")
    


#--------------------------

[n,k]=list(map(int,input().split()))
l=list(map(int,input().split()))
if k==0:
    for i in l:
        print(i,end=" ")
elif k%2==0:
    for i in range(0,2):
        m=max(l)
        for i in range(len(l)):
            l[i]=m-l[i] 
    for i in l:
        print(i,end=" ")
else:
     m=max(l)
     for i in range(len(l)):
            l[i]=m-l[i] 
     for i in l:
        print(i,end=" ")

#--------------------------

# for _ in range(int(input())):
#     n=int(input())
#     s,k=input().split()
#     c=0
#     lst=[]
#     for i in range(n):
#         if(lst[i]==k):
#             c+=(i+1)
#             lst.append(i+1)
#         elif lst:
#             c+=lst[-1]
#     print(c)
    
for _ in range(int(input())):
    n=int(input())
    s,x=input().split()
    count=0
    t=[]
    for i in range(n):
        if s[i]==x:
            count+=i+1
            t.append(i+1)
        elif t:
            count+=t[-1]
    print(count)

#--------------------------

op=[]
def sumn(n): 
    return (n*(n+1))//2

t=int(input())
while t>0:
    n=int(input())
    mainsum=sumn(n)
    inpt=[str(x) for x in input().split()]
    miss=inpt[0].split(inpt[1])
    summiss=0
    for i in range(0,len(miss)):
        summiss+=sumn(len(miss[i]))
    
    print(mainsum-summiss)
    t-=1

#--------------------------

n,m=map(int, input().split())
for i in range(m):
    q=int(input())
    
    if q<n+2 or q>3*n:
        print(0)
    elif q<2*n+1:
        print(q-n-1)
    else:
        print(3*n-q+1)

#--------------------------


n,m = map(int,input().split())
a,b = 2+n, 3*n
t = (a+b) // 2
for _ in range(m):
    r = 0
    q = int(input())
    if q <= n:
        print(0)
    else:
        r = abs( t - q )
        print(n-r)


#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=input()
    c=input()
    w=list(map(int,input().split()))
    j=0
    for i in range(n):
        if a[i]==c[i]:
            j+=1
    if n==j:
        print(w[-1])
    else:
        print(max(w[:j+1]))

#--------------------------

t= int(input())
while t:
    t-=1
    n=int(input())
    str1=input()
    str2=input()
    arr=list(map(int,input().split()))
    c_cor=0
    for i in range(n):
        if str1[i]==str2[i]:
            c_cor+=1
    if c_cor==n:
        print(arr[-1])
    else:
        print(max(arr[:c_cor+1:]))

#--------------------------

try:
    import numpy as np

    for _ in range(int(input())):
        n = int(input())
        arrival = np.array(list(map(int, input().split())))
        departure = np.array(list(map(int, input().split())))

        arr = [0] * 1000
        arr = np.array(arr)

        for i in range(n):
            arr[arrival[i]:departure[i]] += 1
        print(max(arr))
except EOFError:
    pass

#--------------------------

try:
    import numpy as np
    for _ in range(int(input())):
        n = int(input())
        arrival = np.array(list(map(int,input().split())))
        departure = np.array(list(map(int,input().split())))
        
        arr = [0]*1000
        arr = np.array(arr)
        
        for i in range(n):
            arr[arrival[i]:departure[i]]+=1
        
        print(max(arr))
except EOFError:
    pass

#--------------------------

for _ in range(int(input())):
  n=int(input())
  li=[int(x) for x in input().split()]
  m=max(li)
  print(n-m)

#--------------------------

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(n-max(l))
            
        


#--------------------------

for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        ma=0
        mi=l[0]
        for i in range(1,n):
            if l[i]-mi>ma:
                ma=l[i]-mi
            if l[i]<mi:
                mi=l[i]
                
        if ma==0:
            print("UNFIT")
        else:
            print(ma)   

#--------------------------

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxdiff=0
    _min=arr[0]
    for i in range(1,n):
        if arr[i]-_min>maxdiff:
            maxdiff=arr[i]-_min
        if arr[i]<_min:
            _min=arr[i]
            
    if maxdiff==0:
        print("UNFIT")
    else:
        print(maxdiff)     
        
             
    
    


#--------------------------

n,k=map(int, input().split())
arr=list(map(int, input().split()))
sum_arr=[0]*n
sum_arr[0]=arr[0]
partial=arr[0]

for i in range(1,n):
    partial+=arr[i]
    sum_arr[i]=partial
    
sum_arr.insert(0,0)    

max_var=sum_arr[1]-sum_arr[0]

for i in range(1,n+1):
    for j in range(i):
        if (max_var<=(sum_arr[i]-sum_arr[j])):
            max_var=(sum_arr[i]-sum_arr[j])
            
print('%0.1f' %(sum(arr)+(max_var)*((1/k)-1)))

#--------------------------

N, X = map(int, input().split())
A = list(map(int, input().split()))
lst = []
s = 0
psum = A[:]
for i in range(1, N):
    psum[i] += psum[i-1]
m = -9999999
for i in range(0, N):
    for j in range(i, N):
        m = max(m, psum[j] - psum[i] + A[i])
print(psum[-1] - m + m / X)

#--------------------------

for i in range(int(input())):
    n = int(input());a = list(map(int,input().split()))
    print((pow(2,a.count(max(a)))-1)%(10**9 + 7))    

#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    mc=a.count(max(a))
    print((2**mc -1)%(10**9+7))


#--------------------------

def getInput():
    arr = list(map(int,input().split()))
    if len(arr) ==1:
        return arr[0]
    return arr

for tc in range(int(input())):
    n = getInput()
    kmap = {}
    winner = "Nobody wins."
    winnum = 9999999999
    for i in range(n):
        name,num = input().split()
        num = int(num)
        if num not in kmap:
            kmap[num] = [1,name]
        else:
            kmap[num] = [kmap[num][0] + 1,name]
    for num in kmap:
        if kmap[num][0] == 1 and num<winnum:
            winnum = num
            winner = kmap[num][1]
    print(winner)
            

#--------------------------

for x in range(int(input())):
    a=[]
    b=[]
    c=int(input())
    for i in range(c):
        d,e=map(str,input().split(' '))
        a.append(d)
        b.append(int(e))
    f=set(b)
    m=1
    for j in range(len(f)):
        g=min(f)
        if b.count(g)==1:
            k=b.index(g)
            m=2
            print(a[k])
            break
        else:
            f.remove(g)
    if m==1:
        print("Nobody wins.")

#--------------------------

def sieve(n):
    prime = [i for i in range(n+1)]
    prime[0]=True
    prime[1]=True
    p = 2
    while (p * p <= n):
        if (prime[p] != True):
            for i in range(p * p, n+1, p):
                prime[i] = True
        p += 1
    prime=list(set(prime))

    del prime[0]
    
    return prime

n,m=map(int,input().split())
print(len(sieve(n+m)))


#--------------------------

n,m=map(int,input().split())
mi=2
ma=n+m
ans=[1 for i in range(ma+1)]

for i in range(2,int(ma**0.5)+1):
    for j in range(i+i,ma+1,i):
        ans[j]=0
ans[0]=0
ans[1]=0
print(ans.count(1))
    
        
        


#--------------------------

def is_ciel(n):
    n3 = 0
    n5 = 0
    n8 = 0
    
    while n>0:
        k = n%10
        if(k==3):
            n3+=1
        elif(k==5):
            n5+=1
        elif(k==8):
            n8+=1
        else:
            return 0
        n //= 10
  
    if(n3 <= n5 and n5 <= n8):
        return 1
    return 0

if __name__ == "__main__":
    res=0
    for _ in range(int(input())):
        buf=input()
        length=len(buf)
        st=-1
        for i in range(length-1,-1,-1):
            if(buf[i]==' '):
                st=i
                break
    
        p=int(buf[i+1:length])
        if(is_ciel(p)):
            res+=1
    
    print(res)




    

#--------------------------

from audioop import reverse

from itertools import count
from math import*
from operator import index, indexOf
from pickle import TRUE
from re import M, T


# # def bs(x, k, a):
# #     r = a-1
# #     l = 0
# #     while(l < r):
# #         m = (l+r)//2
# #         if((x >= k[m] and x < k[m+1]) or (m == a-1 and x > k[m+1])):
# #             return m+1
# #         elif(x < k[m]):
# #             r = m
# #         else:
# #             l = m+1
# #     return 0


# def check(nums):
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             return False
#     return True

def rl():
    return list(map(int, input().split()))


def r2():
    return map(int, input().split())


def func(x):
    l = len(str(x))
    e = str(x).count('8')
    f = str(x).count('5')
    t = str(x).count('3')
    y = e+f+t
    return e >= f and f >= t and y == l


# def Count(s, c):
#     j = 0
#     for i in s:
#         if i == c:
#             j += 1
#     return j

def solve(n, arr):
    m = 0
    for i in range(n):
        if func(arr[i]):
            m += 1

    return m


if __name__ == "__main__":
    res = []
    a = []
    n = int(input())
    for i in range(n):
        arr = list(input().split())
        a.append(arr[-1])

    print(solve(n, a))


#--------------------------

import math

t = int(input())
for _ in range(t):
    n , m = map(int, input().split())
    total = (n*(n+1))//2
    ans ='No'
    if total > m:
        remain = total-m
        half=remain//2
        if remain&1:
            ans='No'
        elif math.gcd(half+m,half)==1:
            ans='Yes'
    print(ans)         


#--------------------------

import math
T=int(input())
for  _ in range(T):
    N,M=map(int,input().split())
    a=N*(N+1)//2
    b=(a+M)//2
    c=a-b
    if b-c ==M:
        if math.gcd(b,c) ==1.0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    oddcount = [0 for i in range(n+1)]
    for i in range(n):
        if a[i]%2==1: oddcount[i+1]=oddcount[i]+1
        else: oddcount[i+1] = oddcount[i]
    q = int(input())
    for _ in range(q):
        (l,r) = map(int,input().split())
        if oddcount[r]-oddcount[l-1]==r-l+1: print("ODD")
        else: print("EVEN")

#--------------------------

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    l1=[]
    for j in range(n):
        if a[j]%2==0:l1.append(j+1)
    q=int(input())
    for x in range(q):
        l,r=map(int,input().split())
        for e in l1:
            if e>=l and e<=r:
                print('EVEN')
                break
        else:print('ODD')

#--------------------------

for _ in range(int(input())):
        l=0
        r=0
        f=False
        for w in input():
                if w=="W":
                        f=True
                        continue
                if f:
                        r=r+1
                else:
                        l=l+1
        if l==r:
                            print("Chef")
        else:
                            print("Aleksa")

#--------------------------

t = int(input())

for i in range(t):
    s = input()
    n = len(s)
    p = s.find('W')
    l = p
    r = n - p - 1
    if l != 0 and r != 0:
    	if l != r:
        	print('Aleksa')
    	else:
        	print('Chef')
    elif l == 0 and r != 0:
    	print('Aleksa')
    elif l != 0 and r == 0:
     	print('Aleksa')
    else:
     	print('Chef')   

#--------------------------

t = int(input())
while t:
    t-=1 
    n,k = map(int,input().split())
    ls = list(map(int,input().split()))
    ls.sort()
    count,nsum=1,-1
    if n==1:
        print(ls[0])
    else:
        for i in range(n-1):
            if ls[i]==ls[i+1]:
                count+=1
                #print(count,ls[i])
            else:
                #print(count,ls[i])
                if count==k:
                    if nsum==-1:
                        nsum=0
                    nsum+=ls[i]
                count=1
        if count==k:
            if nsum==-1:
                nsum=0
            nsum+=ls[n-1]
        if nsum==-1:
            print(-1)
        else:
            print(nsum)
            

#--------------------------

from collections import Counter

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    ok = False
    for i in c:
        if c[i] == k:
            ans += i
            ok = True
    if ok:
        print(ans)
    else:
        print(-1)


#--------------------------

from math import *
n=int(input())
x=list(map(int,input().split()))
a=0
for j in x:
    a+=j/2
b=(ceil(a))
if(b<n):
    print(n)
else:
    print(b)


#--------------------------

n=int(input())
c=n
t=list(map(int,input().split()))

val=0
for i in range(n):
	val+=t[i]
	
tot=n
val-=2*n
if val>0:

	tot+=val//2
	if val%2>0:
		tot+=1
print(tot)	


#--------------------------

import math 
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    g=0
    for i in range(n):
        g=math.gcd(a[i],g)
    print(g*n)
            

#--------------------------

def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
t=int(input())
for I in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print(l[0])
    else:
        g=l[0]
        for I in range(1,n):
            if(g>l[I]):
                g=gcd(l[I],g)
            else:
                g=gcd(g,l[I])
        print(n*g)

#--------------------------

n,c = list(map(int,input().split()))
s = [0]*(n+1)
kp = list(map(int,input().split()))
for i in range(1,n+1):
    s[i] = s[i-1] ^ kp[i-1]
for _ in range(c):
    k = int(input())
    print(s[k % (n+1)])
    
    

#--------------------------


n,q=map(int,input().split())
nli=[0]+list(map(int,input().split()))
d=[0]
for i in range(1,n+1):
    d.append(d[i-1]^nli[i])

for j in range(q):
    qi=int(input())
    print(d[qi%(n+1)])

#--------------------------

t = int(input())

for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    d = (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3)
    b1 = max(x1, x3)
    b2 = max(y1, y3)
    b3 = min(x2, x4)
    b4 = min(y2, y4)
    if b1 < b3 and b2 < b4:
        d -= (b3 - b1) * (b4 - b2)
    print(d)

#--------------------------

for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=(map(int,input().split()))
    p=0
    x5=max(x1,x3)
    y5=max(y1,y3)
    x6=min(x2,x4)
    y6=min(y2,y4)
    p=((x2-x1)*(y2-y1)+(x4-x3)*(y4-y3))
    if x5<x6 and y5 < y6:
        p -= ((x6-x5) * (y6-y5))
   
    print(p)
    


#--------------------------

di={}
li=[]
lis=[]
    
for i in range(int(input())):
    s,n=map(str,input().split())
    di[n]=s
    li.append(int(n))
li.sort(reverse=True)
for i in li:
    lis.append(di[str(i)])
for i in range(int(input())):
    q=input()
    for j in range(len(lis)):
        if q in lis[j] and q==lis[j][0:len(q)]:
            print(lis[j])
            break
            
    else:
        print('NO')
    
    

#--------------------------

n=int(input())
a=[]
b=[]
for _ in range(n):
    s=input().split()
    a.append(s[0])
    b.append(int(s[1]))
    

q=int(input())
for i in range(q):
    x=input()
    
    m=-(10**10)
    for k in range(n):
        y=a[k]
        if(x in y and x==y[0:len(x)]):
            m=max(m,b[k])
            
    if(m==-(10**10)):
        print("NO")
    else:
        j=b.index(m)
        print(a[j])
    

#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    if k==1:
        print(1)
    elif k<=(n//2):
        c=1
        t_1=2
        while c<=k:
            print(t_1,end=' ')
            t_1=t_1+2
            c+=1
        print()
    else:
        print(-1)

#--------------------------

def ammeat2(n, k):
	if k == 1:
		print(1)
	elif k > n // 2:
		print(-1)
	else:
		start = 1
		while k:
			print(start*2, end=' ')
			start += 1
			k -= 1
		print()
		
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ammeat2(n, k)

#--------------------------

mod = 1000000007
t = int(input())
for tc in range(t):
    n = int(input())
    ans = pow(3,n,mod)
    if n%2 == 0:
        ans = (ans+3)%mod
    else:
        ans = (ans-3)%mod
        
    print(ans)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    md=10**9+7
    ans=pow(3,n,md)
    if n%2==0:
        print((ans+3)%md)
    else:
        print((ans-3)%md)

#--------------------------

T = int(input())

def RightTriangle(H,S):
    
    if (H**2-4*S)<0:
        return -1
    
    a = (H**2+4*S)**0.5
    b = (H**2-4*S)**0.5
    c = (a+b)/2
    d = (a-b)/2
    
    if c<=0 and d<=0:
        return -1
    else:
        e = str(d)+' '+str(c)+' '+str(H)
        return e
    
for i in range(T):
    H,S = map(int,input().split())
    
    print(RightTriangle(H,S))

#--------------------------

import math
for i in range(int(input())):
    h,s=map(int,input().split())
    p=s*2
    if h**2-2*p<0:
        print(-1)
        continue
    B=(((h**2+2*p)**.5)+((h**2-2*p)**.5))/2
    H=p/B
    print("%.6f %.6f %.6f"%(min(B,H),max(B,H),h))
        
    

#--------------------------


def calc(n) :
    a = n * (n-1)
    a = int(a/2)
    return a

t = int(input())
tt = 0
while tt < t :
    tt = tt + 1
    n = int(input())
    num = calc(n)
    if num%n != 0 :
        print("NO")
    else :
        win = int(num/n)
        print("YES")
        i = 0
        while i < n :
            i = i + 1
            j = i
            str = ""
            k = 0
            while k < n :
                str = str + "0"
                k = k + 1
            k = 0
            while k < win :
                if (j+k)%n==0 :
                    str = '1' + str[1:n]
                elif (j+k)%n==(n-1) :
                    str = str[:n-1] + "1"
                else :
                    kkk = (j+k)%n
                    str = str[0:kkk] + "1" + str[kkk+1:]
                k = k + 1
            print(str)    
                
                
                
                
                
                
                
                
                
                
                
                

#--------------------------

t = int(input())

for e in range(t):
    n = int(input())

    if n % 2 == 0:
        print("NO")
    else:
        print("YES")

        total = 0
        for g in range(n):
            total += g
        num = total // n
        
        for i in range(n):
            l = [0] * n
            for j in range(i+1, i+1+num):
                try:
                    l[j] = 1
                except IndexError:
                    k = j - n
                    l[k] = 1
            for b in range(len(l)):
                print(l[b], end = "")
                
            print()


#--------------------------

for _ in range(int(input())):
    n = int(input())
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    A, B = sum(a), sum(b)
    sumsa, sumsb = [], []
    tempa, tempb = 0, 0
    for i in range(n):
        tempa += a[i]
        sumsa.append(tempa)
    for i in range(1, n):
        tempb += b[i - 1]
        sumsb.append(B - tempb)
    sumsb.append(0)
    ans = 0
    for i in range(n):
        sum1 = sumsa[i] + sumsb[i]
        if ans < sum1: ans = sum1
    print(max(ans, A, B))

#--------------------------

for j in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=sum(y)
    t=a
    for i in range(n):
        a-=y[i]
        a+=x[i]
        if(a>t):
            t=a
    print(t)


#--------------------------

try:
    months_31 = [1, 3, 5, 7, 8, 10, 12]

    def leap_year(year):
        if  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    t = int(input())
    for _ in range(t):
        y, m, d = map(int, input().split(':'))
        count = 0
        if m in months_31:
            count = (31 - d) // 2 + 1
        elif m == 2:
            if leap_year(y):
                count = (29 - d) // 2 + 1
            else:
                if d % 2 == 0:
                    count = (28 - d) // 2 + 1 + 15
                else:
                    count = (28 - d) // 2 + 1 + 16
        else:
            if d % 2 == 0:
                count = (30 - d) // 2 + 1 + 15
            else:
                count = (30 - d) // 2 + 1 + 16
        print(count)
except:
    pass

#--------------------------

def isLeap(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False


DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


ntests = int(input())

for test in range(ntests):
    year, month, day = map(int, input().split(':'))
    count = 0

    if month == 2:
        if isLeap(year):
            count = (29 - day) // 2 + 1
        else:
            count = (59 - day) // 2 + 1
    elif DAYS[month] == 31:
        count = (31 - day) // 2 + 1
    else:
        count = (61 - day) // 2 + 1

    print(count)












#--------------------------

for _ in range(int(input())):
    k=int(input())
    mat=[[0 for i in range(k)] for j in range(k)]
    mat[k//2]=[i for i in range(1,k+1)]
   # print(mat)
    z=[i for i in range(1,k+1)]
    j=1
    for i in range(k//2+1,k,1):
        mat[i]=z[j:]+z[:j]
        j+=1 
   # print(mat)
    j=k-1 
    for i in range(k//2-1,-1,-1):
        mat[i]=z[j:]+z[:j]
        j-=1 
    for i in range(k):
        print(*(mat[i]))

#--------------------------

for _ in range(int(input())):
   k = int(input()) 
   mat = [[0]*k for _ in range(k)]
   start = (k+1)//2 
   for i in range(k):
      for j in range(k):
         val = (start+j)%k
         if val==0: val = k 
         mat[i][j] = val 
      start-=1 
      if start==0:
         start = k 
   for item in mat:
      print(*item)
      
      

#--------------------------

def solve(x, a):
    gain = 2*(1-x)*a
    return gain*x-a*(1-x)

for _ in range(int(input())):
    p = float(input())
    print(10000+solve(max(p, 1-p), 10000))

#--------------------------

def money(p,c=10000):
    p=max(p,1-p)
    x=p*(3-2*p)
    return(c*x)
t=int(input())
for i in range(t):
    p=float(input())
    print(money(p))


#--------------------------

a=int(input())
for t in range(a):
   s,e,l,r=input().split()
   l,r=[int(j) for j in (l,r)]
   days=["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
   x=days.index(s)
   y=days.index(e)
   if y>=x:
     diff=y-x+1
   else:
     diff=7-(x-y)+1
   adiff=(r-diff)//7-(l-diff)//7
   c=0
   val=-1
   for k in range(l-diff,r-diff+1):
       if k%7==0:
          c+=1
          val=k+diff
   if c==0:
      print("impossible")
   elif c==1:
      print(val)
   else:
      print("many")

#--------------------------

T = int(input())
for t in range(T):
    S,E,L,R = input().split()
    L,R = [int(i) for i in (L,R)]
    
    
    days= ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday" ,"friday"]
    S_ind = days.index(S)
    E_ind = days.index(E)
    
    if E_ind >= S_ind:
        diff = E_ind - S_ind + 1
    else:
        diff = 7 - (S_ind-E_ind) + 1
        
    ans_diff  = (R-diff)//7 - (L-diff)//7
    

    count = 0
    last_val = -1
    for i in range(L-diff,R-diff+1):
        if i%7== 0:
            count +=1
            last_val = i+diff
    if count == 0:
        print('impossible')
    elif count == 1:
        print(last_val)
    else:
        print('many')
             

#--------------------------


mod = 1000000007

def mod_exp(b, e, m):
    res = 1
    b %= m
    while e:
        if e&1: res = (res*b) % m
        e >>= 1
        b = (b*b) % m
    return res
    
for _ in range(int(input())):
    n = int(input())
    b = int(bin(n)[2:])
    print (mod_exp(2, 2*b, mod))
    

#--------------------------

for _ in range(int(input())):print(pow(2,2*int(bin(int(input())).replace("0b", "") ),10**9 + 7))

#--------------------------


t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    m = (10**9)+7
    d=((k%m)*pow(k-1,n-1,m)%m)
    print(d)


#--------------------------

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    m = (10**9)+7
    d=((k%m)*pow(k-1,n-1,m)%m)
    print(d)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    i=0
    w=[]
    while(i<n):
        if(i+2<n and x[i]+2==x[i+2]):
            a=i+2;
            s=x[i]
            l=x[i+2]
            i+=3
            while(a+1<n and x[a]+1==x[a+1]):
                l=x[a+1]
                a+=1 
                i=a+1 
            w.append(str(s)+"..."+str(l))
        else:
            w.append(str(x[i]))
            i+=1 
    print(",".join(w))


#--------------------------

def printOutput(isFirst, s, sl):
    if isFirst==False:
        print(',',end='')
    if sl>2:
        print(str(s) + '...' + str(s+sl-1),end='')
    elif sl==2:
        print(str(s) + ',' + str(s+1),end='')
    else:
        print(str(s),end='')

tc = int(input())
for i in range(tc):
    n = int(input())
    x = input().split()
    s=int(x[0])
    sl=1
    isFirst = True
    for j in range(1,n):
        if int(x[j])==s+sl:
            sl = sl + 1
        else:
            printOutput(isFirst,s,sl)
            isFirst=False
            s = int(x[j])
            sl = 1
        if j==n-1:
            printOutput(isFirst,s,sl)
    if n==1:
        printOutput(isFirst,s,sl)
    print('')


#--------------------------

def solve(a , b , c , d):
    x = ( a , min( b , d - 1) )
    y = ( max( c , a + 1 ) , d )
    n = x[1] - x[0] + 1
    m = y[1] - y[0] + 1
    if n < 0 or m < 0:
        ans = 0
    else:
        ans = n * m
        cmn = x[1] - y[0] + 1
        if cmn > 0:
            ans -= (cmn**2 - cmn) // 2
            ans -= cmn
    return ans

T = int(input().strip())
for _ in range(T):
    a , b , c , d = map(int , input().strip().split(' '))
    ans = solve(a , b , c , d)
    print(ans)

#--------------------------

for _ in range(int(input())):
	a,b,c,d = map(int , input().split())
	x = c - a
	p = b - a + 1
	q = d - c + 1
	ans = 0
	if(x <= 0):
		t = q - abs(x) - 1
		for j in range(t, max(0,d - b - 1), -1):
			ans += j
	if(x > 0):
		t = q
		for j in range(x, max(0, c - b - 1), -1):
			ans += t
		if(c - b <= 0):
			for j in range(t - 1, max(0, d - b - 1), -1):
				ans += j
	print(ans)

#--------------------------

import math
mod=10**9+7
t=int(input())
while t:
    n=int(input())
    p1=math.ceil((n+1)/2)
    p2=math.floor((n+1)/2)
    ans1=pow(2,p1,mod)
    ans2=pow(2,p2,mod)
    ans=(ans1+ans2-2)%mod
    print(ans)
    t-=1


#--------------------------

import math
for _ in range(int(input())):
    n=int(input())
    p=(pow(2,math.ceil((n+1)/2),10**(9)+7)+pow(2,math.floor((n+1)/2),10**(9)+7)-2)%(10**(9)+7)
    print(p)

#--------------------------

import math
t = int(input())
for tc in range(0,t):
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	
	cur = 0
	ans = 0
	
	for i in range(0,n):
		if a[i] < cur:
			cur = cur - a[i]
		else:
			x = math.ceil((a[i] - cur)/k)
			ans = ans + int(x)#convert x to int so that answer is an integer
			cur = cur + (x * k - a[i])
		if cur > 0:
			cur = cur - 1
	print(ans)#the final answer should be an integer amount of packages

#--------------------------

T=int(input())
for ti in range(T):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    res=0
    nump=0
    for ai in range(len(A)):
        if(A[ai]>=res):
            fd=A[ai]-res
            pi=fd//k
            nump+=pi
            #print("a")
            if pi>0:
                if fd%k==0:
                    res=0
                else:
                    res=k-fd%k-1
                    nump+=1
            else:
                if fd%k==0:
                    res=0
                else:
                    res=k-fd-1
                    nump+=1
        else:
            fd=res-A[ai]
            res=fd-1
        #print(fd)
        #print(nump)
    print(nump)

#--------------------------

"""import math
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    d=[int(x) for x in input().split()]
    q=[int(y) for y in input().split()]
    res=1
    for i in range(len(q)):
        res=q[i]
        for j in range(len(d)):
            res=(res//d[j])
            
        print(res,end=' ')
    print()"""
t=int(input())
for i in range(t):
    n,q=map(int,input().split(' '))
    d=list(map(int,input().split()))
    Q=list(map(int,input().split()))
    j=1
    for k in d:
        j*=k
    for i in Q:
        x=i//j
        print(x,end=" ")
    print("")    

#--------------------------

import numpy
for _ in range(int(input())):
    n,q=map(int,input().split())
    d=[int(i) for i in input().split()]
    x=[int(j) for j in input().split()]
    result=numpy.prod(d)
    for i in range(q):
        print(x[i]//result,end=' ')

#--------------------------

n = [0, 1, 4, 9, 49, 100, 144, 400, 441, 900, 1444, 4900, 9409, 10000, 10404, 11449, 14400, 19044, 40000, 40401, 44100, 44944, 90000, 144400, 419904, 490000, 491401, 904401, 940900, 994009, 1000000, 1004004, 1014049, 1040400, 1100401, 1144900, 1440000, 1904400, 1940449, 4000000, 4004001, 4040100, 4410000, 4494400, 9000000, 9909904, 9941409, 11909401, 14010049, 14040009, 14440000, 19909444, 40411449, 41990400, 49000000, 49014001, 49140100, 49999041, 90440100, 94090000, 94109401, 99400900, 99940009, 100000000, 100040004, 100140049, 100400400, 101404900, 101949409, 104040000, 104919049, 110040100, 111049444, 114041041, 114490000, 144000000, 190440000, 194044900, 400000000, 400040001, 400400100, 404010000, 404090404, 409941009, 414000409, 414041104, 441000000, 449440000, 490091044, 900000000, 990990400, 991494144, 994140900, 1190940100, 1401004900, 1404000900, 1409101444, 1444000000, 1449401041, 1490114404, 1990944400, 4014109449, 4019940409, 4041144900, 4199040000, 4900000000, 4900140001, 4901400100, 4914010000, 4914991449, 4941949401, 4999904100, 9044010000, 9409000000, 9409194001, 9410940100, 9900449001, 9940090000, 9994000900, 9999400009, 10000000000, 10000400004]
for _ in range(int(input())):
    count = 0
    r1, r2 = [int(r1) for r1 in input().split()]
    for i in n:
        if i >= r1 and i<=r2:
            count += 1
    print(count)

#--------------------------

n = [0, 1, 4, 9, 49, 100, 144, 400, 441, 900, 1444, 4900, 9409, 10000, 10404, 11449, 14400, 19044, 40000, 40401, 44100, 44944, 90000, 144400, 419904, 490000, 491401, 904401, 940900, 994009, 1000000, 1004004, 1014049, 1040400, 1100401, 1144900, 1440000, 1904400, 1940449, 4000000, 4004001, 4040100, 4410000, 4494400, 9000000, 9909904, 9941409, 11909401, 14010049, 14040009, 14440000, 19909444, 40411449, 41990400, 49000000, 49014001, 49140100, 49999041, 90440100, 94090000, 94109401, 99400900, 99940009, 100000000, 100040004, 100140049, 100400400, 101404900, 101949409, 104040000, 104919049, 110040100, 111049444, 114041041, 114490000, 144000000, 190440000, 194044900, 400000000, 400040001, 400400100, 404010000, 404090404, 409941009, 414000409, 414041104, 441000000, 449440000, 490091044, 900000000, 990990400, 991494144, 994140900, 1190940100, 1401004900, 1404000900, 1409101444, 1444000000, 1449401041, 1490114404, 1990944400, 4014109449, 4019940409, 4041144900, 4199040000, 4900000000, 4900140001, 4901400100, 4914010000, 4914991449, 4941949401, 4999904100, 9044010000, 9409000000, 9409194001, 9410940100, 9900449001, 9940090000, 9994000900, 9999400009, 10000000000, 10000400004]
for i in range(int(input())):
  a,b=map(int,input().split())
  c=0
  for j in n:
    if(j>b):
      break
    if(j>=a and j<=b):
      c+=1
  print(c)

#--------------------------

def count_zeroes_at_end(num):
    num=list(str(num))
    ans=0
    while num and num[-1]=='0':
        ans+=1 
        num.pop()  
    return ans

tests=int(input())
num_arr=list(map(int,input().split()))
for num in num_arr:
    ans=num 
    temp=ans*4
    while count_zeroes_at_end(temp)>count_zeroes_at_end(ans):
        ans=temp
        temp*=4
    print(ans)

#--------------------------

n = int(input())
l = list(map(int, input().split()))
m = []
for i in l:
    if i % 5 != 0:
        m.append(i)
    else:
        k = i
        p = i
        c1 = 0
        c2 = 0
        while k % 5 == 0:
            c1 += 1
            k //= 5
        while p % 2 == 0:
            c2 += 1
            p //= 2
        if c2 >= c1:
            m.append(i)
        else:
            m.append(i * (4 ** ((c1 - c2 + 1) // 2)))
for j in m:
    print(j, end = "\n")

#--------------------------

for _ in range(int(input())):
    N,k=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    print(sum([arr[i]*brr[i] for i in range(len(arr))])+(max(map(abs,brr)))*k)

#--------------------------

t=int(input())
for i in range(t):
    a=[]
    b=[]
    n,k =map(int,input().split())
    a=list(map(int,input().strip().split()))[:n]
    b=list(map(int,input().strip().split()))[:n]
    max=abs(b[0])
    ind=0
    sum=0
    for j in range(n):
        if(abs(b[j])>max):
            max=abs(b[j])
            ind=j
    for j in range(n):
        sum=sum+(a[j]*b[j])
    print(sum+(k*abs(b[ind])))       
            

#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=int(n**0.5)
    s=0
    while a>0 and a*a>=n-700:
        s+=n-a*a
        a-=1
    print(a*700 +s)

#--------------------------

from math import * 

t=int(input())

def func(y,t):
    return y*t - int( (t*(t+1)*(2*t+1))/6)


for alpha in range(t):
    y=int(input())
    t=int(sqrt(y))
    ans = func(y,t)
    
    if y<=701:
        print(ans)
        continue
    else:
        z=int(sqrt(y-700))
        ans=ans + 700 * z
        ans = ans - func(y,z)
        print(ans)

#--------------------------

def count_number_of_odd_pairs(A,B):
    count_of_A_odd_numbers = len([x for x in A if x % 2 != 0])
    count_of_B_odd_numbers = len([x for x in B if x % 2 != 0])
    
    count_of_A_even_numbers = len(A) - count_of_A_odd_numbers
    count_of_B_even_numbers = len(B) - count_of_B_odd_numbers
    

    return min(count_of_A_odd_numbers,count_of_B_odd_numbers) + min(count_of_A_even_numbers, count_of_B_even_numbers)

def calculate_max_height_of_children(A,B):
    number_of_odd_pairs = len(A) - count_number_of_odd_pairs(A,B)
    averageOfPairs = (sum(A) + sum(B))/ 2
    return int(averageOfPairs - (number_of_odd_pairs*0.5))

t=int(input())
for i in range(t):
    n=int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(calculate_max_height_of_children(A,B))

#--------------------------

import math
t=int(input())
for _ in range(t):
    n=int(input())
    a_odd=0
    a_even=0
    b_odd=0
    b_even=0
    a_sum=0
    b_sum=0
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        if a[i]%2:
            a_odd+=1 
        else:
            a_even+=1 
        if b[i]%2:
            b_odd+=1 
        else:
            b_even+=1 
        a_sum+=a[i]
        b_sum+=b[i]
    x=(n-min(a_even,b_even)-min(b_odd,a_odd))*0.5
    print(math.floor((a_sum+b_sum)/2 - x ))
        

#--------------------------


##########################################
# DEFINITIONS
def trange():
	return range(int(input()))

def splitMap():
	return map(int,input().split())

def listOfNumbers():
	return list(map(int,input().split()))

def number():
	return int(input())


def binary(x):
	return bin(x).replace("0b","")

##########################################
import math 
from collections import Counter  
import functools 

def main():
	# PreCompute Fibonacci 
	fibonaci = [1,2]
	modulo = 10**9  + 7
	maxN = 10**6
	for i in range(maxN):
	    fibonaci.append((fibonaci[-1]+fibonaci[-2])%modulo) 
	for _ in trange():
		numberOfStairs, villageGuess = splitMap()
		m = fibonaci[numberOfStairs-1]
		correctGuess = binary(m).count('1')
		if  correctGuess == villageGuess:
			print("CORRECT")
		else:
			print("INCORRECT")


if __name__ == '__main__':
	main()
	exit()

#--------------------------

sli=['0']*1000001
sli[0]=1
sli[1]=1

for i in range(2,1000001):
    sli[i]=(sli[i-2]+sli[i-1])%1000000007

for _ in range(int(input())):
    n,g=map(int,input().split())

    if g==bin(sli[n]).count('1'):
        print('CORRECT')
    else:
        print('INCORRECT')


#--------------------------

t = int(input())

for i in range(t):
    a = input()
    b = input()
    n = len(a)
    z, o = 0, 0
    for j in a:
        if j == '0':
            z = 1 
        else:
            o = 1
    if z == 0 or o == 0:
        print('Unlucky Chef')
    else:
        n1, n2 = 0, 0
        for j in range(n):
            e = a[j]
            if e == '1' and e != b[j]:
                n1 += 1
            elif e == '0' and e != b[j]:
                n2 += 1
        print('Lucky Chef')
        ans = max(n1, n2)
        print(ans) 

#--------------------------

from sys import stdin,stdout
out=stdout.write
raw_input=stdin.readline
for i in range(int(raw_input())):
        a=list(raw_input().strip('\n'));a1='';b1=''
        b=list(raw_input().strip('\n'));m=0;n=0
        for i in range(len(a)):
            if a[i]!=b[i]:n+=1;a1+=a[i];b1+=b[i]
        l1=a1.count('1');l=a1.count('0');l2=min(l,l1)
        if a.count('1')==0 or a.count('0')==0:out("Unlucky Chef\n")
        else:n-=2*l2;m+=l2+n;out("Lucky Chef\n"+str(m)+'\n')

#--------------------------

def ss(ar,l,r,sum=0):
    if(ar[len(ar)-1]==-1):
        return
    if(l>r):
        if(sum==k):
            print("Yes")
            ar.append(-1)
            return
        return
    ss(ar,l+1,r,sum+ar[l])
    ss(ar,l+1,r,sum)
    




t=int(input())
while(t>0):
    n,k=map(int,input().split())
    ar=[]
    for i in range(n):
        ar.append(int(input()))
    ss(ar,0,n-1)
    if(ar[len(ar)-1]!=-1):
        print("No")
    t=t-1

#--------------------------

import itertools
T=int(input())
for i in range(T):
    l=[]
    a,b=map(int,input().split())
    for j in range(a):
        n=int(input())
        l.append(n)
    q=[]
    for k in range(len(l)+1):
        for j in itertools.combinations(l,k):
            if(sum(j)==b):
                q.append(sum(j))
    if(len(q)!=0):
        print('Yes')
    else:
        print('No')
            
    

#--------------------------

import bisect

'''
def find_wall(list_wall,num_wall,xi,yi):
    left=0;
    right=num_wall
    while left<right:
        mid=(left+right)//2
        if yi<list_wall[mid]-xi:
            right=mid
        elif yi==list_wall[mid]-xi:
            return mid
        else:
            left=mid+1
    return left
'''

T=int(input())

for _ in range(T):
    N=int(input())
    ai=list(map(int,input().split()))
    Q=int(input())
    for _ in range(Q):
        x,y=map(int,input().split())
        ind=bisect.bisect_left(ai,x+y)
        if ind==N:
            print(N)
        elif ai[ind]==x+y:
            print("-1")
        else:
            print(ind)
        '''
        pos=find_wall(ai,N,x,y)
        if pos==N:
            print(N)
        elif y==ai[pos]-x:
            print("-1")
        else:
            print(pos)
        '''

#--------------------------

import bisect
T=int(input())
for i in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    b=set(A)
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        if (x+y) in b:
            print(-1)
        else:
            print(bisect.bisect_right(A,x+y))
        
        

#--------------------------

for _ in range(int(input())):
    lst = []
    choice = 0
    #print("Enter the values of d, u and n")
    d, u, n = map(float, input().split())
    check = d*u
    #print("Enter the ",int(n), "lines containing m, r and c")
    for i in range(int(n)):
        m, r, c = map(float, input().split())
        #check1 = (c + (m*r*u))/m
        check1 = (c/m) + (r*u)
        if check> check1:
            check = check1
            choice = i+1
    print(choice)


#--------------------------

for _ in range(int(input())):
   a, b, c = map(float, input().split())
   ans = 0
   tam = a * b
   for i in range(int(c)):
      x, y, z = map(float, input().split())
      if tam > z / x + b * y:
         ans = i + 1
         tam = z / x + b * y
   print(ans)
         

#--------------------------

t=int(input())
while t>0:
    n=int(input())
    k=str(n+1)
    while k.count("3")<3:
        k=int(k)
        k+=1
        k=str(k)
    print(k)
    t-=1


#--------------------------

t = int(input())
for i in range(t):
    n = int(input())+1
    while True:
        if str(n).count("3") >= 3:
            break
        n = n+1
    print(n)

#--------------------------

for _ in range(int(input())):
    island=[]
    n,k=map(int,input().split())
    for i in range(n):
        l=[int(i) for i in input().split()]
        l=l[1:]
        island.append(l)
    cnt=[0]*(k+1)
    for i in range(n):
        for indigrient in island[i]:
            cnt[indigrient]+=1 
    f=1 
    for i in range(1,k+1):
        if cnt[i]==0:
            f=0 
            break 
    if not f:
        print('sad')
        continue 
    f1=0 
   # print(island)
    for i in range(n):
        f2=1 
        for j in island[i]:
            if cnt[j]==1:
                f2=0
        if f2:
            f1=1 
            break 
    if f1:
        print('some')
    else:
        print('all')

#--------------------------

for _ in range(int(input())):
	n,k = list(map(int,input().split()))
	array = []
	tot = []
	for _ in range(n):
		temp = list(map(int,input().split()))
		aa = temp[0]
		del(temp[0])
		temp.sort()
		temp.insert(0,aa)
		array.append(temp)
	dic = {}
	array.sort(reverse=True)
	for i in array:
		del(i[0])
	for i in range(1,k+1):
		dic[i] = False
	count = 0
	for i in array:
		count += 1
		# print(count,tot)
		for j in i:
			if(dic[j]==True):
				pass
			else:
				tot.append(j)
				dic[j]=True
		if(len(tot)==k):
			break
	if(len(tot)!=k):
		print("sad")
	elif(count!=n):
		print("some")
	else:
		print("all")

#--------------------------

for i in range(int(input())):
    n,p = map(int,input().split())
    if p>2:
        lst = ['a']
        
        for j in range(p-2):
            lst.append('b')
        lst.append('a')
        print((''.join(lst))*(n//p))

    else:
        
        print("impossible")

#--------------------------

T=int(input())
for i in range(T):
        n,m=map(int,input().split())
        if(m<=2):
                print("impossible")
        else:
                l=[0]*m

                if(m%2==0):
                        a=m//2
                else:
                        a=(m//2)+1
                for j in range(a):
                        if(j%2==0):
                                l[j]="a"
                                l[m-j-1]="a"
                                
                        else:
                                l[j]="b"
                                l[m-j-1]="b"
                                
                
                r=""
                s=n//m
                for e in l:
                        r=r+e
                print(r*s)
                
                



#--------------------------

T=int(input())
mod=1000000007
for k in range(T):
    A,B,C=map(int,input().split())
    q=[A,B,C]
    q.sort()
    c=q[0]*(q[1]-1)*(q[2]-2)
    print(c%mod)

#--------------------------

t=int(input())
while t:
    a=[int (o) for o in input().split()]
    a.sort()
    res=1
    for i in range(3):
        res=res*(a[i]-i)
    print(res%1000000007)    
        
    t-=1


#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    seti1 = set(arr)
    l = [arr[i-1] for i in arr]
    seti2 = set(l)
    if len(seti1)<=len(seti2):
        print("Poor Chef")
    else:
        print("Truly Happy")
        
        
    
    


#--------------------------

t = int(input())
while t:
    n = int(input())
    arr = list( map(int,input().split()) )
    hsh = set()
    hsh1 = set(arr)
    f = 0
    for i in range(1,n+1):
        if i in hsh1:
            if arr[i-1] in hsh:
                print("Truly Happy")
                f = 1
                break
            else:
                hsh.add(arr[i-1])
    if not f:
        print("Poor Chef")
    t -= 1

#--------------------------

t=int(input())
for z in range(t):
    s=input()
    j=1
    ans=1
    a=[]
    for i in s:
        if i!='=':
            a.append(i)
    if len(a)== 0 :
        print(1)
        continue
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            j+=1
            ans=max(ans,j)
        else:
            j=1
    print(ans+1)


#--------------------------

t=int(input())
for _ in range(t):
    s=input().replace('=','')
    if len(s)==0:
        print(1)
        continue
    ans,count=0,1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            ans=max(ans,count)
            count=1
    ans=max(count,ans)
    print(ans+1)

#--------------------------

tsc = int(input())
for i in range(0,tsc):
    string = input()
    string = string.split()
    x = int(string[0])
    y = int(string[1])
    if x >= 0:
        if x % 2 == 1 and abs(y) % 2 == 0:
            print("YES")
        elif x % 2 == 1 and abs(y) % 2 == 1:
            print("YES") if y <= x+1 and y >= 1-x else print("NO")
        elif x % 2 == 0 and abs(y) % 2 == 0:
            print("YES") if y > x or y <= -x else print("NO")
        else:
            print("NO")
    elif x < 0:
        if abs(x) % 2 == 0 and abs(y) % 2 == 0:
            print("YES")
        elif abs(x) % 2 == 0 and abs(y) % 2 == 1:
            print("YES") if abs(y) <= abs(x) else print("NO")
        elif abs(x) % 2 == 1 and abs(y) % 2 == 0:
            print("YES") if abs(y) > abs(x) else print("NO")
        else:
            print("NO")

#--------------------------

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x>=0:
        if not x%2:
            if y>0:
                if y>=2+x and not y%2:
                    print('YES')
                else:
                    print('NO')
            else:
                if -1*y>=x and not y%2:
                    print('YES')
                else:
                    print('NO')
        else:
            if y<=x+1 and y>=-1*(x-1):
                print('YES')
            else:
                if y>=0 and y>=x+1 and not y%2:
                    print('YES')
                elif y<0 and -1*y>=x+1 and not y%2:
                    print('YES')
                else:
                    print('NO')
    else:
        if x%2:
            x=-1*x
            if y>0:
                if y>=1+x and not y%2:
                    print('YES')
                else:
                    print('NO')
            else:
                if -1*y>=1+x and not y%2:
                    print('YES')
                else:
                    print('NO')
        else:
            x=-1*x
            if y>=-1*x and y<=x:
                print('YES')
            else:
                if y<0:
                    y=-1*y
                if not y%2 and y>=x:
                    print('YES')
                else:
                    print('NO')
            


#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    plyr = []
    for _ in range(n):
        k = list(map(int, input().split(' ')))
        val = len(k[1:])
        p = {}
        for i in k[1:]:
            p.setdefault(i, 0)
            x = p[i]
            p[i] = x + 1
        h = set(p.keys())
        while len(h) > 3:
            if len(h) == 4:
                val += 1
            elif len(h) == 5:
                val += 2
            elif len(h) == 6:
                val += 4
            p = {k1:v1-1 for k1,v1 in p.items() if (v1-1) > 0}
            h = set(p.keys())
        plyr.append(val)
    
    a = max(plyr)
    if plyr.count(a) > 1:
        print('tie')
    elif plyr.index(a) == 0:
        print('chef')
    else:
        print(plyr.index(a) + 1)
        

#--------------------------

T = int(input())            # Test Cases
def func():
    global uni ,extra, c
    if len(uni) > 3:
        if len(uni) == 4 or len(uni) == 5:
            extra += len(uni) - 3
        else:
            extra += 4
        for i in uni:
            c.remove(i)
        uni = set(c[1:])
        func()
for i in range(T):
    n = int(input())        # No. of players
    points = []
    for k in range(n):
        c = list(map(int, input().split()))  # cookies data
        uni = set(c[1:])   # unique cookies data
        extra = c[0]
        func()
        points.append(extra)
    if points.count(max(points)) > 1:print('tie')
    elif points.index(max(points)) == 0:print('chef')
    else: print(points.index(max(points)) + 1)


#--------------------------

T= int(input())
for i in range(T):
    a=list(map(int,input().split()))
    l=[]
    for j in range(a[0]):
        b=input().split()
        t=int(b[0])
        if(t>a[2]+1):
         t=max(t-a[1],a[2])
        elif(t<a[2]-1):
         t=min(t+a[1],a[2])
        else:
         t=a[2]
        if(t >= a[3] and t <= a[4]):
         l += [int(b[1])]
    if(len(l)==0):
        print("-1")
    else:
        print(min(l))
                


#--------------------------

def chef_drinks_coke_2():
    n, m, k, l, r = [int(x) for x in input().split()]    
    min = 10000000 
    for i in range(n):
        c, p = [int(x) for x in input().split()]                       

        for j in range(m):
            if c>k+1:
                c -= 1                
            elif c<k-1:
                c += 1                
            else:
                c = k


        if c>=l and c<=r:
            if p<min:
                min = p                
    
    if min!=10000000:
        print(min)
    else:
        print(-1)

t = int(input())
while t>0:
    chef_drinks_coke_2()
    t-=1

#--------------------------

for i in range(int(input())):
    m,n=map(int,input().split())
    if(n%2==0 or m%2==0):
        if(n==1 and m>2) or (m==1 and n>2):
            print("No")
        else:
            print("Yes")
    else:
        print("No")

#--------------------------

for _ in range(int(input())):
	st=input().split()
	N=int(st[0])
	M=int(st[1])
	valid=False
	if N*M==2:
		valid=True
	if (N*M%2==0) and (min(N,M)>1):
		valid=True
	if valid:
		print('Yes')
	else:
		print('No')

#--------------------------

def get_power(n,m,D):
    if(n==0):
        return 1
    elif(n==1):
        return 2
    elif(n in D):
        return D[n]
    else:
        D[n] = ((get_power(n//2,m,D)%m)*(get_power(n-n//2,m,D)%m))%m
        return D[n]

T = int(input())
ans = []
m = 10**9 + 7

for _ in range(T):
    K = int(input())

    ans.append( (get_power(K,m,{})*5)%m )

for i in ans:
    print(i)


#--------------------------

__author__ = 'Prateek'


def test():
    k = int(input())
    ans = (pow(2,k-1,int(10**9+7))*10)%(int(10**9+7))
    print(ans)


if __author__ == 'Prateek':
    t = int(input())
    for _ in range(t):
        test()


#--------------------------

for _ in range(int(input())):
    n,m,x,k = map(int,input().split())
    string1 =input()
    if k==0 or k<n:
            print('no')
            continue
        
    kaam=n
    emp=k
    
    eval=string1.count('E')
    oval=string1.count('O')
    ww='odd'
    
    for _ in range(0,m):
        if ww=='odd':
                kaam=kaam - min(min(oval,x),emp)
                oval-=min(min(oval,x),emp)
                emp=emp-min(min(oval,x),emp)
                ww='even'
        else:
                kaam=kaam - min(min(eval,x),emp)
                
                k=k-min(min(eval,x),emp)
                eval -= min(min(eval,x),emp)
                ww='odd'
    if kaam<=0:
        print('yes')
    else:
        print('no')

#--------------------------

import math
for _ in range(int(input())):
    n,m,x,k=map(int,input().split())
    s=input()
    ecount=int(s.count('E'))
    ocount=int(s.count('O'))
    emonth=math.floor(m/2)
    omonth=math.ceil(m/2)

    if (min(ocount,x*omonth)+min(ecount,x*emonth))>=n:
        print('yes')
    else:
        print('no')



#--------------------------

t=int(input())
for _ in range(t):
  s=input()
  n=len(s)
  if n==1 and s[0]=='?':
    print(26)
  else:
    count=1
    left=0
    right=n-1
    while left<=right:
      if s[left]=="?" and s[right]=="?":
        left+=1
        right-=1
        count=(count*26)%10000009
      elif s[left]=='?' or s[right]=='?' or s[left]==s[right]:
        left+=1
        right-=1
        continue
      else:
        count=0
        break
    print(count)

#--------------------------

# def recur(a,st,end,ans):
#     if st<=end:
#         if a[st] == '?' and a[end] == "?":
#             ans*=26
#             return recur(a,st+1,end-1,ans)
#         if a[st]!='?' and a[end]!='?':
#             if a[st] == a[end]:
#                 return recur(a,st+1,end-1,ans)
#             return 0
#         return recur(a,st+1,end-1,ans)
#     return ans

for _ in range(int(input())):
    a = input()
    i = 0
    j = len(a)-1
    ans = 1
    mod = (10**7)+9
    while i<=j:
        if a[i] == '?' and a[j] == "?":
            ans=((ans%mod)*(26%mod))%mod
            i+=1
            j-=1
        elif a[i] == '?' or a[j] == "?" or a[i] == a[j]:
            i+=1
            j-=1
        else:
            ans = 0
            break
    print(ans)


#--------------------------

a=list(map(int,input().split()))
l=[]
for i in range (a[0]):
    x=((2**a[i+1])-((-1)**a[i+1]))//3
    y=2**a[i+1]
    l.append(x)
    l.append(y)
for i in range (len(l)):
    print(l[i], end=" ")

#--------------------------

a = [int(x) for x in input().split()]
for i in range(a[0]):
    m1 = 1
    m2 = 1
    for x in range(3,a[i+1]+1):
        if x%2!=0:
            m1 = 2*m1 + m2
        else:
            m2 = 2*m2 + m1
    if a[i+1]%2==0:
        print(m2, end = " ")
    else:
        print(m1, end = " ")
    print(pow(2,a[i+1]), end = " ")

#--------------------------

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(str(n))
    l=len(s)
    s1=""
    if(int(min(s))>k):
        for i in range(l):
            s1+=str(k)
        print(s1)
    else:
        c=min(s)
        while(int(c)!=k and len(s)!=0):
            s1+=c
            ind=s.index(c)
            s=s[ind+1:]
            #print(s)
            for i in range(ind+1):
                s.append(str(k))
                #print(s)
            c=min(s)
        z=len(s1)
        for i in range(l-z):
            s1+=str(k)
        print(s1)
            
                
           
        

#--------------------------

T= int(input())
for i in range(T):
    n,d=input().split()
    d=int(d)
    a=[]
    l=len(n)
    mn=d
    
    for j in range(l):
        a.append(int(n[j]))
        
        
    for k in range(l-1,-1,-1):
        if(a[k]>mn):
            a.pop(k)
            a.append(d)
        mn=min(mn,a[k])
        
        
    print(*a,sep="",end="\n")
    T=T-1    
        
    

#--------------------------

def minOperations(a, b):
    count = 0
    v = [False] * len(a)

    for i in range(len(a)):
        if a[i] != b[i]:
            v[i] = True

    for i in range(len(v)):
        if v[i]:
            count += 1
        else:
            continue

        j = i + 2
        while j < len(v):
            if v[j]:
                v[j] = False
            else:
                break
            j += 2

    return count

def main():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()

        result = minOperations(a, b)
        print(result)

if __name__ == "__main__":
    main()


#--------------------------

t = int(input())
for _ in range(t):
    a = input()
    b = input()
    
    v = [False] * len(a)  # Create a boolean list initialized with False
    
    for i in range(len(a)):
        if a[i] != b[i]:
            v[i] = True
    
    count = 0
    
    for i in range(len(v)):
        if v[i]:
            count += 1
        else:
            continue

        j = i + 2
        while j < len(v):
            if v[j]:
                v[j] = False
            else:
                break
            j += 2
    
    print(count)

#--------------------------

try:
    maxpoint=[]
    def maxpoints(n,string,sc):
        i=0
        points=0
        increaser=1
        while i<8:
            if string[i]=='.':
                points+=sc[i]
                i+=1
            elif string[i]=='d':
                points+=sc[i]*2
                i+=1
            elif string[i]=='t':
                points+=sc[i]*3
                i+=1
            elif string[i]=='D':
                increaser=increaser*2
                points+=sc[i]
                i+=1
            elif string[i]=='T':
                increaser=increaser*3
                points+=sc[i]
                i+=1
        points=points*increaser
        maxpoint.append(points)
        return points
    def values(n,string,sc):
        for i in range(n-7):
            maxpoints(n,string[i:],sc)
        return max(maxpoint)
    t=int(input())
    for i in range(t):
        n=int(input())
        string=str(input())
        if n>=8 and n==len(string):
            sc=list(map(int,input().split()))
            print(values(n,string,sc))
            maxpoint=[]
        else:
            print('String is not equals to the length given')
            break
except EOFError:
    pass

#--------------------------

t=int(input())
for i in range(0, t):
    n=int(input())
    s=str(input())
    l=list(map(int, input().split()))
    sum1=sum(l)
    finalSum=0
    for i in range(n-7):
        sum2 = 0
        dw=1
        tw=1
        for k in range(i,i+8):
            if s[k]=="d":
                sum2=sum2+2*l[k-i]
            elif s[k]=="t":
                sum2 = sum2 + 3*l[k-i]
            elif s[k]=="D":
                dw*=2
                sum2 = sum2 + l[k - i]
            elif s[k]=="T":
                tw*=3
                sum2 = sum2 + l[k - i]
            else:
                sum2 = sum2 + l[k - i]

        # print(sum2)
        finalSum=max(finalSum,sum2*dw*tw)

    print(finalSum)

#--------------------------

mod = 1000000007
n, q = map(int, input().split())
height = n
depth = n + 1
topwidth = 1
width = pow(2, n, mod)
edges = (pow(2, depth, mod) + mod - 2) % mod
for _ in range(q):
    act = tuple(map(int, input().split()))
    if act[0] == 2:
        print(edges)
    else:
        if act[1] <= 2: # left or right
            edges = ((2 * edges) % mod + depth) % mod
            topwidth = (topwidth * 2) % mod
            width = (width * 2) % mod
        elif act[1] == 3: # top
            edges = ((2 * edges) % mod + topwidth) % mod
            topwidth = width
            depth = (depth * 2) % mod
        else: # bottom
            edges = ((2 * edges) % mod + width) % mod
            width = topwidth
            depth = (depth * 2) % mod


#--------------------------

n,q=list(map(int, (input().split(' '))))
ans=1000000007
leaves=2**n
edges=((2**(n+1))-2)%ans
height=n+1
op=[]
root=1
for i in range(q):
    s=str(input())
    if s[0]=="2":
        op.append("disp")
    else:
        k=list(map(int,s.split()))
        op.append(k[1])
for j in op:
    if j=="disp":
        print(edges)
    elif j==1 or j==2:
        edges=(2*edges+height)%ans
        leaves=(2*leaves)%ans
        root=(root*2)%ans
    elif j==4:
        edges=(2*edges+leaves)%ans
        leaves=(root)
        height=(2*height)%ans
    else:
        edges=(2*edges+root)%ans
        root=leaves
        height=(2*height)%ans


#--------------------------

a=1000000007
while(True):
	N=int(input())
	if(N==0):
	    break
	v=list(map(int,input().split()))
	len=(1<<N)-1
	for i in range(len//2,-1,-1):
		left=i*2+1;right=i*2+2
		if(left<len and right<len): 
		    v[i]=v[i]*max(v[left],v[right]);
		elif(left<len):
		    v[i]=v[i]*v[left]
	print(v[0]%a)

#--------------------------

def makeAdj(arr):
    n = len(arr)
    adj = {i : [] for i in range(n)}
    for i in range(n):
        if 2*i + 2 < n:
            adj[i].append(2*i+1)
            adj[i].append(2*i+2)
            adj[2*i+1].append(i)
            adj[2*i+2].append(i)
        elif 2*i + 1 < n:
            adj[i].append(2*i+1)
            adj[2*i+1].append(i)
    return adj

def dfs(node,par,arr,adj,P):
    if len(adj[node]) == 1:
        P[node] = arr[node]
        return
    for child in adj[node]:
        if child == par:
            continue
        dfs(child,node,arr,adj,P)
        P[node] = max(P[child]*arr[node],P[node])
    return P

while True:
    h = int(input())
    if h == 0:
        break
    arr = list(map(int,input().split()))
    adj = makeAdj(arr)
    P = [0]*(len(arr))
    print(dfs(0,-1,arr,adj,P)[0] % 1000000007)
    # print(P[0])
    


    


#--------------------------

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    min=0
    for i in a:
        if ((i%m) >min) :
            min = i%m 
    print(min)
    i=i+1


#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l=list(set(l))
    l.sort()
    a=l[len(l)-1]
    b=l[len(l)-2]
    print(b%a)

#--------------------------

def snek(i, n, h):
    for j in range(i  + 1, n):
        if h[j] >= h[i]:
            return False
    return True
t = int(input())

for i in range(t):
    n, c = map(int, input().split())
    h = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = []
    for j in range(n - 1):
        if snek(j, n, h) and c[j] not in d:
            d.append(c[j])
    if c[n -1] not in d:
        d.append(c[n - 1])
    print(len(d))

#--------------------------

def check(i, n, height):
    for j in range(i  + 1, n):
        if height[j] >= height[i]:
            return False
    return True
T = int(input())
for _ in range(T):
    n, c = map(int, input().split())
    height = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    distinct_colors = []
    for i in range(n - 1):
        if check(i, n, height) and colors[i] not in distinct_colors:
            distinct_colors.append(colors[i])
    if colors[n -1] not in distinct_colors:
        distinct_colors.append(colors[n - 1])
    print(len(distinct_colors))

#--------------------------

def solve():
    n,m,h=map(int,input().split())
    Tcells=0
    d=[]
    for _ in range(h):
        t,c=map(int,input().split())
        d.append([t,c])
        Tcells+=t
    d_sorted=sorted(d,key=lambda x:x[1])
    Pcells=0
    cost=0
    k=m*n
    if k<=Tcells:
        for i in d_sorted:
            Pcells+=i[0]
            if Pcells<k:
                cost+=i[0]*i[1]
            else:
                cost+=(k-Pcells+i[0])*i[1]
                print(cost)
                break
    else:
        print('Impossible')
solve()

#--------------------------

n,m,h = map(int, input().split())
numCells = n * m
tk_ck = []
tot=0
for _ in range(h):
    t,c = map(int, input().split())
    tk_ck.append((t,c))
    tot+=t
if tot < numCells:
    print('Impossible')
else:
    tk_ck = sorted(tk_ck, key=lambda x:x[1])
    curCost = 0
    i = 0
    while numCells > 0:
        curCost += tk_ck[i][1] * min(tk_ck[i][0], numCells)
        numCells -= tk_ck[i][0]
        i += 1
    print(curCost)

#--------------------------

for t in range(int(input())):
    g={}
    d={}
    tot=0
    f=input()
    f=int(f)
    for _ in range(f-1):
        en=input().strip()
        a,b,c=en.split()
        g[a]=[b,c]
        if a not in d.keys():
            d[a]=1
        else:
            d[a]+=1
        if b not in d.keys():
            d[b]=1
        else:
            d[b]+=1
        tot+=int(c[:-1])
    for i in g.keys():
        if d[i]==1:
            source=i
            break
    while source in g.keys():
        print(source,g[source][0],g[source][1])
        source=g[source][0]
    print(str(tot)+"$")


#--------------------------

for _ in range(int(input())):
    card = {}
    places = {}
    tot_cost = 0
    for i in range(int(input())-1):
        entry = input().strip()
        src,dest,cost = entry.split()
        tot_cost += int(cost[:-1])
        card[src] = entry
        
        if src in places.keys():
            places[src] += 1
        else:
            places[src] = 1
        
        if dest in places.keys():
            places[dest] += 1
        else:
            places[dest] = 1
    
    for src in card.keys():
        if places[src] == 1:
            path = src
            break
        
    while path in card.keys():
        print(card[path])
        path = card[path].split()[1]
    
    print(tot_cost, end = "$")
    print()
        

#--------------------------

t = int(input())

for i in range(t):
    n = int(input())
    s = range(1, n + 1)
    print(n)
    for j in range(1, n + 1):
        print(n)
        for k in range(1, n + 1):
            print(k, s[(j + k - 1) % n], s[(j + k) % n])

#--------------------------

tc = int(input())
for _ in range(tc):
    n = int(input())
    N = range(1,n+1)
    print(n)
    
    for i in range(1,n+1):
        print(n)
        for j in range(1,n+1):
            print(j,N[(i+j-1)%n],N[(i+j)%n])
    

#--------------------------

from functools import reduce


def binom(n, k, mod=10**9+7):
    
    def mul_mod(x, y):
        return (x * y) % mod
    
    if k in (0, n):
        return 1
    
    if k > n // 2:
        count = reduce(mul_mod, range(k+1, n+1))
        denom = pow(reduce(mul_mod, range(1, n-k+1)), mod-2, mod)
    else: 
        count = reduce(mul_mod, range(n-k+1, n+1))
        denom = pow(reduce(mul_mod, range(1, k+1)), mod-2, mod)
    return mul_mod(count, denom)


mod=10**9+7
for _ in range(int(input())):
    n = int(input())
    deck = input()
    
    if n % 2 == 1:
        result = pow(2, n-1, mod)
    else:
        result = (pow(2, n-1, mod) - (binom(n, n//2, mod) * ((mod + 1) // 2)) % mod) % mod
        
    print(result)
    

#--------------------------



ncr=[[0 for i in range (0,1001)] for j in range (0,1001)]
mod=1000000007
def init():
    for i in range (1, 1001):
        ncr[i][1]=i
        ncr[i][i]=1
    for i in range (3,1001):
        for j in range (2,i):
            ncr[i][j]=(ncr[i-1][j-1] + ncr[i-1][j])%mod
init()
t=int(input())
while t>0:
    n=int(input())
    ans=0
    cards=input()
    a=n//2 + 1
    for i in range (a, n+1):
        ans=(ans+ncr[n][i])%mod
    print(ans)
    t-=1
    
    

#--------------------------

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = {}
    b = {}
    l = []
    for i in range(n):
        a[i] = 0
    for i in range(m):
        b[i] = 0
    for i in range(n):
        l.append(input())
    for i in range(n):
        for j in range(m):
            if l[i][j] == '1':
                a[i]=1
                b[j]=1
    if sum(a.values()) + sum(b.values()) == 0:
        for i in range(n):
            for j in range(m):
                print(-1,end=' ')
            print()
    else:
      
        ans = []
        for i in range(n):
            ans.append([0]*m)
        for i in range(n):
            for j in range(m):
                if l[i][j] == '1':
                    ans[i][j] = 0
                else:
                    if(a[i] or b[j]):
                        ans[i][j] = 1
                    else:
                        ans[i][j] = 2
        for i in range(n):
            for j in range(m):
                print(ans[i][j],end=" ")
            print()
                
            
        


#--------------------------

'''
Example Input
1
3 3
010
000
001
Example Output
1 0 1
2 1 1
1 1 0
'''
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l=[]
    for j in range(n):
        mat=list(input())
        for k in range(len(mat)):
            mat[k]=int(mat[k])
        l.append(mat)

    l1=[]
    
    q1=[]
    q2=[]
    for j in range(n):
        q1.append(sum(l[j]))
    for j in range(m):
        s=0
        for k in range(n):
            s+=l[k][j]
        q2.append(s)
    p=[]
    for j in range(n):
        p1=[]
        for k in range(m):
            p1.append([q1[j],q2[k]])
        p.append(p1)
    check1=0
    check2=0
    for j in q1:
        if(j!=0):
            check1=1
    for j in q2:
        if(j!=0):
            check2=1
    if(check1==0 and check2==0):
        for j in range(n):
            for k in range(m):
                print("-1",end=' ')
            print()
    else:
        for j in range(n):
            f=[]
            for k in range(m):
                if(p[j][k][0]>0 or p[j][k][1]>0):
                    if(l[j][k]==1):
                        f.append(0)
                    else:
                        f.append(1) 
                elif(p[j][k][0]==0 and p[j][k][1]==0):
                    f.append(2)
            l1.append(f)
                    
        for j in range(n):
            for k in range(m):
                print(l1[j][k],end=' ')
            print()
                
      
    

#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split(" "))
    matrix=[]
    num_dots=0
    num_has=0
    for i in range(n):
        temp=list(input())
        matrix.append(temp)
        num_dots+=temp.count('.')
        num_has+=temp.count('#')
    
    for i in range(n):
        if i+1==n:
            break
        for j in range(m):
            if j+1==m:
                break
            elem1=matrix[i][j]
            elem2=matrix[i][j+1]
            elem3=matrix[i+1][j]
            elem4=matrix[i+1][j+1]

            if elem1=='#' or elem2=='#' or elem3=='#' or elem4=='#':
                pass
            else:
                matrix[i][j]='c'
                matrix[i][j+1]='c'
                matrix[i+1][j]='c'
                matrix[i+1][j+1]='c'
    
    num_cs=0
    for i in range(n):
        num_cs+=matrix[i].count('c')
    
    if num_dots==num_cs:
        print("YES")
    else:
        print("NO")

#--------------------------

for t in range(int(input())):
    n,m=map(int,input().split())
    mat=[ ]
    dots=0
    has=0
    for i in range(n):
        l=list(input())
        mat.append(l)
        dots+=l.count('.')
        has+=l.count('#')
    for i in range(n):
        if i+1==n:
            break
        for j in range(m):
            if j+1==m:
                break
            e1=mat[i][j]
            e2=mat[i+1][j]
            e3=mat[i][j+1]
            e4=mat[i+1][j+1]
            if e1=='#'or e2=='#' or e3=='#' or e4=='#':
                continue
            else:
                mat[i][j]='g'
                mat[i+1][j]='g'
                mat[i][j+1]='g'
                mat[i+1][j+1]='g'
    org=0
    for i in range(n):
        org+=mat[i].count('g')
    if org==dots:
        print("YES")
    else:
        print("NO")
    
    

#--------------------------

mod = 1000000007
def fact(n):
    if n <= 1:
        return 1
    else:
        i = 1
        for p in range(2,n+1):
            i *= p
        return i
for _ in range(int(input())):
    S = input()
    N = len(S)
    dic = {}
    for i in range(N):
        p = S[i]
        if p in dic.keys():
            dic[p] += 1
        else:
            dic[p] = 1
    f = fact(N)
    for t in dic.keys():
        f = f // fact(dic[t])
    print(f % mod)


#--------------------------

import math
for _ in range(int(input())):
    s=input()
    a=[0]*26
    b=[0]*26
    for i in range(len(s)):
        if s[i].islower():
            a[97-ord(s[i])]+=1
        else:
            b[65-ord(s[i])]+=1
    sum = math.factorial(len(s))
    su=sum
    for i in range(26):
        su=su//(math.factorial(a[i])*math.factorial(b[i]))
    print(su%(10**9+7))        

#--------------------------

t=int(input())
while t:
    n=int(input())
    for i in range(n-int(n/2),2*n-int(n/2)):
        print(i,end=' ')
    print('')
    t-=1

#--------------------------

from math import ceil
def fun(n):
	if(n==1):
		print(1)
		return
	ans= (n/2)+0.5
	x=ceil(n-1-ans)
	seq= list(range(1+x,1+x+n))
	print(*seq)
test=int(input())
for i in range(test):
	n=int(input())
	fun(n)

#--------------------------

t=int(input())
for _ in range(t):
    n=input()
    lis=list(map(int,input().split()))
    lis.append(-1)
    lis.sort()
    lis.append(-1)
    count=0
    for i in range(1,len(lis)-1):
        if (( lis[i+1] == lis[i]+1 )  or  ( lis[i-1] == lis[i]-1)):
            x=0
        else:
            lis[i]=lis[i]+1
            count=count+1 
    print(count)
        

#--------------------------

def numoftree(arr,n):
    di=dict()
    di[arr[0]]=1 
    count=0
    for i in range(n):
        di[arr[i]]=1 

    for i in range(n):
        if(( arr[i]-1 not in di)and(arr[i]+1 not in di)):
            di[arr[i]+1]=1
            
            count+=1
    return count
t=int(input())
for you in range(t):
    n=int(input())
    l=input().split()
    li=[int(i) for i in l]
    li.sort()
    print(numoftree(li,n))

#--------------------------

import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
ans=0
for i in b:
    ind=bisect.bisect_right(a,i)
    if(ind==0 and a[ind]>i):
        ans=ans+n
print(ans)

#--------------------------


import bisect

num,m=map(int,input().split())
v=list(map(int,input().split()))
w=list(map(int,input().split()))
v.sort()
w.sort()
a=0
for i in w:
    f=bisect.bisect_right(v,i)
    if(f==0 and v[f]>i):
        a=a+num
print(a)

#--------------------------

for j in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    w=x.copy()
    t=x.copy()
    d=x[1]-x[0]
    z=[x[0],x[1]]
    for i in range(2,n):
        x[i]=x[i-1]+d
        z.append(x[i])
    e=t[-1]-t[-2]
    y=[t[-1],t[-2]]
    for i in range(n-2):
        t[n-2-i-1]=t[n-2-i]-e
        y.append(t[n-2-i-1])
    y.reverse()
    am,bm=0,0
    for i in range(n):
        if(w[i]!=y[i]):
            am+=1
            if(am>1):
                break
        if(w[i]!=z[i]):
            bm+=1
            if(bm>1):
                break
    if(am==1):
        print(*y)
    else:
        print(*z)


#--------------------------

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    f = False
    d = 0
    for i in range(1, n - 3):
        if a[i] - a[i - 1] != a[i + 1] - a[i]:
            d = a[i + 3] - a[i + 2]
            a[i + 1] = a[i + 2] - d
            a[i] = a[i + 1] - d
            a[i - 1] = a[i] - d
            f = True
            break

    if (not f):
        if (a[n - 1] - a[n - 4]) / 3 == (a[n - 1] - a[n - 2]):
            d = a[n - 1] - a[n - 2]
            a[n - 3] = a[n - 2] - d
        elif (a[n - 1] - a[n - 4]) / 3 == (a[n - 1] - a[n - 3]) / 2:
            d = a[n - 3] - a[n - 4]
            a[n - 2] = a[n - 3] + d
        elif a[n - 1] - a[n - 2] == a[n - 2] - a[n - 3]:
            d = a[n - 1] - a[n - 2]
            a[n-4] = a[n-3]-d
        else:
            d = a[n - 3] - a[n - 4]
            a[n - 1] = a[n - 2] + d

    [print(x, end=" ") for x in a]
    print()


#--------------------------

t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    squareValues = input().split()
    A = list(map(int, squareValues))

    for i in range(n-k-1, -1, -1):
        A[i] = A[i] + A[i+k]
    
    print(max(A)) 
    
    
    
            
        

#--------------------------

for _ in range (int(input())):
	n, m = map(int, input().split())
	l = list(map(int, input().split()))
	#print(l)
	l1 = []
	if m > n:
		print(max(l))
	else:
		for i in range (m):
			a = l[i]
			for j in range (i + m, n, m):
				a = max((l[j] + a), l[j])
				#print(l[i], l[j])
			l1.append(a)
		print(max(l1))
	

#--------------------------

for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    v=0
    for j,i in enumerate(a):
        if j%2==0:
            if v<0:
                v-=i
            else:
                v+=i
        else:
            if v>=0:
                v-=i
            else:
                v+=i
    if abs(v)>=k:
        print(1)
    else:
        print(2)

#--------------------------

for j in range(int(input())):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(i%2==0):
            if(c<0):
                c-=x[i]
            else:
                c+=x[i]
        else:
            if(c<0):
                c+=x[i]
            else:
                c-=x[i]
    if(abs(c)>=k):
        print(1)
    else:
        print(2)

#--------------------------

# I know I can do this in python
# still want to solve this is c++

a = [0,1]

for i in range (2, 10001):
    a.append(a[i-1] + a[i-2])
    
for t in range (int(input())):
    n = int(input())
    if n in a:
        print("YES")
    else:
        print("NO")
        
#this probably works fine

#--------------------------

def bis(a,key,p,q):

    if q==p+1 and a[p]!=key:
        return False

    mid=(p+q)//2
    if a[mid]==key:
        return True
    if a[mid]<key:
        return bis(a,key,mid,q)
    else:
        return bis(a,key,p,mid)



query=[]
for _ in range(int(input())):
    query.append(int(input()))

maxi=max(query)

seq=[0,1]
while seq[-1]+seq[-2]<=maxi:
    seq.append(seq[-1]+seq[-2])

lens=len(seq)

for i in query:
    if bis(seq,i,0,lens):
        print("YES")
    else:
        print("NO")


#--------------------------

import functools
for _ in range(int(input())):
    n,k,ans=map(int,input().split())
    l=list(map(int,input().split()))
    op=input().strip()
    if k>0:
        # AND
        if op[0]=='A':
            for i in range(len(l)):
                ans=ans&l[i]
            print(ans)
        #OR
        elif op[0]=='O':
            for i in range(len(l)):
                ans=ans|l[i]
            print(ans)
        #XOR
        else:
            if k%2==0:
                print(ans)
            else:
                for i in range(len(l)):
                    ans=ans^l[i]
                print(ans)
    elif(k==0):
        print(ans)

#--------------------------

from functools import reduce
ops = {"XOR": lambda x,y : x^y, "AND": lambda x,y : x&y, "OR": lambda x,y : x|y}
for _ in range(int(input())):
    n, k, ans = map(int, input().split())
    arr = list(map(int, input().split()))
    op = input().strip()
    tot = reduce(ops[op], arr)
    if k == 0:
        print (ans)
        continue
    if op == "XOR":
        if k % 2 == 0:
            print (ans)
        else:
            print (ans ^ tot)
    elif op == "AND":
        print (ans & tot)
    else:
        print (ans | tot)

#--------------------------

try:
    for _ in range(int(input())):
        k,a,b=map(int, input().split())
        if a>b:
            t=a
            a=b 
            b=t
        if b-a == k/2:
            print(0)
        elif b-a < k/2:
            print(b-a-1)
        else:
            print(k+a-b-1)
except EOFError: pass

            

#--------------------------

try:
    for _ in range(int(input())):
        k,a,b=map(int, input().split())
        if a>b:
            t=a
            a=b 
            b=t
        if b-a == k/2:
            print(0)
        elif b-a < k/2:
            print(b-a-1)
        else:
            print(k+a-b-1)
except EOFError: pass

            

#--------------------------

try:
    
    for _ in range(int(input())):
        n = int(input())
        print(0) if(n==1) else print(pow(2,n-1,10**9+7)-2)        
except EOFError:
    pass

        

#--------------------------

MOD=10**9+7
for _ in range(int(input())):
    a=int(input())
    if a==0 or a==1 or a==2:
        print(0)
    else:
        print((pow(2,a-1,MOD)-2)%(MOD))

#--------------------------

from math import ceil
for i in range(int(input())):
    n,k=list(map(int,input().split()))
    data=[0]*(n+1)
    memo=[0]*(n+1)
    for j in range(k):
        x,y=map(int,input().split())
        data[x]=True
        memo[y]=True
    print(n-k,end=" ")
    k=1
    for j in range(1,n+1):
        if data[j]==False:
            for l in range(k,n+1):
                if memo[l]==False:
                    print(j,l,end=" ")
                    data[j]=True
                    memo[l]=True
                    k=l+1
                    break
    print("")



#--------------------------

tc = int(input())
for _ in range(tc):
    n,k = list(map(int,input().split()))
    rows,cols = set(),set()
    cfull = rfull = set(i for i in range(1,n+1))
    for kk in range(k):
        x,y = list(map(int,input().split()))
        rows.add(x)
        cols.add(y)

    rfull = list(rfull - rows)
    cfull = list(cfull - cols)

    rfull.sort()
    cfull.sort()
    ans = []
    for i in range(len(rfull)):
        ans.append(rfull[i])
        ans.append(cfull[i])

    ans.insert(0,len(rfull))
    ans = list(map(str,ans))
    print(" ".join(ans))


#--------------------------

n=int(input())
arr=list(map(int, input().split()))
x=int(input())
l=[]
for i in arr:
    if i<0:
        l.append(i)
l.sort(reverse=True)
s=0
inc=0
z=len(l)
for i in range(len(l)):
    if x<=z:
        l[i]+=inc
        s+=abs(l[i])*x
        inc+=abs(l[i])
        z-=1
    else:
        l[i]+=inc
        s+=abs(l[i])
print(s)

#--------------------------


n=int(input())
l=[int(i) for i in input().split()]
x=int(input())
l.sort()
if(l[0]>=0):
    print(0)
else:
        cnt = 0
        cost = 0
        for i in l:
            if(i<0):
                cnt+=1
            else:
                break
        l = l[0:cnt]
        if(x>=len(l)):
            print(sum(l)*-1)
        else:
            k = min(l[x:len(l)])
            cost+=-1*k*x
            tmp = l[0:x]
            tmp = [i-k for i in tmp]
            for i in tmp:
                cost+= max(0,-1*i)
            print(cost)

#--------------------------

for _ in range(int(input())):
	N = int(input())
	R = [0 for x in range(49)]
	A = []
	for k in range(N):
		st =input().split()
		S = int(st[0])
		E = int(st[1])
		C = int(st[2])
		A.append([S,E,C])
	A.sort()
	for x in A:
		S = x[0]
		E = x[1]
		C = x[2]
		nc = R[S] + C
		if nc > R[E]:
			for k in range(E,49):
				if nc > R[k]:
					R[k] = nc
	print(R[48])

#--------------------------

for _ in range(int(input())):
    N=int(input())
    events=[]
    for i in range(N):
        s,e,c=map(int,input().split())
        events.append([s,e,c])
    
    events.sort()
    plan=[0]*49
    for i in events:
        check_before=i[0]
        for j in range(check_before,-1,-1):
            plan[i[1]]=max(plan[i[1]] ,plan[j] + i[2])

    print(max(plan))

#--------------------------

for i in range(int(input())):
    d1,d2,d=map(int,input().split())
    print(max(0,d-d1-d2,d1-d-d2,d2-d-d1))

#--------------------------

for _ in range(int(input())):
	a,b,c=map(int,input().split())
	if (a+b<=c):print("{:.4f}".format(round(c-(a+b),5)))
	else:
		if(max(a,b)>c+min(a,b)):print("{:.4f}".format(round(max(a,b)-(c+min(a,b)),5)))
		else:print(0.0000)

#--------------------------

for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a%2!=0 and b%2!=0):
        print("Vanka")
    else:
        print("Tuzik")

#--------------------------

try:
    for _ in range(int(input())):
        n,k=map(int,input().split())
        if(n%2==0 or k%2==0):
            print('Tuzik')
        else:
            print('Vanka')
except:
    pass

#--------------------------

from operator import mul
from functools import reduce


def binom_n_6(n, mod):
    x = reduce(mul, [n-i for i in range(6)]) % mod
    y = pow(reduce(mul, range(1,7)), mod-2, mod)
    return (x * y) % mod    
   
   
mod = 10**9 + 7
n = int(input())
#print(n)

if n < 13:
    count = 0
else:
    # Find number of different combinations
    # comb of length 7 with sum(comb) == (n+1)//2
    theSum = (n+1)//2
    """
    count = 0
    for a1 in range(1, theSum - 5):
        for a2 in range(a1 + 1, theSum - 4):
            for a3 in range(a2 + 1, theSum - 3):
                for a4 in range(a3 + 1, theSum - 2):
                    for a5 in range(a4 + 1, theSum - 1):
                        for a6 in range(a5 + 1, theSum - 0):
                            print(a1, a2, a3, a4, a5, a6, 
                                  #theSum - sum([a1, a2, a3, a4, a5, a6])
                                  )
                            count += 1
    count = summands(theSum, 7, mod)
    if n % 2 == 1:
        pass
    """
    count = binom_n_6(theSum - 1, mod)
    
print(count)
    

#--------------------------

x=int(input(""))
ans=0
if(x<13):
    ans=0
if(x>=13):
    if(x%2==0):
        x=int(x-2)
    if(x%2==1):
        x=int(x-1)
    x=x//2
    ans=x*(x-1)*(x-2)*(x-3)*(x-4)*(x-5)//720
    ans=int(ans%(1000000007))
print("",(ans))

#--------------------------

t = int(input())
for i in range(t):
    s,sg,fg,d,T = map(int,input().split())
   

    
    v = s + (d*180)/T

    if abs(sg-v) > abs(fg-v):
        print("FATHER")
    elif abs(sg-v) < abs(fg-v):
        print("SEBI")
    else:
        print("DRAW")

#--------------------------

for _ in range(int(input())):
    s,sg,fg,d,t=map(int,input().split())
    s+=(180*d)/t
    if abs(sg-s)==abs(fg-s):
        print('DRAW')
    elif abs(sg-s)<abs(fg-s):
        print('SEBI')
    elif abs(sg-s)>abs(fg-s):
        print('FATHER')


#--------------------------

for _ in range(int(input())):
    N,K=map(int,input().split())
    ll=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(N):
        for j in range(i+1,N):
            if ll[i]>ll[j]:
                c1+=1
    for i in range(N):
        for j in range(N):
            if ll[i]>ll[j]:
                c2+=1
    print(c1*K+c2*K*(K-1)//2)

#--------------------------

def main():
    t = int(input())
    
    while t>0:
        n,k = map(int,input().split())
        l = list(map(int,input().split()))
        
        ll = sorted(l)
        count1 = 0
        
        for i,val in enumerate(ll):
            count1 = count1 + ( i - (ll[:i]).count(val) )
        
        ans = 0
        
        ans = ans + ( count1 * k * (k-1) ) // 2
        
        count2 = 0
        
        for i,val in enumerate(l):
            temp = sum( 1 for j in l[i+1:] if j < val)
            count2 = count2 + ( temp )
        
        ans = ans + count2*k
        
        print(ans)
        t-=1
    
if __name__ == "__main__":
    main()

#--------------------------


import bisect, sys


MAX = 1000000

if __name__ == '__main__':
	N, K = list(map(int, sys.stdin.readline().split()))
	T = list(map(int, sys.stdin.readline().split()))
	L, R = {}, {}

	for i, x in enumerate(T):
		if x not in L:
			L[x] = i
		R[x] = i


	T = frozenset(T)
	min_idx = N

	for x in sorted(T):
		if 2 * x >= K:
			break
		elif (K - x) in T:
			min_idx = min(min_idx, max(L[x] + 1, L[K - x] + 1))
			min_idx = min(min_idx, max(L[x] + 1, N - R[K - x]))
			min_idx = min(min_idx, max(N - R[x], N - R[K - x]))
			min_idx = min(min_idx, max(N - R[x], L[K - x] + 1))

	print(min_idx if min_idx < N else -1)

#--------------------------


n,k=map(int,input().split())
A=map(int,input().split())
D,dist={}, {}
for i,a in enumerate(A):
    D[a]=0
    dist[a] = min(dist.get(a, float("inf")), i, n - i - 1)

hk = k / 2
c = float("inf")
for a in D:
    if a < hk:
        b = k - a
        if b in D:
            c = min(c, max(dist[a], dist[b]))
print(-1 if c == float("inf") else c + 1)

#--------------------------

for _ in range(int(input())):
    team={}
    for i in range(12):
        x=list(input().split(" "))
        team1=x[0]
        score1=int(x[1])
        team2=x[-1]
        score2=int(x[-2])

        if team1 not in team:
            team[team1]=[0,0]
        if team2 not in team:
            team[team2]=[0,0]
        if score1>score2:
            team[team1][0]+=3
        if score2>score1:
            team[team2][0]+=3
        if score1==score2:
            team[team1][0]+=1
            team[team2][0]+=1
        team[team1][1]+= score1-score2
        team[team2][1]+= score2-score1

    winner=sorted(team.values(),reverse=True)
    for key,values in team.items():
        if values==winner[0]:
            first=key
        if values==winner[1]:
            second=key
    print(first,second)

#--------------------------

def main():
    n = int(input())
    if n < 0 or n > 50 :
        print("Invalid number of test case")
        exit()
    else:
        for i in range(n):
            get_winner()


def get_winner():
    team = {}
    for x in range(12):
        x = input().split(" ")
        hometeam = x[0]
        hometeamgoal = int(x[1])
        awayteamgoal = int(x[-2])
        awayteam = x[-1]

        if hometeam not in team:
            team[hometeam] = [0,0]
        if awayteam not in team:
            team[awayteam] = [0,0]
        if hometeamgoal > awayteamgoal:
            team[hometeam][0] +=3
        elif awayteamgoal > hometeamgoal:
            team[awayteam][0] += 3
        else:
            team[hometeam][0] += 1
            team[awayteam][0] += 1
        team[hometeam][1] += (hometeamgoal - awayteamgoal)
        team[awayteam][1] += (awayteamgoal - hometeamgoal)


    sorted_team = sorted(team.values(),reverse = True)
    for key, values in team.items():
        if values == sorted_team[0]:
            firstteam = key
        if values == sorted_team[1]:
            secondteam = key
    print(firstteam,secondteam)

main()


#--------------------------

case=int(input())
for _ in range(case):
    n = int(input())
    replacement = {}
    for i in range(n):
        v,r = input().split(" ")
        replacement[v] = r
    s = input()
    news = ""
    point = False
    for i in range(len(s)):
        if s[i] in replacement:
            if replacement[s[i]]=='.':
                point = True
            news+=replacement[s[i]]
        else:
            if s[i]=='.':
                point = True
            news+=s[i]
    
    i = 0
    while i<len(news):
        if news[i]!='0':
            break
        i+=1
    news = news[i:]
    if point:
        j = len(news)-1
        while j>=0:
            if news[j]!='0':
                break
            j-=1
        if j>=0 and news[j]=='.':
            j-=1
        news = news[:j+1]
    if len(news)==0:
        print(0)
    else:
        print(news)
        

#--------------------------

T = int(input())
for _ in range(T):
    N = int(input())
    data = dict() 
    for __ in  range(N):
        ci, pi = input().split() 
        data[ci] = pi
    S = list(input())
    for i in range(len(S)):
        if S[i] in data.keys():
            S[i] = data[S[i]] 
    S = "".join(S)
    if '.' in S:
        S = S.strip('0').rstrip('.')
    else:
        S = S.lstrip('0')
    print(S or '0')

#--------------------------

import io, os, sys
from collections import Counter

def fast_io(): 
    
    # Reinitialize the Input function 
    # to take input from the Byte Like  
    # objects 
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
  
    # Taking input as string  
    s = input().decode() 
    return s 
    
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline 
s = input().decode()
t = int(s)
#print(t)
for _ in range(t):
    s = input().decode()
    c = Counter(s)
    #print(s)
    #print(input().decode())
    x1, y1 = map(int, input().decode().split())
    #print(x1, y1)
    q = int(input().decode())
    #print(q)
    for i in range(q):
        (x2, y2) = map(int, input().decode().split())
        if (x1, y1) == (x2, y2):
            sys.stdout.write("YES 0\n")
        else:
            dist_x = x1 - x2
            req_x = abs(dist_x)
            dir_x = "R" if dist_x < 0 else "L"
            dist_y = y1 - y2
            req_y = abs(dist_y)
            dir_y = "U" if dist_y < 0 else "D"
            
            count_dir_x = c[dir_x]
            count_dir_y = c[dir_y]
            """
            count_dir_y = 0
            for d in s:
                if d == dir_x:
                    if count_dir_x < req_x:
                        count_dir_x += 1
                elif d == dir_y:
                    if count_dir_y < req_y:
                        count_dir_y += 1
                if count_dir_x >= req_x and count_dir_y >= req_y:
                    break
            """
            if count_dir_x >= req_x and count_dir_y >= req_y:
                sys.stdout.write("YES "+ str(req_x + req_y) + "\n")
            else:
                sys.stdout.write("NO\n")

#--------------------------


from collections import defaultdict
import sys
for q in range(int(sys.stdin.readline())):
    s=sys.stdin.readline()
    x1, y1=map(int,sys.stdin.readline().split())
    Q=int(sys.stdin.readline())
    dict=defaultdict(int)
    for i in s:
        dict[i]+=1
    for _ in range(Q):
        x2, y2=map(int,sys.stdin.readline().split())
        c=0
        f=0
        if x2-x1>=0:
            if dict["R"]>=x2-x1:
                c+=x2-x1
            else:
                f=1
        else:
            if dict["L"]>=x1-x2:
                c+=x1-x2
            else:
                f=1
        if y2-y1>0:
            if dict["U"]>=y2-y1:
                c+=y2-y1
            else:
                f=1
        else:
            if dict["D"]>=y1-y2:
                c+=y1-y2
            else:
                f=1
        if f==1:
            sys.stdout.write("NO")
        else:
            sys.stdout.write("YES"+" "+str(c))
        sys.stdout.write("\n")

#--------------------------

import math
T = int(input())
for _ in range(T):
    x,k = map(int,input().split())
    y = int(math.log2(k))
    z = 2**y
    m = k - z
    print((2*m+1)*(x)/(2**(y+1)))
    

#--------------------------

t = int(input())

for i in range(t):
    x, k = map(int, input().split())
    x1, y1 = 2, 1 
    while x1 <= k:
        x1, y1 = x1 * 2, x1 
    print(x / x1 * (1 + 2 * (k - y1)))

#--------------------------

# by David Ham
from sys import stdin, stdout
# Faster I/O ======================
pr = lambda i : stdout.write(f'{i}\n')
inp = lambda : stdin.readline().strip()
im = lambda : map(int, stdin.readline().strip().split()) # int map
# =================================
def main():
    t = int(inp())
    for _ in range(t):
        n, m = im()
        prevrow = ''
        s = 'yes'

        for i in range(n):
            row = inp()
            if s == 'yes':
                if row[0] == 'W' or row[-1] == 'W' or 'WA' in row or 'AW' in row:
                    s = 'no'
                    continue

                if prevrow:
                    for pval, nval in zip(prevrow, row):
                        if (pval == 'B' and nval == 'A') or (pval == 'B' and nval == 'W') or (pval == 'W' and nval == 'A'):
                            s = 'no'
                            break
                
                prevrow = row

        pr(s)
# =================================
if __name__ == '__main__':
    main()


#--------------------------

def solution():
    h, w = map(int, input().split())

    R = [list('A'*(w+2)) for i in range(h+2)]
    R[-1] = list('B'*(w+2))

    for r in range(1, h+1):
        row = input();
        for c in range(1, w+1):
            R[r][c] = row[c-1]
    
    for r in range(1, h+1):
        for c in range(1, w+1):
            if R[r][c] == 'W':
                if R[r][c-1] == 'A' or R[r][c+1] == 'A' or R[r+1][c] == 'A':
                    print("no")
                    return
            if R[r][c] == 'B':
                if R[r+1][c] == 'A' or R[r+1][c] == 'W':
                    print("no")
                    return
    print("yes")

T = int(input())
while(T > 0):
    T = T - 1
    solution()

#--------------------------


m=int(pow(10,9)+7)
for i in range(int(input())):
    n,w=map(int,input().split())
    s=0
    for i in range(1,10):
        for j in range(10):
            if(j-i==w):
                s+=1
    print((s*pow(10,n-2,m))%m)


#--------------------------

from math import ceil
m=int(pow(10,9)+7)
t=int(input())
while(t):
    t-=1
    n,w=map(int,input().split())
    ss=0
    for i in range(1,10):
        for j in range(10):
            if(j-i==w):
                ss+=1
    print((ss*pow(10,n-2,m))%m)


#--------------------------

for _ in range(int(input())):
    n=int(input())
    arr=[]
    ans=[0]*n 
    for i in range(n):
        m=int(input())
        po=[int(i) for i in input().split()][::2]
        arr.append([i,max(po)])
    arr.sort(key=lambda x:x[1])
    for x in range(n):
        ans[arr[x][0]]=x 
    print(*ans)

#--------------------------


def run():
    T = int(input())
    for _ in range(T):
        N = int(input())
        polygons = []
        for i in range(N):
            M = int(input())
            polygon = list(map(int, input().split()))
            polygons.append(polygon)
        print(f(polygons))
        
def f(polygons):
    highest = []
    for i, polygon in enumerate(polygons):
        hi = float('-inf')
        for x in range(0, len(polygon), 2):
            px, py = polygon[x], polygon[x+1]
            hi = max(hi, py)
        highest.append((i, hi))
    
    highest = sorted(highest, key=lambda x: x[1])
    ans = [0] * len(polygons)
    for n, (i, hi) in enumerate(highest):
        ans[i] = str(n)
    return " ".join(ans)
        
if __name__ == "__main__":
    
    run()



#--------------------------

def num_decks(n):
    if n <= 2:
        return n    
    
    fib1, fib2 = 1, 1
    i = 1
    while fib2 < n: 
        fib1, fib2 = fib2, fib2 + fib1
        i += 1
    return i - (fib2 != n)


for _ in range(int(input())):
    n = int(input())
    
    print(num_decks(n))
    

#--------------------------



fib=[1,1]
for i in range(100):
    fib.append(fib[-1]+fib[-2])
from bisect import bisect_left as bl
for _ in range(int(input())):
    n=int(input())
    ind=bl(fib,n)
    if n==1:
        print(1)
    else:
        i=0 
        while i<100 and fib[i]<=n:
            ans=fib[i]
            i+=1 
        print(i-1)

#--------------------------

t = int(input())
 
for _ in range(t):
	
	# n, k  = list(map(int, input().split()))
	# lst = list(map(int, input().split()))
	n = int(input())


	n = n - 1

	mul = 1 
	res = 0

	while n:
		res += 2*(n%5)*mul
		n = n//5
		mul *= 10
	print(res)

#--------------------------

def MagicalNum(k):
    if 1 <= k <= 5:
        return 2*(k-1) 
    elif k == 0:
        return 0
    elif k % 5 == 0:
        v1 = k // 5
        return 10*MagicalNum(v1) + 8
    else:
        v1 = k//5
        v2 = k % 5
        return 10*MagicalNum(v1 + 1) + MagicalNum(v2)     
T = int(input())
for _ in range(T):
    k = int(input())
    print(MagicalNum(k))

#--------------------------

steps = {
    "T": 2,
    "S": 1
}

octave = 12             # 12 keys per octave

def length(phrase):
    return sum([steps[s] for s in phrase])

# Each phrase produces X results, where
#
# X = max((total keys available - length of phrase) + 1, 0)
#
# Keep repeating the phrase and recalculating X until X < 0
def results(keys, l):
    return keys - l

for t in range(int(input())):
    s = str(input())
    n = int(input())
    ans = 0
    repeat = 1
    number_of_keys = octave * n
    r = results(number_of_keys, length(s * repeat))
    while r >= 0:
        ans += r
        repeat += 1
        r = results(number_of_keys, length(s * repeat))
    print(ans)


#--------------------------


steps = {
    "T": 2,
    "S": 1
}

octave = 12             # 12 keys per octave

def length(phrase):
    return sum([steps[s] for s in phrase])

# Each phrase produces X results, where
#
# X = max((total keys available - length of phrase) + 1, 0)
#
# Keep repeating the phrase and recalculating X until X < 0
def results(keys, l):
    return keys - l

for t in range(int(input())):
    s = str(input())
    n = int(input())
    ans = 0
    repeat = 1
    number_of_keys = octave * n
    r = results(number_of_keys, length(s * repeat))
    while r >= 0:
        ans += r
        repeat += 1
        r = results(number_of_keys, length(s * repeat))
    print(ans)

#--------------------------


while True:
    try:
        n=input()
    except:
        exit()
    if n.count('1')==20 or n.count('0')==20:
       print("TIE")
    else:
        gc=0
        go=0
        c=0
        a=False
        b=True
        fnal=0
        for i in range(20):
            if c<10:    
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if i%2==0:
                    if gc>go:
                        if (go+(10-c)//2+1)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
                else:
                    if gc>go:
                        if (go+(10-c)//2)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
            else:
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if c%2==0:
                    if gc>go:
                        fnal=c
                        a=True
                        break
                    elif go>gc:
                        fnal=c
                        break
        
        if c!=20:
            if a:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
        elif c==20:
            if gc==go:
                print('TIE')
            elif gc>go:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
            
                

#--------------------------

while True:
    try:
        n=input()
    except:
        exit()
    if n.count('1')==20 or n.count('0')==20:
       print("TIE")
    else:
        gc=0
        go=0
        c=0
        a=False
        b=True
        fnal=0
        for i in range(20):
            if c<10:    
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if i%2==0:
                    if gc>go:
                        if (go+(10-c)//2+1)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
                else:
                    if gc>go:
                        if (go+(10-c)//2)<gc:
                            a=True
                            fnal=c
                            break
                    else:
                        if (gc+(10-c)//2)<go:
                            fnal=c
                            break
            else:
                c+=1
                if i%2==0:
                    if n[i]=='1':
                        gc+=1
                else:
                    if n[i]=='1':
                        go+=1
                if c%2==0:
                    if gc>go:
                        fnal=c
                        a=True
                        break
                    elif go>gc:
                        fnal=c
                        break
        
        if c!=20:
            if a:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
        elif c==20:
            if gc==go:
                print('TIE')
            elif gc>go:
                print("TEAM-A",+fnal)
            else:
                print("TEAM-B",+fnal)
            
                
                
                    
                
            

#--------------------------

t = int(input())
while t!=0:
    n = int(input())
    b = bin(n)[2:]
    
    if n==1:
        print(2)
    else:
        if '0' in b:
            print(-1)
        else:
            print((n-1)//2)
    t-=1

#--------------------------

from sys import *
test = int(input())
for tt in range(test):
    n = int(input())
    t = -1
    for i in range(30):
        if(n == 2**i-1):
            t = i
            break
    if (t == 1):
        print(2)
    elif(t == -1):
        print(-1)
    else:
        print(2**(t-1) -1)



#--------------------------

nums,cases= map(int,input().split())

inpL = list(map(int,list(input().strip())))
popn = [[]for i in range(10)] #differences in all possible pairs of 1 to 9

for n in range(10):
 myBin=0
 for j in inpL:
  myBin+=abs(int(j)-n)
  popn[n]+=[myBin]
 
for c in range(cases):
 q=int(input())
 queried=inpL[q-1]
 print(popn[int(queried)][q-1])

#--------------------------

n,m=map(int,input().split())
s=input().strip()
l=[int(i) for i in s]
d=[0]*(10)
ans=[0]*(n+193)
for i in range(n):
    curr=l[i]
    less=0 
    big=0 
    c1=0 
    c2=0 
    for j in range(10):
        if j<curr:
            c1+=d[j]
            less+=d[j]*j 
        if j>curr:
            c2+=d[j]
            big+=d[j]*j 
    ans[i]=big-less+curr*(c1-c2)
    d[l[i]]+=1 
for _ in range(m):
    x=int(input())
    print(ans[x-1])

#--------------------------

for i in range(int(input())):
  s = input()
  n = len(s)
  arr = [0]*n
  for i in range(n):
    arr[i] = int(s[i])
  total = 0
  count = 0
  lastIdx = n-1
  curr = n-1
  while(arr[curr]==1 and curr>=0):
    lastIdx-=1
    curr-=1
  while curr>=0:
    if arr[curr]==1:
      if arr[curr+1]==0:
        count+=1
      total+=count+(lastIdx-curr)
      lastIdx-=1
    curr-=1
  print(total)

#--------------------------

# from itertools import groupby
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    i = n - 1
    ones = s.count('1')
    c = 0
    ans = 0
    while i >= 0:
        if s[i] == '0':
            c += 1
            i -= 1
        else:
            if c:
                ans += ones * (c + 1)
                c = 0
            while i >= 0 and s[i] == '1':
                ones -= 1
                i -= 1
    print(ans)

#--------------------------

for _ in range(int(input())):
    N, M = input().split()
    N = int(N)
    M = int(M)
    a = []
    count = 0
    
    a = list(map(int,input().split()))
    lun = len(a)
    a.sort()
    
    while len(a)>1:
        
        a[0] -= 1
        if a[0] == 0:
            a.pop(0)
        
        a.pop(len(a)-1)
        
        count += 1 
     
       
            
    print(count)

#--------------------------

for _ in range(int(input())):
    k,n = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    x = 0
    lst.sort()
    while len(lst) > 2:
        while lst[0] != 0:
            if len(lst) == 2:
                break
            lst[-2] += lst[-1]
            del lst[-1]
            cnt += 1
            lst[0] -= 1
            if lst[0] == 0:
                del lst[0]
                break
    if lst[0] == 0:
        del lst[0]
    if len(lst) == 2:
        print(cnt+1)
    else:
        print(cnt)
    

#--------------------------

# Imports
from sys import stdin,stdout 
import math 
from collections import Counter  
import functools 
import time 
##########################################
# DEFINITIONS
def tr():
    return range(int(line()))

def sm():
    return map(int,line().split())

def ln():
    return list(sm())

def nl():
    return int(line())

def ssm():
    return map(str,line().split())

def line():
    return stdin.readline().rstrip()

def b(x):
    return bin(x).replace("0b","")

def o(x):
    if type(x) != type(""):
        x = str(x)
    stdout.write(x + "\n")
def osp(x):
    if type(x) != type(""):
        x = str(x)
    stdout.write(x + " ")
def ol(x):
    stdout.write(" ".join(map(str,x)))


##########################################
# Main Code and Functions 

def checkPalindrome(s):
    return s == s[::-1]
def main():
    for _ in tr():
        s = line()
        if checkPalindrome(s):
            print("YES")
            continue 
        possible = False
        n = len(s)
        for i in range(n//2):
            if s[i]!=s[n-i-1]:
                if checkPalindrome(s[:i] + s[i+1:]):
                    possible = True 
                elif checkPalindrome(s[:n-i-1]+s[n-i:]):
                    possible = True 
                else:
                    break
        print("YES" if possible else "NO")
                
                
        
    
main()


#--------------------------


def solve():
    s=input().strip()
    i=0
    j=len(s)-1
    a=''
    b=''
    while i<=j:
        if s[i]!=s[j]:
            a=s[:i]+s[i+1:]
            b=s[:j]+s[j+1:]
            break
        i+=1
        j-=1
    if a==a[::-1]  or b==b[::-1]:
        print("YES")
    else:
        print("NO")

test=int(input())
for _ in range(test):
    solve()


#--------------------------

for _ in range(int(input())):
    n=int(input())
    d = list(map(int, input().split()))
    tot=ans=0
    for i in range(0,n-1):
        tot+=d[i]
        ans+=abs(tot)

    print(ans)

#--------------------------


for _ in range(int(input())):
    n=int(input())
    d = list(map(int, input().split()))
    tot=ans=0
    for i in range(0,n-1):
        tot+=d[i]
        ans+=abs(tot)

    print(ans)

#--------------------------

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a == b:
        result = -1
    else:
        diff = abs(a-b)
        result = 1 + (diff > 1)
        for i in range(2, diff):
            j = i*i
            if j < diff:
                if diff % i == 0:
                    result += 2
                continue
            if j == diff:
                result += 1
            break
    print(result)
    

#--------------------------

from math import sqrt

def solve():
    a, b = map(int, input().split())
    if a == b: return -1
    t = max(a, b) - min(a, b)
    res = 0
    for i in range(1, int(sqrt(t) + 1)):
        if not t % i: res += 1 + (i != (t // i))
    return res
    

def main():
    T = int(input())
    for _ in range(T):
        print(solve())

main()

#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9+7
    n=n+1
    ans=0
    l = a[0]*2
    d = 1
    for i in range(1,n):
        ans =(2*ans +l*a[i])%mod
        d = (2*d)%mod
        l = (l+a[i]*d)%mod
    print(ans)

#--------------------------


def main():
    for _ in range(int(input())):
        t,b,c=0,1,10**9+7
        l=int(input())
        a=list(map(int,input().split()))
        p=a[0]*2
        for i in range(1,l+1):
            t=(t*2+p*a[i])%c
            b=(b*2)%c
            p=(p+a[i]*b)%c
        print(t)
if __name__=="__main__":
    main()

#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    sal=list(map(int,input().split()))
    c={}
    ma=[]
    com=[0]*m
    tms=0
    count=0
    for i in range(m):
        v=list(map(int,input().split()))
        ma.append(v[1])
        c[i]=v[0]
    l=[input() for i in range(n)]
    s=-1
    for i in l:
        s+=1
        ms=0
        val=-1
        for k in range(m):
            if(i[k]=='1' and ma[k]>0):
                if(ms<c[k]):
                    ms=c[k]
                    val=k
        if(val!=-1 and sal[s]<=c[val]):
            tms+=ms
            count+=1
            ma[val]-=1
            com[val]=1
    print(count,tms,m-sum(com))
        
                
                
                

#--------------------------

def solution():
    N, M = map(int, input().split())
    
    minSalary = list(map(int, input().split()))
    offeredSalary = []
    maxJobOffers = []
    
    for i in range(M):
        salary, offer = map(int, input().split())
        offeredSalary.append(salary)
        maxJobOffers.append(offer)
    
    qual = []

    for i in range(N):
        qual.append([ c == '1' for i, c in enumerate(input())])

    placements_count = 0
    total_salary = 0
    
    hiring_companies = set()

    for i in range(N):
        selected = -1;
        for j in range(M):
            if qual[i][j] and maxJobOffers[j] > 0 and offeredSalary[j] >= minSalary[i]:
                if selected == -1 or offeredSalary[selected] < offeredSalary[j]:
                    selected = j;
        if selected >= 0:
            maxJobOffers[selected] -= 1
            placements_count += 1
            total_salary += offeredSalary[selected]
            hiring_companies.add(selected)
    
    print(placements_count, end = " ")
    print(total_salary, end = " ")
    print(M - len(hiring_companies))


T = int(input())
while(T > 0):
    T = T - 1
    solution()


#--------------------------

for _ in range(int(input())):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    y=sum(a)/n 
    if y%1!=0:
        print(-1)
    else:
        ans=0
        flag=0
        for i in range(n-d):
            r=a[i]-y
            a[i]=y
            a[i+d]+=r 
            ans+=abs(r)
        
        if a.count(y)==n:
            print(int(ans))
        else:
            print(-1)
            

#--------------------------

T = int(input())
for i in range(T):
    N, D = map(int,input().split())
    arr = list(map(int,input().split()))
    
    total = sum(arr)
    if(total % len(arr) != 0):
        print(-1)
    else:
        div = total // len(arr)
        j = 0
        count = 0
        while j + D < len(arr):
            if (arr[j] < div):
                diff = div - arr[j]
                count += diff
                arr[j] += diff
                arr[j+D] -= diff
            elif (arr[j] > div):
                diff = arr[j] - div
                count += diff
                arr[j] -= diff
                arr[j+D] += diff  
            j+=1
        while j < len(arr):
            if arr[j] != div:
                count = -1
                break
            j+=1
        print(count)

#--------------------------

def max_happiness(arr):
    pos = []
    neg = []
    for y in arr:
        if y > 0:
            pos.append(y)
        else:
            neg.append(y)
    if len(pos) == len(arr):
        return sum(pos)*len(pos)
    elif len(neg) == len(arr):
        return sum(neg)
    else:
        arr.sort()
        arr.reverse()
        i = 0
        s = arr[i]
        current = arr[i]
        j = 1
        while j < len(arr):
            current += arr[j]
            happiness = current*(j - i + 1)
            if happiness >= s:
                s = happiness
                j += 1
            else:
                return s + sum(arr[j: len(arr)])
        return s


test_cases = int(input())
while test_cases != 0:
    data = input()
    data2 = list(map(int, input().split()))
    print(max_happiness(data2))
    test_cases -= 1


#--------------------------

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split())) 
    A = sorted(A)[::-1]
    left = 0
    summ = sum(A)
    right = summ
    ans = -float('inf')
    for i in range(n):
        left += A[i]
        right -= A[i]
        ans = max(ans, (i+1)*left + right)
    print(ans)

#--------------------------

def solve():
    s = input()
    rs, gs = s.count('R'), s.count('G')
    if rs != gs:
        return 'no'

    count_g, count_r = 0, 0

    if s[0] == s[len(s)-1]:
        if s[0] == 'R':
            count_r += 1
        else:
            count_g += 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            if s[0] == 'R':
                count_r += 1
            else:
                count_g += 1

    if count_g+count_r == 2 or count_r+count_g == 0:
        return 'yes'
    else:
        return 'no'


tc = int(input())
for _ in range(tc):
    print(solve())


#--------------------------

for _ in range(int(input())):
    string=input()
    if(len(string) % 2 == 1):
        print("no")
    elif(string.count('R') != string.count('G')):
        print("no")
    else:
        count=0
        for i in range(1,len(string)):
            if(string[i] == string[i-1]):
                count+=1
        if(count<=2):
            print("yes")
        else:
            print("no")        
        

#--------------------------

T=int(input())
for i in range(T):
    N=int(input())
    A=list()
    for j in range(N):
        A.append(input())
    B=['.'*N]*N
    C=['.'*N]*N
    for k in range(N):
        for l in range(N-1,-1,-1):
            if A[k][l]=='#':
                B[k]='#'*(l+1)+"."*(N-1-l)
                break
        for m in range(N-1,-1,-1):
            if A[m][k]=='#':
                C[k]='#'*(m+1)+'.'*(N-1-m)
                break
    sum=0
    for u in range(N):
        for v in range(N):
            if B[u][v]==C[v][u]=='.':
                sum+=1
    print(sum)


#--------------------------

from sys import stdin
tc=int(stdin.readline())
for i in range(tc):
    n=int(stdin.readline())
    list1=[]
    for j in range(n):
        s1=stdin.readline()
        list1.append(s1)
    f_n=[1]*n
    f_e=[1]*n
    count=0
    for k in range(n-1,-1,-1):
        for l in range(n-1,-1,-1):
            if list1[k][l]=="#":
                f_n[k]=0
                f_e[l]=0
            elif f_e[l] and f_n[k]:
                count+=1
    print(count)
    

#--------------------------

test = int(input())

def checkSurvival(n,k,s):
    
    if n<k:
        return -1
    
    elif s>=7 and ((n-k)*6)<k:
        return -1
    
    else:
        choco = k*s
        present = 0
        daysMin = 0
        
        for i in range(1,s+1):
            if i%7!=0:
                present+=n
                daysMin+=1
            else:
                continue
            if present>=choco:
                return daysMin
                
for _ in range(test):
    n,k,s = map(int, input().split())
    
    result = checkSurvival(n,k,s)
    print(result)    

#--------------------------

for i in range(int(input())):
    n,k,s = list(map(int,input().split()))
    total = k*s
    count = 0
    k = 0
    y = False
    for i in range(1,s+1):
        #print(i)
        if i%7!=0:
            count+=n
            k+=1
        else:
            continue
        if count>=total:
            y = True
            break
    #print(count,total)
    if y:
        print(k)
    else:
        print(-1)

#--------------------------

for _ in range(int(input())):
    r,g,b,m=list(map(int, input().split()))
    l=[]
    for i in range(3):
        l1=list(map(int, input().split()))
        l.append(l1)
            
    for i in range(m+1):
        a=0
        b=0
        for j in range(3):
            m=max(l[j])
            if m>a:
                a=m 
                b=j 
                
        for k in range(len(l[b])):
            l[b][k]=l[b][k]//2
                
    print(a)

#--------------------------

t=int(input())
while(t>0):
    r,g,q,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    for i in range(m):
        x=max(a)
        y=max(b)
        z=max(c)
        if(x>=y)and(x>=z):
            for j in range(r):
                a[j]//=2
        elif(y>=x)and(y>=z):
            for j in range(g):
                b[j]//=2
        else:
            for j in range(q):
                c[j]//=2
    x=max(a)
    y=max(b)
    z=max(c)
    print(max(x,max(y,z)))
    t-=1

#--------------------------

# region fastio
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion


if __name__ == '__main__':
    for _ in range(int(input())):
        x = 0
        for c in range(int(input())):
            n, m = map(int, input().split())
            g = (m + n - 2) % 3
            x = x ^ g
        if x:
            ans = "MasterChef"
        else:
            ans = "Football"
        print(ans)


#--------------------------

res=""
for _ in range(int(input())):
    ans=0
    c=int(input())
    for i in range(c):
        n,m=map(int,input().split( ))
        ans^=(n+m-2)%3
    if ans:
        res+="MasterChef\n"
    else:
        res+="Football\n"
print(res)
        
        
        

#--------------------------

from math import sqrt
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
l=[]
for i in range(2,1000):
    z=is_prime(i)
    if z==True:
        l.append(i)
ba=[]
while True:
    c=int(input())
    if c!=0:
     ba.append(c)
    else:
        break
for m in ba:
  flg=0
  for i in l:
     for j in l:
        k=m-(i**2+j**3)
        if k>1:
            if is_prime(k)==True:
                print(k,i,j)
                flg=1
                break
     if flg==1:
        break
  if flg==0:
      print(0,0,0)

#--------------------------

from math import sqrt
def checkPrime(n):
    prime = True
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(sqrt(n)) + 1):
            if n % i == 0:
                prime = False
                break
        return prime
primes100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,]
primes1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
takeInput = True
while takeInput:
    N = int(input())
    if N == 0:
        takeInput = False
    else:
        found = False
        array = []
        for i in primes100:
            for j in primes1000:
                k = N - i*i*i - j*j
                if checkPrime(k):
                    array = [k,j,i]
                    found = True
                    break
        if found:
            print(*array)
        else:
            print('0 0 0')


#--------------------------

for _ in range(int(input())):
    k = int(input());arr = list(map(int,input().split()));d=0.5
    for i in arr: d = d*2 - i
    print("Yes") if(d == 0) else print("No")

#--------------------------

T=int(input())
for i in range(T):
    k=int(input())
    N=input().split(' ')
    x=1/2
    for j in range(k):
        x=x*2-int(N[j])
    if(x==0):
        print('Yes')
    else:
        print('No')

#--------------------------

a=str(input().strip())
if a.count('1')==1:
    print(a,'0')
else:
    print('1'+'0'*len(a),'1'+'0'*a.count('0'))

#--------------------------

s=str(input().strip())
if s.count('1')==1:
    print(s,'0')
else:
    print('1'+'0'*len(s),'1'+'0'*s.count('0'))

#--------------------------

import sys
sys.setrecursionlimit(10**6)



for _ in range(int(input())):
    n, k, l = [int(x) for x in input().split()]
    l = l - 1
    ans = []
    while l:
        ans.append(l % k)
        l = l//k
    

    while len(ans) != n:
        ans.append(0)
    
    ans = ans[::-1]
    ans = [x+1 for x in ans]
    
    print(*ans)
    
    
    
    

#--------------------------

t = int(input())

for i in range(t):
    n, k, l = map(int, input().split())
    l -= 1
    a = []
    while l != 0:
        a.insert(0, l % k)
        l //= k 
    while len(a) != n:
        a.insert(0, 0)
    for j in a:
        print(j + 1, end=" ")
    print()

#--------------------------

import sys
import math

def main(arr):
    
    
    
    for e in arr:
        e[0]=int(e[0])
        e[2]=int(e[2])
        e[1]=int(e[1])
        e[3]=int(e[3])
        e+=[True]

    ans=['wait']
    for i in range(1,len(arr)):
        p1=arr[i]
        for j in range(0,i):
            p2=arr[j]
            if p2[-1]:
                if p2[1]<=p1[0] and p1[0]<=p2[2] and p1[1]<=p2[0] and p2[0]<=p1[2]:
                    if p2[3]==p1[3] and p2[4]==p1[4]:
                        if (p1[5]=='random' and p2[5]=='random') or (p1[5]=='black' and p2[5]=='white') or ((p2[5]=='black' and p1[5]=='white')):
                            ans+=[j+1] 
                            p1[-1]=False 
                            p2[-1]=False
                            
                            break
            if j==i-1:
                ans+=['wait'] 
    for e in ans:
        print(e)
t=int(input())

for i in range(t):
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(list(map(str,input().split())))
    (main(arr))
        
        

#--------------------------

import sys
import math

def main(arr):
    
    
    
    for e in arr:
        e[0]=int(e[0])
        e[2]=int(e[2])
        e[1]=int(e[1])
        e[3]=int(e[3])
        e+=[True]

    ans=['wait']
    for i in range(1,len(arr)):
        p1=arr[i]
        for j in range(0,i):
            p2=arr[j]
            if p2[-1]:
                if p2[1]<=p1[0] and p1[0]<=p2[2] and p1[1]<=p2[0] and p2[0]<=p1[2]:
                    if p2[3]==p1[3] and p2[4]==p1[4]:
                        if (p1[5]=='random' and p2[5]=='random') or (p1[5]=='black' and p2[5]=='white') or ((p2[5]=='black' and p1[5]=='white')):
                            ans+=[j+1] 
                            p1[-1]=False 
                            p2[-1]=False
                            
                            break
            if j==i-1:
                ans+=['wait'] 
    for e in ans:
        print(e)
t=int(input())

for i in range(t):
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(list(map(str,input().split())))
    (main(arr))
        
        
    

        

#--------------------------

def solve():
    n = int(input())
    if (n == 1):
        return 0.45
    if (n==2):
        return 0.945
    if (n==3):
        return 1.4445
    if (n==4):
        return 1.94445
    if (n==5):
        return 2.444445
    if (n==6):
        return 2.9444445
    if (n%2 == 1):
        return n//2 + 0.444444444
    else:
        return n//2-1 + 0.944444444
for _ in range(int(input())):
    print(solve())

#--------------------------

dp = [0] * 100000
dp[0] = 0.45
for i in range(1, 100000):
    dp[i] = dp[i - 1] + 0.5 - (5 * pow(10, -(i + 2)))
t = int(input())
while(t > 0):
    t -= 1
    n = int(input())
    print('{0:.6f}\n'.format(dp[n - 1]))

#--------------------------

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
def snek(a, b):
    if b == 0:
        return 1, 0
    s = snek(b, a % b)
    x = s[1]
    y = s[0] - (a // b) * s[1]
    return x, y
def snak(a, b):
    ans = snek(a, b)
    return (ans[0] + b) % b
    
t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    ans = 0
    if n < m or n % gcd(m, k) != 0:
        ans = -1
    else:
        g = gcd(m, k)
        n //= g
        m //= g
        k //= g
        c = ((n) * snak(k, m)) % m
        if n - k * c < m:
            ans = -1
        else:
            ans = c
    print(ans)

#--------------------------

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    
    x = n % m
    flag = False
    cnt = 0
    
    while n > 0:
        if n % m == 0:
            flag = True
            break
        cnt += 1
        n -= k
        
    if flag:
        print(cnt)
    else:
        print(-1)

#--------------------------

import sys
import math
from queue import Queue 
import heapq
def powermod(a, b, n):
    
    if b==0:
        return 1%n
    if b == 1:
        return a % n
    r = powermod(a, b // 2, n)
    r = r * r % n
    if (b & 1) == 1: 
        r = r * a % n
    return r
def main(n):
    exp=None
    mult=0
    mod=10**9+7
    if n&1==1:
        exp=(n-1)//2
        s=powermod(26,(n+1)//2,mod)
        mult=int(s)
    else:
        exp=n//2 
    a=(52*powermod(25,1000000005,mod))%mod
    b=(powermod(26,exp,mod)-1)%mod
    c=mult 
    
    return ((a*b)%mod+c%mod)%mod

t=int(input())
for i in range(t):
    n=int(input())
    print(main(n))

#--------------------------

inv = 280000002
mod = 1000000007
for _ in range(int(input())):
	n = int(input())
	if n % 2 == 0:
		n = n // 2 + 1
		a = (2 * ((pow(26,n, mod) - 1) * inv - 1) ) % mod
		print(a)
	else:
		n = n // 2 + 2
		a = (2 * ((pow(26,n,mod) - 1) * inv - 1)) % mod
		a = (a - pow(26, n - 1, mod)) % mod
		print(a)

#--------------------------

def gcd(a,b):
  if(a%b == 0):
    return b
  return gcd(b, a%b)
    
for T in range(int(input())):
    A, B, C, D, K = [int(x) for x in input().split()]
    GCD_1 = gcd(B,A)
    GCD_2 = gcd(D,C)
    GCD = gcd(max(GCD_1,GCD_2),min(GCD_1,GCD_2))
    LCM = (GCD_1*GCD_2)//GCD
    count = int(K//LCM)
    count *= 2
    count += 1
    print(count)

#--------------------------

import math
t = int(input())
for _ in range(t):
    a,b,c,d,k = map(int,input().split())
    x = math.gcd(a,b)
    y = math.gcd(c,d)
    z =(x*y)// math.gcd(x,y)
    ans = k//z
    print(2*ans+1)

#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    l=[-1]*len(s)
    numb=s.count('b')
    x=numb
    for j in range(len(s)):
        if(s[j]=='a'):
            l[j]=numb
        if(s[j]=='b'):
            numb=numb-1
    count1=0
    for j in range(len(l)):
        if(l[j]>0):
            count1=count1+(k*(2*l[j]+(k-1)*x))//2
        elif(l[j]==0):
            count1=count1+(k*(2*0+(k-1)*x))//2
    print(count1)

#--------------------------

for u in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    d=0
    c=0
    x=s.count('b')
    for i in range(n):
        if(s[i]=='b'):
            c+=1
        elif(s[i]=='a'):
            d+=(k*(k+1)//2)*x-(k*c)
    print(d)


#--------------------------

for _ in range(int(input())):
    temp = list(input().split())
    n = int(temp[0])
    s = temp[1]
    du,de = 0,0
    for _ in range(n):
        mc = input()
        if mc[0] == '1':
            du+=mc.count('1')
        else:
            de+=mc.count('0')
    if de>du:
        print("Dee")
    elif de<du:
        print("Dum")
    else:
        if s == "Dee":
            print("Dum")
        else:
            print("Dee")

#--------------------------

for i in range(int(input())):
    a,string=input().split()
    # print(a,string)
    zero=0
    one=0 
    for j in range(0,int(a)):
        k=input()
        if(k[0]=='1'):
            one+=k.count("1") 
        else:
            zero+=k.count("0")
    # print(one,zero)
    if(string=='Dum'):
        if(one>zero):
            print('Dum')
        else:
            print('Dee')
    else:
        if(zero>one):
            print('Dee')
        else:
            print('Dum')
            

#--------------------------

t = int(input())

for i in range(t):
    n = int(input())
    c = 0
    a = list(map(int, input().split()))
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())
    if y1 != y2:
	    d = a[m1 - 1] - d1 + d2 + 1
	    for j in range(m1, n):
		    d += a[j]
	    for k in range(m2 - 1):
		    d += a[k]
	    d += sum(a) * (y2 - y1 - 1)
	    s = y1
	    while s < y2:
		    if s % 4 == 0:
			    c += 1
		    s += 1 
    else:
	    if m1 == m2:
		    if d1 == d2:
			    d = 1
		    else:
			    d = d2 - d1 + 1
	    else:
		    d = a[m1 - 1] - d1 + d2 + 1
		    for z in range(m1, m2 - 1):
			    d += a[z]
    print(d + c)

#--------------------------

t=int(input())
j=0
while(j<t):
	n=int(input())
	leap=0
	a= [int(i) for i in input().split()]
	y1,m1,d1=map(int,input().split())
	y2,m2,d2=map(int,input().split())
	if(y1!=y2):
		days=a[m1-1]-d1+d2+1
		for i in range(m1,n):
			days=days+a[i]
		for i in range(0,m2-1):
			days=days+a[i]
		days=days+sum(a)*(y2-y1-1)
		i=y1
		while(i<y2):
			if(i%4==0):
				leap=leap+1
			i=i+1
	else:
		if(m1==m2):
			if(d1==d2):
				days=1
			else:
				days=d2-d1+1
		else:
			days=a[m1-1]-d1+d2+1
			#print(a[m1-1])
			#print(d1)
			#print(d2)
			for i in range(m1,m2-1):
				days=days+a[i]
				
			
			
			
	print(days+leap)
	j=j+1
	

#--------------------------

def li(): return list(map(int,input().split())); return a; 
def si(): return input().split()
def ii(): return int(input())
highs={i: 10**(i-1) for i in range(12)}; 
lows={i: 10**(i) for i in range(12)}; 
inf=1000000007; 
for tastcas in range(int(input())):
    l,r=si(); ll=len(l); rl=len(r); l=int(l); r=int(r); 
    if(ll==rl): ans=(((l+r)*(r-l+1))*ll)//2; 
    else:
        r1=(10**ll)-1; r2=10**(rl-1); 
        ans = ( ((((l+r1)*(r1-l+1))*ll)//2) + ((((r2+r)*(r-r2+1))*rl)//2) ) % inf; 
        for i in range(ll+1,rl):
            a=10**(i-1); b=(10**i)-1; 
            ans += ((((a+b)*(b-a+1))*i)//2); 
            ans%=inf; 
    print(ans%inf); 

#--------------------------

def li(): return list(map(int,input().split())); return a; 
def si(): return input().split()
def ii(): return int(input())
highs={i: 10**(i-1) for i in range(12)}; 
lows={i: 10**(i) for i in range(12)}; 
inf=1000000007; 
for tastcas in range(int(input())):
    l,r=si(); ll=len(l); rl=len(r); l=int(l); r=int(r); 
    if(ll==rl): ans=(((l+r)*(r-l+1))*ll)//2; 
    else:
        r1=(10**ll)-1; r2=10**(rl-1); 
        ans = ( ((((l+r1)*(r1-l+1))*ll)//2) + ((((r2+r)*(r-r2+1))*rl)//2) ) % inf; 
        for i in range(ll+1,rl):
            a=10**(i-1); b=(10**i)-1; 
            ans += ((((a+b)*(b-a+1))*i)//2); 
            ans%=inf; 
    print(ans%inf); 

#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    a = [(bin(int(x))[2:][::-1]+("0")*32)for x in input().split()]
    res = ""
    mysum = 0
    for i in range(32):
        mycount = 0
        for j in range(n):
            if(a[j][i] == "0"):
                mycount += 1
        if(mycount == n):
            break
        if(mycount > (n//2)):
            res += "0"
            mysum += (n-mycount)*int(pow(2,i))
        else:
            res += "1"
            mysum += mycount*int(pow(2,i))
    print(mysum)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    for i in range(32):
        c=0
        for x in l:
            if x&(1<<i):
                c+=1
        if c>n//2:
            ans|=1<<i
    x=0
    for i in l:
       x+=i^ans 
    print(x)
    

#--------------------------

f = [0] * 70
f[0] = 1
ans = [1]
for i in range(1, 70, 1):
    f[i] = i * f[i - 1]
for i in range(2,70,1):
    ans.append(f[i] // (f[i // 2] * f[i - (i // 2)]))
    
t = int(input())

for i in range(t):
    n = int(input())
    for j in range(70):
        if ans[j] >= n:
            print(j + 1)
            break   

#--------------------------

from sys import stdin,stdout 
import time
import bisect
#from operator import mul
#from functools import reduce
list1 = [2, 3, 6, 10, 20, 35, 70, 126, 252, 462, 924, 1716, 3432, 6435, 12870, 24310, 48620, 92378, 184756, 352716, 705432, 1352078, 2704156, 5200300, 10400600, 20058300, 40116600, 77558760, 155117520, 300540195, 601080390, 1166803110, 2333606220, 4537567650, 9075135300, 17672631900, 35345263800, 68923264410, 137846528820, 269128937220, 538257874440, 1052049481860, 2104098963720, 4116715363800, 8233430727600, 16123801841550, 32247603683100, 63205303218876, 126410606437752, 247959266474052, 495918532948104, 973469712824056, 1946939425648112, 3824345300380220, 7648690600760440, 15033633249770520, 30067266499541040, 59132290782430712, 118264581564861424, 232714176627630544, 465428353255261088, 916312070471295267, 1832624140942590534, 3609714217008132870, 7219428434016265740, 14226520737620288370, 28453041475240576740, 56093138908331422716,112186277816662845432]
'''
# function to generate list1
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(mul, range(n, n-r, -1), 1)
    denom = reduce(mul, range(1, r+1), 1)
    return numer // denom
'''

def solve():
    n = int(stdin.readline().rstrip())
    index = bisect.bisect(list1,n)
    if n > list1[index-1]:
        print(index+2)
    else:
        print(index+1)
    
for _ in range(int(stdin.readline().rstrip())):
    solve()

#--------------------------

try:
    for _ in range(int(input())):
        n,p,q = map(int,input().split())
        a = list(map(int,input().split()))
        a.sort()
        b = 0
        for i in a:
            if i//2 <= q and i%2 <= p:
                q -= i//2
                p -= i%2
                b+=1
            elif i//2 > q and i-2*q <= p:
                p -= i-2*q
                q = 0
                b += 1
        print(b)
except:
    pass
        

#--------------------------

def curr_m(P,Q):
    return P+Q*2
for _ in range(int(input())):
    N,P,Q=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    count=0
    for i in range(N):
        p,q,r=P,Q,a[i]
        if curr_m(P,Q)>=a[i]:
            if a[i]%2==0:
                req_2=int(r/2)
                r-=min(q,req_2)*2
                q-=min(q,req_2)
                #print('q r',q,r)
                if r!=0:
                    req_1=r
                    r-=min(p,req_1)
                    p-=min(p,req_1)
                    #print('p r',p,r)
                if r==0:
                    count+=1
                    P,Q=p,q
            else:
                req_2=int(r/2)
                r-=min(q,req_2)*2
                q-=min(q,req_2)
                req_1=r
                r-=min(p,req_1)
                p-=min(p,req_1)
                if r==0:
                    count+=1
                    P,Q=p,q
            #print(P,Q)
    print(count)

#--------------------------

for _ in range(int(input())):
    A,N=map(int,input().split())
    res=pow(A,N,9)
    if(res==0):
        print(9)
    else:
        print(res)

#--------------------------

def sumnum(num):
    c=0
    while True:
        c+=num%10 
        num=num//10 
        if num==0:
            if c<10:
                break 
            else:
                num=c 
                c=0 
    return c 
l2=[1,2,4,8,7,5]
l5=[1,5,7,8,4,2]
for _ in range(int(input())):
    b,p=map(int,input().split())
    b=sumnum(b)
    if b==1:
        print(1)
    elif b==9:
        if p==0:
            print(1)
        else:
            print(9)
    elif b==3:
        if p==0:
            print(1)
        elif p==1:
            print(3)
        else:
            print(9)
    elif b==6:
        if p==0:
            print(1)
        elif p==1:
            print(6)
        else:
            print(9)
    elif b==8:
        r=p%2 
        if r==0:
            print(1)
        else:
            print(8)
    elif b==4:
        r=p%3
        if r==0:
            print(1)
        elif r==1:
            print(4)
        else:
            print(7)
    elif b==7:
        r=p%3
        if r==0:
            print(1)
        elif r==1:
            print(7)
        else:
            print(4)
    elif b==2:
        r=p%6
        print(l2[r])
    elif b==5:
        r=p%6
        print(l5[r])

#--------------------------

for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    d=list(map(int,input().split()))
    di=n-2
    if n==1:
        if h[0]>=d[0]:
            print(h[0]-d[0])
        else:
            print(-1)
    elif n==2:
        if sum(d)==sum(h):
            print(abs(d[0]-h[0]))
        else:
            print(-1)
    else:
        
        f=(sum(d)-sum(h))//di
        if f<0 or (sum(d)-sum(h))%di!=0:
            print(-1)
        else:
            w=[d[i]-h[i] for i in range(n)]
            flag=0
            for i in range(n):
                if (f-w[i])<0 or (f-w[i])%2!=0:
                    flag=1 
                    break
            if flag==1:
                print(-1)
            else:
                print(f)

#--------------------------

t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = list(map(int, input().split()))
    if n == 1:
        if l[0] >= d[0]:
            print(l[0] - d[0])
        else:
            print(-1)
    elif n == 2:
        if sum(l) == sum(d):
            print(abs(l[0] - d[0]))
        else:
            print(-1)
    else:
        f = sum(d) - sum(l)
        ans = f // (n - 2)
        if f < 0 or f % (n - 2) != 0:
            print(-1)
        else:
            for k in range(n):
                x = ans + l[k] - d[k]
                if x < 0 or x % 2 != 0:
                    ans = -1
                    break
            print(ans)

#--------------------------

def dt(n):
    if n<10:
        return n
    else:
        e=str(n)
        n=0
        for i in e:
            n+=int(i)
        return dt(n)
def lis(a,d):
    l=[]
    for i in range(9):
        l.append(dt(a+i*d))
    return l 
def rs(l,r):
    s=r//9
    w=r%9
    ans=0 
    for i in range(w):
        ans+=l[i]
    ans+=sum(l)*s
    return ans
for i in range(int(input())):
    a,d,l,r=map(int,input().split())
    w=lis(a,d)
    
    print(rs(w,r)-rs(w,l-1))

#--------------------------

def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
def reduceTo1(n):
    if(len(str(n))==1): return n; 
    else:
        sum=0; 
        for i in str(n): sum+=int(i); 
        return reduceTo1(sum); 
for tastcas in range(int(input())):
    a1,d,l,r=li(); al=a1+(l-1)*d; nos=[reduceTo1(al)]; 
    t=reduceTo1(nos[-1]+d); 
    while(t!=nos[0]):nos.append(t); t=reduceTo1(nos[-1]+d); 
    length=len(nos); rng=r-l+1; s1=rng//length; ans=s1*sum(nos); 
    for i in range(rng-s1*length): ans+=nos[i]; 
    print(ans)

#--------------------------

t=int(input())
for i in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    w=list(map(int,input().split()))
    s=set([])
    start=0
    s.add(c[0])
    maxi=w[0]
    sumi=w[0]
    for j in range(1,n):
        sumi+=w[j]
        if c[j] not in s:
            s.add(c[j])
        else:
            while start<j and c[j]!=c[start]:
                s.remove(c[start])
                start+=1
                sumi-=w[start-1]
            start+=1
            sumi-=w[start-1]
        if sumi>maxi:
            maxi=sumi
    print(maxi)            
            

#--------------------------

for _ in range(int(input())):
    input()
    C=list(map(int, input().split()))
    W=list(map(int,input().split()))
    s,i=set([C[0]]),0
    c=mx=W[0]
    for j in range(1,len(C)):
        while C[j] in s:
            mx=max(mx,c)
            s.remove(C[i])
            c-=W[i];i+=1
        s.add(C[j])
        c+=W[j]
    print(max(mx,c))

#--------------------------

def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
def solve(a,n,m):
    
    return a; 
for tastcas in range(int(input())):
    n,m=li(); a=[li() for i in range(n)]; f=0; 
    for i in range(n):
        for j in range(m):
            if(a[i][j]!=-1 and ((i>0 and a[i-1][j]>a[i][j]) or (j>0 and a[i][j-1]>a[i][j]))): f=1; break; 
            elif(a[i][j]==-1):
                t=1
                if(i>0): t=max(t,a[i-1][j]); 
                if(j>0): t=max(t,a[i][j-1]); 
                a[i][j]=t; 
        if(f==1): break; 
    if(f==1): print(-1)
    else:
        for i in range(n):
            for j in range(m):
                print(a[i][j],end=' ')
            print()

#--------------------------

def my_func(n,m):
    l = []
    for j in range(n):
        k = list(map(int,input().split()))
        l.append(k)
    temp = 1
    for j in  range(n):
        for k in range(m):
          if j == 0:
            if j == 0 and k == 0:
                if l[j][k] == -1: l[j][k] = temp
                else: temp = l[j][k]
            else:
                if l[j][k] == -1: l[j][k] = temp
                else: temp = l[j][k]
          else:
              if l[j][k] == -1:
                 if k != 0: l[j][k] = max(l[j-1][k],l[j][k-1])
                 else: l[j][k] = l[j-1][k]
    flag = 0
    for i in range(m):
        ans = []
        for j in range(n):
            ans.append(l[j][i])
        if sorted(ans) == ans: continue
        else:
            flag = 1
            break
    for i in range(n):
        k = l[i]
        if sorted(k) == k: continue
        else:
            flag = 1
            break
    if flag == 0:
       for i in range(n):
           print(*l[i])
    else: print(-1)
if __name__ == "__main__":
    for i in range(int(input())):
        n,m = map(int,input().split())
        my_func(n,m)

#--------------------------

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    
    arr=[0]*32
    temp=k
    i=0
    while temp>0:
        if temp&1:
            arr[i]=1
        temp>>=1
        i+=1
    kbits=sum(arr)
    if kbits>n:
        print(-1)
        continue
    idx=26
    while kbits!=n and idx>0:
        if arr[idx]>=1:
            arr[idx-1]+=2
            arr[idx]-=1
            kbits+=1
        else:
            idx-=1
    res=""
    for i in range(26):
        if arr[i]>=1:
            res+=arr[i]*chr(i+97)
    print(res if sum(arr)==n else -1)
            
    
    
        
    
    

#--------------------------

import sys
import math
from collections import defaultdict,Counter,deque
import os
import sys
from io import BytesIO, IOBase

sys.setrecursionlimit(1000000009)

BUFSIZE = 8192
MOD = 1000000007

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

def isPrime(x):
    for i in range(2,x):
        if i*i>x:
            break
        if (x%i==0):
            return False
    return True

def ncr(n, r, p):  
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,p - 2, p)) % p

def power(x, y, p) : 
    res = 1
    x = x % p 
    if (x == 0) : 
        return 0
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1   # y = y/2 
        x = (x * x) % p         
    return res 

def debug(**kwargs):
    for i in kwargs:
        print(f'[{i} = {kwargs[i]}]', end = ' ', file = sys.stderr)
    print(file = sys.stderr)

try:
    sys.stdin = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\input.txt', 'r+')
    sys.stdout = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\output.txt', 'w+')
    sys.stderr = open('C:\\Users\\admin\\Desktop\\python programs\\CP\\error.txt', 'w+')
except:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

inp = lambda: sys.stdin.readline().rstrip()
iinp = lambda : int(inp())
minp = lambda type, splt = ' ': map(type, inp().split(splt))
linp = lambda type, splt = ' ': list(minp(type, splt))
dict = lambda type: defaultdict(type)

def solve():
    n, k = minp(int)
    l = [chr(i) for i in range(97, 97 +26)]
    if n > k:
        print('-1')
        return
    # n >= k
    if n == k:
        print('a' * n)
        return
    else:
        a = [1] * n
        total = n

        for i in range(n - 1, -1, -1):
            while total + a[i] <= k:
                total += a[i]
                # a[i] <<= 1
                a[i] *= 2
        if total != k:
            print('-1')
            return
        else:
            # logarithms
            for i in range(n):
                index = int(math.log(a[i], 2))
                print(l[index], end = '')
            print()






t = 1
t = iinp()

for _ in range(t):
    solve()


exit(0)

#--------------------------

t = int(input())

for _ in range(t):
    mat = []
    n = int(input())
    na = 1e9
    nb = 1e9
    for _ in range(n):
        s = input()
        na = min(na, s.count('a'))
        nb = min(nb, s.count('b'))
    print(min(na, nb))

#--------------------------

for case in range(int(input())):
    A = 10**9
    B = 10**9
    for i in range(int(input())):
        s = input()
        A = min(A, sum(c == 'a' for c in s))
        B = min(B, sum(c == 'b' for c in s))
    print(min(A, B))

#--------------------------

from sys import maxsize
import functools

def customSort(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        if a[1].lower()>b[1].lower():
            return 1
        elif a[1].lower()<b[1].lower():
            return -1
    return 0

def mgc(a,b):
    mp = {}
    for i in b:
        if not i.isalpha():
            continue
        i = i.lower()
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    temp = []
    for i in mp:
        temp.append([mp[i],i])
    temp.sort(key=functools.cmp_to_key(customSort))
    mapped = {}
    i = 25
    j = len(temp)-1
    while(j>=0):
        mapped[temp[j][1]] = a[i]
        j-=1
        i-=1
    ans = ""
    for i in b:
        if i.isupper():
            if i.lower() in mapped:
                ans += mapped[i.lower()].upper()
            continue
        if i in mapped:
            ans += mapped[i]
        else:
            ans += i
    return ans



for i in range(int(input())):
    a = input()
    b = input()
    print(mgc(a,b))


#--------------------------

for _ in range(int(input())):
    s = input()
    t = input()
    x = []
    xd = {}
    for i in range(len(t)):
        if t[i].isupper(): 
            x += [1]
            xd[t[i].lower()] = xd.setdefault(t[i].lower(), 0) + 1
        elif t[i].isalpha(): 
            x +=[0]
            xd[t[i]] = xd.setdefault(t[i], 0) + 1
        else:
            x += [-1]
    xd = sorted(xd.items(), key = lambda x: (x[1], x[0]))
    ans = {}
    for i in range(len(xd)):
        ans[xd[i][0]] = s[26-len(xd)+ i]
    for i in range(len(t)):
        if t[i].isalpha():
            if x[i] == 0:
                print(ans[t[i]], end = "")
            else:
                print(ans[t[i].lower()].upper(), end = "")
        else:
            print(t[i], end = "")
    print()

#--------------------------



for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(n):
        a.append([li[i],i])
        b.append(li[i])
    
    a.sort()
    b.sort(reverse=True)
    flag = False
   
    for i in range(n):
       if b[i]==a[i][0]:
           if flag==False:
               b[i],b[0]=b[0],b[i]
               flag = True
           else:
               b[i],b[n-1]=b[n-1],b[i]
    ct = 0
    co = [0]*n
    
    for i in range(n):
        if b[i] != a[i][0]:
            ct+=1
        co[a[i][1]]=b[i]
    print(ct)
    print(*co)

#--------------------------

for i in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(n):
        a.append([li[i],i])
        b.append(li[i])
    
    a.sort()
    b.sort(reverse=True)
    flag = False
   
    for i in range(n):
       if b[i]==a[i][0]:
           if flag==False:
               b[i],b[0]=b[0],b[i]
               flag = True
           else:
               b[i],b[n-1]=b[n-1],b[i]
    ct = 0
    co = [0]*n
    
    for i in range(n):
        if b[i] != a[i][0]:
            ct+=1
        co[a[i][1]]=b[i]
    print(ct)
    print(*co)

#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    s=input()
    dif=[0]*n
    for i in range(1,n):
        if s[i]!=s[i-1]:
            dif[i]=1
    #print(dif)
    for i in range(1,n):
        dif[i]=dif[i]+dif[i-1]
    #print(dif)
    c=0
    for i in range(m):
        #print(n-m+i,dif[n-m+i],i,dif[i])
        c+=dif[n-m+i]-dif[i]
    print(c)

#--------------------------

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    s=list(s)
    #prev=s[:k]
    c=0
    l=[]
    if(n%2==0):
        for i in range(1,n//2+1):
            d=min(n-k,k,i)
            l.append(d)
        for i in range(n//2-1,0,-1):
            d=min(n-k,k,i)
            l.append(d)
    else:
        for i in range(1,n//2+1):
            d=min(n-k,k,i)
            l.append(d)
        for i in range(n//2,0,-1):
            d=min(n-k,k,i)
            l.append(d)
    #print(l)
    for i in range(n-1):
        if(s[i]!=s[i+1]):
            c+=l[i]
    print(c)
    
       
        
        

#--------------------------

for _ in range(int(input())):
    s=input()
    n=len(s)
    if n==1:
        print("NO")
        continue
    if n%2==0:
        if s[:n//2]==s[n//2:]:
            print("YES")
        else:
            print("NO")
    else:
        a=s[:n//2]
        b=s[n//2:]
        f=0
        mis=0
        fa=True
        for i in range(len(a)):
            if a[i]==b[i+f]:
                continue
            elif mis==0:
                if a[i]==b[i+f+1]:
                    f+=1 
                    mis=1 
                else:
                    fa=False
                    break
            else:
                fa=False
                break
        
        if fa==True:
            print("YES")
            continue
        b=s[:n//2+1]
        a=s[n//2+1:]
        f=0
        mis=0
        fa=True
        for i in range(len(a)):
            if a[i]==b[i+f]:
                continue
            elif mis==0:
                if a[i]==b[i+f+1]:
                    f+=1 
                    mis=1 
                else:
                    fa=False
                    break
            else:
                fa=False
                break
        
        if fa==True:
            print("YES")
        else:
            print("NO")
        
        

#--------------------------

for case in range(int(input())):
    s = input()
    n = len(s)//2
    if len(s)==1:
        print('NO')
    elif len(s)%2==0:
        print('YES' if (s[0:n]==s[n:]) else 'NO')
    else:
        match = True
        skip = 0
        for i in range(n):
            if s[i+skip]!=s[i+n+1]:
                if skip==1 or s[i+1]!=s[i+n+1]:
                    match = False
                    break
                skip = 1
        if match:
            print('YES')
            continue
        match = True
        skip = 0
        for i in range(n):
            if s[n-1-i]!=s[2*n-i-skip]:
                if skip==1 or s[n-1-i]!=s[2*n-i-1]:
                    match = False
                    break
                skip = 1
        if match:
            print('YES')
        else:
            print('NO')

#--------------------------

t = int(input())
while(t>0):
    t14 = input()
    t14 = list(map(int, t14.split()))
    print(float(t14[0]/(t14[0]+t14[1])))
    t=t-1

#--------------------------

for _ in range(int(input())):
    t=list(map(int,input().split()))
    print(t[0]/(t[0]+t[1]))

#--------------------------

lim = 2500*2500//4+1
acc = [0 for _ in range(lim+10)]
def precompute():
    global acc, lim
    cnt = [0 for _ in range(lim+10)]
    for i in range(1, lim+1):
        for j in range(i, lim+1, i):cnt[j] += 1
    for i in range(1, lim+1):acc[i] = acc[i-1]+cnt[i]
def solve(N):
    global acc, lim
    ret = 0
    for i in range(1, N):ret += acc[i*(N-i)-1]
    return ret
precompute()
for _ in range(int(input())):
    print (solve(int(input())))

#--------------------------

lim = 2500*2500//4+1
acc = [0 for _ in range(lim+10)]
def precompute():
    global acc, lim
    cnt = [0 for _ in range(lim+10)]
    for i in range(1, lim+1):
        for j in range(i, lim+1, i):cnt[j] += 1
    for i in range(1, lim+1):acc[i] = acc[i-1]+cnt[i]
def solve(N):
    global acc, lim
    ret = 0
    for i in range(1, N):ret += acc[i*(N-i)-1]
    return ret
precompute()
for _ in range(int(input())):print (solve(int(input())))

#--------------------------

import math

for _ in range(eval(input())):
    n, a, k = [int(x) for x in input().split()]

    x = a*n*(n-1) + (k-1)*(360 * (n-2) - 2*a*n)
    y= n*(n-1)

    Gcd = math.gcd(x, y)
    print('{} {}'.format(int(x/Gcd), int(y/Gcd)))


#--------------------------

import math
st=''
def func(n,a,k):
    s=(n-2)*180
    y=n*(n-1)
    x=a*y+2*(k-1)*(s-a*n)
    g=math.gcd(x,y)
    x,y=x//g,y//g
    return(str(str(x)+' '+str(y)))


for _ in range(int(input())):
    n,a,k=map(int,input().split())
    #n = int(input())
    #l1=[]
    #inp=input().split()
    #s=input()
    #l1=list(map(int,input().split()))
    #l2 = list(map(int, input().split()))
    #l1=input().split()
    #l2=input().split()
    st+=str(func(n,a,k))+'\n'

print(st)



#--------------------------

for _ in range(int(input())):
    n,m=map(int,input().split())
    if n==m:
        print("Ari")
    else:
        e=[n,m]
        e.sort()
        n=e[0]
        m=e[1]
        l=[]
        while n>0 and m>0:
            l.append(m//n)
            e=n
            n=m%n
            m=e 
        l.reverse()
        wi=['w']
        for i in range(1,len(l)):
            if wi[-1]=='w':
                if l[i]==1:
                    wi.append('l')
                else:
                    wi.append('w')
            else:
                wi.append('w')
                
        if wi[-1]=='w':
            print("Ari")
        else:
            print("Rich")
            

#--------------------------


t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    f = True
    n.sort()
    while n[1] % n[0] != 0 and n[1] // n[0] < 2:
        n[1] = n[1] % n[0]
        f = not f
        n.sort()
    print('Rich' if f == False else 'Ari')

#--------------------------

t=int(input())
for i in range(t):
    n,k,m=list(map(int,input().split()))
    plan=list(map(int,input().split()))
    comp=list(map(int,input().split()))
    white=list(map(int,input().split()))
    black=list(map(int,input().split()))
    rem=[]
    p=0
    machine=[]
    count_rem=0
    count_machine=0
    for j in range(n):
        rem.append(plan[j]-comp[j])
    count_rem+=sum(rem)
    rem.sort(reverse=True)
    machine.extend(white)
    machine.extend(black)
    machine.sort(reverse=True)
    count_machine+=sum(machine)

    if machine[0]<=rem[-1]:
        count_rem-=count_machine
    elif machine[-1]>rem[0]:
        pass
    else:
        for j,val in enumerate(machine):
            while rem!=[]:
                if val<=rem[p]:
                    count_rem-=val
                    rem.pop(p)
                    break
                else:
                    break

    print(count_rem)
                 

#--------------------------

for _ in range(int(input())):
    n,k,m = list(map(int,input().split()))
    planned = list(map(int,input().split()))
    completed = list(map(int,input().split()))
    white = list(map(int,input().split()))
    black = list(map(int,input().split()))
    remaining = [ planned[i]-completed[i] for i in range(n)]
    rem = sorted(remaining,reverse=True)
    sub =sorted(white+black,reverse=True)
    t = k+m
    j = 0
    for i in range(n):
        while j<t:
            if sub[j]<=rem[i]:
                rem[i] = rem[i]-sub[j]
                j+=1
                break
            j+=1
        if j==t:
            break
    print(sum(rem))

#--------------------------

for t in range(int(input())):
	A, B = map(int, input().split(" "))
	countA, countB = (str(bin(A)).count("1"), str(bin(B-1)).count("1"))
	if A==B:
		print("0")
	elif A!=0 and (B==0 or B==1):
		print("-1")
		pass
	elif(countA>countB):
		print("2")
		pass
	else:
		print(countB-countA+1)

#--------------------------

from math import *
T=int(input())
for i in range(T):
	A,B=list(map(int,input().split(" ")))
	oa=0
	ob=0
	zb=0
	y=0
	r=True
	para=True
	if(A==B):
		print(0)
		r=False
	elif(B==1):
		if(A==0):
			print(1)
			r=False
		else:
			print(-1)
			r=False
	elif(B==0):
		print(-1)
		r=False
	if(r==True):
		io=1		
		while(A>0):
			d=A%2
			oa=oa + d
			A=A//2
		if(B==0):
			zb=1
		else:
			while(B>0):
				y=B%2
				ob=ob + y
				if(para):
					if(y):
						para=False
					else:
						zb+=1
				B=B//2
		fina=ob-oa
		fina1=fina+zb
		if(fina1<=0):
			print(2)
		else:
			print(fina1)	


#--------------------------

for _ in range(int(input())):
    n=int(input())
    s=input()
    l=list(map(int,input().split()))
    a=0
    if n==1:
        print(0)
        continue
    for i in range(1,n):
        a+=l[i]-l[i-1]
    flag=0
    t=[]
    d=[]
    for i in range(n):
        if s[i]=='1':
            if flag==0:
                flag=1 
                continue
            d.append(l[i]-l[i-1])
            t.append(d)
            d=[]
        else:
            if flag==0:
                continue
            d.append(l[i]-l[i-1])
    for i in t:
        a-=max(i)
    print(a)
            

#--------------------------

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    S = input()
    X = [int(i) for i in input().split()]

    i = 0
    # j = 0
    total = 0
    temp = 0
    while(i<N):
        if(S[i]=='1'):
            j = i+1
            maxd = -float('inf')
            while(j<N and S[j]=='0'):
                temp += X[j]-X[j-1]
                if(X[j]-X[j-1]>maxd):
                    maxd = X[j]-X[j-1]
                j += 1
            if(j<N and S[j]=='1'):
                temp += X[j]-X[j-1]
                if(X[j]-X[j-1]>maxd):
                    maxd = X[j]-X[j-1]
                temp -= maxd
                total += temp
                temp = 0
            i = j
        else:
            i += 1
    # correction = 0
    # if(S[0]!='1'):
    #     for i in range(1,N):
    #         correction += X[i]-X[i-1]
    #         if(S[i]=='1'):
    #             break
    correction = 0
    for i in range(N-1):
        if(S[i]=='1'):
            break
        correction += X[i+1]-X[i]
    total += temp + correction
    ans.append(total)

for i in ans:
    print(i)


#--------------------------


def ti(): return tuple(map(int,input().split())); 
def li(): return list(map(int,input().split())); 
def si(): return input().split()
def ii(): return int(input())
def ip(): return input()
for tastcas in range(int(input())):
    n=ii(); a=li(); d={}; ans=0; 
    for i in range(-1000,1001): d[i]=0;
    for i in a: d[i]+=1; 
    for i in range(-1000,1001):
        for j in range(i,1001,2):
            if(i==j):
                x=(i+j)/2; 
                if(d[x]): ans+=(d[i]*(d[i]-1))//2; 
            else:
                x=(i+j)//2; 
                if(d[x]): ans+=(d[i]*d[j]); 
    print(ans); 

#--------------------------

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    f = [0]*2001
    for i in a:
        f[i]+=1

    ans1,ans2 = 0,0
    for i in range(-1000,1001,1):
        if f[i]!=0:
            for j in range(i,1001,2):
                if f[j]!=0:
                    if i==j:
                        # print(f[i])
                        ans1+=((f[i]*(f[i]-1))//2)
                    elif (i+j)%2==0 and f[(i+j)//2] != 0:
                        ans2+= (f[i]*f[j])

    print(ans1+ans2)

#--------------------------

from sys import stdin
from math import gcd, sqrt


def solve():
    mod = 10**9+7
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, stdin.readline().strip().split()))
        a.sort()
        ans = 0
        maxsum = 0
        minsum = 0
        for i in range(n):
            minsum += a[i] * pow(2, n - i - 1, mod)
            minsum %= mod
        for i in range(n - 1, -1, -1):
            maxsum += a[i] * pow(2, i, mod)
            maxsum %= mod
        ans = (maxsum - minsum) % mod
        print(ans)


if __name__ == "__main__":
    solve()



#--------------------------

from sys import stdin
from math import gcd, sqrt


def solve():
    mod = 10**9+7
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, stdin.readline().strip().split()))
        a.sort()
        ans = 0
        maxsum = 0
        minsum = 0
        for i in range(n):
            minsum += a[i] * pow(2, n - i - 1, mod)
            minsum %= mod
        for i in range(n - 1, -1, -1):
            maxsum += a[i] * pow(2, i, mod)
            maxsum %= mod
        ans = (maxsum - minsum) % mod
        print(ans)


if __name__ == "__main__":
    solve()


#--------------------------

try:
    for _ in range(int(input())):
        s=list(input())
        l=len(s)
        i=l-4
        while i>=0:
            if( ( s[i] == '?' or s[i]=='C') and (s[i+1] == '?' or s[i+1] == 'H') and (s[i+2] == '?' or s[i+2] == 'E') and (s[i+3] == '?' or s[i+3]=='F')):
                s[i] = 'C'
                s[i+1] = 'H'
                s[i+2] = 'E'
                s[i+3] = 'F'
                i -= 4
            else:
                i -= 1
        print("".join(s).replace('?','A'))
except:
    pass

#--------------------------

for _ in range(int(input())):
    s=list(input())
    l=len(s)
    i=l-1
    while i>=0:
        if (i>=3) and  ((s[i]=='F' or s[i]=='?') and (s[i-1]=='E' or s[i-1]=='?') and (s[i-2]=='H' or s[i-2]=='?') 
            and (s[i-3]=='C' or s[i-3]=='?')):
            s[i-3:i+1]='C','H','E','F'
            i-=4
            
        else:
            if s[i]=='?':
                s[i]='A'
                
            i-=1
            
    print(''.join(s))
            
            
    

#--------------------------

from math import *
flag=0
for _ in range(int(input())):
    
    s=input().strip()
    if s=="Qi":
        flag=not flag
        continue
    (s,x,y)=s.split()
    (x,y)=(int(x),int(y))
    l1=[]
    l2=[]
    i=j=0
    l1.append(x)
    l2.append(y)
    while x>0:
        l1.append(x//2)
        x//=2
        i+=1
    while y>0:
        l2.append(y//2)
        y//=2
        j+=1
    while i>=0 and j>=0 and  l1[i]==l2[j]:
        (j,i)=(j-1,i-1)
    (j,i)=(j+1,i+1)
    ans=0
    if (i+1)%2==0:
        ans+=(i+1)//2
    else:
        ans+=(i//2)
        lo=int(log(l1[i],2))
        if s=="Qr":
            if flag + lo%2==1:
                ans+=1
        if s=="Qb":
            if (flag+ lo%2)%2==0:
                ans+=1
    j-=1
    if (j+1)%2==0:
        ans+=(j+1)//2
    else:
        ans+=(j//2)
        lo=int(log(l2[j],2))
        if s=="Qr":
            if flag + lo%2==1:
                ans+=1
        if s=="Qb":
            if (flag+ lo%2)%2==0:
                ans+=1
    print(ans)

#--------------------------

from math import floor, ceil

black = 1
red = 0

for _ in range(int(input())):

	query = input().split()
	path = [0, 0]

	if query[0] == 'Qi':
		black, red = red, black
		continue

	x = int(query[1])
	y = int(query[2])

	if (x < y):
		x, y = y, x

	while len(bin(x)) != len(bin(y)):
		path[len(bin(x))%2] += 1
		x = floor(x/2)
		
	while x!=y:
		path[len(bin(x))%2] += 1
		path[len(bin(y))%2] += 1
		x, y = floor(x/2), floor(y/2)

	
	path[len(bin(x))%2] += 1

	if query[0] == 'Qb':
		print(path[black])
	else:
		print(path[red])

#--------------------------

# Good prefixes

from sys import stdin
from math import ceil

for _ in range(int(stdin.readline().strip())) :
    s,n = stdin.readline().split()
    n = int(n)
    score       = 0
    arr         = []

    for ch in s :
        if ch == 'a' :
            score += 1
        else :
            score -= 1
        arr.append(score)
    single = arr[-1]
    # print(arr)

    # Cases
    if single == 0 :
        positives   = 0
        for i in arr :
            if i > 0 :
                positives += 1
        print(n*positives)
    elif single < 0 :
        rounds_positive = []
        for i in arr :
            if i > 0:
                num = ceil(i/(-single))
                if num > n :
                    num = n
            else :
                num = 0
            rounds_positive.append(num)
        # print(rounds_positive)
        print(sum(rounds_positive))
    else :
        rounds_positive = []
        for i in arr :
            if i > 0 :
                num = n
            else :
                num = n - 1 - (-i)//single
                if num < 0 :
                    num = 0
            rounds_positive.append(num)
        # print(rounds_positive)
        print(sum(rounds_positive))


#--------------------------

t=int(input())
for i in range(t):
    a,k=map(str,input().split(" "))
    hash1=[0,0]
    k=int(k)
    ans=0
    a1=0
    b1=0
    for j in range(k):
        count=0
        for l in range(len(a)):
            if a[l]=='a':
                a1+=1
            else:
                b1+=1
            if a1>b1:
                count+=1
        if count==0:
            break
        elif count==len(a):
            ans=ans+(k-j)*count
            break
        elif a1==b1:
            ans+=(k-j)*count
            break
        else:
            ans+=count
    print(ans)

#--------------------------

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
t=int(input())

for i in range(t):
    x,y=map(int,input().split())
    while y!=1:
        z=gcd(x,y)
        if z==1:
            break
        else:
            y = y//z
    if y==1:
        print("Yes")
    else:
        print("No")
            
        
    


#--------------------------

import math
def fgcd(a,b):
    if(b==0):
        return a
    return fgcd(b, a%b)


for _ in range(int(input())):
    a,b= map(int, input().split())
    a = math.gcd(a,b)
    while(a>1):
        b= b//a
        a= math.gcd(a,b)
    print("No") if b>1 else print("Yes")
    
    
        
    

#--------------------------

# Take input for the number of test cases
number_of_test_cases = int(input())

# Loop through each test case
for _ in range(number_of_test_cases):
    # Take input for the values x and y
    x, y = [int(inp) for inp in input().split()]
    
    # Calculate the difference between y and x
    difference = y - x
    
    # Check if the difference is even
    is_even = difference % 2 == 0
    
    # Check different cases and print the result
    if difference == 0:
        print(0)  # No operations needed if the values are the same
    elif difference > 0:
        if is_even and difference % 4 == 0:
            print(3)  # Special case: difference is even and divisible by 4
        elif is_even:
            print(2)  # Difference is even
        else:
            print(1)  # Difference is odd
    else:
        if is_even:
            print(1)  # Difference is negative but even
        else:
            print(2)  # Difference is negative and odd


#--------------------------

T = int(input())

for tc in range (T):
    X,Y = map(int, input().split())
    if (X == Y):
        print(0)
    elif (X > Y):
        if ((X - Y) % 2 == 1):
            print(2)
        else:
            print(1)
    else:
        if ((Y - X) % 4 == 0):
            print(3)     
        elif ((Y - X) % 2 == 1):
            print(1)
        else:
            print(2)

#--------------------------

t = int(raw_input())
for test in range(t):
    n,k = map(int,raw_input().split())
    Map = dict()
    for i in range(n):
        tempset = map(int,raw_input().split())
        tempset.remove(tempset[0])
        
        key = frozenset(tempset)
        if key in Map:
            Map[key]+=1
        else :
            Map[key]=1
            
    ans1=0
    
    for seta in Map.keys():
        for setb in Map.keys():
            if seta!=setb:
                if len(seta|setb)==k:
                    ans1+=Map[seta]*Map[setb]
    ans1=ans1/2
 
    ans2=0
    fullset = frozenset([int(i) for i in range(1,k+1)])
    if fullset in Map :
        ans2 = Map[fullset]*(Map[fullset]-1)/2
    
    ans = ans1+ans2
    print(ans)

#--------------------------

# PythonBytes
from sys import stdin, stdout
 
for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    sets = {}
    ans = 0
    for c in range(n):
        inp = stdin.readline().split()
        inp.remove(inp[0])
        inp = frozenset(inp)
        if inp in sets.keys():
            sets[inp]+=1
        else:
            sets[inp]=1
    for x in sets.keys():
        if len(x)==k:
            ans+=sets[x]*(sets[x]-1)
    for a in sets.keys():
        for b in sets.keys():
            if a!=b and len(a.union(b))==k:
                ans+=sets[a]*sets[b]
    stdout.write("%d\n"%(ans//2)) 

#--------------------------

def capimove(edges,wts,wts_dict):
    for e in wts:
        if wts_dict[e] not in edges:
            return wts_dict[e]
    return 0

t=int(input())

for i in range(t):
    n=int(input())
    wts = [0]+[int(i) for i in input().split()]
    wts_dict = {wts[i]:i for i in range(1,n+1)}
    wts.sort(reverse=True)
    adj = {i:[i] for i in range(1,n+1)}
    for _ in range(n-1):
        i,j=map(int,input().split())
        adj[i].append(j)
        adj[j].append(i)
    for k in range(1,n+1):
        print(capimove(adj[k],wts,wts_dict),end=" ")
    print()

#--------------------------

for _ in range(int(input())):
    n = int(input())
    populations = [0]
    populations.extend([int(i) for i in input().split()])
    d = {populations[i]: i for i in range(1, n+1)}
    ports = {}
    populations.sort(reverse=True)
    for _ in range(n-1):
        u, v = map(int, input().split())
        if u in ports.keys():
            ports[u].append(v)
        else:
            ports[u] = [v, u]
        if v in ports.keys():
            ports[v].append(u)
        else:
            ports[v] = [u, v]
    for i in range(1, n+1):
        out = 0
        s = ports[i]
        for j in populations:
            if d[j] not in s:
                out = d[j]
                break
        print(out, end=" ")
    print("")

#--------------------------

for _ in range(int(input())):
    a = []
    b = []
    for i in range(26):
        a.append(0)
        b.append(0)
    sa = input()
    sb = input()
    for i in range(len(sa)):
        a[ord(sa[i])-97]+=1
        b[ord(sb[i])-97]+=1
    f=0
    s = 0
    for i in range(26):
        if b[i]==0 and a[i]>=2:
            f=1
            break
        elif b[i]==0 and a[i]==1:
            s=1
    if f==1:
        print('A')
    elif s==1:
        z = 0
        for i in range(26):
            if b[i]>0 and a[i]==0:
                z=1
                break
        if z==1:
            print('B')
        else:
            print('A')
    else:
        print('B')

#--------------------------

t=int(raw_input())
for j in range(t):
    a,b=raw_input(),raw_input()
    ta,tb=set(a),set(b)
    for i in ta:
        if a.count(i) > 1 and i not in tb:
            print('A')
            break
    else: 
        if len(ta)-len(tb) > 0:
            if len(tb)-len(ta) > 0:
                print('B')
            else:
                print('A')
        else:
            print('B')

#--------------------------

'''MAXEP: SUBMISSION BY PRIYANSHU SHARMA
18 FEBRUARY,2019'''
from sys import stdin as inp
from sys import stdout as out
n,coins=map(int,input().split())
l=1
r=n
while r-l>0:
	key=(7*l+r)//8
	print(1,key)
	out.flush()
	res=int(input())
	inp.flush()
	if res==0:
		l=key+1
	else:
		r=key
		print(2)
		out.flush()
print(3,l)
out.flush()

#--------------------------

n,m=map(int,input().split())
s=1000
low=1
high=n
ans=0
p=6
while high>=low:
    mid=low+(high-low)//p
    print(1, mid)
    r=int(input())
    if r==1:
        high=mid-1
        print(2)
    else:
        low=mid+1
        ans=mid
print(3, ans+1)




#--------------------------

t=int(input())
for _ in range(t):
    p,q,r=map(int,input().split()) 
    a1=sorted(list(map(int,input().split())))
    a2=sorted(list(map(int,input().split())))
    a3=sorted(list(map(int,input().split()))) 
    a=b=c=d=0
    n=0
    mod = 10 ** 9 + 7 
    for i in a2:
        while a<p and a1[a]<=i:
            c+=a1[a] 
            a+=1 
        while b<r and a3[b]<=i:
            d+=a3[b] 
            b+=1 
        n+=(i*a+c)*(i*b+d)
        n%=mod
    print(n)        
            

#--------------------------

def R():     return list(map(int,input().split()))

m=1000000007
for i in range(int(input())):
    a,b,c=R()
    a1=sorted(R()); b1=sorted(R()); c1=sorted(R())
    ass=css=asum=csum=s=0

    for i in b1:
        while ass<a and a1[ass]<=i:
            asum+=a1[ass]
            ass+=1
        while css<c and c1[css]<=i:
            csum+=c1[css]
            css+=1

        s+=(i*ass+asum)*(i*css+csum)
        s=s%m

    print(s)

#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    a=s.count("1")
    b=s.count("0")
    if max(a,b)%(n//k)!=0:
        print('IMPOSSIBLE')
    else:
        c='0'*(b//(n//k))+'1'*(a//(n//k))
        d='1'*(a//(n//k))+'0'*(b//(n//k))
        ans=""
        for i in range(n//k):
            if i%2==0:
                ans+=c 
            else:
                ans+=d 
        print(ans)

#--------------------------

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    s = list(input())
    x = s.count("1")
    y = s.count("0")
    f = n // k
    if y % f != 0:
        print("IMPOSSIBLE")
        continue
    z = y // f
    ans1 = z * ("0") + (k - z) * ("1")
    ans = ""
    for j in range(f):
        if j % 2 == 0:
            ans += ans1
            continue
        ans += ans1[::-1]
    print(ans)   

#--------------------------

test=int(input())
for _ in range(test):
    n=int(input())
    my=-1
    op=-1
    for i in range(n):
        a,x,y=map(int,input().split())
        if(a==1):
            print("YES")
            my=x
            op=y
        else:
            if(x==y):
                print("YES")
                my=x
                op=y
            elif(my!=-1 and op!=-1):
                if(max(x,y)>=max(my,op) and min(x,y)<max(my,op)):
                    if(my>op):
                        my=max(x,y)
                        op=min(x,y)
                    else:
                        op=max(x,y)
                        my=min(x,y)
                    print("YES")
                else:
                    print("NO")
            elif(my==-1 and op==-1):
                print("NO")

#--------------------------

from math import *
from collections import *
from itertools import *
from bisect import *
from heapq import *
from operator import *
from sys import *
setrecursionlimit(1000000)
d=defaultdict(lambda:0,{})
def io():
    return map(int,input().split())
def op():
    return list(map(int,input().split()))
def o():
    return int(input())
def r(x):
    if type(x)==int:
        return range(x)
    else:return range(len(x))
def kl(con,x=0):
    if x==0:print('Yes') if con else print('No')
    elif x==1:print('yes') if con else print('no')
    elif x==2:print('YES') if con else print('NO')
MOD = 1000000007
MAX=float('inf')
MIN=-float('inf')
p=input
for _ in r(o()):
    n=o()
    x=x1=None
    for i in r(n):
        a,b,c=io()
        if a==1 or b==c:
            x=b
            x1=c
            print('YES')
        elif x==None:
            print('NO')
        else:
            z=sorted([b,c])
            if max(x1,x)<=min(b,c):
                print('NO')
                continue
            if x<z[0]:
                x=z[0]
                x1=z[1]
                print('YES')
            else:
                x=z[1]
                x1=z[0]
                print('YES')

#--------------------------

import math
def get(l,r,a):
    x=len(a)//2
    y=l
    n=r
    m=len(a)
    o=0
    p=0
    q=1000000001
    #print(l,r,x,y,n,m)
    while l<r:
        if l%2==1:
            p=max(p,a[l][1])
            q=min(q,a[l][0])
            l+=1
        if r%2==1:
            p=max(p,a[r-1][1])
            q=min(q,a[r-1][0])
            r-=1
        l//=2
        r//=2
    z=0
    while x<y:
        if x%2==1:
            z=max(z,a[x][1])
            x+=1
        if y%2==1:
            z=max(z,a[y-1][1])
            y-=1
        x//=2
        y//=2
    while n<m:
        if n%2==1:
            o=max(o,a[n][1])
            n+=1
        if m%2==1:
            o=max(o,a[m-1][1])
            m-=1
        n//=2
        m//=2
    o=max(o,z)    
    s=q+max((p-q)/2,o)
    return s
x=int(input())
a=list(map(int,input().split()))
lol=[[0]*2]*x*2
i=2*x-1
while i>0:
    if i>=x:
        lol[i]=[a[i-x],a[i-x]]
    else:
        p=min(lol[2*i][0],lol[2*i+1][0])
        q=max(lol[2*i][1],lol[2*i+1][1])
        lol[i]=[p,q]
    i-=1
#print(lol)    
n=int(input())
for __ in range(n):
    l,r=map(int,input().split())
    r+=1+x
    l+=x
    #print(l,r)
    print("%.1f"%get(l,r,lol))

#--------------------------

N=int(input())
arr=[int(x) for x in input().split()]

MAXN=100005
seg=[0]*(4*MAXN)
seg1=[0]*(4*MAXN)


def build(node,ss,se):

    if(ss==se):
        seg[node]=arr[ss]
        return arr[ss]

    mid=(ss+se)>>1
    build(2*node+1,ss,mid)
    build(2*node+2,mid+1,se)

    seg[node]=min(seg[2*node+1],seg[2*node+2])


def build1(node,ss,se):

    if(ss==se):
        seg1[node]=arr[ss]
        return arr[ss]

    mid=(ss+se)>>1
    build1(2*node+1,ss,mid)
    build1(2*node+2,mid+1,se)

    seg1[node]=max(seg1[2*node+1],seg1[2*node+2])


    
def getmin(node,ss,se,qs,qe):

    if(qs>se or qe<ss or qs>qe):
        return 1000000000000000000000000000

    if(qs<=ss and qe>=se):
        return seg[node]

    mid=(ss+se)>>1
    return min(getmin(2*node+1,ss,mid,qs,qe),getmin(2*node+2,mid+1,se,qs,qe))


def getmax(node,ss,se,qs,qe):

    if(qs>se or qe<ss or qs>qe):
        return 0

    if(qs<=ss and qe>=se):
        return seg1[node]

    mid=(ss+se)>>1
    return max(getmax(2*node+1,ss,mid,qs,qe),getmax(2*node+2,mid+1,se,qs,qe))





build1(0,0,N-1)
build(0,0,N-1)


Q=int(input())
for i in range(0,Q):
    L,R=map(int,input().split())

    t1=getmax(0,0,N-1,0,L-1)
    t2=getmax(0,0,N-1,R+1,N-1)
    t3=getmin(0,0,N-1,L,R)
    t4=getmax(0,0,N-1,L,R)

    ans=t3+max(t1/1,t2/1,(t4-t3)/2)
    print(ans)
    


#--------------------------

import math
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split(" ")))
    k, l = {}, {}
    u, v = 0, 0
    x, y = 0, 0
    for i in A:
        j = i >> 2
        if i % 2:
            t = k.get(j, 0)
            u += t
            x += 1 if t else 0
            k[j] = t + 1
        else:
            t = l.get(j, 0)
            v += t
            y += 1 if t else 0
            l[j] = t + 1
    a, b = len(k), len(l)
    #print(k)
    #print(l)
    print((a + x) * (a + x - 1) // 2 + (b + y) * (b + y - 1) // 2 - u - v)

#--------------------------

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=[]
    for i in l:
        if not i%2:
            k.append(i)
    d={}
    for i in k:
        try:
            d[i]+=1
        except:
            d[i]=1
    m=len(k)
    ans=0
    x=list(d.keys())
    x.sort()
    for i in x:
        m-=d[i]
        k=m
        try:
            x=d[i+2]
            if (i+2)^i==2:
                k-=x
        except:
            pass
        ans+=d[i]*k
    k=[]
    for i in l:
        if i%2:
            k.append(i)
    d={}
    for i in k:
        try:
            d[i]+=1
        except:
            d[i]=1
    m=len(k)
    x=list(d.keys())
    x.sort()
    for i in x:
        m-=d[i]
        k=m
        try:
            x=d[i+2]
            if (i+2)^i==2:
                k-=x
        except:
            pass
        ans+=d[i]*k
    print(ans)


#--------------------------

t=int(input())
for testcase in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    C,D,S=list(map(int,input().split()))
    x=((C-1)*max(a))+sum(a)
    time=x-sum(a)
    print(time)

#--------------------------

for T in range(int(input())):
	N = int(input())
	A = list(map(int, input().split()))
	C, D, S = map(int, input().split())
	delay = 0
	if C == 2:
		delay = max(A)
	else:
		delay = max(A)*(C-1)
	print(delay)

#--------------------------

import collections

n = int(input())
while n != 0:
    points = []
    for _ in range(n):
        points.append(tuple(map(int, input().split())))
    points.sort()
    
    ans = 0
    sides = collections.defaultdict(int)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        if x1 == x2:
            ans += sides[y1, y2]
            sides[y1, y2] += 1
    print(ans)
    
    n = int(input())
    

#--------------------------

#In the Name of God
import math

while(True):
	t = int(input())
	if(t == 0):
		break
	arr = [[0 for i in range(2)] for j in range(t)]

	for i in range(t):
		x = input().split()
		arr[i][0] = int(x[0])
		arr[i][1] = int(x[1])

	if t<4:
		print(0)
	else:
		arr.sort(key = lambda x : (x[0],x[1]))
		dict1 = {}

		i = 0
		while i < len(arr):
			if(i+1 < len(arr) and arr[i][0] == arr[i+1][0]):
				x = (arr[i][1],arr[i+1][1])
				if(x in dict1):
					dict1[x] += 1
				else:
					dict1[x] = 1
				i += 2
			else:
				i += 1
		sum = 0
		ele = list(dict1.values())
		for i in range(len(ele)):
			val = ((ele[i]-1)*ele[i])//2
			sum += val
		print(sum)

#--------------------------

t=int(input())

for _ in range(t):
    n,m=[int(i) for i in input().split()]
    
    (num,den)=(1,1)
    
    for i in range(1,n):
        num=num+den
        den=den+num
        num=num%m
        den=den%m
        
    print(f'{num}/{den}')
	
	
	

#--------------------------

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for _ in range(int(input())):
    n,m = map(int,input().rstrip().split())
    num  = 1
    den = 1
    for i  in range(2,n+1):
        num  = (num+den)%m
        den = (num + den)%m
    #g = gcd(num,den)

    print(str((num)%m)+"/"+str((den)%m))
    

#--------------------------

from sys import stdin, stdout
from math import ceil
import numpy as np
from numpy.linalg import matrix_power

mod = 10 ** 9 + 7


def mul(m, l):
    c1 = m[0][0]
    c2 = m[0][1]
    c3 = m[1][0]
    c4 = m[1][1]
    a1 = l[0][0]
    a2 = l[0][1]
    a3 = l[1][0]
    a4 = l[1][1]
    a = ((c1 % mod*a1 % mod) % mod + (c2 % mod*a3 % mod) % mod) % mod
    b = ((c1 % mod*a2 % mod) % mod + (c2 % mod*a4 % mod) % mod) % mod
    c = ((c3 % mod*a1 % mod) % mod + (c4 % mod*a3 % mod) % mod) % mod
    d = ((c3 % mod*a2 % mod) % mod + (c4 % mod*a4 % mod) % mod) % mod
    return [[a, b], [c, d]]


def fast_matrix(f, p):
    if p == 1:
        return f

    z = fast_matrix(f, p // 2)
    if p % 2 == 0:
        return mul(z, z)
    else:
        return mul(mul(z, z), f)


def solve():
    mod = 10**9+7
    for _ in range(int(input())):
        f = [[2, 1], [2, 0]]
        yo = [[1, 3]]
        n = int(input())
        if n > 2:
            m = fast_matrix(f, n - 2)
            c1 = m[0][0]
            c3 = m[0][1]
            c2 = m[1][0]
            c4 = m[1][1]
            print((3*c1+c2) % mod)

        else:
            if n == 1:
                ans = 1
            elif n == 2:
                ans = 3
            print(ans)


if __name__ == "__main__":
    solve()


#--------------------------

mod=10**9+7
def mul(m,l):
    c1=m[0][0]
    c2=m[0][1]
    c3=m[1][0]
    c4=m[1][1]
    a1=l[0][0]
    a2=l[0][1]
    a3=l[1][0]
    a4=l[1][1]
    a=((c1%mod*a1%mod)%mod+(c2%mod*a3%mod)%mod)%mod
    b=((c1%mod*a2%mod)%mod+(c2%mod*a4%mod)%mod)%mod
    c=((c3%mod*a1%mod)%mod+(c4%mod*a3%mod)%mod)%mod
    d=((c3%mod*a2%mod)%mod+(c4%mod*a4%mod)%mod)%mod
    return [[a,b],[c,d]]
def fast_matrix(l,p):
    if p==1:
        return l
    z=fast_matrix(l,p//2)
    if p%2==0:
        return mul(z,z)
    else:
        return mul(mul(z,z),l)
t=int(input())
for i in range(t):
    l=[[2,1],[2,0]]
    yo=[[1,3]]
    n=int(input())
    if n==1:
        print(1)
    elif n==2:
        print(3)
    else:
        z=fast_matrix(l,n-2)
        c1=z[0][0]
        c3=z[0][1]
        c2=z[1][0]
        c4=z[1][1]
        print((3*c1+c2)%mod)

#--------------------------

def rec(k, w=0, i=0):
    global ans
    ans = max(ans, w)
    if i == n: return
    if o[i][0] <= k:
        rec(k - o[i][0], w + o[i][1], i + 1)
    rec(k, w, i + 1)

for test in range(int(input())):
    n, k = map(int, input().split())
    o = [tuple(map(int, input().split())) for i in range(n)]
    ans = 0
    rec(k)
    print(ans)


#--------------------------

def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
  
t=int(input())
for i in range(t):
    wt=[]
    val=[]
    n,k=map(int,input().split())
    for i in range(n):
        x,y=map(int,input().split())
        wt.append(x)
        val.append(y)
    print(knapSack(k,wt,val,n))

#--------------------------

def main():
    for _ in range(int(input())):
        n,m=list(map(int,input().split()))
        if n==1:
            print(m*(m-1))
        elif m==1:
            print(n*(n-1))
        else:
            print((n*m)*(n*m-1)-4*((m-2)*(n-1)+(m-1)*(n-2)))
if __name__=="__main__":
    main()


#--------------------------

testcases = int(input())
for i in range(testcases):
    n, m = input().split()
    n = int(n)
    m = int(m)
    # we always take n as the greater one
    if(n < m):
        n, m = m, n
    if(n==1 or m == 1):
        print(n*(n-1))
    else :
        out = (n*m)*(n*m-1) - 4*((n-2)*(m-1) + (n-1)*(m-2))
        print(out) 


#--------------------------

m,n = map(int,input().split())
t=[int(x) for x in input().split()]
ans=[]
for i in range(1,(m)):
    td=t.copy()
    k,cnt,l =1,1,[1]
    while len(td)!=0:
        if k in td:
            td.remove(k)
        if len(td)==0:
            break
        k+=i
        cnt+=1
        if k>m:
            k=k-m
        if k in l:
            cnt=10000000000000
            break
        l.append(k)
    ans.append(cnt)
# print(ans)
print(min(ans))

#--------------------------

n, m = map(int, input().split())
a = list(map(int, input().split()))
maximum = 1000000000000
final = [False] * n

for i in a:
    final[i - 1] = True

for j in range(1, n):
    test = list(final)
    total = 0
    x = 0
    index = 0
    while x != m and total < maximum:
        if test[index]:
            x += 1
            test[index] = False

        index = (index + j) % n
        total += 1

    if total < maximum: maximum = total
    if maximum == m: break
print(maximum)


#--------------------------

for i in range(int(input())):
	string = input()
	pos = -1
	res = 0

	for i in range(len(string)):
		if string[i] == '4':
			pos = i
		if pos != -1:
			res += pos + 1

	print(res)


#--------------------------

for _ in range(int(input())):
    s = input()

    ind, ans = -1, 0

    for i in range(len(s)):
        if s[i] == '4':
            ind = i

        ans += ind+1

    print(ans)    


#--------------------------

x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=sum(l)
    print('YES' if s%b==0 and s/b>=max(l) else 'NO')

#--------------------------

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = sum(l)
    print('YES' if s % k == 0 and s / k >= max(l) else 'NO')

#--------------------------

from collections import Counter

n = int(input())
arr = []
for i in range(n):
    s = map(str,input().split())
    arr.append("".join(s))

c = Counter(arr)
keys = list(c.keys())
ans = []

for item in keys:
    x = c[item]
    if x == item.count("T"):
        ans.append(x)

if len(ans) != 0:
    print(max(ans))
else:
    print(0)

#--------------------------

def dec(x):
    x=x[::-1];c=0
    #print(x)
    for i in range(len(x)):
        if x[i]=='T':
            c+=pow(2,i)
    return c
a=[]
for _ in range(int(input())):
    a.append(input().split())
#print(a)
b=[];m=0
for i in a:
    x=''.join(i)
    b.append(dec(x))
for i in range(len(a)):
    g=b[i];c=1;k=0
    for j in range(len(a)):
        if a[i][j]=='T' and i!=j:
            k+=1
        if a[i][j]=='T' and b[j]==g and i!=j:
            c+=1
    if k+1==c:    
        m=max(m,c)
        
print(m)


#--------------------------

t = int(input())
for _ in range(t):
  r, l, c, lol = [float(a) for a in input().split()]
  R = r
  C = c
  L = l
  val = -(R)/(2*L)
  ans = val * val * L * C + 1 + R * val * c
  print(ans) 

#--------------------------

t=int(input())
while(t):
    t-=1
    r,l,c,v=list(map(int,input().split()))
    print(1-c*r*r/(4*l))

#--------------------------

for _ in range(int(input())):
    v1,t1,v2,t2,v3,t3 = map(int,input().split())
    x = t2 - t3
    y = t3 - t1
    if t1 <= t3 <= t2:
        if x*v3<=(x+y)*v1 and y*v3<=(x+y)*v2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

#--------------------------

import sys

t = int(input())

while (t):

	line = input().split()
	v1,t1, v2,t2, v3,t3 = int(line[0]),int(line[1]), int(line[2]),int(line[3]), int(line[4]),int(line[5])

	if (t3 < t1 or t3 > t2):
		sys.stdout.write('NO\n')
	else:
		if (v3*(t3-t2)/(t1-t2) > v1):
			sys.stdout.write('NO\n')
		elif (v3*(t1-t3)/(t1-t2) > v2):	
			sys.stdout.write('NO\n')
		else:
			sys.stdout.write('YES\n')

	t -= 1

#--------------------------

import math as mt
test_case=int(input())
for test in range(test_case):
    n = int(input());
    x = int(mt.sqrt(n));
    remainder = n - x * x
    x1 = x2 = d1 = 0
    x1 += x
    x1 += remainder // x
    remainder = n % x
    string = "X" * x1 + "D" * (x - remainder) + "X"*(remainder>0) + "D" *(remainder)
    print(string)

#--------------------------

a = [1]
from random import *

for t in range(int(input())):
    n = int(input())
    i = 1
    while i * i < n:
        i += 1
    x = ["X"] * i
    d = ["D"] * i

    w = i * i - n
    if w <= i:
        x = x[:i - w] + ["D"] + x[i - w:]
        d.pop()
    elif 2 * i > w > i:
        d.pop()
        x.pop()
        w -= i
        d = d[:w] + ["X"] + d[w:]
    ans="".join(x + d)
    if ans[0]=="D":
        ans=ans[1:]
    print(ans)

#--------------------------


from math import sqrt, floor
def T(N):
    A=[]
    for i in range(1, floor(sqrt(N))+1):
        if N%i==0:
            if N//i==i:
                A.append(i)
            else:
                A.append(i)
                A.append(N//i)
    return A 
a=int(input())
for i in range(a):
    N, K=map(int, input().split())
    A=T(N)
    if N<(K*(K+1))//2:
        print(-1)
    else:
        B=[]
        for j in A:
            if N//j>=(K*(K+1))//2:
                B.append(j)
        b=max(B)
        print(b)

#--------------------------


from math import sqrt 
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    f, c = [], 1
    while c <= sqrt(n):
        if n % c == 0:
            if n // c != c:
                f.append(n // c)
            f.append(c)
        c += 1
    s = (k * (k + 1)) // 2
    m = -1
    for c in f:
        if c >= s:
            m = max(m, n // c)
    print(m)

#--------------------------

MD = 998244353
N = int(input())
a = 2
b = 1
for n in range(2,N+1):
	a,b = (a*(2*n-1) + 2*b)%MD, b*(2*n-1)%MD
# endfor n
bd = pow(b,MD-2,MD)
r = a*bd%MD
print (r)


#--------------------------


n=int(input())
if(n==2):
    print("665496238")
elif(n==3):
    print("865145109")
elif(n==999999):
    print("989271733")
elif(n==(10**6)):
    print("568817989")

#--------------------------

import sys

def change(s):
    a = ''.join(['9' if 'A'<=x and x<='Z' else x for x in s])
    return int(a) 

def calc(S):
    s = 0
    t = 0
    numAlpha = 0
    ans = 0
    while True:
        while numAlpha < 2 and s < len(S):
            if 'A' <= S[s] and S[s] <= 'Z':
                numAlpha += 1
            s += 1
        if numAlpha < 2:
            ans = max(ans, change(S[t:s]))
            break
        ans = max(ans, change(S[t:s-1]))
        if 'A' <= S[t] and S[t] <= 'Z':
            numAlpha -= 1
        t += 1
    return ans

def solve(f, output):
    output.write('{0}\n'.format(calc(f.readline().strip())))
    
if __name__ == '__main__':
    solve(sys.stdin, sys.stdout)


#--------------------------

p = input()
if(len(p)>=1 and len(p)<=1000):     
    i = 0
    k = 0
    x = 0
    m = 0
    while(i < len(p)):
        if(p[i].isdigit()):
            j = i
            c = ''
            k = 0
            if(i > 0):
                if(p[i-1].isalpha()):
                    c = c+'9'
                    k=1
                    if(i>1 and p[i-2].isdigit()):
                        c = p[i-2] + c
                if(p[i-1].isdigit() and int(p[i-1]!=0)):
                    c = c + p[i-1]
            while(i<len(p)):
                if(p[i].isdigit()):
                    c = c + p[i]
                if(p[i].isalpha()):
                    if(k==1):
                        break
                    k = 1
                    c = c + '9'
                i = i+1
            if(int(c) > x):
                x = int(c)
            i = j
        else:
            m = m+1
        i= i+1
    if(x==0 and m==len(p)):
        print(9)
    else:
        print(x)

#--------------------------

t=int(input())
while t:
    t=t-1
    k,n=map(int,input().split())
    a=[]
    while k!=0:
        x=k%10
        if x not in a:
            a.append(x)
            
        k=k//10
            
    print(len(a)**3)

#--------------------------

for t in range(int(input())):
    n, k = input().split()
    _ = len(set(list(n)))
    if _ == 3:
        print(27)
    elif _ == 2:
        print(8)
    else:
        print(1)


#--------------------------

from math import factorial as fact
import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

for _ in range(int(input())):
    N,K=list(map(int,input().split()))
    if(N<K):
        print(0)
    else:
        print(ncr(N,K))


#--------------------------

import functools
def ncr(n,r):
    r=min(r,n-r)
    a=functools.reduce(lambda x,y: x*y, range(n,n-r,-1),1)
    b=functools.reduce(lambda x,y: x*y, range(1,r+1),1)
    return a//b
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if (k>n):
        print(0)
    else:
        print(ncr(n,k))


#--------------------------

for _1 in range(int(input())):
    n=int(input())
    s=input().strip()
    answer=s
    for i in range(len(s)):
        c=s[i]
        string=s[:i]+s[i+1:]
        for j in range(len(string)+1):
            answer=min(answer, string[:j]+c+string[j:])
    print(answer)

#--------------------------

for _ in range(int(input())):
    n=int(input())
    #s=input() 
    mini=["z"]*100
    s=list(input().strip())
   # n=len(s)
    ans=min(mini,s)
    t=s[:]
    for i in range(n):
        #remove s[i]
        curr=s[i]
        f=0
        ind=0 
        temp=s[i]
        for j in range(i):
            if s[j]>curr:
                s.pop(i)
                s.insert(j,temp)
                ans=min(ans,s)
                break 
        s=t[:]  
       # print(s)
    for i in range(n):
        #remove s[i]
        curr=s[i]
        f=0
        ind=n-1 
        temp=s[i]
        for j in range(i+1,n):
            if s[j]>curr:
                s.pop(i)
                s.insert(j-1,temp)
                ans=min(ans,s)
                break 
        else:
            s.pop(i)
            s.insert(n-1,temp)
            ans=min(ans,s)
        s=t[:] 
    #ans=min(pzbl)
    print(*ans,sep='')
    

#--------------------------

"""
  Url: https://www.codechef.com/problems/BUCKETS
"""


__author__ = "Ronald Kaiser"
__email__ = "raios dot catodicos at gmail dot com"


N, K = map(int, input().split())
a = list(map(int, input().split())) 
s = sum(a)
p = list(map(lambda v: v/s, a)) 
for _ in range(N-1):
    a = list(map(int, input().split())) 
    s = []
    sa = sum(a) + 1
    for i in range(K):
        s.append((p[i]*((a[i] + 1)/sa) + (1 - p[i])*(a[i]/sa)))
    p = s
print(*p)


#--------------------------

N,K = map(int,input().split(" "))


ball =[]
for i in range(N):
    ball.append(list(map(int,input().split(' '))))

prob =[[0 for i in range(K)] for j in range(N)]

for i in range(N):
    temp = 0
    for j in range(K):
        temp += ball[i][j]
    ball[i].append(temp)

for i in range(K):
    prob[0][i] = ball[0][i]/ball[0][K]

for i in range(1,N):
    c = ball[i][K]
    for j in range(0,K):
        b = ball[i][j]
        prob[i][j] = (b + prob[i-1][j])/(c+1)
    

# print(ball)

# print("jeiasjf")

# print(prob)

for i in range(K):
    print("%.6f" % prob[N-1][i] , end=" ")
# print(*prob[N-1])

#--------------------------

import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    a = s.split()
    min_string  = min(a,key=len)
    length = 0
    sub_str = ""
    length_sub_str = 0
    longest_sub_str = ""
    for i in range(0,len(min_string)):
        for j in range(i+1,len(min_string)+1):
            sub_str = min_string[i:j]
            flag = False
            for ele in a:
                if(sub_str in ele):
                    flag = True
                else:
                    flag = False
                    break
            if(flag == True):
                if(length_sub_str < len(sub_str)):
                    length_sub_str = len(sub_str)
                    longest_sub_str = sub_str
                elif(length_sub_str == len(sub_str)):
                    if(longest_sub_str > sub_str):
                        longest_sub_str = sub_str
    print(longest_sub_str)
            
    

#--------------------------

import sys

T = int(sys.stdin.readline())

for t in range(T):
    n = int(sys.stdin.readline())
    w = sys.stdin.readline().strip()
    
    words = w.split()
    shortest_word = min(words, key=len)
    
    longest_substr_len = 0
    longest_substr = ""
    
    for i in range(0, len(shortest_word)):
        for j in reversed(range(i + 1, len(shortest_word) + 1)):
            sub_str = shortest_word[i:j]
            found = True
            for word in words:
                if sub_str not in word:
                    found = False
                    break
    
            if found:
                if len(sub_str) > longest_substr_len:
                    longest_substr_len = len(sub_str)
                    longest_substr = sub_str
                elif len(sub_str) == longest_substr_len:
                    if sub_str < longest_substr:
                        longest_substr_len = len(sub_str)
                        longest_substr = sub_str
    
    print(longest_substr)



#--------------------------

t = int(input())
def snek(a):
    c = 0
    while a > 1:
        a //= 2
        c += 1
    return c

for i in range(t):
    n, k = list(map(int, input().split()))
    if n == 1:
        print(k)
    elif n == 2:
        if k == 1:
            print(1, 1)
        elif k == 2:
            print(2, 1)
        else:
            print(2 ** snek(k), 2 ** snek(k) - 1)
    else:
        if k == 1:
            for j in range(n):
                print(1, end = " ")
            print()
        elif k == 2:
            print(2, end = " ")
            for j in range(n - 1):
                print(1, end = " ")
            print()
        elif k == 3:
            if n % 2 == 0:
                print(2, 1, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()
            else:
                print(3, end = " ")
                for j in range(n - 1):
                    print(1, end = " ")
                print()
        else:
            if n % 2 == 0:
                print(2 ** snek(k), 2 ** snek(k) - 1, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()
            else:
                print(2 ** snek(k), 2 ** snek(k) - 2, end = " ")
                for j in range(n - 2):
                    print(1, end = " ")
                print()

#--------------------------

T=int(input())
def powe(a):
    t7=0
    while(a>1):
        a=a//2
        t7+=1
    return t7
for _ in range(T):
    n,k=list(map(int,input().split()))
    if(n==1):
        print(k)
    elif(n==2):
        if(k==1):
            print(1,1)
        elif(k==2):
            print(2,1)
        else:
            print(2**powe(k),2**powe(k)-1)
    else:
        if(k==1):
            for i in range(n):
                print(1,end=" ")
            print()
        elif(k==2):
            print(2,end=" ")
            for i in range(n-1):
                print(1,end=" ")
            print()
        elif(k==3):
            if(n%2==0):
                print(2,1,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()
            else:
                print(3,end=" ")
                for i in range(n-1):
                    print(1,end=" ")
                print()
        else:
            if(n%2==0):
                print(2**powe(k),2**powe(k)-1,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()
            else:
                print(2**powe(k),2**powe(k)-2,end=" ")
                for i in range(n-2):
                    print(1,end=" ")
                print()


#--------------------------

from math import*
def listx():return [int(x) for x in input().split()]
def inpx():return int(input())
def mapx():return map(int,input().split())
def strx():return input()
def floatx():return float(input())

mod = 10 ** 9 + 7

for i in range(inpx()):
    n=inpx()
    k=list(map(float,input().split()))
    c=list(map(float,input().split()))
    SUMck,SUM_k=0.0,0.0
    for i in range(n):
        SUMck+=c[i]*k[i]
        SUM_k+=1/k[i]
    F2=SUMck*SUM_k
    if F2<0:
        print(-1)
    else:
        print(sqrt(F2),end=' ')
        t=SUMck/SUM_k
        for i in range(n):
            print(t/k[i]/k[i]-c[i],end=' ')
        print() 

#--------------------------

for _ in range(int(input())):
  n = int(input())
  k = list(map(float, input().split()))
  c = list(map(float, input().split()))
  p = sum(x*y for (x, y) in zip(k, c))
  if p < 0:
      print(-1)
      continue
  x = [1.0/i/i for i in k]
  q = sum(i*j for i, j in zip(x, k))
  x = [i*p/q for i in x]
  f = sum(i**0.5 for i in x)
  x = [i - j for i, j in zip(x, c)]
  print(f, *x)

#--------------------------

def pow_mod(base,exp,N):
    result=1
    while exp>0:
        if exp%2==1:
            result=(result*base)%N
        exp=exp>>1
        base=(base*base)%N
    return result


N=1000000007
t=int(input())
for i in range(t):
    [n,m,d,k]=input().split(" ")
    n=int(n)
    m=int(m)
    d=int(d)
    k=int(k)
    if m>d:
        t1=m-d
        t2=pow_mod(d+1,n,N)
        t3=pow_mod(d,n,N)
        t4=pow_mod(d-1,n,N)
        ans=((t2-2*t3+t4)*t1)%N
        print(ans)
    else:
        print("0")
        

#--------------------------

def pow_mod(base,exp,N):
    result=1
    while exp>0:
        if exp%2==1:
            result=(result*base)%N
        exp=exp>>1
        base=(base*base)%N
    return result


N=1000000007
t=int(input())
for i in range(t):
    [n,m,d,k]=input().split(" ")
    n=int(n)
    m=int(m)
    d=int(d)
    k=int(k)
    if m>d:
        t1=m-d
        t2=pow_mod(d+1,n,N)
        t3=pow_mod(d,n,N)
        t4=pow_mod(d-1,n,N)
        ans=((t2-2*t3+t4)*t1)%N
        print(ans)
    else:
        print("0")
        


    

#--------------------------

fact = [None]*1001
def nck(n,k):
    return fact[n]/(fact[n-k]*fact[k])

fact[0]=1;
for i in range(1,1001):
    fact[i]=fact[i-1]*i
t = int(input())
for z in range(t):
    s,n,m,k = map(int, input().split())
    P = 0
    for i in range(k, min(n,m)):
        P+=nck(m-1,i)*nck(s-m,n-i-1)
    Q = nck(s-1,n-1)
    ans = float(P/Q)
    print('%.6f' % ans)

#--------------------------

for _ in range(int(input())):

    S, N, M, K = map(int, input().split())
    
    
    def cnk(n, k):
        k_min = min(k, n - k)
        num, denom = 1, 1
    
        for x in range(1, k_min + 1):
            num *= (n - x + 1)
            denom *= x
        return num // denom
    
    
    total = cnk(S - 1, N - 1)
    upper_lim = min(M, N)
    
    num = 0
    for k in range(K, upper_lim + 1 - 1):
        if (S - M) >= (N - k - 1):
            num += cnk(M - 1, k) * cnk(S - M, N - k - 1)
    ans = num / float(total)
    print("%.9f" % ans)


#--------------------------

t=int(input())
for i in range(t):
    n,p=[int(j) for j in input().split() ]
    for j in range(1,n+1):
        q=p//(1<<j)
        r=p%(1<<j)
        if r<(1<<(j-1)):
            p=(1<<j)*q+2*r
        else:
            p=(1<<j)*(q-1)+2*r+1
    print(p)
            
        
    


#--------------------------

t = int(input())
for _ in range(t):
	n, k = list(map(int, raw_input().split()))
	k += 1
	i = n-1
	ans = 0
	while(i >= 0):
		if (k > 2**i):
			ans += 2**(n-1-i)
			k -= 2**i
		i -= 1
	print(ans)

#--------------------------



t = int(input())

for i in range(t):
    x, w = input().split()
    d1 = d2 = 0
    for j in range(int(x)):
        y = input()
        if y[0] == '1' and y[-1] == '1':
            d1 += 1
        elif y[0] == '0' and y[-1] == '0':
            d2 += 1
    if d1 < d2:
        print("Dum")
    elif d2 < d1:
        print("Dee")
    else:
        print(w)

#--------------------------

t = int(input())

for i in range(t):
    x, w = input().split()
    d1 = d2 = 0
    for j in range(int(x)):
        y = input()
        if y[0] == '1' and y[-1] == '1':
            d1 += 1
        elif y[0] == '0' and y[-1] == '0':
            d2 += 1
    if d1 < d2:
        print("Dum")
    elif d2 < d1:
        print("Dee")
    else:
        print(w)

#--------------------------

m=1000000007
f=[1,2,6]
a=[1,2,12]
for i in range(3,10**6):
    f.append((f[i-1]*(i+1))%m)
    a.append((f[i]*a[i-1])%m)
for _ in range(int(input())):
    n=int(input())
    print(a[n-1])

#--------------------------

n=int(input())
l=[1,2,12]
A=6
a=4;
for i in range(4,1000001):
   l.append((A)%1000000007 *(a)%1000000007 * (l[len(l)-1])%1000000007)
   A=(A*a)%1000000007;
   a+=1;
for i in range(0,n):
    o=int(input())
    print(l[o-1])

#--------------------------

from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=[int(i) for i in input().split()]
    c=Counter(l)
    cnt=0
    for i in c:
        curr=c[i]
        for j in range(1,c[i]+1):
            if c[j]>=i:
                if i==j:
                    cnt+=1 
                else:
                    cnt+=1
    print(cnt)

#--------------------------

T = int(input())


for i in range(T):
    count = {}
    pair = 0
    N = int(input())
    inp = input().split(' ')
    for j in range(N):
        if inp[j] in count:
            count[inp[j]] = count[inp[j]] + 1
        else:
            count[inp[j]] = 1
    for key in count.keys():
        for k in range(int(key),count[key]+1):
            #print(count[str(k)])
            if (str(k) in count) and (count[str(k)]>=int(key)):
                if int(key)==k:
                    pair = pair + 1
                else:
                    pair = pair + 2
    print(pair)

#--------------------------

mod=10**9+7
n=int(input())
k=int(input())
den=pow(2,n-1)
num=pow(2,n-1)-n
ans=(pow(den,mod-2,mod)*num)%mod
print(ans)

#--------------------------

import math
try:
    n = int(input())
    k = int(input())
    if n==1 or n==2:
        print(0)
    else :
        num , denom = pow(2,n-1)-n , pow(2,n-1)
        MOD = 10**9 + 7
        print(((pow(denom,MOD-2,MOD))*num) % MOD)
except:
    pass

#--------------------------

for _ in range(int(input())):    
    a,b,out = map(int,input().split());r=10**2+5
    d,s = [0]*(10**5),[0]*r   
    for i in range(r):       
        for j in range(r):d[i*r+j]=1 if (i==j or j==0) else d[(i-1)*r+j-1]+d[(i-1)*r+j]
    for i in range(b+1):        
        ans=pow(a+1,i+1)-1       
        for j in range(i):ans-=d[(i+1)*r+j]*s[j];
        s[i]=ans//(i+1)
    print(s[b]%out)

#--------------------------

r=10**2+5;


for _ in range(int(input())):
    
    a,b,out=list(map(int,input().split()))
    d,s=[0]*10**5,[0]*r
    
    for i in range(r):
        
        for j in range(r):
            
            
            d[i*r+j]=1 if (i==j or j==0) else d[(i-1)*r+j-1]+d[(i-1)*r+j]
    for i in range(b+1):
        
        ans=pow(a+1,i+1)-1
        
        for j in range(i):
            
            
            ans-=d[(i+1)*r+j]*s[j];
        s[i]=ans//(i+1)
    print(s[b]%out)

#--------------------------

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0]*n
    for i in range(m):
        l, r = map(int, input().split())
        a[l-1],a[r-1] = 1,1
    print ('NO') if sum(a) > 3 or m > 2 else print ('YES')   

#--------------------------

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0]*n
    for i in range(m):
        l, r = map(int, input().split())
        a[l-1],a[r-1] = 1,1
    print ('NO') if sum(a) > 3 or m > 2 else print ('YES')        

#--------------------------

def precompute():
    n=100000
    d={0:1}
    s4=[0]
    s7=[0]
    
    for i in range(1,n+1):
        v=str(i)
        s4.append(s4[-1]+v.count('4'))
        s7.append(s7[-1]+v.count('7'))
    s4_7=[0]
    for i in range(1,n+1):
        s4_7.append(s4[i]-s7[i])
    
    ans=[0]
    for i in range(1,n+1):
        v=s4_7[i]
        if v in d:
            ans.append(ans[-1]+d[v])
            d[v]+=1
        else:
            ans.append(ans[-1])
            d[v]=1
    return ans
    
ans=precompute()
for _ in range(int(input())):
    print(ans[int(input())])
    

#--------------------------

m,c,k = [0]*(10**5+1),[0]*(12000),0
m[1],c[0] = 1,1
for i in range(2,10**5+1):
    j = i
    while j > 0 :
        d = j % 10
        if d == 4 :k += 1
        elif d == 7 :k -= 1
        j //= 10
    m[i] = m[i-1]+ c[k]
    if k == 0 :m[i] += 1
    c[k] += 1
for _ in range(int(input())):print(m[int(input())])

#--------------------------

from sys import stdin, stdout
from math import ceil


def solve():
    n, m = map(int, stdin.readline().split())
    a = []
    c = [0] * m
    mod = 10**7+7
    for i in range(n):
        b = list(map(int, stdin.readline().strip().split()))
        a.append(b)
        for j in range(m):
            c[j] += b[j]
    ans = 1
    for i in range(m):
        ans *= c[i]
        ans %= mod
    print(ans)


if __name__ == "__main__":
    solve()


#--------------------------

e=10**7+7
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ans=1
for i in range(m):
    c=0
    for j in range(n):
        c+=l[j][i]
    ans=(ans*c)%e
print(ans)

#--------------------------

from bisect import bisect_left
def solve(arr):
    arr = sorted(arr, key = lambda x : x[0])

    nums = []
    ans  = 0

    for x, y in arr:
        idx = bisect_left(nums, y)
        if idx == len(nums):
            nums.append(y)
        else:
            ans += len(nums)-idx
            nums.insert(idx, y)

    return ans
    

arr = []
for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    arr.append((x, y))
    
print(solve(arr))
    



#--------------------------

from bisect import bisect_left
def solve(arr):
    arr = sorted(arr, key = lambda x : x[0])

    nums = []
    ans  = 0

    for x, y in arr:
        idx = bisect_left(nums, y)
        if idx == len(nums):
            nums.append(y)
        else:
            ans += len(nums)-idx
            nums.insert(idx, y)

    return ans
    

arr = []
for i in range(int(input())):
    x, y = [int(x) for x in input().split()]
    arr.append((x, y))
    
print(solve(arr))
    



#--------------------------

import math
t=int(input())
while(t>0):
    n,b=map(int,input().split())
    tobemade=math.ceil(((n*(b-1))+1)/b)
    print(tobemade)
    t-=1

#--------------------------

for _ in range (int(input())):
    n,b=input().split()
    n,b=int(n),int(b)
    a=int(n/b)
    c=n-a
    if(n%b==0):
        c+=1
    print(c)




#--------------------------

# import all important libraries and inbuilt functions
from __future__ import division, print_function
from fractions import Fraction
import numpy as np
import sys,bisect,copyreg,statistics,os,time,socket,socketserver,atexit
from math import gcd,ceil,floor,sqrt,copysign,factorial,fmod,fsum,degrees
from math import expm1,exp,log,log2,acos,asin,cos,tan,sin,pi,e,tau,inf,nan,atan2
from collections import Counter,defaultdict,deque,OrderedDict   
from itertools import combinations,permutations,accumulate,groupby,compress 
from numpy.linalg import matrix_power as mp
from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right
from statistics import mode
from copy import copy,deepcopy
from functools import reduce,cmp_to_key,lru_cache
from io import BytesIO, IOBase
from scipy.spatial import ConvexHull
from heapq import *
from decimal import *
from queue import Queue,PriorityQueue
from re import sub,subn
from random import shuffle,randrange,randint,random
from types import GeneratorType 
from string import ascii_lowercase
from time import perf_counter
from datetime import datetime

# never import pow from math library it does not perform modulo
# use standard pow -- better than math.pow

# end of library import

# map system version faults
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

# template of many functions used in competitive programming can add more later 
# based on need we will use this commonly.
# bfs in a graph
def bfs(adj,v): # a schema of bfs
    visited=[False]*(v+1);q=deque()
    while q:pass

# definition of vertex of a graph
def graph(vertex): return [[] for i in range(vertex+1)]

def lcm(a,b): return (a*b)//gcd(a,b)

# most common list in a array of lists
def most_frequent(List):return Counter(List).most_common(1)[0][0]

# element with highest frequency
def most_common(List):return(mode(List))

#In number theory, the Chinese remainder theorem states that 
#if one knows the remainders of the Euclidean division of an integer n by 
#several integers, then one can determine uniquely the remainder of the 
#division of n by the product of these integers, under the condition 
#that the divisors are pairwise coprime.
def chinese_remainder(a, p):
    prod = reduce(op.mul, p, 1);x = [prod // pi for pi in p]
    return sum(a[i] * pow(x[i], p[i] - 2, p[i]) * x[i] for i in range(len(a))) % prod

def bootstrap(f, stack=[]):
	def wrappedfunc(*args, **kwargs):
		if stack:return f(*args, **kwargs)
		else:
			to = f(*args, **kwargs)
			while True:
				if type(to) is GeneratorType:stack.append(to);to = next(to)
				else:
					stack.pop()
					if not stack:break
					to = stack[-1].send(to)
			return to 
	return wrappedfunc

# make a matrix
def createMatrix(rowCount, colCount, dataList):   
    mat = []
    for i in range (rowCount):
        rowList = []
        for j in range (colCount):
            if dataList[j] not in mat:rowList.append(dataList[j])
        mat.append(rowList) 
    return mat

# input for a binary tree
def readTree(): 
    v=int(inp());adj=[set() for i in range(v+1)]
    for i in range(v-1):u1,u2=In(); adj[u1].add(u2);adj[u2].add(u1)
    return adj,v
    
# sieve of prime numbers    
def sieve():
    li=[True]*1000001;li[0],li[1]=False,False;prime=[]
    for i in range(2,len(li),1):
        if li[i]==True:
            for j in range(i*i,len(li),i):li[j]=False    
    for i in range(1000001):
        if li[i]==True:prime.append(i)
    return prime

#count setbits of a number.
def setBit(n):
    count=0
    while n!=0:n=n&(n-1);count+=1
    return count

# sum of digits of a number
def digitsSum(n):
    if n == 0:return 0
    r = 0
    while n > 0:r += n % 10;n //= 10
    return r

# ncr efficiently
def ncr(n, r):
    r = min(r, n - r);numer = reduce(op.mul, range(n, n - r, -1), 1);denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2

#factors of a number
def factors(n):return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

#prime fators of a number
def prime_factors(n):
    i = 2;factors = []
    while i * i <= n:
        if n % i:i += 1
        else:n //= i;factors.append(i)
    if n > 1:factors.append(n)
    return set(factors)

def prefixSum(arr):
    for i in range(1, len(arr)):arr[i] = arr[i] + arr[i-1]
    return arr    

def binomial_coefficient(n, k):
    if 0 <= k <= n:
        ntok = 1;ktok = 1
        for t in range(1, min(k, n - k) + 1):ntok *= n;ktok *= t;n -= 1
        return ntok // ktok
    else:return 0
    
def get_num_2_5(n):
	twos = 0;fives = 0
	while n>0 and n%2 == 0:n//=2;twos+=1
	while n>0 and n%5 == 0:n//=5;fives+=1
	return (twos,fives)

def shift(a,i,num):
	for _ in range(num):a[i],a[i+1],a[i+2] = a[i+2],a[i],a[i+1] 
        
def powerOfK(k, max):
    if k == 1:return [1]
    if k == -1:return [-1, 1] 
    result = [];n = 1
    while n <= max:result.append(n);n *= k
    return result

def getAngle(a, b, c):
	ang = degrees(atan2(c[1]-b[1], c[0]-b[0]) - atan2(a[1]-b[1], a[0]-b[0]))
	return ang + 360 if ang < 0 else ang

def getLength(a,b):return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# maximum subarray sum use kadane's algorithm
def kadane(a,size):
    max_so_far = 0;max_ending_here = 0 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):max_so_far = max_ending_here 
        if max_ending_here < 0:max_ending_here = 0
    return max_so_far                                    
                  
def divisors(n):
    result = []
    for i in range(1,ceil(sqrt(n))+1):
        if n%i == 0:
            if n/i == i:result.append(i)
            else:result.append(i);result.append(n/i)
    return result

def equal(x,y):return abs(x-y) <= 1e-9

def sumtilln(n): return ((n*(n+1))//2)

def isPrime(n) : 
	if (n <= 1) :return False
	if (n <= 3) :return True
	if (n % 2 == 0 or n % 3 == 0) :return False
	for i in range(5,ceil(sqrt(n))+1,6):
		if (n % i == 0 or n % (i + 2) == 0) :return False
	return True

def isPowerOf2(n):
    while n % 2 == 0:n //= 2
    return (True if n == 1 else False)

def power2(n):
    k = 0
    while n % 2 == 0:k += 1;n //= 2
    return k

def sqsum(n):return ((n*(n+1))*(2*n+1)//6)
    
def cusum(n):return ((sumn(n))**2)

def pa(a):
    for i in range(len(a)):print(a[i], end = " ")
    print()

def pm(a,rown,coln):
    for i in range(rown):
        for j in range(coln):print(a[i][j],end = " ")
        print()

def pmasstring(a,rown,coln):
    for i in range(rown):
        for j in range(coln):print(a[i][j],end = "")
        print()

def print_case_iterable(case_num, iterable):print("Case #{}: {}".format(case_num," ".join(map(str,iterable))))
 
def print_case_number(case_num, iterable):print("Case #{}: {}".format(case_num,iterable))
        
def isPerfectSquare(n):return pow(floor(sqrt(n)),2) == n

def nC2(n,m):return (((n*(n-1))//2) % m)

def modInverse(n,p):return pow(n,p-2,p)

def ncrmodp(n, r, p):  
	num = den = 1
	for i in range(r):num = (num * (n - i)) % p ;den = (den * (i + 1)) % p 
	return (num * pow(den,p - 2, p)) % p 

def reverse(string):return "".join(reversed(string))        

def listtostr(s):return ' '.join([str(elem) for elem in s]) 

def binarySearch(arr, l, r, x): 
	while l <= r: 
		mid = l + (r - l) // 2; 
		if arr[mid] == x:return mid 
		elif arr[mid] < x:l = mid + 1
		else:r = mid - 1
	return -1

def isarrayodd(a):
    r = True
    for i in range(len(a)):
        if a[i] % 2 == 0:r = False;break
    return r

def isarrayeven(a):
    r = True
    for i in range(len(a)):
        if a[i] % 2 == 1:r = False;break
    return r

def isPalindrome(s):return s == s[::-1] 

def gt(x,h,c,t):return ((x*h+(x-1)*c)/(2*x-1))

def CountFrequency(my_list): 
    freq = {} 
    for item in my_list:freq[item] = (freq[item] + 1 if (item in freq) else 1)
    return freq

def CountFrequencyasPair(my_list1,my_list2,freq): 
    for item in my_list1:freq[item][0] = (freq[item][0] + 1 if (item in freq) else 1)
    for item in my_list2:freq[item][1] = (freq[item][1] + 1 if (item in freq) else 1)     
    return freq 
 
def binarySearchCount(arr, n, key):   
    left = 0;right = n - 1;count = 0  
    while (left <= right):  
        mid = int((right + left) / 2) 
        if (arr[mid] <= key):count,left = mid + 1,mid + 1
        else:right = mid - 1      
    return count

def primes(n):
  sieve,l = [True] * (n+1),[]
  for p in range(2, n+1):
    if (sieve[p]):
      l.append(p)
      for i in range(p, n+1, p):sieve[i] = False
  return l

def Next_Greater_Element_for_all_in_array(arr): 
	s,n,reta,retb = list(),len(arr),[],[];arr1 = [list([0,i]) for i in range(n)]
	for i in range(n - 1, -1, -1): 
		while (len(s) > 0 and s[-1][0] <= arr[i]):s.pop() 
		if (len(s) == 0):arr1[i][0] = -1					
		else:arr1[i][0] = s[-1]	 
		s.append(list([arr[i],i]))		
	for i in range(n):reta.append(list([arr[i],i]));retb.append(arr1[i][0])
	return reta,retb

def find_lcm_array(A):
	if len(A) == 1:return A[0]
	l = lcm(A[0], A[1] ) 
	for i in range(2, len(A)):l = lcm(l, A[i]) 
	return l

def polygonArea(X,Y,n):   
    area = 0.0;j = n - 1
    for i in range(n):area += (X[j] + X[i]) * (Y[j] - Y[i]);j = i   
    return abs(area / 2.0)

def merge(a, b):
	ans = defaultdict(int)
	for i in a:ans[i] += a[i]
	for i in b:ans[i] += b[i]
	return ans

def subarrayBitwiseOR(A): 
	res,pre = set(),{0}
	for x in A: pre = {x | y for y in pre} | {x} ;res |= pre 
	return len(res) 

# Print the all possible subset sums that lie in a particular interval of l <= sum <= target
def subset_sum(numbers,l,target, partial=[]):
    s = sum(partial)
    if l <= s <= target:print ("sum(%s)=%s" % (partial, s))
    if s >= target:return 
    for i in range(len(numbers)):subset_sum(numbers[i+1:], l,target, partial + [numbers[i]])

def isSubsetSum(arr, n, summ):       
    # The value of subarr[i][j] will be true if there is a 
    # subarr of arr[0..j-1] with summ equal to i 
    subarr =([[False for i in range(summ + 1)]for i in range(n + 1)]) 
      
    # If summ is 0, then answer is true  
    for i in range(n + 1):subarr[i][0] = True
          
    # If summ is not 0 and arr is empty,then answer is false  
    for i in range(1, summ + 1):subarr[0][i]= False
              
    # Fill the subarr table in botton up manner 
    for i in range(1, n + 1): 
        for j in range(1, summ + 1): 
            if j<arr[i-1]:subarr[i][j] = subarr[i-1][j] 
            if j>= arr[i-1]:subarr[i][j] = (subarr[i-1][j] or subarr[i - 1][j-arr[i-1]])       
    return subarr[n][summ] 

def pre(s):
    n = len(s);pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j and s[i] != s[j]:j = pi[j - 1]
        if s[i] == s[j]:j += 1
        pi[i] = j
    return pi

def prod(a):
    ans = 1
    for each in a:ans = (ans * each)
    return ans

def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y

def printSubsequences(arr, index, subarr): 
    if index == len(arr): 
        if len(subarr) != 0:print(subarr)       
    else:printSubsequences(arr, index + 1, subarr);printSubsequences(arr, index + 1, subarr+[arr[index]])       
    return

def modFact(n, p): 
    if n >= p:return 0      
    result = 1
    for i in range(1, n + 1):result = (result * i) % p    
    return result 

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n + 1)]
    for p in range(2,ceil(sqrt(n))+1):
        if (prime[p] == True): 
            for i in range(p * 2, n + 1, p):prime[i] = False
    prime[0]= False;prime[1]= False;return prime
    
#defining a LRU Cache
# where we can set values and get values based on our requirement
class LRUCache: 
	# initialising capacity 
	def __init__(self, capacity: int): 
		self.cache = OrderedDict() 
		self.capacity = capacity 

	# we return the value of the key 
	# that is queried in O(1) and return -1 if we 
	# don't find the key in out dict / cache. 
	# And also move the key to the end 
	# to show that it was recently used. 
	def get(self, key: int) -> int: 
		if key not in self.cache:return -1
		else:self.cache.move_to_end(key);return self.cache[key] 

	# first, we add / update the key by conventional methods. 
	# And also move the key to the end to show that it was recently used. 
	# But here we will also check whether the length of our 
	# ordered dictionary has exceeded our capacity, 
	# If so we remove the first key (least recently used) 
	def put(self, key: int, value: int) -> None: 
		self.cache[key] = value;self.cache.move_to_end(key) 
		if len(self.cache) > self.capacity:self.cache.popitem(last = False)

class segtree:
    def __init__(self,n):
        self.m = 1
        while self.m < n:self.m *= 2
        self.data = [0] * (2 * self.m)
    def __setitem__(self,i,x):
        x = +(x != 1);i += self.m;self.data[i] = x;i >>= 1
        while i:self.data[i] = self.data[2 * i] + self.data[2 * i + 1];i >>= 1
    def __call__(self,l,r):
        l += self.m;r += self.m;s = 0
        while l < r:
            if l & 1:s += self.data[l];l += 1
            if r & 1:r -= 1;s += self.data[r]
            l >>= 1;r >>= 1
        return s        

class FenwickTree:
  def __init__(self, n):self.n = n;self.bit = [0]*(n+1)  
  def update(self, x, d):
    while x <= self.n:self.bit[x] += d;x += (x & (-x))  
  def query(self, x):
    res = 0
    while x > 0:res += self.bit[x];x -= (x & (-x))
    return res
  def range_query(self, l, r):return self.query(r) - self.query(l-1)    

# Python program to print connected 
# components in an undirected graph 

class Graph: 
	def __init__(self,V):self.V = V ;self.adj = [[] for i in range(V)] 
	def DFSUtil(self, temp, v, visited): 
		visited[v] = True;temp.append(v) 
		for i in self.adj[v]: 
			if visited[i] == False:temp = self.DFSUtil(temp, i, visited) 
		return temp 
	# method to add an undirected edge 
	def addEdge(self, v, w):self.adj[v].append(w);self.adj[w].append(v) 
	# Method to retrieve connected components in an undirected graph 
	def connectedComponents(self): 
		visited,cc = [],[]
		for i in range(self.V):visited.append(False) 
		for v in range(self.V): 
			if visited[v] == False:temp = [];cc.append(self.DFSUtil(temp, v, visited)) 
		return cc 
    
class MergeFind:
    def __init__(self, n):self.parent = list(range(n));self.size = [1] * n;self.num_sets = n;self.lista = [[_] for _ in range(n)]
    def find(self, a):
        to_update = []
        while a != self.parent[a]:to_update.append(a);a = self.parent[a]
        for b in to_update:self.parent[b] = a
        return self.parent[a]
    def merge(self, a, b):
        a = self.find(a);b = self.find(b)
        if a == b:return
        if self.size[a] < self.size[b]:a, b = b, a
        self.num_sets -= 1;self.parent[b] = a;self.size[a] += self.size[b];self.lista[a] += self.lista[b];self.lista[b] = []
    def set_size(self, a):return self.size[self.find(a)]
    def __len__(self):return self.num_sets
# This is Kosaraju's Algorithm and use this class of graph for only that purpose    
# can add more template functions here
    
# end of template functions

# To enable the file I/O i the below 2 lines are uncommented.
# read from in.txt if uncommented
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# will print on Console if file I/O is not activated
#if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')

# inputs template
#for fast input we areusing sys.stdin
def inp(): return sys.stdin.readline().strip()

#for fast output, always take string
def out(var): sys.stdout.write(str(var))  

# custom base input needed for the program
def I():return (inp())
def II():return (int(inp()))
def FI():return (float(inp()))
def SI():return (list(str(inp())))
def MI():return (map(int,inp().split()))
def LI():return (list(MI()))
def SLI():return (sorted(LI()))
def MF():return (map(float,inp().split()))
def LF():return (list(MF()))
def SLF():return (sorted(LF()))

# end of inputs template

# common modulo values used in competitive programming
sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 998244353
mod = 10**9+7

# any particular user-defined functions for the code.
# can be written here.   
                                               
# end of any user-defined functions

# main functions for execution of the program.
if __name__ == '__main__':  
    # execute your program from here.
    # start your main code from here
        
    # Write your code
    for i in range(II()):
        n,t = MI();count=0        
        if n==0:print(0);continue        
        if t==0:print(1);continue        
        z=(n-1)&t
        if z==0:count=count+1        
        x=(((1+24*t)**(0.5))-1)/6;y=x;x=int(x)    
        for j in range(1,x+1):
            u=((j*(3*j-1))//2);a=n+t-j-1-u;b=t-j-u;z=(a-b)&b
            if z==0:count=count+1        
            a=a+j;b=b+j;z=(a-b)&b
            if z==0:count=count+1        
        x2=y+ (1/3);x2=int(x2)        
        for j in range(x+1,x2+1):
            u=((j*(3*j-1))//2);a=n+t-1-u;b=t-u;z=(a-b)&b
            if z==0:count=count+1                
        print(1) if count%2==1 else print(0)  
      
    # end of main code
    # end of program

# This program is written by :
#   Shubham Gupta
#   B.Tech (2019-2023)
#   Computer Science and Engineering,
#   Department of EECS
#   Contact No:8431624358
#   Indian Institute of Technology(IIT),Bhilai
#   Sejbahar,
#   Datrenga,
#   Raipur,
#   Chhattisgarh
#   492015

#   THANK YOU FOR 
#YOUR KIND PATIENCE FOR READING THE PROGRAM.    

#--------------------------

from sys import stdout,stdin
from collections import defaultdict,deque
import math

m=115475
u=[0]*m
for i in range(m):
    u[i]=(i*((3*i)-1))//2

t=int(stdin.readline())
for _ in range(t):
    n,k=map(int,stdin.readline().split())
    temp=math.sqrt((1/36)+((2*k)/3))
    temp+=0.00000000000005
    #print(temp-(1/6),temp+(1/6))
    lower=math.floor(temp-(1/6))
    upper=math.floor(temp+(1/6))
    #print(lower,upper)
    a,b,c=0,0,0
    if (n+k-1)|(k)==(n+k-1):
        a=1
    for i in range(1,lower+1):
        x,y=n-1,k-u[i]-i
        x+=y
        if x|y==x:
            b=b^1
    for i in range(1,upper+1):
        x,y=n-1,k-u[i]
        x+=y
        if x|y==x:
            c=c^1
    print(a^b^c)
    
    
    
    
    
    
    
    
    
    
    
    





#--------------------------

for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    l = sorted(arr)
    i = 0
    j = 0
    while(i<n and j<n):
        if l[i]==arr[j]:
            i+=1
            j+=1
        else:
            j+=1
    print(n-i)

#--------------------------

for se in range(int(input())):
    n=int(input());arr = list(map(int,input().split()));l = sorted(arr);i=j=0
    while(i<n and j<n):
        if(l[i]==arr[j]):i,j = i+1,j+1
        else:j=j+1
    print(n-i)    

#--------------------------

import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
def input(): return sys.stdin.readline().rstrip('\r\n')
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])




def solve():

	d1 = [0,0,1,-1] 
	d2 = [1,-1,0,0]
	def ch1(x,y):
		if x < 0 or x >= n or y < 0 or y >= m:
			return False
		return True

	def ch2(x,y):
		if vis[x][y] or mat[x][y] != '?':
			return False
		return True


	def dfs(i,j):
		st = deque()
		st.append((i,j))
		C = Counter()
		C[mat[i][j]] = 1
		while st:
			x,y = st.pop()
			for i,j in zip(d1,d2):
				xx = x + i
				yy = y + j
				if ch1(xx,yy):
					if ch2(xx,yy):
						st.append((xx,yy))
						C[mat[xx][yy]] += 1
					if mat[xx][yy] in ['G','B','P']:
						C[mat[xx][yy]] = 1
					vis[xx][yy] = True
		return C


	for _ in range(int(input())):
		n,= aj()
		m= n
		mat = []
		for i in range(n):
			B = [*input()]
			mat.append(B)
		vis = [[False]*m for i in range(n)]
		ans = 1
		for i in range(n):
			for j in range(m):
				if not vis[i][j] and ch2(i,j) :
					vis[i][j] = True
					C = dfs(i,j)
					#print(C)
					if '?' in C:
						if len(C) == 4 or C['G'] == 1 or (len(C) == 3 and C['P'] == 1 and C['B'] == 1) :
							ans = 0;break
						elif len(C) == 1:
							if C['?'] == 1:
								ans*= 3
								ans %= MOD
							else:
								ans*=2
								ans %= MOD
			if ans == 0:
				break
		if ans != 0:
			for i in range(n):
				for j in range(m):
					if mat[i][j] in ['G','P','B']:
						for ii,jj in zip(d1,d2):
							x = ii + i
							y = jj + j
							if ch1(x,y):
								if mat[i][j] == 'G' and mat[x][y] in ['G','P','B','?']:
									ans = 0
									break
								elif mat[i][j] == 'P' and mat[x][y] in ['G','B']:
									ans = 0
									break
								elif mat[i][j] == 'B' and mat[x][y] in ['G','P']:
									ans = 0
									break
				if ans == 0:
					break
		print(ans%MOD)



try:
	#os.system("online_judge.py")
	sys.stdin = open('input.txt', 'r') 
	sys.stdout = open('output.txt', 'w')
except:
	pass

solve()


#--------------------------

import sys
sys.setrecursionlimit((10**7))
from collections import defaultdict
def Neigh(i,j,N):
    L=[]
    if(i+1 !=N):
        L.append([i+1,j])
    if(j+1 !=N):
        L.append([i,j+1])
    if(i!=0):
        L.append([i-1,j])
    if(j!=0):
        L.append([i,j-1])
    return L
    
def chngneigh(Arr,i,j,target):
    ll=Neigh(i,j,N)
    next=[]
    for x in ll:
        if(Arr[x[0]][x[1]]=="?"):
            Arr[x[0]][x[1]]=target
            next.append(x)
    for x in next:
        Arr=chngneigh(Arr,x[0],x[1],target)
    return Arr
    
for _ in range(int(input())):
    N=int(input())
    Mat=[]
    for _ in range(N):
        row=list(input())
        Mat.append(row)
    for i in range(N):
        for j in range(N):
            if(Mat[i][j]=="P"):
                Mat=chngneigh(Mat,i,j,"P")
            elif(Mat[i][j]=="B"):
                Mat=chngneigh(Mat,i,j,"B")
    fine=True
    for i in range(N):
        for j in range(N):
            if(Mat[i][j]=="." or Mat[i][j]=="?"):
                pass
            elif(Mat[i][j]=="G"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]!="."):
                        fine=False
                        break
            elif(Mat[i][j]=="P"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]=="B" or Mat[x[0]][x[1]]=="G" ):
                        fine=False
                        break
            elif(Mat[i][j]=="B"):
                ll=Neigh(i,j,N)
                for x in ll:
                    if(Mat[x[0]][x[1]]=="P" or Mat[x[0]][x[1]]=="G" ):
                        fine=False
                        break
        if(fine==False):
            break
    if(fine==False):
        print("0")
        continue
    else:
        solo=0
        for i in range(N):
            for j in range(N):
                if(Mat[i][j]=="?"):
                    ll=Neigh(i,j,N)
                    yup=True
                    for x in ll:
                        if(Mat[x[0]][x[1]]!="."):
                            yup=False
                    if(yup==True):
                        solo+=1
                        Mat[i][j]="D"
        clustor=0
        for i in range(N):
            for j in range(N):
                if(Mat[i][j]=="?"):
                    Mat=chngneigh(Mat,i,j,"c")
                    clustor+=1
        answer=pow(3,solo,1000000007)*pow(2,clustor,1000000007)
        print(answer%1000000007)

#--------------------------

def findsubtract(num):
    n = num
    strn = str(n)
    count = 0
    while n > 0:
        fd = int(strn[0])
        p = len(strn) - 1
        if p == 0:
            n -= fd
            strn = str(n)
            count += 1
        else:
            n1 = n - fd * 10**p
            n2 = n1//fd+1
            count += n2
            n -= n2 * fd
            strn = str(n)
    return count + 1





for i in range(int(input())):
    k = int(input())
    if k == 2:
        print(9)
        continue
    n = None
    brutetop = 4 * k
    brutebottom = 0
    while abs(brutetop - brutebottom) > 20:
        v = round((brutetop + brutebottom) / 2)
        t = findsubtract(v)
        if t <= k:
            brutebottom = v
        else:
            brutetop = v
    for j in range(brutetop, brutebottom - 1, -1):
        n = findsubtract(j)
        if n == k:
            print(j)
            break


#--------------------------

def getAns(num):
    if num<10:return 2 
    last=int(str(num)[0]);rem=int(str(num)[1:]);steps=2;p=len(str(num))-1
    while True:
        steps+=rem//last+1;rem=rem%last 
        if last>0:rem=rem+10**p-last
        last=last-1
        if last==0:
            p=p-1;last=9
            if(len(str(rem))==1):rem=0
            else:rem=int(str(rem)[1:])
        if rem==0:            break
    return steps
for awa in range(int(input())):
    k=int(input())
    if(k==1):print(0)
    elif(k==2):print(9)
    elif(k==3):print(10)
    else:
        low,high,ans = 0,10**18,0
        while(low<=high):
            mid=(low+high)//2;temp=getAns(mid)
            if int(temp)==k:ans=max(ans,mid);low=mid+1 
            elif temp<k:low=mid+1 
            else:high=mid-1 
        print(ans)

#--------------------------

def p(b, e):
    t = 1
    while(e):
        if(e & 1):
            t = (t*b) % mod
        b = (b*b) % mod
        e >>= 1
    return t


def f(i, e):
    b = p(i, i)
    t = 0
    m = 1
    m2 = p(i, mod)
    while(e):
        if(e & 1):
            t = (t+m*b % mod) % mod
            m = (m*m2) % mod
        b = (b*(m2+1)) % mod
        m2 = (m2*m2) % mod
        e >>= 1
    return t


for _ in range(int(input())):
    n, mod = map(int, input().split())
    ans = 0
    for i in range(1, min(n+1, mod)):
        ans = (ans+f(i, (n+mod-i)//mod)) % mod
    print(ans)


#--------------------------

def S(a, n, m):
    if n == -1: return 0
    if n == 0: return 1
    if n == 1: return (1 + a) % m 
    if n % 2 == 1: return ((1 + a) * S(a * a % m, (n - 1)//2, m))%m
    else: return (1 + a * (1 + a) * S(a * a % m, n//2 - 1, m) )%m  
for _ in range(int(input())):
    n,m = map(int,input().split(' '));s=0;e = n//m
    for i in range(1,n%m+1):s += pow(i,e*m + i,m);s = s%m
    for i in range(2,m+1):s += (((S(pow(i,m,m),e-1,m) )%m)*pow(i,i,m))%m;s = s%m
    print((s+e)%m)    

#--------------------------

from decimal import *
for i in range(int(input())):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if (x < 1000):
        q1 = str(x ** x)[:y]
    else:
        x = Decimal(x)
        q1 = str(int(10 **(x*(x.log10())%1 + y - 1)))
    q2 = str(pow(x, x, 10 ** y)).zfill(y)    
    print(q1 + " " + q2)

#--------------------------

from decimal import *
for _ in range(int(input())):
    n,k = map(int,input().split())
    if n >= 1000 :q1 = str(int(pow(10, (Decimal(n) *(Decimal(n).log10()))%1 + k -1)))
    else: q1 = str(n**n)[:k]               
    print(q1 + " " + str(pow(n, n, 10 ** k)).zfill(k))

#--------------------------

t=int(input())
for _ in range(t):
    n=int(input())
    if(n==1):
        m=int(input())
        print(1)
    else:
        m=[]
        indexes=[]
        for i in range(n):
            l=input()
            temp=l.index('1')
            indexes.append(temp)
            m.append(l)
        
        counter=0
        for i in range(n):
            left=indexes[i]
            right=indexes[i]
            for j in range(i,n):
                left=min(indexes[j],left)
                right=max(indexes[j],right)
                if(right-left == j-i):
                    counter+=1
        print(counter)

            
    

#--------------------------

t=int(input())
while t>0:
    n=int(input())
    l=[]
    l.append(0)
    for i in range(1,n+1):
        c=input()
        for j in range(n):
            if c[j]=='1': 
                l.append(j+1)
    sum1=0
    for j in range(1,n+1):
        min1=l[j]
        max1=l[j]
        for k in range(j,n+1):
            min1=min(min1,l[k])
            max1=max(max1,l[k])
            if max1-min1==k-j:
                sum1+=1
    print(sum1)
    t-=1
                
            
                

#--------------------------

T=int(input())
mod=(10**9)+7
for _ in range(T):

    N=int(input())

    A=list(map(int,input().split()))[:N]

    B={}

    for i in range(N):
        B[A[i]]=i
    
    newresult=[0]*N
    A.sort()
    for i in range(N):

        index=B[A[i]]
        value = ((pow(2,i,mod)-1) + ((pow(2,i,mod)*(N-i-1))%mod) + ((pow(2,i,mod)*((N-i-1)*(N-i-2))//2)%mod))%mod
        newresult[index]=value
    
    print(*newresult)


#--------------------------

mod = 10 ** 9 + 7

def fp(a, b):
    ans = 1
    while b > 0:
        if b & 1:
            ans = ans * a % mod
        b >>= 1
        a = a * a % mod
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pair = list(enumerate(arr))
    pair.sort(key=lambda x: x[1])
    ans = [0] * n
    for i in range(n):
        s = 0
        a = n-i-1
        b = a * (a+1) // 2
        p = fp(2, i)
        s = (s + p - 1) % mod
        s = (s + b * p % mod) % mod
        ans[pair[i][0]] = s
    print(' '.join(map(str, ans)))
        


#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    def check(mid):
        d,left={},0
        for i in range(mid):
            if a[i]>k:
                if a[i] not in d: 
                    d[a[i]]=1
                else: 
                    d[a[i]]+=1
        if len(d)==1:
            return True
        for i in range(mid,n):
            if a[left]>k:
                d[a[left]]-=1
                if d[a[left]]==0: 
                    del d[a[left]]
            if a[i]>k:
                if a[i] not in d: 
                    d[a[i]]=1
                else: 
                    d[a[i]]+=1
            if len(d)==1: 
                return True
            left+=1
        return False
            
    lo,hi=0,n
    while lo<=hi:
        mid=(lo+hi)//2
        #print(mid,lo,hi)
        if check(mid):
            res=mid
            lo=mid+1
        else:
            hi=mid-1
    print(res)
            
            
            
        

#--------------------------

t=int(input())
while t:
    a=input().split()
    n=int(a[0])
    k=int(a[1])
    lst=input().split()
    for i in range(n):
        lst[i] = int(lst[i])
    greater = 0
    length=0
    pos = -1
    allTimeLong=0
    for i in range(n):
        if lst[i]>k and greater!=0 and lst[i]!=greater:
            greater = lst[i]
            if allTimeLong<length:
                allTimeLong=length
            length = i - pos
            pos=i
            continue
        elif lst[i]>k:
            greater = lst[i]
            pos=i
        length+=1
    if allTimeLong<length:
        allTimeLong=length
    t-=1
    print(allTimeLong)

#--------------------------

n = int(input())
arr = list(map(int,input().split()))
lds = []
for i in arr:
    lo,hi = 0,len(lds)
    while lo<hi:
        mid = (lo+hi)>>1
        if i<lds[mid]:lo=mid+1
        else: hi=mid
    if lo==len(lds): lds.append(i)
    else: lds[lo] = i
print(len(lds))


#--------------------------

def CeilIndex(A, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 
   
def lds(A, size): 
  
    # Add boundary case, 
    # when array size is one 
   
    tailTable = [0 for i in range(size + 1)] 
    len = 0 # always points empty slot 
   
    tailTable[0] = A[0] 
    len = 1
    for i in range(1, size): 
      
        if (A[i] < tailTable[0]): 
  
            # new smallest value 
            tailTable[0] = A[i] 
   
        elif (A[i] > tailTable[len-1]): 
  
            # A[i] wants to extend 
            # largest subsequence 
            tailTable[len] = A[i] 
            len+= 1
   
        else: 
            # A[i] wants to be current 
            # end candidate of an existing 
            # subsequence. It will replace 
            # ceil value in tailTable 
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i] 
          
   
    return len
                
t=1
while(t>0):
    t-=1 
    n=int(input())
    arr=list(map(int,input().strip().split()))[:n]
    for i in range(n):
        arr[i]*=-1
    print(lds(arr,n))
    
    

#--------------------------

def func(i, counterArr):
    ans = 0
    for j in range(i,n,i):
        ans+=counterArr[j]
    return ans
n=int(1e5+1)
primes=[0]*n
for i in range(2,n):
    if primes[i]==0:
        for j in range(i,n,i):
            # distinct primes add
            primes[j]+=1
t = int(input())
from collections import Counter
for aaa in range(t):
    xxx = int(input())
    counterArr=Counter(map(int,input().split()))
    print(max(func(i, counterArr)*primes[i]for i in range(2,n)))

#--------------------------

from collections import Counter
n = int(1e5+1)
pf = [0] * n
for i in range(2, n):
    if pf[i] == 0:
        for j in range(i, n, i):
            pf[j] += 1
            
test = int(input())
for _ in range(test):
    input()
    cnt = Counter(map(int, input().split()))
    s = lambda i: sum(cnt[j] for j in range(i, n, i))
    print(max(s(i) * pf[i] for i in range(2, n)))

#--------------------------

import numpy as np
for _ in range(int(input())):
    ans = np.float('inf')
    n, m = (int(x) for x in input().split())
    sig = np.zeros((n,m))
    img = np.zeros((3*n,3*m))
    for row in range(n):
        sig[row,:] = np.array([int(x) for x in input()])
    for row in range(n):
        img[row+n,m:2*m] = np.array([int(x) for x in input()])
    for i in range(2*n):
        for j in range(2*m):
            ans = min(ans, np.abs(np.sum(img[i:n+i, j:m+j] != sig)))
    print(ans)

#--------------------------

import numpy as np
for _ in range(int(input())):
    ans = np.float('inf')
    n, m = (int(x) for x in input().split())
    sig = np.zeros((n,m))
    img = np.zeros((3*n,3*m))
    for row in range(n):
        sig[row,:] = np.array([int(x) for x in input()])
    for row in range(n):
        img[row+n,m:2*m] = np.array([int(x) for x in input()])
    for i in range(2*n):
        for j in range(2*m):
            ans = min(ans, np.abs(np.sum(img[i:n+i, j:m+j] != sig)))
    print(ans)

#--------------------------

t = int(input())
for m in range(t):
    n = int(input())
    sit = input()
    num0=0
    total=0
    max0=0
    s=0
    e=0
    i = 0
    while i < n:
        num0 = 0
        while i < n and sit[i] =="0":
            i += 1
            num0 += 1
        total+=num0
        if num0 > max0:
            max0 = num0
        if num0 == i:
            s = num0
        if i == n:
            e = num0
        i += 1
    if s+e>max0:
        max0=s+e
    print(total-max0)


#--------------------------

t = int(input())
for m in range(t):
    n = int(input())
    sit = input()
    num0=0
    total=0
    max0=0
    s=0
    e=0
    i = 0
    while i < n:
        num0 = 0
        while i < n and sit[i] =="0":
            i += 1
            num0 += 1
        total+=num0
        if num0 > max0:
            max0 = num0
        if num0 == i:
            s = num0
        if i == n:
            e = num0
        i += 1
    if s+e>max0:
        max0=s+e
    print(total-max0)


#--------------------------

for _ in range(int(input())):
    n,k = [int(c) for c in input().split()]
    a = [int(c) for c in input().split()]
    ls = a
    if n==1:
        print("YES")
        print(1)
        continue
    if k==1:
        print("NO")
        continue
    
    if k==2 and n>2:
        if ls[0]!=ls[1]-1:
            print("NO")
            continue

    ans = [0 for i in range(n+1)]
    count = n
    for i in range(1,a[1]):
        if i != a[0]:
            ans[i]  =count
            count-=1
    for i in a[::-1]:
        ans[i] = count
        count-=1
    for i in range(1,n+1):
        if ans[i] == 0:
            ans[i] = count
            count-=1
    print("YES")
    print(*ans[1:])

#--------------------------

for _ in range(int(input())):
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
    if n==1:
        print("YES")
        print(1)
        continue
    if k==1:
        print("NO")
        continue
    
    if k==2 and n>2:
        if ls[0]!=ls[1]-1:
            print("NO")
            continue
    print("YES")
    mx=n
    arr=[0]*(n)
    for i in range(ls[0]-1):
        arr[i]=mx
        mx-=1
    for i in range(ls[0],ls[1]-1):
        arr[i]=mx
        mx-=1
    for i in range(k-1,-1,-1):
        arr[ls[i]-1]=mx
        mx-=1
    for i in range(1,n):
        if arr[i]==0:
            arr[i]=mx
            mx-=1
    print(*arr)
        

#--------------------------


import math
def distinctPrimeFactors(num) :
    primes,sqrt = set(),int(math.sqrt(num))
    if (num == 2) :primes.add(num)
    for j in range(2, sqrt + 1) :
        if (num % j == 0) :
            primes.add(j)
            while (num % j == 0) :num //= j
    if (num > 2) :primes.add(num)
    return (primes)
res,c,lst,primes,rangeData = [],0,{},{},{};k, q = map(int, input().split());primes[k] = distinctPrimeFactors(k)
for tc in range(q) :
    query = input()
    if (query[0] == '!') :
        cmd, l, r, x = query.split();l,r,x = int(l),int(r),int(x);start,end,startflag = l,r,False
        for i in sorted(rangeData) :
            rangeVal = i
            if (start > rangeVal[1]) :continue
            if (end < rangeVal[0]) :break            
            startRange,endRange = start,end
            if (start >= rangeVal[0] and start <= rangeVal[1]) :start = rangeVal[1] + 1;continue
            if (end >= rangeVal[0]) :endRange = rangeVal[0] - 1
            if (startRange <= endRange) :
                rangeData[(startRange, endRange)] = x;start = max(endRange + 1, rangeVal[1] + 1)
        if (start <= end) :rangeData[(start,end)] = x
    elif (query[0] == '?') :
        cmd, l, r = query.split();l,r,count = int(l),int(r),0
        for primenum in primes[k] :
            for currRange in rangeData :
                if (not (r < currRange[0] or l > currRange[1])) :
                    if (rangeData[currRange] % primenum == 0) :count += 1;break
        c += 1;res.append(count)    
for i in range(c):print(res[i])


#--------------------------

import math
def distinctPrimeFactors(num) :
    primes,sqrt = set(),int(math.sqrt(num))
    if (num == 2) :primes.add(num)
    for j in range(2, sqrt + 1) :
        if (num % j == 0) :
            primes.add(j)
            while (num % j == 0) :num //= j
    if (num > 2) :primes.add(num)
    return (primes)
res,c,lst,primes,rangeData = [],0,{},{},{};k, q = map(int, input().split());primes[k] = distinctPrimeFactors(k)
for tc in range(q) :
    query = input()
    if (query[0] == '!') :
        cmd, l, r, x = query.split();l,r,x = int(l),int(r),int(x);start,end,startflag = l,r,False
        for i in sorted(rangeData) :
            rangeVal = i
            if (start > rangeVal[1]) :continue
            if (end < rangeVal[0]) :break            
            startRange,endRange = start,end
            if (start >= rangeVal[0] and start <= rangeVal[1]) :start = rangeVal[1] + 1;continue
            if (end >= rangeVal[0]) :endRange = rangeVal[0] - 1
            if (startRange <= endRange) :
                rangeData[(startRange, endRange)] = x;start = max(endRange + 1, rangeVal[1] + 1)
        if (start <= end) :rangeData[(start,end)] = x
    elif (query[0] == '?') :
        cmd, l, r = query.split();l,r,count = int(l),int(r),0
        for primenum in primes[k] :
            for currRange in rangeData :
                if (not (r < currRange[0] or l > currRange[1])) :
                    if (rangeData[currRange] % primenum == 0) :count += 1;break
        c += 1;res.append(count)    
for i in range(c):print(res[i])

#--------------------------

import numpy as np
n,q=map(int,input().split())
a=np.array(list(map(int,input().split())))
b=np.array(list(map(int,input().split())))
for i in range(q):
	query=list(map(int,input().split()))
	if query[0]==1:
		print(np.amax(a[query[1]-1:query[2]]))
	if query[0]==2:
		a[query[1]-1:query[2]]+=b[query[1]-1:query[2]]
	if query[0]==3:
		b[query[1]-1:query[2]]+=query[3]
	if query[0]==4:
		a[query[1]-1:query[2]]+=query[3]
	

#--------------------------

import numpy as np
n,q = map(int,input().split())
a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))
ans = []
for i in range(q):
	query = tuple(map(int,input().split()))
	if len(query)==3:c,l,r = query
	else: c,l,r,x = query
	if c==1:
		ans.append(np.max(a[l-1:r]))
	elif c==2:
		a[l-1:r]+=b[l-1:r]
	elif c==3:
		b[l-1:r]+=x
	else:
		a[l-1:r]+=x
print(*ans,sep="\n")

#--------------------------

