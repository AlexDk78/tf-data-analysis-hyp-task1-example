import pandas as pd
import numpy as np


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    import scipy.stats as stats
    alpha = 0.08
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    se = ((p1 * (1 - p1)) / x_cnt + (p2 * (1 - p2)) / y_cnt) ** 0.5
    z = (p1 - p2) / se
    z_crit = abs(stats.norm.ppf(alpha / 2))
    if abs(z) > z_crit:
        return True
    else:
        return False
