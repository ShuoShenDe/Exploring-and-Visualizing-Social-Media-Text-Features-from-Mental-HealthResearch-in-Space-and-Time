from sklearn.linear_model import LogisticRegression
from read_data import read_csv, read_predic_csv
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split
import pandas as pd

# 0.955
if __name__ == "__main__":
    # training_path='./code/bgd_mentalhealth/bgd_mentalhealth/training_data/train_features.csv'
    # training_features,training_label=read_csv(training_path)
    training_path = '../predict/training.csv'

    features, label = read_csv(training_path)

    # print(label)
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2,  shuffle=True)
    X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, shuffle=True)

    model = LogisticRegression(solver='liblinear', penalty='l1', tol=1e-5, max_iter=100).fit(X_train, y_train)
    # print(model.coef_)
    print(model.score(X_train, y_train))
    print(model.score(X_eval, y_eval))
    evaluated_model(model, X_test, y_test)

    predict_path = '../predict/predict_wdc_.csv'
    features_predict = read_predic_csv(predict_path)
    result = model.predict(features_predict)
    print(list(result).count(1))
    print(list(result).count(0))


    df = pd.read_csv('../predict/predict_wdc_new_AB_.csv')
    df["LR"] = result
    df.to_csv("../predict/predict_wdc_new_AB_LR_.csv", index=False)
