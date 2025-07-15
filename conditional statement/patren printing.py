# for i in range(5):
#     for j in range(5):
#         print("*",end = '\t')
#     print()

# for i in range(5):
#     for j in range(5):
#         print("*",end = " ")
#     print()


# for i in range(5):
#     for j in range(0,i+1):
#         print(i,end = ' ')
#     print()

# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end = ' ')
#     print()

# a = int(input("enter the size: = "))
# for i in range(a):
#     for spaces in range(a-i-1):
#         print(" ",end = ' \t')
#     for stars in range(2*i-1):
#         print("*",end = '\t')
#     print()

rows = 6
cols = 7
for i in range(rows):
    for j in range(cols):
        if i==0 and j%3!= 0:
            print(" * ", end = '')
        elif i==1 and j%3==0:
             print(" * ", end ='')
        elif i-j ==2:
             print(" * ", end ='')
        elif i-j ==2:
            print(" * ", end='')
        elif i+j ==8:
            print(" * ", end='')
        else:
             print("   ", end ='')
    print()






