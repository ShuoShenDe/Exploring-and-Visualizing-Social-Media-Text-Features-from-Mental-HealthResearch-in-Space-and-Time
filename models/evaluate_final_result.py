import pandas as pd
import numpy as np

if __name__ == "__main__":
    predict_path = '../predict/nyc_03082021_final_result.csv'
    df = pd.read_csv(predict_path)
    # df["AB"] = result
    # df.to_csv("./predict/predict_nyc_AB_.csv", index=False)
    list(df['AB']).count(0)
    add1 = np.add(df['AB'], df['LR'])
    add1 = np.add(add1, df['NB'])
    add1 = np.add(add1, df['RF'])
    add1 = np.add(add1, df['SVM'])
    print(list(df['SVM']).count(0))
    print(list(df['SVM']).count(1))
    print("0: %d" % list(add1).count(0))
    print("1: %d" % list(add1).count(1))
    print("2: %d" % list(add1).count(2))
    print("3: %d" % list(add1).count(3))
    print("4: %d" % list(add1).count(4))
    print("5: %d" % list(add1).count(5))

    df["final"] = np.where(add1 < 3, 0, 1)
    df.to_csv("../predict/nyc_03082021_final_result.csv", index=False)
