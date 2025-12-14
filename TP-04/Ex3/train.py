import torch
import torch.nn as nn
import torch.optim as optim
from model import Net
from dataset import load_xor
import matplotlib.pyplot as plt

def train():

    X, y = load_xor()

    model = Net()
    criterion = nn.BCELoss()     # Correct loss for sigmoid output
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    losses = []
    accs = []

    for epoch in range(2000):
        y_pred = model(X)

        loss = criterion(y_pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

        predictions = (y_pred > 0.5).float()
        accuracy = (predictions == y).float().mean().item()
        accs.append(accuracy)

        if epoch % 200 == 0:
            print(f"Epoch {epoch} Loss: {loss.item():.4f} Acc: {accuracy:.2f}")

    # Plot training curve
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.plot(losses)
    plt.title("Loss Curve")

    plt.subplot(1,2,2)
    plt.plot(accs)
    plt.title("Accuracy Curve")

    plt.savefig("training_curve.png")
    print("\nSaved training_curve.png")

