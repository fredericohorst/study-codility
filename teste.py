

# indices = [1,2,3,4,5,6]
# K = 3
indices = [1,2,3]
K = 2


train = []
test = []
array1 = []
array2 = []
# diff = abs(len(array1) - len(array2))
for i in range(len(indices)):
    if i < K:
        array1 = indices[i:K]
        array2 = indices[K:len(indices)-i]
        if abs(len(array1) - len(array2)) <= 1 and (array1 != [] or array2 != []):
            print(array1)
            print(array2)
            print(abs(len(array1) - len(array2)))
            train.append(str(array1))
            test.append(str(array2))
    # array1.append()
    # array2.append()
    # print(array1)
    # print(array2)
array = (str(train) + str(test))
print(array)

# for i in K:
# teste = indices.pop(-2)
# print(teste)
# array1 = indices[0:K]
# array2 = indices[K:len(indices)]
# tam = abs(len(array1) - len(array2))
# if abs(len(array1) - len(array2)) > 1:


#
# print(array1)
# print(array2)
# print(tam)
# print(array1+array2)

# ([1,2,3],2)
# ([1,2,3,4,5,6],3)