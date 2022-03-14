import numpy as np
from sklearn import preprocessing
# Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from read_data import read_csv, read_predic_csv
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import classification_report
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split
import pandas as pd

# 0.932
if __name__ == "__main__":
    # training_path='./code/bgd_mentalhealth/bgd_mentalhealth/training_data/train_features.csv'
    # training_features,training_label=read_csv(training_path)

    training_path = '../predict/training.csv'

    features, label = read_csv(training_path)
    # print(label)
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42, shuffle=True)
    X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, shuffle=True)

    # Create a Gaussian Classifier
    model = GaussianNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)

    print(model.score(X_train, y_train))

    cv = RepeatedStratifiedKFold(n_splits=50, n_repeats=5, random_state=2)
    n_scores = cross_val_score(model, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    # report performance
    print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))

    evaluated_model(model, X_eval, y_eval)
    print(model.score(X_test, y_test))

    predict_path = '../predict/predict_wdc_.csv'
    features_predict = read_predic_csv(predict_path)

    result = model.predict(features_predict)
    print(list(result).count(1))
    print(list(result).count(0))


    df = pd.read_csv('../predict/predict_wdc_new_AB_LR_.csv')
    df["NB"] = result
    df.to_csv("../predict/predict_wdc_new_AB_LR_NB.csv", index=False)
