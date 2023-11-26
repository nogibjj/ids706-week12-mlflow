import pandas as pd
import os
def test_main():
    assert os.path.exists("data/stock_data.csv")
    df = pd.read_csv("data/stock_data.csv")
    assert df.shape[0] > 0
    assert df.shape[1] > 0

if __name__ == "__main__":
    test_main()