import re
def beautify(sentence):
    sentence = re.match(r'(\w+)[\.\?!,: ]*', sentence).group(1)
    sentence = sentence[0].upper() + sentence[1:]
    return sentence + '?'
