from sklearn.neighbors import NearestCentroid
from read_data import read_csv
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split

# 0.534
if __name__ == "__main__":
    # training_path='./code/bgd_mentalhealth/bgd_mentalhealth/training_data/train_features.csv'
    # training_features,training_label=read_csv(training_path)
    training_path = '../predict/training.csv'
    features, label = read_csv(training_path)
    # print(label)
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=32, shuffle=True)
    X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, random_state=47, shuffle=True)
    # features, label=read_csv()
    clf = NearestCentroid()
    clf.fit(X_train, y_train)
    print(clf.get_params())
    print(clf.score(X_train, y_train))

    evaluated_model(clf, X_test, y_test)
