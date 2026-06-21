import pandas as pd
import nltk
from nltk import sent_tokenize
from nltk.tag.perceptron import PerceptronTagger

def add_pos_tags(data):
    data = data.copy()
    tagger = PerceptronTagger()

    data['pos_tags'] = data['lemmatized_Comments'].apply(
        lambda tokens: tagger.tag(tokens)
    )

    return data


def extract_nouns(pos_tags):
    if not isinstance(pos_tags, list):
        return []
    return [word for word, tag in pos_tags if tag.startswith('NN')]


def add_nouns(data):
    data = data.copy()
    data['nouns'] = data['pos_tags'].apply(extract_nouns)
    return data


def get_noun_counts(data, top_n=20):
    noun_counts = data['nouns'].explode().value_counts().head(top_n)
    return noun_counts


def get_filtered_noun_counts(data, top_n=20):
    useless_aspects = [
        'phone', 'year', 'loving', 'fine', 'month',
        'penny', 'day', 'feel', 'crisp'
    ]

    noun_counts = (
        data['nouns']
        .explode()
        .loc[lambda x: ~x.isin(useless_aspects)]
        .value_counts()
        .head(top_n)
    )

    return noun_counts

def get_all_phrases_containing_tar_wrd(target_word, tar_passage, left_margin=5, right_margin=5):
    tokens = nltk.word_tokenize(tar_passage)
    tokens = [x for x in tokens if len(x) > 2]

    text = nltk.Text(tokens)
    c = nltk.ConcordanceIndex(text.tokens, key=lambda s: s.lower())

    concordance_txt = [
        text.tokens[
            list(map(lambda x: x - 5 if (x - left_margin) > 0 else 0, [offset]))[0]:
            offset + right_margin
        ]
        for offset in c.offsets(target_word)
    ]

    return [''.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]


def create_phrases_dataframe(data):
    reviews = data['Cleancomment'].dropna().astype(str)
    relevant_aspects = ['battery', 'price', 'quality', 'performance']

    phrases = []
    aspects = []
    review_ids = []

    for idx, review in reviews.items():
        try:
            for sentence in sent_tokenize(review):
                for important_word in relevant_aspects:
                    phrases_in_sentence = get_all_phrases_containing_tar_wrd(
                        important_word,
                        sentence,
                        left_margin=5,
                        right_margin=5
                    )

                    for phrase in phrases_in_sentence:
                        aspect = 'other'

                        for imp_word in relevant_aspects:
                            if imp_word in phrase.lower():
                                aspect = imp_word

                        aspects.append(aspect)
                        phrases.append(phrase)
                        review_ids.append(idx)

        except Exception:
            pass

    phrasesDF = pd.DataFrame({
        'review_id': review_ids,
        'aspect': aspects
    })

    phrasesDF = phrasesDF.merge(
        data[['review_text', 'sentiment']],
        left_on='review_id',
        right_index=True,
        how='left'
    )[['review_text', 'sentiment', 'aspect']]

    return phrasesDF