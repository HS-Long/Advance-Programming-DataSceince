import torch
import torch.nn as nn
import torch.optim as optim
from utils.debug_tools import debug_here


def train_model(model, train_loader, num_epochs=20, lr=0.001, debug=False):

    criterion = nn.CrossEntropyLoss()      # ⬅ FIX: Correct loss function
    optimizer = optim.Adam(model.parameters(), lr=lr)

    loss_history = []
    acc_history = []

    for epoch in range(num_epochs):

        running_loss = 0
        correct = 0
        total = 0

        for batch_idx, (images, labels) in enumerate(train_loader):

            if debug and batch_idx == 0:
                # ⬅ Debug only first batch
                print("Debugging first batch tensors:")
                print("Images shape:", images.shape)
                print("Labels shape:", labels.shape)
                debug_here()

            outputs = model(images)

            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            _, predicted = outputs.max(1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total

        loss_history.append(epoch_loss)
        acc_history.append(epoch_acc)

        print(f"Epoch {epoch+1}/{num_epochs} - Loss: {epoch_loss:.4f}  Acc: {epoch_acc:.2f}%")

    return loss_history, acc_history
