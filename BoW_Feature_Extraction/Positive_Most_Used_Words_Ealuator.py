import pandas as pd
from operator import itemgetter

inputdata = []
dataframe = pd.read_csv("trainning_pos.csv")
inputdata = dataframe['text'].astype(str).values.tolist()
joinedtweets = "\n".join(inputdata)

def vectorize(tokens):
    ''' This function takes list of words in a sentence as input
    and returns a vector of size of filtered_vocab.It puts 0 if the
    word is not present in tokens and count of token if present.'''
    vector = []
    for w in filtered_vocab:
        vector.append(tokens.count(w))
    return vector

def unique(sequence):
    '''This functions returns a list in which the order remains
    same and no item repeats.Using the set() function does not
    preserve the original ordering,so i didnt use that instead'''
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


# create a list of stopwords
stopwords = ["to", "is", "a", ]  # "the", "of", "and", "you", "this"
# list of special characters.You can use regular expressions too
special_char = [",", ":", " ", ";", ".", "?"]
# convert the input to lower case
joinedtweets = joinedtweets.lower()
# split the sentences into tokens
tokens1 = joinedtweets.split()
print(tokens1)
# create a vocabulary list
vocab = unique(tokens1)
# print(vocab)
# filter the vocabulary list
filtered_vocab = []
for w in vocab:
    if w not in stopwords and w not in special_char:
        filtered_vocab.append(w)
print(filtered_vocab)
# convert sentences into vectords
vector1 = vectorize(tokens1)
print(vector1)
# calculate indexes of words with highest presence
meta_lst = list(enumerate(vector1))
sorted_meta_lst = sorted(meta_lst, key=itemgetter(1))
print(sorted_meta_lst)
# print values of the highest 15 indexes found
print(filtered_vocab[1], filtered_vocab[5], filtered_vocab[6], filtered_vocab[61], filtered_vocab[9],
      filtered_vocab[14], filtered_vocab[4],
      filtered_vocab[2], filtered_vocab[66], filtered_vocab[293], filtered_vocab[46], filtered_vocab[129],
      filtered_vocab[68], filtered_vocab[35], filtered_vocab[45], filtered_vocab[112])

Most_Used_Words = [filtered_vocab[1], filtered_vocab[5], filtered_vocab[6], filtered_vocab[61], filtered_vocab[9],
                   filtered_vocab[14], filtered_vocab[4],
                   filtered_vocab[2], filtered_vocab[66], filtered_vocab[293], filtered_vocab[46], filtered_vocab[129],
                   filtered_vocab[68], filtered_vocab[35], filtered_vocab[45], filtered_vocab[112]]

with open('Positive_Most_Used_Words.txt', 'w') as f:
    f.write('Vocabolary:')
    f.write('\n')
    f.write(str(filtered_vocab))
    f.write('\n')
    f.write('Vector:')
    f.write('\n')
    f.write(str(vector1))
    f.write('\n')
    f.write('Sorted Indexes and Count of elements for the Vocabulary:')
    f.write('\n')
    f.write(str(sorted_meta_lst))
    f.write('\n')
    f.write('Most Used Words with this Training Data:')
    f.write('\n')
    f.write(str(Most_Used_Words))
