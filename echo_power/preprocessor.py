
import numpy as np

def normalize_signal(v, i):
    v_norm = (v - np.mean(v)) / np.std(v)
    i_norm = (i - np.mean(i)) / np.std(i)
    return np.expand_dims(np.stack([v_norm, i_norm], axis=-1), axis=0)
