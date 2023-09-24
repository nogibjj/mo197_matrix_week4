"""
This should not run with python3.8 and above

"""

from pysurvival.models.semi_parametric import CoxPHModel
from pysurvival.models.multi_task import LinearMultiTaskModel

def build_coxph_model(X, T, E):
    coxph_model = CoxPHModel()
    coxph_model.fit(X=X, T=T, E=E, init_method='he_uniform',
                    l2_reg=1e-4, lr=.4, tol=1e-4)
    return coxph_model

def build_mtlr_model(X, T, E):
    mtlr_model = LinearMultiTaskModel()
    mtlr_model.fit(X=X, T=T, E=E, init_method='glorot_uniform',
                    optimizer='adam', lr=8e-4)
    return mtlr_model


