from sklearn import svm
from read_data import read_csv, read_predic_csv
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, accuracy_score
from evaluate_model import evaluated_model
from sklearn.model_selection import train_test_split
import pandas as pd

# 0.875

if __name__ == "__main__":
    # training_path='./code/bgd_mentalhealth/bgd_mentalhealth/training_data/train_features.csv'
    # training_features,training_label=read_csv(training_path)
    training_path = '../predict/training.csv'

    features, label = read_csv(training_path)
    # print(label)
    X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42, shuffle=True)
    X_train, X_eval, y_train, y_eval = train_test_split(X_train, y_train, test_size=0.25, shuffle=True)

    model = svm.SVC(probability=True, kernel='linear')

    model.fit(X_train, y_train)
    print(model.coef_)
    print(model.score(X_train, y_train))
    print(model.score(X_eval, y_eval))
    print(model.score(X_test, y_test))
    evaluated_model(model, X_test, y_test)

    predict_path = '../predict/predict_wdc_.csv'
    features_predict = read_predic_csv(predict_path)

    result = model.predict(features_predict)
    print(list(result).count(1))
    print(list(result).count(0))

    df = pd.read_csv("../predict/predict_wdc_new_AB_LR_NB_RF.csv")
    df["SVM"] = result
    df.to_csv("../predict/predict_wdc_new_AB_LR_NB_RF_SVM.csv", index=False)
