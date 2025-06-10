def get_stock_data(tickers):
    import pandas as pd
    import numpy as np
    dates = pd.date_range(start='2024-01-01', periods=100)
    data = {ticker: np.random.rand(100) * 100 for ticker in tickers}
    return pd.DataFrame(data, index=dates)
  
