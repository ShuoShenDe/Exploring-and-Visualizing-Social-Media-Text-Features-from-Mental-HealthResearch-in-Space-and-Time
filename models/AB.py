from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score

from sklearn.metrics import confusion_matrix, accuracy_score
from read_data import read_csv, read_predic_csv
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import pandas as pd

# 0.992
if __name__ == "__main__":
    # X, y = make_classification(n_samples=1000, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
    training_path = '../predict/training.csv'
    features, label = read_csv(training_path)

    # print(label)
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=22, shuffle=True)
    X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, random_state=47, shuffle=True)
    model = AdaBoostClassifier(n_estimators=300, random_state=2, learning_rate=0.01, algorithm='SAMME.R')
    model.fit(X_train, y_train)

    print(model.score(X_train, y_train))
    print(model.score(X_eval, y_eval))
    evaluated_model(model, X_eval, y_eval)

    print(model.score(X_test, y_test))
    evaluated_model(model, X_test, y_test)


    predict_path = '../predict/predict_wdc_.csv'
    features_predict = read_predic_csv(predict_path)
    result = model.predict(features_predict)

    print(list(result).count(1))
    print(list(result).count(0))
    # evaluate the model
    # cv = RepeatedStratifiedKFold(n_splits=500, n_repeats=50, random_state=5)
    # n_scores = cross_val_score(model, features, label, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    # report performance
    # print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))

    df = pd.read_csv(predict_path)
    df["AB"] = result
    df.to_csv("../predict/predict_wdc_new_AB_.csv", index=False)
