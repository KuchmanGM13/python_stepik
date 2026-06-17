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