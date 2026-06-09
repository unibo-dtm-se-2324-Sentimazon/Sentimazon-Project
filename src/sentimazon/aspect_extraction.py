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