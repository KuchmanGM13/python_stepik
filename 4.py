#set


myset1 = set(range(10))          # множество из элементов последовательности
myset2 = set([1, 2, 3, 4, 5])    # множество из элементов списка
myset3 = set('abcd')             # множество из элементов строки
myset4 = set((10, 20, 30, 40))   # множество из элементов кортежа

print(myset1)
print(myset2)
print(myset3)
print(myset4)


fruits = {
    'apple', 'banana', 'cherry', 'avocado', 'pineapple',
    'apricot', 'banana', 'avocado', 'grapefruit',
}



sortfruits = sorted(fruits, reverse=True)
print(*sortfruits, sep='\n')

myset = set()
for i in range(10):
    if i % 2 == 0:
        myset.add('even')
    else:
        myset.add('odd')

print(len(myset))