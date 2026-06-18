#dict

#info_tuple = (['name', 'Timur'], ['age', 28], ['job', 'Teacher']) 
info_list = [('name', 'Timur'), ('age', 28), ('job', 'Teacher')] 
info_dict = dict(info_list)
print(info_dict) 

dict1 = dict.fromkeys(['name', 'age', 'job'], 'Missed information')

languages = {'Python': 'Гвидо ван Россум', 
             'C#': 'Андерс Хейлсберг', 
             'Java': 'Джеймс Гослинг'}

info = dict(name = 'Timur', age = 28, job = 'Teacher')

print(languages)
print(info)

users = [
    {'name': 'Hank', 'phone': '124-3818', 'email': 'hank@gmail.com'},
    {'name': 'Petr', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Sasha', 'phone': '449-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
    {
        'name': 'Maria',
        'phone': '12-129-3149',
        'email': 'm.shark@yandex.ru',
        'city': 'Pskov'
    },
    {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
    {
        'name': 'Tony',
        'phone': '242-449-3878',
        'email': 'tony.ggg@mail.ru',
        'birth_year': 1111
    },
]

result = []
for user in users:
    if user['phone'][-1] == '8':
        result.append(user['name'])

print(*sorted(result))


result = []
for user in users:
    if 'email' not in user or not user['email']:
        result.append(user['name'])
print(*sorted(result))


#Print the English names of the digits in the input number, separated by spaces.
s = tuple(input())
numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
l = []
# for i in range(len(s)):
#     for num in numbers:
#         if num in s[i]:
#             l.append(numbers[num])
        
# print(*l, end = ' ')
for c in s:
    print(numbers[c], end=' ')


#Print the course information in the format: Course: Room, Teacher, Time
curs_dict = {
    'CS101' : [3004, 'Хайнс', '8:00'],
    'CS102' : [4501, 'Альварадо', '9:00'],
    'CS103' : [6755, 'Рич', '10:00'],
    'NT110' : [1244, 'Берк', '11:00'],
    'CM241' : [1411, 'Ли', '13:00'],
}


key = input()
room, teacher, time = curs_dict[key]
print(f'{key}: {room}, {teacher}, {time}')



#Phone keypad
d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}

s = tuple(input())
for c in s:
    for key, value in d.items():
        if c in value:
            print(key*c, end = '')

#Add two dictionaries together, if they have the same key, add the values together, if not, just add the key and value to the result.
dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}
result = dict1.copy()
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)

#Print the Morse code for the input word, separating the letters with spaces.
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
mydict = dict(zip(letters, morse))
word = input().upper()

for c in word:
    if c in mydict:
        print(mydict[c], end=' ')


#Count the frequency of each character in the input string and print the result as a dictionary.
text = "TheyDon'tKnowThatWeKnowTheyKnowWeKnow"

result = {}
for num in text:
    result[num] = result.get(num, 0) + 1

print(result)       



#A program that outputs the most frequently occurring word in the string `text`. If there are multiple such words, the one that is lexicographically smallest must be output.
result = {}
for word in text.split():
    result[word] = result.get(word, 0) + 1

max_count = max(result.values())
candidates = [word for word, count in result.items() if count == max_count]
print(min(candidates))


#A program that groups the pets by their owners and prints the result in the format: Owner Name Owner Surname (Owner Age): Pet1, Pet2, ...
pets = [
    ('Барсик', 'Маша', 'Петрова', 17),
    ('Джек', 'Галина', 'Лагунова', 45),
    ('Муся', 'Александр', 'Каракулов', 28),
    ('Буся', 'Маша', 'Петрова', 17),
    ('Кира', 'Вова', 'Пухарев', 54),
]

pets_dict = {}
for pet in pets:
    name, owner_name, owner_surname, age = pet
    if (owner_name, owner_surname, age) not in pets_dict:
        pets_dict[(owner_name, owner_surname, age)] = []
    pets_dict[(owner_name, owner_surname, age)].append(name)

for owner, pet_names in pets_dict.items():
    print(f'{owner[0]} {owner[1]} ({owner[2]}): {", ".join(pet_names)}')    