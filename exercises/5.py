#For given n attempts, count how many users solved the problem correctly and what percentage of attempts were correct.
n = int(input())

correct_users = set()
correct_attempts = 0


for _ in range(n):
    line = input()
    name, result = line.split(': ')
    
    if result == 'Correct':
        correct_attemps += 1
        correct_users.add(name)

if len(correct_users) == 0:
    print('Вы можете стать первым, кто решит эту задачу"')
else:
    perscentage = (correct_attempts / n) * 100

    rounded_percentage = int(perscentage + 0.5)

    print(f'Верно решили {len(correct_users)} учащихся')
    print(f"Из всех попыток {rounded_percentage}% верных")



myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}

#myset3 = myset1 | myset2
myset3 = myset1.union(myset2)
print(myset3)
#myset4 = myset1 & myset2
myset4 = myset1.intersection(myset2)
print(myset4)
#myset5 = myset1 - myset2
myset5 = myset1.difference(myset2)
print(myset5)
#myset6 = myset1 ^ myset2
myset6 = myset1.symmetric_difference(myset2)
print(myset6)
#print(myset1 |= myset2)
#myset1.update(myset2)

#myset1.intersection_update(myset2)
#myset1 &= myset2
#myset1.difference_update(myset2)
#myset1 -= myset2
#myset1.symmetric_difference_update(myset2)
#myset1 ^= myset2

#The program is given two lines of text containing numbers as input. Write a program that determines the number of numbers that appear in both the first and second lines.
myset1 = (input().split())
myset2 = (input().split())
myset3 = set(myset1).intersection(set(myset2))
print(len(myset3))

#The program is given two lines of text containing numbers as input. Write a program that prints all the numbers in ascending order that appear in both the first and second lines.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
myset3 = myset1.intersection(myset2)
print(*sorted(myset3))

#The program is given two lines of text containing numbers as input. Write a program that prints all the numbers in the first line but not the second, in ascending order.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
print(*sorted(myset1 - myset2))


#The program is given a natural number n as input, followed byn distinct natural numbers, each on a separate line. Write a program that prints all common digits in ascending order for all input numbers.
n = int(input())
myset1 = set(input())
for i in range(n - 1):
    text = set(input())
    myset1.intersection_update(text)
print(*sorted(myset1))


set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}
#print(set1 <= set2)
print(set1.issubset(set2))
#print(set1 >= set2)
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))



#The program is given two numbers as input. Write a program that determines whether these numbers contain the same digit.
myset1 = set((input()))
myset2 = set((input()))

if myset1.isdisjoint(myset2):
    print('NO')
else:
    print('YES')


#The program is given two numbers as input. Write a program that determines whether the first number contains all the digits contained in the second number (regardless of repetition, i.e., the number of digits) or not.
myset1 = set((input()))
myset2 = set((input()))


if myset1.issuperset(myset2):
    print('YES')
else:
    print('NO')


#Three students are given computer science grades on a 10-point scale. Write a program that prints the set of grades that both the first and second students have, but the third student does not.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
myset3 = set(list(map(int, input().split())))

result = (myset1 & myset2) - myset3
print(*sorted(result, reverse=True))

#Three students' math grades are given on a 10-point scale. Write a program that displays grades that are shared by no more than two students.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
myset3 = set(list(map(int, input().split())))

all_three = myset1 & myset2 & myset3
result = (myset1 | myset2 | myset3) - all_three
print(*sorted(result))

#Three students are given physics grades on a 10-point scale. Write a program that prints the set of grades for the third student that are not found in either the first or second student.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
myset3 = set(list(map(int, input().split())))

result =  myset3 - (myset1 | myset2)
print(*sorted(result, reverse=True))


#Three students' biology grades are given on a 10-point scale. Write a program that prints the set of grades that are not shared by any of the three students.
myset1 = set(list(map(int, input().split())))
myset2 = set(list(map(int, input().split())))
myset3 = set(list(map(int, input().split())))
myset4 = {i for i in range(1, 11)}

result =  myset4 - (myset1 | myset2 | myset3)
print(*sorted(result))
