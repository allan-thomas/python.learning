# n,k=6,1
# for i in range(1,n):
#     for j in range(1,n-i,1):
#         print(k, end=' ' )
#         k+=1
#     print()

a =[[1,2,3],[4,5,6],[7,8,-9]]
min = a[0][0]
for i in range(0,3):
    for j in range(0,3):
        if a[i][j]<min:
            min=a[i][j]
print(min)
