import numpy as np


def calculate(data):
    if len(data) != 9:
        print("List must contain nine numbers.")

    
    a = np.array(data).reshape(3, 3)

    
    statistics = {}
    for stat in ['mean', 'var', 'std', 'max', 'min', 'sum']:
        statistics[stat] = [
            getattr(np, stat)(a, axis=0).tolist(),
            getattr(np, stat)(a, axis=1).tolist(),
            getattr(np, stat)(a.flatten()).tolist()
        ]

    return statistics


