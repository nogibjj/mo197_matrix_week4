"""
1. Run test so that Python 3.8 and fails
"""

# main.py
from pysurvival.datasets import Dataset
from pysurvival.utils.metrics import concordance_index
from src.survival import build_coxph_model, build_mtlr_model

def main():
    # Loading and splitting a simple example into train/test sets
    X_train, T_train, E_train, X_test, T_test, E_test = \
        Dataset('simple_example').load_train_test()

    # Checking the model performance for CoxPH model
    coxph_model = build_coxph_model(X_train, T_train, E_train)
    c_index1 = concordance_index(model=coxph_model, X=X_test, T=T_test, E=E_test)
    print("CoxPH model c-index = {:.2f}".format(c_index1))

    # Checking the model performance for MTLR model
    mtlr_model = build_mtlr_model(X_train, T_train, E_train)
    c_index2 = concordance_index(model=mtlr_model, X=X_test, T=T_test, E=E_test)
    print("MTLR model c-index = {:.2f}".format(c_index2))

if __name__ == "__main__":
    main()
