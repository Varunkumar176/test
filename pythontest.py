n=int(input("enter a num :"))
st=""
st1=""
while n>1:
    a=n%2
    n=n//2
    st=st+str(a)
    if n==1:
        st+=str(n)
    r=st[::-1]
for i in r :
    if i=="1":
        st1+="0"
    else:
        st1+="1"
count=0
st2=st1[::-1]
for i in range(len(st2)):
    q=int(st2[i])(2*i)
    count+=q
print(f"compliment num is {count}" )
