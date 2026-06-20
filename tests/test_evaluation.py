from sentimazon.evaluation import compute_metrics


def test_compute_metrics_returns_four_values():
    y_true = ["Positive", "Negative", "Positive"]
    y_pred = ["Positive", "Negative", "Negative"]

    acc, precision, recall, f1 = compute_metrics(y_true, y_pred)

    assert 0 <= acc <= 1
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= f1 <= 1