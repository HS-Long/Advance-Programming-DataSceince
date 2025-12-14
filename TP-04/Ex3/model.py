import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1)
        self.sigmoid = nn.Sigmoid()   # Correct for binary classification

    def forward(self, x):
        x = nn.ReLU()(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x
