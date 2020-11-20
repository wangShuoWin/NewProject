i = [7,7,7,8,8,8,1,1,1,2,2,3,3,4,4,7,8,9]

a = list(set(i))
print(a)


k = [1,3,4,5]
l = [2,3,6,7]

for f in  l:
    print(f)
    k.append(f)
print(k)
w = list(set(k))
print(w)


def bubbleSort(arr):#冒泡排序
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])

def nine():
    # 九九乘法表

    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(j, i, i * j), end='')
        print()

def Start():
    for i in range(1,10):
        for j in range(1,i+1 ):
            print('*',end='')
        print()


if __name__=="__main__":
   nine()
   Start()