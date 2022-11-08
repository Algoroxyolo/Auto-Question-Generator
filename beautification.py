def beautify(sentence):
    sentence = sentence[0].upper() + sentence[1:]
    sentence.replace('.','?')
    return sentence
