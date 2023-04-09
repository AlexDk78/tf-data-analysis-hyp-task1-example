import pandas as pd
import numpy as np


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    import math
    from scipy.stats import norm
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (p1*x_cnt + p2*y_cnt) / (x_cnt + y_cnt)
    z = (p1 - p2) / math.sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
    alpha = 0.08
    z_alpha_2 = norm.ppf(1-alpha/2)
    return abs(z) > z_alpha_2
