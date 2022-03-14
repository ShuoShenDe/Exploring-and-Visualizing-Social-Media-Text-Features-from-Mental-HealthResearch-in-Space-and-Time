import pandas as pd
from operator import itemgetter

inputdata = []
dataframe = pd.read_csv("trainning_neg.csv")
inputdata = dataframe['text'].astype(str).values.tolist()
joinedtweets = "\n".join(inputdata)

def vectorize(tokens):
    ''' This function takes list of words in a sentence as input
    and returns a vector of size of filtered_vocab.It puts 0 if the
    word is not present in tokens and count of token if present.'''
    vector=[]
    for w in filtered_vocab:
        vector.append(tokens.count(w))
    return vector
def unique(sequence):
    '''This functions returns a list in which the order remains
    same and no item repeats.Using the set() function does not
    preserve the original ordering,so i didnt use that instead'''
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
#create a list of stopwords
stopwords=["to","is","a", ] #"the", "of", "and", "you", "this"
#list of special characters.You can use regular expressions too
special_char=[",",":"," ",";",".","?"]
#convert the input to lower case
joinedtweets=joinedtweets.lower()
#split the sentences into tokens
tokens1=joinedtweets.split()
print(tokens1)
#create a vocabulary list
vocab = unique(tokens1)
#print(vocab)
#filter the vocabulary list
filtered_vocab = []
for w in vocab:
    if w not in stopwords and w not in special_char:
        filtered_vocab.append(w)
print(filtered_vocab)
#convert sentences into vectords
vector1 = vectorize(tokens1)
print(vector1)
#calculate indexes of words with highest presence
meta_lst = list(enumerate(vector1))
sorted_meta_lst = sorted(meta_lst, key=itemgetter(1))
print(sorted_meta_lst)
#print values of the highest 15 indexes found
print(filtered_vocab[4], filtered_vocab[53], filtered_vocab[48], filtered_vocab[157], filtered_vocab[55], filtered_vocab[77], filtered_vocab[9], filtered_vocab[43],filtered_vocab[94], filtered_vocab[8],
      filtered_vocab[246], filtered_vocab[0], filtered_vocab[6], filtered_vocab[143], filtered_vocab[100], filtered_vocab[162], filtered_vocab[160], filtered_vocab[169], filtered_vocab[360], filtered_vocab[131],filtered_vocab[176], filtered_vocab[300] )

Most_Used_Words = [filtered_vocab[4], filtered_vocab[53], filtered_vocab[48], filtered_vocab[157], filtered_vocab[55], filtered_vocab[77], filtered_vocab[9], filtered_vocab[43],filtered_vocab[94], filtered_vocab[8],
      filtered_vocab[246], filtered_vocab[0], filtered_vocab[6], filtered_vocab[143], filtered_vocab[100], filtered_vocab[162], filtered_vocab[160], filtered_vocab[169], filtered_vocab[360], filtered_vocab[131],filtered_vocab[176], filtered_vocab[300]]

with open('Negative_Most_Used_Words.txt', 'w') as f:
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
