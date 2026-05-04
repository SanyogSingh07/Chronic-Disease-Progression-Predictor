import numpy as np

def create_sequences(data, target_index, seq_len=5):
    X, y = [], []

    for i in range(len(data) - seq_len):
        X.append(data[i:i+seq_len].flatten())
        y.append(data[i+seq_len, target_index])

    return np.array(X), np.array(y)
