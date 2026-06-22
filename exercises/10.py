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
