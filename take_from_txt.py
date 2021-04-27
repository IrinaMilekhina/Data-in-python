def tokenize_text(text):
    sentences = text.split('.')
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    return set(words)


text = open('sample.txt', 'r').read()
result = tokenize_text(text)

print(result)
