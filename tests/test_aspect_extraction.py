from sentimazon.aspect_extraction import extract_nouns


def test_extract_nouns_returns_only_nouns():
    pos_tags = [
        ("battery", "NN"),
        ("good", "JJ"),
        ("phones", "NNS"),
        ("run", "VB")
    ]

    result = extract_nouns(pos_tags)

    assert result == ["battery", "phones"]


def test_extract_nouns_handles_invalid_input():
    result = extract_nouns("not a list")

    assert result == []