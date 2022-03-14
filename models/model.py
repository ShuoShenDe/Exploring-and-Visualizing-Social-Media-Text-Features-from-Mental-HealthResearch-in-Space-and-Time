from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from read_data import read_csv, read_predic_csv
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn import svm

training_path = '../predict/training.csv'
features, label = read_csv(training_path)
x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=22, shuffle=True)
x_train, x_eval, y_train, y_eval = train_test_split(x_train, y_train, test_size=0.25, random_state=47, shuffle=True)
predict_path = '../predict/nyc_03082021_final.csv'

features_predict = read_predic_csv(predict_path)
df = pd.read_csv(predict_path)

output_path ="../predict/nyc_03082021_final_result.csv"

def AB_model():
    model = AdaBoostClassifier(n_estimators=300, random_state=2, learning_rate=0.01, algorithm='SAMME.R')
    model.fit(x_train, y_train)
    print("AB model")
    print("train accuracy ", model.score(x_train, y_train))
    print("evaluate accuracy ", model.score(x_eval, y_eval))
    print("test accuracy ", model.score(x_test, y_test))
    result = model.predict(features_predict)
    df["AB"] = result


def LR():
    model = LogisticRegression(solver='liblinear', penalty='l1', tol=1e-5, max_iter=100).fit(x_train, y_train)
    print("LR model")

    print("train accuracy ", model.score(x_train, y_train))
    print("evaluate accuracy ", model.score(x_eval, y_eval))
    # evaluated_model(model, x_test, y_test)
    print("test accuracy ", model.score(x_test, y_test))
    result = model.predict(features_predict)
    df["LR"] = result


def NB_model():
    print("NB model")
    # Create a Gaussian Classifier
    model = GaussianNB()
    # Train the model using the training sets
    model.fit(x_train, y_train)
    cv = RepeatedStratifiedKFold(n_splits=50, n_repeats=5, random_state=2)
    n_scores = cross_val_score(model, x_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    print("train accuracy ", model.score(x_train, y_train))
    print("evaluate accuracy ", model.score(x_eval, y_eval))
    # report performance
    # print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))
    # evaluated_model(model, x_eval, y_eval)
    print("test accuracy ", model.score(x_test, y_test))
    result = model.predict(features_predict)
    df["NB"] = result


def RF_model():
    print("RF model")

    # define the model
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    # evaluate the model
    # cv = RepeatedStratifiedKFold(n_splits=30, n_repeats=5, random_state=3)
    # n_scores = cross_val_score(model, x_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    # report performance
    print("train accuracy", model.score(x_train, y_train))
    print("evaluate accuracy", model.score(x_eval, y_eval))
    print("test accuracy ", model.score(x_eval, y_eval))
    evaluated_model(model, x_test, y_test)
    result = model.predict(features_predict)
    df["RF"] = result


def SVM():
    model = svm.SVC(probability=True, kernel='linear')
    model.fit(x_train, y_train)
    print("SVM model")

    print("train accuracy ", model.score(x_train, y_train))
    print("evaluate accuracy ", model.score(x_eval, y_eval))
    print("test accuracy ", model.score(x_test, y_test))
    result = model.predict(features_predict)
    df["SVM"] = result


if __name__ == "__main__":
    AB_model()
    LR()
    NB_model()
    RF_model()
    SVM()
    df.to_csv(output_path, index=False)
