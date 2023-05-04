import numpy as np
import torch
import matplotlib.pyplot as plt
from sklearn.datasets import make_s_curve

def generate_dataset(n, noise=0.1):
    s_curve,_ = make_s_curve(10**4,noise=noise)
    s_curve = s_curve[:,[0,2]]/10.0
    dataset = torch.Tensor(s_curve).float()
    data = s_curve.T

    fig,ax = plt.subplots()
    ax.scatter(*data,color='blue',edgecolor='white');

    ax.axis('off')
    plt.show()
    return dataset