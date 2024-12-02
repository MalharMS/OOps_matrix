# creating a matrix using list by taking input


# matrix = [];
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         element = int(input(""))
#         row.append(element)
#     matrix.append(row)
# print(matrix)


rows1, cols2 = list(map(int, input().split()))

mat1 = []
for i in range(rows1):
    temp_list = list(map(int, input().split()))
    mat1.append(temp_list)
print(mat1)

rows2, cols2 = list(map(int, input().split()))

mat2 = []
for i in range(rows2):
    temp_list = list(map(int, input().split()))
    mat2.append(temp_list)
print(mat2)

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        result[i][j] = mat1[i][j] + mat2[i][j]
        

for r in result:
    print(r)
