import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def cleancomments(comment):
    comment = re.sub('@[A-Za-z0-9_]+','',str(comment))
    comment = re.sub('https://[A-Za-z0-9./]+','',str(comment))
    comment = re.sub('#[A-Za-z0-9./]+','',str(comment))
    comment = re.sub(r'[^\w]', ' ', str(comment))
    comment = comment.lower()
    return comment


def apply_cleaning(data):
    data = data.copy()
    for index, row in data.iterrows():
        data.loc[index,'Cleancomment'] = cleancomments(data.loc[index,'review_text'])
    return data


def apply_stop_words(data):
    data = data.copy()
    stop_words = set(nltk.corpus.stopwords.words('english'))
    data['applied stop_words'] = data['Cleancomment'].apply(
        lambda x: ' '.join([comment for comment in x.split() if comment not in (stop_words)])
    )
    return data


def apply_tokenization(data):
    data = data.copy()
    data['tokenized_Comments'] = data.apply(
        lambda row: nltk.word_tokenize(row['applied stop_words']),
        axis=1
    )
    return data


def apply_lemmatization(data):
    data = data.copy()
    lemmatizer = WordNetLemmatizer()

    data['lemmatized_Comments'] = data['tokenized_Comments'].apply(
        lambda tokens: [lemmatizer.lemmatize(token) for token in tokens]
    )
    return data


def preprocess_reviews(data):
    data = apply_cleaning(data)
    data = apply_stop_words(data)
    data = apply_tokenization(data)
    data = apply_lemmatization(data)
    return data