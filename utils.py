import sklearn
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score,average_precision_score,balanced_accuracy_score
import pandas 

def evaluation_metrics(y_predt,y_test,is_print=False,print_and_return=False):
    '''
    Takes as two argument 'y_pred' and 'y_test' and return or print the evaluation metrics.
    '''
    acc_score=accuracy_score(y_pred=y_predt,y_true=y_test)
    conf_mat=confusion_matrix(y_pred=y_predt,y_true=y_test)
    f1_scr=f1_score(y_pred=y_predt,y_true=y_test)
    avg_pres_score=average_precision_score(y_score=y_predt,y_true=y_test)
    bal_acc_score=balanced_accuracy_score(y_pred=y_predt,y_true=y_test)
    
    if is_print == True:
        print("-"*45)
        print("Evaluation Metrics")
        print("-"*45)
        print(f"Accuracy Score:{acc_score}")
        print(f"Balanced Accuracy Score:{bal_acc_score}")
        print(f"F1-Score:{f1_scr}")
        print(f"Average Precision Score:{avg_pres_score}")
        print(f"Confusion Matrix:\n{conf_mat}")
        print("-"*45)
    
    elif print_and_return == True:
        print("-"*45)
        print("Evaluation Metrics")
        print("-"*45)
        print(f"Accuracy Score:{acc_score}")
        print(f"Balanced Accuracy Score:{bal_acc_score}")
        print(f"F1-Score:{f1_scr}")
        print(f"Average Precision Score:{avg_pres_score}")
        print(f"Confusion Matrix:\n{conf_mat}")
        print("-"*45)

        return acc_score,bal_acc_score,f1_scr,avg_pres_score,conf_mat
    
    else:
        return acc_score,bal_acc_score,f1_scr,avg_pres_score,conf_mat


