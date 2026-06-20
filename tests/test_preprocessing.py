import pandas as pd

from sentimazon.preprocessing import cleancomments, apply_cleaning


def test_cleancomments_lowercases_text():
    result = cleancomments("GOOD Phone!")

    assert result == "good phone "


def test_cleancomments_removes_hashtag_text():
    result = cleancomments("#Great")

    assert result == ""


def test_apply_cleaning_adds_cleancomment_column():
    data = pd.DataFrame({
        "review_text": ["Good phone!"],
        "sentiment": ["Positive"]
    })

    result = apply_cleaning(data)

    assert "Cleancomment" in result.columns