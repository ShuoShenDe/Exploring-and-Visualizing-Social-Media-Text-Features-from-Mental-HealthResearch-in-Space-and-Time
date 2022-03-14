import pandas as pd
import gensim
from gensim.parsing.preprocessing import preprocess_documents
import json
'''
df = pd.read_csv("wiki_movie_plots_de1duped.csv", sep=",")
df = df[df["Release Year"] >= 2000]
text_corpus = df["Plot"].values
'''
tweets = []

with open('stream_nyc_box.jsonl') as f:
    for i in f:
        readableRow = []
        tags = []
        # Load data
        if len(i) < 10:
            continue
        data = json.loads(i)
        tweets.append(data['text'])
        #print(data['text'])

print(tweets)
joinedtwee = "\n".join(tweets)
#text_corpus = data["text"].values
processed_corpus = preprocess_documents(joinedtwee)
dictionary = gensim.corpora.Dictionary(processed_corpus)
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

tfidf = gensim.models.TfidfModel(bow_corpus, smartirs="npu")
corpus_tfidf = tfidf[bow_corpus]

lsi = gensim.models.LsiModel(corpus_tfidf, num_topics=1000)
index = gensim.similarities.MatrixSimilarity(lsi[corpus_tfidf])


new_doc = gensim.parsing.preprocessing.preprocess_string("depression sadness")
new_vec = dictionary.doc2bow(new_doc)
vec_bow_tfidf = tfidf[new_vec]
vec_lsi = lsi[vec_bow_tfidf]
sims = index[vec_lsi]
for s in sorted(enumerate(sims), key=lambda item: -item[1])[:10]:
    print(f'{tweets} : {str(s[1])}')


#  source https://medium.com/betacom/latent-semantic-indexing-in-python-85880414b4de