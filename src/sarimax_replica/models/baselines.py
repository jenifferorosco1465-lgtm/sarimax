import numpy as np

def seasonal_naive(train, horizon: int, season: int = 12):
    values=np.asarray(train, dtype=float)
    if len(values) < season:
        return np.repeat(values[-1], horizon)
    return np.array([values[-season + (i % season)] for i in range(horizon)])
