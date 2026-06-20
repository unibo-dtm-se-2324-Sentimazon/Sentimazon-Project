import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def normalize_sentiment_labels(phrasesDF):
    phrasesDF = phrasesDF.copy()

    phrasesDF['sentiment'] = phrasesDF['sentiment'].str.strip().str.capitalize()
    phrasesDF['vader_label'] = phrasesDF['vader_label'].str.strip().str.capitalize()

    phrasesDF['DistilBERT_transformer_sentiment'] = (
        phrasesDF['DistilBERT_transformer_sentiment']
        .str.strip()
        .str.capitalize()
    )

    phrasesDF['RoBERTa_transformer_sentiment'] = (
        phrasesDF['RoBERTa_transformer_sentiment']
        .str.strip()
        .str.capitalize()
    )

    phrasesDF['RoBERTa_transformer_sentiment'] = (
        phrasesDF['RoBERTa_transformer_sentiment']
        .replace('Neutral', 'Negative')
    )

    return phrasesDF


def compute_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        average='weighted',
        zero_division=0
    )

    return acc, precision, recall, f1


def create_results_table(phrasesDF):
    v_acc, v_prec, v_rec, v_f1 = compute_metrics(
        phrasesDF['sentiment'],
        phrasesDF['vader_label']
    )

    d_acc, d_prec, d_rec, d_f1 = compute_metrics(
        phrasesDF['sentiment'],
        phrasesDF['DistilBERT_transformer_sentiment']
    )

    r_acc, r_prec, r_rec, r_f1 = compute_metrics(
        phrasesDF['sentiment'],
        phrasesDF['RoBERTa_transformer_sentiment']
    )

    results_table = pd.DataFrame({
        'Model': ['VADER', 'DistilBERT', 'RoBERTa'],
        'Accuracy': [v_acc, d_acc, r_acc],
        'Precision': [v_prec, d_prec, r_prec],
        'Recall': [v_rec, d_rec, r_rec],
        'F1-score': [v_f1, d_f1, r_f1]
    })

    results_table = results_table.round(4)

    return results_table