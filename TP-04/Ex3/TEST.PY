# file: src/train.py (BROKEN VERSION)

import torch
import torch.nn as nn
import torch.optim as optim
import pdb

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        pdb.set_trace()  # Debug: Network initialization
        self.fc = nn.Linear(2, 1)
        self.relu = nn.ReLU()   # ❌ Wrong activation for binary classification

    def forward(self, x):
        pdb.set_trace()  # Debug: Forward pass
        return self.relu(self.fc(x))   # ❌ Wrong output activation

# Fake dataset: XOR
X = torch.tensor([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y = torch.tensor([0.,1.,1.,0.])     # labels not reshaped

pdb.set_trace()  # Debug: Before model and training setup
model = Net()
criterion = nn.CrossEntropyLoss()   # ❌ Wrong loss for binary
optimizer = optim.SGD(model.parameters(), lr=1.0)   # ❌ Too high LR

for epoch in range(2000):
    if epoch == 0:
        pdb.set_trace()  # Debug: First epoch - check shapes and loss
    y_pred = model(X)

    loss = criterion(y_pred, y)    # ❌ Shape mismatch
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(epoch, loss.item())
