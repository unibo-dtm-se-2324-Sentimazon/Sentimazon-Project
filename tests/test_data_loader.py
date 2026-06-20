import pandas as pd

from sentimazon.data_loader import select_review_columns


def test_select_review_columns():
    data = pd.DataFrame({
        "review_text": ["Good phone", "Bad battery"],
        "sentiment": ["Positive", "Negative"],
        "extra_column": [1, 2]
    })

    result = select_review_columns(data)

    assert list(result.columns) == ["review_text", "sentiment"]
    assert len(result) == 2