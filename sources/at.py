import sys
sys.stdout = open('input.txt', 'w')
print(100000)
for i in range(1, 100001):
    print(i, end=" ")
