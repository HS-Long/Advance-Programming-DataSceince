import torch
from torchvision import datasets, transforms

def load_data(batch_size=64):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))        # ⬅ FIX: Normalize inputs
    ])

    train = datasets.MNIST(root="./mnist", train=True, download=True, transform=transform)
    test = datasets.MNIST(root="./mnist", train=False, download=True, transform=transform)

    train_loader = torch.utils.data.DataLoader(train, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader
