import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 897113152 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    alpha = 0.08

    cts = np.array([x_success, y_success])
    cnt = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(cts, cnt, alternative = 'smaller')
    
    return pval < alpha
