import textstat
import json
import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from afinn import Afinn
import re

nltk.download()



readables = []
afinn = Afinn(language='en')

with open('stream_nyc_box.jsonl') as f:
    for i in f:
        readableRow = []
        tags = []
        # Load data
        if len(i) < 10:
            continue
        data = json.loads(i)
        # print(data)
        # print(data["text"])

        #positive or negative
        readableRow.append(afinn.score(data["text"]))

        # PoS
        words = word_tokenize(data["text"])
        pos_tags = nltk.pos_tag(words)
        # print(pos_tags)
        #verb tenses
        for index, tag in enumerate(pos_tags):
            match = re.search('\w.*', tag[1])
            if match:
                # if tag[0] == "n't" or tag[0] == "not":
                #     pos_tags[index] = (pos_tags[index][0], "NEG")
                if "VB" in tag[1]:
                    tags.append(tag[1])
        tags = list( dict.fromkeys(tags))
        readableRow.append(",".join(tags))

        # text readability
        readableRow.append(textstat.syllable_count(data["text"]))  # Syllable Count
        readableRow.append(textstat.difficult_words(data["text"]))

        readableRow.append(
            textstat.flesch_reading_ease(data["text"]))  # How difficult a reading passage is to understand
        # print(textstat.smog_index(test_data))
        readableRow.append(textstat.flesch_kincaid_grade(data["text"]))
        readableRow.append(
            textstat.coleman_liau_index(data["text"]))  # grade level of the text using the Coleman-Liau Formula
        readableRow.append(textstat.automated_readability_index(
            data["text"]))  # a number that approximates the grade level needed to comprehend the text
        readableRow.append(textstat.gunning_fog(data[
                                                    "text"]))  # The index estimates the years of formal education a person needs to understand the text on the first reading
        readableRow.append(
            textstat.linsear_write_formula(data["text"]))  # the grade level using the Linsear Write Formula
        readableRow.append(textstat.dale_chall_readability_score(
            data["text"]))  # returns the grade level using the New Dale-Chall Formula
        readableRow.append(textstat.text_standard(
            data["text"]))  # returns the estimated school grade level required to understand the text
        readableRow.append(
            textstat.crawford(data["text"]))  # an estimate of the years of schooling required to understand the text
        readableRow.append(textstat.gutierrez_polini(data["text"]))  # Scores for more complex text are not reliable
        # print(textstat.fernandez_huerta(test_data))
        # print(textstat.szigriszt_pazos(test_data))
        # print(readableRow)
        readableRow.append(data["text"])
        readables.append(readableRow)

with open('syntactic_nyc.csv', 'w', encoding='UTF8') as w:
    writer = csv.writer(w)
    # write the header
    header = ["afinn_score","verb_tenses", "syllable_count", "difficult_words", "flesch_reading_ease", "flesch_kincaid_grade",
              "coleman_liau_index", "automated_readability_index",
              "gunning_fog", "text_standard", "text_standard", "text_standard", "crawford", "gutierrez_polini","text"]
    writer.writerow(header)
    # print(readables)
    writer.writerows(readables)
