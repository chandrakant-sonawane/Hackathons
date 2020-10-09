import pandas as pd
import numpy as np
import json
import re
import emoji
from collections import OrderedDict
from sentence_transformers import SentenceTransformer

def data_cleaning(data):
    # expand_contractions
    CONTRACTION_MAP = eval(open('CONTRACTION_MAP.txt', 'r').read())
    def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

        contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                          flags=re.IGNORECASE|re.DOTALL)
        def expand_match(contraction):
            match = contraction.group(0)
            first_char = match[0]
            expanded_contraction = contraction_mapping.get(match)\
                                    if contraction_mapping.get(match)\
                                    else contraction_mapping.get(match.lower())                       
            expanded_contraction = first_char+expanded_contraction[1:]
            return expanded_contraction

        expanded_text = contractions_pattern.sub(expand_match, text)
        expanded_text = re.sub("'", "", expanded_text)
        return expanded_text
    data['cleaned_user_review'] = data['user_review'].apply(lambda x: expand_contractions(x))
    # removing "Early Access Review"
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub('^Early Access Review', '', x))
    # removing URLs
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r"http\S+", "", x))
    # removing emojis
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(emoji.get_emoji_regexp(), '', x))
    # removing repetitive words
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r'\b(\w+)( \1\b)+', r'\1', x))
    # removing repetitive phrases
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: (' '.join(OrderedDict((w,w) for w in x.split()).keys())))
    # removing repetitive letters or punctuations
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r'([!,.+?])\1+', r'\1\1', x))
    # removing selective punctuations
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r"[|~|\\\\|./|_|-|<|>|#|@|!|&]",'', x))
    # removing special characters
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r'[^\x00-\x7f]',r' ', x))
    # removing more than single space
    data['cleaned_user_review'] = data['cleaned_user_review'].apply(lambda x: re.sub(r'\s+', ' ', x))
    
    return data

#load the BERT model
embedder = SentenceTransformer(r'.\BERTLarge')

train = pd.read_csv(r"train.csv", encoding='utf8')
cleaned_train_data = data_cleaning(train)

train_data = pd.DataFrame()
train_data['review_id'] = cleaned_train_data["review_id"]
train_data['user_review'] = cleaned_train_data["user_review"]
train_data["cleaned_user_review"] = cleaned_train_data["cleaned_user_review"]
train_data['embedded_review']= embedder.encode(cleaned_train_data["cleaned_user_review"])
train_data['user_suggestion'] = cleaned_train_data["user_suggestion"]

train_data.to_json(r"new_train_data.json")

##################################################################################################

test = pd.read_csv(r"test.csv", encoding='utf8')
cleaned_test_data = data_cleaning(test)

test_data = pd.DataFrame()
test_data['review_id'] = cleaned_test_data["review_id"]
test_data['user_review'] = cleaned_test_data["user_review"]
test_data["cleaned_user_review"] = cleaned_test_data["cleaned_user_review"]
test_data['embedded_review']= embedder.encode(cleaned_test_data["cleaned_user_review"])

test_data.to_json(r"new_test_data.json")
