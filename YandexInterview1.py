#Для двух массивов целых чисел длины N, для всех K от 1 до N,
#посчитать количество общих чисел на префиксах длины K.
#[1, 2, 3, 4], [0, 2, 1, 3] -> [0, 1, 2, 3]
#[1,2,2,3,4], [2,2,0,1,3] -> [0,1,2,3,4]

arr1 = [1,2,2,3,4]
arr2 = [2,2,0,1,3]
N = len(arr1)

answer = []
#N^2
for i in range(N):
    set1 = set(arr1[:i])
    set2 = set(arr2[:i])
    answer.append(len(set1.intersection(set2)))
print(answer)


hashh = dict()
answer = []
count = 0
#N
for i, j in zip(arr1, arr2):
    if (i, False) in hashh and hashh[(i, False)] > 0:
        count += 1
        answer.append(count)
        hashh[(i, False)]-=1
        continue
    else:
        hashh[(i, True)] = 0
        hashh[(i, True)] += 1

    if (j, True) in hashh and hashh[(j, True)] > 0:
        count += 1
        answer.append(count)
        hashh[(j, True)]-=1
        continue
    else:
        hashh[(j, False)] = 0
        hashh[(j, False)] += 1
    answer.append(count)
print(answer)
