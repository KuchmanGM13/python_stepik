#Advertising bots or scammers frequently send messages that substitute Cyrillic characters with Latin ones or other similar symbols (homoglyphs). This is done to bypass anti-spam filters, hinder keyword searches, and mimic normal text (including in website names).
#Write a function `replace_homoglyphs()` that takes a text string `text` containing homoglyphs and returns a new string with all homoglyphs replaced by the corresponding Russian letters. Use the following homoglyph dictionary for your solution (where the keys are the homoglyph characters and the values ​​are the Russian letters):

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

text = input()

print(replace_homoglyphs(text))