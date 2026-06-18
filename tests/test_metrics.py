from sarimax_replica.evaluation.metrics import forecast_metrics

def test_perfect_forecast():
    m=forecast_metrics([1,2,3],[1,2,3])
    assert m["mae"]==0 and m["rmse"]==0
