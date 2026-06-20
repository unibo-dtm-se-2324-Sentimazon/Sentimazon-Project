import time
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline


def apply_vader_sentiment(phrasesDF):
    phrasesDF = phrasesDF.copy()

    start_vader = time.time()

    vader_sentiment = []
    vader_sentiment_neg = []
    vader_sentiment_pos = []

    sid = SentimentIntensityAnalyzer()

    for sentence in phrasesDF['review_text']:
        try:
            vader_sentiment.append(sid.polarity_scores(sentence)['compound'])
            vader_sentiment_pos.append(sid.polarity_scores(sentence)['pos'])
            vader_sentiment_neg.append(sid.polarity_scores(sentence)['neg'])
        except Exception:
            vader_sentiment.append(0.5)
            vader_sentiment_neg.append(0.0)
            vader_sentiment_pos.append(0.0)

    phrasesDF['vader_sentiment'] = pd.Series(vader_sentiment)
    phrasesDF['vader_sentiment_neg'] = pd.Series(vader_sentiment_neg)
    phrasesDF['vader_sentiment_pos'] = pd.Series(vader_sentiment_pos)

    phrasesDF['vader_label'] = phrasesDF['vader_sentiment'].apply(
        lambda x: 'positive' if x >= 0.05 else ('negative' if x <= -0.05 else 'neutral')
    )

    end_vader = time.time()
    vader_time = end_vader - start_vader

    return phrasesDF, vader_time


def apply_distilbert_sentiment(phrasesDF):
    phrasesDF = phrasesDF.copy()

    start_trans = time.time()

    sentiment_model = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    DistilBERT_transformer_sentiment = []
    DistilBERT_transformer_sentiment_neg = []
    DistilBERT_transformer_sentiment_pos = []

    for sentence in phrasesDF['review_text']:
        try:
            result = sentiment_model(sentence)[0]

            if result['label'] == 'POSITIVE':
                DistilBERT_transformer_sentiment_pos.append(result['score'])
                DistilBERT_transformer_sentiment_neg.append(1 - result['score'])
                DistilBERT_transformer_sentiment.append(result['score'])
            else:
                DistilBERT_transformer_sentiment_neg.append(result['score'])
                DistilBERT_transformer_sentiment_pos.append(1 - result['score'])
                DistilBERT_transformer_sentiment.append(-result['score'])

        except Exception:
            DistilBERT_transformer_sentiment.append(0.0)
            DistilBERT_transformer_sentiment_neg.append(0.0)
            DistilBERT_transformer_sentiment_pos.append(0.0)

    phrasesDF['DistilBERT_transformer_sentiment'] = pd.Series(
        DistilBERT_transformer_sentiment
    )
    phrasesDF['DistilBERT_transformer_sentiment_neg'] = pd.Series(
        DistilBERT_transformer_sentiment_neg
    )
    phrasesDF['DistilBERT_transformer_sentiment_pos'] = pd.Series(
        DistilBERT_transformer_sentiment_pos
    )

    phrasesDF['DistilBERT_transformer_sentiment'] = phrasesDF.apply(
        lambda row:
        'positive'
        if row['DistilBERT_transformer_sentiment_pos'] > row['DistilBERT_transformer_sentiment_neg']
        else 'negative',
        axis=1
    )

    end_trans = time.time()
    trans_time = end_trans - start_trans

    return phrasesDF, trans_time


def apply_roberta_sentiment(phrasesDF):
    phrasesDF = phrasesDF.copy()

    start_trans = time.time()

    roberta_model = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

    RoBERTa_transformer_sentiment = []
    RoBERTa_transformer_sentiment_neg = []
    RoBERTa_transformer_sentiment_pos = []

    for sentence in phrasesDF['review_text']:
        try:
            result = roberta_model(sentence)[0]
            label = result['label']
            score = result['score']

            if label == 'LABEL_2':
                RoBERTa_transformer_sentiment_pos.append(score)
                RoBERTa_transformer_sentiment_neg.append(1 - score)
                RoBERTa_transformer_sentiment.append(score)
            else:
                RoBERTa_transformer_sentiment_neg.append(score)
                RoBERTa_transformer_sentiment_pos.append(1 - score)
                RoBERTa_transformer_sentiment.append(-score)

        except Exception:
            RoBERTa_transformer_sentiment.append(0.0)
            RoBERTa_transformer_sentiment_neg.append(0.0)
            RoBERTa_transformer_sentiment_pos.append(0.0)

    phrasesDF['RoBERTa_transformer_sentiment'] = pd.Series(
        RoBERTa_transformer_sentiment
    )
    phrasesDF['RoBERTa_transformer_sentiment_neg'] = pd.Series(
        RoBERTa_transformer_sentiment_neg
    )
    phrasesDF['RoBERTa_transformer_sentiment_pos'] = pd.Series(
        RoBERTa_transformer_sentiment_pos
    )

    phrasesDF['RoBERTa_transformer_sentiment'] = phrasesDF.apply(
        lambda row:
        'positive'
        if row['RoBERTa_transformer_sentiment_pos'] > row['RoBERTa_transformer_sentiment_neg']
        else 'negative',
        axis=1
    )

    phrasesDF = phrasesDF.drop(
        columns=[
            'RoBERTa_transformer_sentiment_pos',
            'RoBERTa_transformer_sentiment_neg'
        ],
        errors='ignore'
    )

    end_trans = time.time()
    trans_time = end_trans - start_trans

    return phrasesDF, trans_time