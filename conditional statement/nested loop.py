# n=int(input(&quot;enterthe num = &quot;))
# fact = 1
# for i in range (1,n+1):
# fact *=i
# print(f&quot;factorial is = {fact}&quot;)

# n=int(input(&quot;enterthe num = &quot;))
# prime = True
# if n&lt;2:
# prime = False
# else:
# for i in range(2,n):
# if n%i==0:
# prime = False
# break
# print(&quot;prime&quot;if prime else &quot;Not Prime&quot;)

# for i in range(10):
# for j in range(10):
# print(i,j)

n= int(input("enter the multiplication num = "))
for i in range (1,n+1):
    print(i)
    for j in range(1,11):
        print(f"{i}x{j}= {i*j}")

