# %%
import numpy as np


# %%
def rotate(x_old, y_old):
    r = np.sqrt(x_old*x_old + y_old*y_old)
    c = x_old/r
    s = y_old/r
    if x_old>0:
        return [-c, s]
    else:
        return [c, -s]

# %%
def rotate_action(x,y, goc):
    [c1,s1] = goc
    x_new = x*c1 -y*s1
    y_new = x*s1 + y*c1
    return [x_new,y_new]


