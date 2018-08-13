from nltk import word_tokenize,sent_tokenize

def remove_punctuation(sentence):
    to_delete = "./:;<=>?@[\]^_`{|}~#$%&'()*+,!"
    to_delete2 = '"'
    to_replace = "-"
    return sentence.lower().rstrip().strip().translate(str.maketrans('', '', to_delete)).translate(
                str.maketrans('', '', '1234567890')).translate(str.maketrans('', '', to_delete2)).translate(
                str.maketrans(to_replace, " "))
senteces=[]
with open('author-quote.txt','r') as quotes:
    for line in quotes:
        t_sen=sent_tokenize(line.split('\t')[1])
        for sentence in t_sen:
            sentence=remove_punctuation(sentence)
            if 5<len(word_tokenize(sentence))<20:
                senteces.append(sentence)

for sentence in senteces:
    print(sentence)
print(len(senteces))


