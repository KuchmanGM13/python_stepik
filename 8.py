#The first line contains a single integer n — the number of words in the dictionary. The next n lines contain the words and their definitions, separated by a colon and a space. The next line contains an integer m — the number of search words for which the definitions need to be output. The next m lines contain the words themselves, one per line.

n = int(input())
my_dict = {}
my_list = []
for i in range(n):
    text = input().split(': ')
    my_list.append(text)
my_dict = dict(my_list)    

m = int(input())

for i in range(m):
    s = input().lower()
    found =False
    for key, value in my_dict.items():
        if s in key.lower():
            print(value)
            found = True
            break
    if not found:
        print('Не найдено')


#A program that checks if the two input strings are anagrams of each other (i.e., they contain the same characters in a different order). The program should ignore spaces and punctuation, and it should be case-insensitive.
s1 = [i for i in input().lower() if i.isalpha()]
s2 = [i for i in input().lower() if i.isalpha()]

        
if sorted(s1) == sorted(s2):
    print('YES')
else:
    print('NO')


#The first line specifies a single integer n — the number of phone numbers Timur has saved in his phonebook. The next n  lines contain the phone numbers and their owners' names, separated by a space. The following line contains an integer m — the number of search queries from Timur. The next m lines contain the queries themselves, one per line. Each query is the name of a friend whose phone numbers Timur wants to find.
n = int(input())

my_dict = {}

for _ in range(n):
    phone, name = input().split()
    name = name.lower()
    
    if name not in my_dict:
        my_dict[name] = []
        
    my_dict[name].append(phone)
    
m = int(input())

for _ in range(m):
    name = input().lower()
    
    if name in my_dict:
        print(*my_dict[name])
    else:
        print('абонент не найден')


#The first line contains the encrypted word. The second line specifies an integer n—the number of letters in the dictionary. The next n lines list the frequency of each specific letter of the alphabet in the word, in the format `<letter>: <frequency>`.
#The program must output the decoded word.
secret = input()
n = int(input())
my_dict = {}

for _ in range(n):
    ch, num  = input().split(': ')
    my_dict[int(num)] = ch

result = ''
for ch in secret:
    count = secret.count(ch)
    decoded_letter = my_dict[count]
    result += decoded_letter
    
print(result)

#The program is given a string of text as input. Write a program that outputs the least common word, case-insensitively. If there are multiple such words, output the one with the lowest lexicographic order.
text = input()

for ch in ".,!?:;-":
    text = text.replace(ch, "")
text = text.lower()

result = {}
for word in text.split():
    result[word] = result.get(word, 0) + 1

min_count = min(result.values())
candidates = [word for word, count in result.items() if count == min_count]
print(min(candidates))


#The program is given a string containing identifier strings as input. Write a program that corrects them so that the resulting string contains no duplicates. To do this, append the suffix _n to duplicate identifiers, where n is the number of times such an identifier has already appeared.
words = input().split()
counts = {}
result = []

for word in words:
    if word in counts:
        result.append(f"{word}_{counts[word]}")
        counts[word] += 1
    else:
        result.append(word)
        counts[word] = 1

print(*result)


#To enter a paid parking lot, you need to obtain a ticket, which generates a digital ID. Then, upon exiting, you need to scan this ticket and pay (if necessary). If your car is parked for more than two hours, a fee of 3 rubles/minute will be charged for the excess time (two hours). Otherwise, there is no fee.
n = int(input())
entry = {}
for _ in range(n):
    car_id, time = input().split(': ')
    entry[car_id] = time

m = int(input())
result = []

for _ in range(m):
    car_id, time = input().split(': ')
    h1, m1 = map(int, entry[car_id].split(':'))
    h2, m2 = map(int, time.split(':'))
    
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    
    if t2 < t1:
        t2 += 24 * 60
    
    duration = t2 - t1
    
    if duration > 120:
        pay = (duration - 120) * 3
        result.append(f"{car_id}: {pay}₽")
    else:
        result.append(f"{car_id}: плата не взимается")

print('\n'.join(result))