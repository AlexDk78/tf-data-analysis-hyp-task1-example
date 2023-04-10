import pandas as pd
import numpy as np
from scipy import stats
import math

chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    alpha=0.08
    
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    difference = p1 - p2
 
    z_value = difference / math.sqrt(
        p_combined * (1 - p_combined) * (1 / x_success + 1 / y_success)
    ) 
    distr = stats.norm(0, 1)  
    
    p_value = (1 - distr.cdf(abs(z_value))) * 2 
    
    if (p_value < alpha):
      return True
    else: 
      return False
