import torch

def load_xor():
    X = torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
    y = torch.tensor([[0.],[1.],[1.],[0.]])   # must be column vector
    return X, y
