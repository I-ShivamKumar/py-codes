#n=list(map(int,input().split(" ")))
#print(n)

# text="This is my first file program"
# file=open("abc.txt",'w')
# file.write(text)
# file.close()

def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)

n=5
print(sum(n))