
from read_data import read_csv
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.metrics import classification_report

def evaluated_model(model,X_test,y_test):
    # test_path='./code/bgd_mentalhealth/bgd_mentalhealth/training_data/eva_features.csv'
    # test_features,test_label=read_csv(test_path)

    
    predicted = model.predict(X_test)
    print('predict and ture value')
    print(predicted[:100])
    print(y_test[:100])

    print('model score: %.3f' % (model.score(X_test,y_test)))
    print('Accuracy_score: %.3f' % (accuracy_score(y_test, predicted)))
    # predict_prob = model.predict_proba(test_features)
    # print(predict_prob)
    matrix=confusion_matrix(y_test, predicted, normalize='all')
    print(matrix)
    print(classification_report(y_test, predicted, target_names=['health','unhealth']))