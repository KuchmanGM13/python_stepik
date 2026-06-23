from collections import Counter

def add_query_string(url : str, query : dict):
    result = url
    if query:
        result += '?'
        pairs = []
        for key, value in query.items():
            pairs.append(f'{key}={value}')
        result += '&'.join(pairs)
    return result

print(add_query_string('pygen.ru', {'per': '10', 'page': 1}))

def dict_diff(data1, data2):
    result = {}
    all_keys = set(data1) | set(data2)
    for key in all_keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] != data2[key]:
            result[key] = 'changed'
        else:
            result[key] = 'unchanged'
    return result        
            
            
data1 = {'one': 1, 'two': 2, 'four': 4}
data2 = {'two': 2.5, 'three': 3, 'four': 4}
print(dict_diff(data1, data2))


def is_access_allowed(ip_address, mode, ip_access_list):
    if mode == 1:
        if ip_address in ip_access_lists['black list']:
            return 'НЕТ'
        return 'ДА'
    elif mode == 2:
        if ip_address in ip_access_lists['white list']:
            return 'ДА'
        return 'НЕТ'


black_list = [
    '45.34.12.200', '78.91.204.34', 
    '78.94.127.35', '96.124.37.82',
]
white_list = [
    '14.231.64.173', '75.34.2.179',
]
ip_access_lists = {
    'black list': black_list, 
    'white list': white_list,
}
print(
    is_access_allowed(
        '224.27.189.35',
        1, 
        ip_access_lists,
    )
)


def transform(txt):
    d = {}
    for i, ch in enumerate(txt):
        d.setdefault(ch, set()).add(i)
    return d


print(transform('Аметист'))


def replace_homoglyphs(txt):
    res = ''
    for ch in txt:
        if ch in homoglyphs:
            res  += homoglyphs[ch]
        else:
            res += ch
    return res


homoglyphs = {
    'e': 'е', 'y': 'у', 'o': 'о', 'p': 'р', 'a': 'а',
    'ʍ': 'м', 'ʙ': 'в', 'Φ': 'Ф', 'k': 'к', 'x': 'х',
    'c': 'с', 'E': 'Е', 'T': 'Т', 'ȹ': 'ф', 'Ͷ': 'И',
    'ʜ': 'н', 'O': 'О', 'P': 'Р', 'A': 'А', 'H': 'Н',
    'K': 'К', 'Ƅ': 'ь', 'ͷ': 'и', 'ɯ': 'ш', 'X': 'Х',
    'C': 'С', 'B': 'В', 'M': 'М', 'π': 'п', '3': 'З',
    'Γ': 'Г', 'ʮ': 'ч',
}

text = 'XoʮeɯƄ зapaбaтыʙaтƄ oт 5K ʙ cyтkͷ? Haπͷɯͷ ʜaʍ ʙ ʮaтe.'
print(replace_homoglyphs(text))


#It traverses the list once (O(n)) and counts all occurrences at once—which is why it is ~2,300 times faster
# def print_product_list(product_list: list):
#     counts = Counter(product_list)
#     lines = []
#     for name, count in counts.items():
#         label = emojis_product.get(name, name)
#         lines.append(f'{label}: {count}')
#     print(*lines, sep='\n')



def print_product_list(product_list : list):
    result = {}
    for key in product_list:
        if key in emojis_product:
            result[emojis_product[key]] = product_list.count(key)
        else:
            result[key] = product_list.count(key)
            
    lines = []
    for name, count in result.items():
        lines.append(f'{name}: {count}')
    return print(*lines, sep = '\n')
    
emojis_product = {
    'яблоко': '🍎', 'хлеб': '🍞', 'конфеты': '🍬', 'лимон': '🍋',
    'морковь': '🥕', 'огурец': '🥒', 'помидор': '🍅', 'яйцо': '🥚',
    'чеснок': '🧄', 'авокадо': '🥑', 'спички': '🥢', 'соль': '🧂',
    'филе говядины': '🥩', 'киви': '🥝', 'лук': '🧅', 'сыр': '🧀',
}    


product_list = [
    'молоко', 'яйцо', 'колбаса', 'лук',
    'помидор', 'помидор', 'майонез',
    'хлеб', 'лук', 'сливочное масло',
]
print_product_list(product_list)   




balances = {}


def bank(operation: str, client: str, amount: int | None):
    if client not in balances:
        balances[client] = 0
    
    if operation == 'top up':
        balances[client] += amount 
    elif operation == 'withdraw':
        balances[client] -= amount
    elif operation == 'pay':
        balances[client] -= amount
    elif operation == 'show balance':
        print(balances[client])
                            

arthur = 'id-1004'
tony = 'id-78923'
bank('top up', tony, 500)
bank('show balance', arthur, None)
bank('pay', tony, 120)
bank('top up', arthur, 1000)
bank('show balance', arthur, None)
bank('withdraw', tony, 200)
bank('show balance', tony, None)


from collections import Counter

def scrabble(letters: str, word: str):
    letters_count = Counter(letters.lower())
    words_count = Counter(word.lower())
    for ch, count in words_count.items():
        if letters_count[ch] < count:
            return False
    return True    



print(scrabble('BEEGEEK', 'geekbee'))
print(scrabble('tg', 'tgg'))
print(scrabble('BEBEEGEEK', 'geekbee'))


spending_list = {}

def show_top_categories(spendings: list, num: int): 
    counts = Counter()
    for categrie, summa in spendings:
        counts[categrie] += summa
        
    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:num]
    top_sorted = sorted(top, key=lambda x: x[0])
    for categrie, summa in top_sorted:
        print(categrie)
        
spendings = [
    ('аптека', 1300), ('пекарня', 350),
    ('проезд в автобусе', 43),
    ('ресторан', 2300), ('кофейня', 300),
    ('аптека', 2900), ('зоотовары', 750),
    ('кофейня', 290), ('ресторан', 3540),
    ('проезд в автобусе', 43),
    ('такси', 540), ('кино', 880),
]

show_top_categories(spendings, 4)   


def is_subfolder(folder_dict: dict, subfolder: str, folder: str) -> bool:
    children = folder_dict.get(folder, [])
    if subfolder in children:
        return True
    else:
        for child in children:
            if is_subfolder(folder_dict, subfolder, child):
                return True
    return False


folder_system = {
    'My': [
        'Cartoons', 'Films', 'Series',
    ],
    'Cartoons': [
        'Bolt (2008)', 'Ben 10 (2005)',
        'Finding Nemo (2003)',
    ],
    'Films': [
        'Joker (2019)', 'Wonka (2023)',
        'Gone Girl (2014)',
    ],
    'Series': [
        'Stranger Things (2016-2025)',
        'Fallout (2024-)',
        'Chernobyl (2019)',
    ],
}
print(is_subfolder(
    folder_system,
    'Fallout (2024-)',
    'My',
))

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

result = {value: key for key, value in months.items()}
print(result)
