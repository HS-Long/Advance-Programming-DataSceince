from model.net import SimpleNet
from data.dataset import load_data
from trainer.train import train_model
import matplotlib.pyplot as plt


def main():
    train_loader, _ = load_data()
    model = SimpleNet()

    # Enable PDB debugging in first batch
    loss_history, acc_history = train_model(
        model, 
        train_loader,
        num_epochs=5,
        lr=0.001,
        debug=True
    )

    # Plot training curve
    plt.plot(loss_history)
    plt.title("Training Loss")
    plt.show()

    plt.plot(acc_history)
    plt.title("Training Accuracy")
    plt.show()


if __name__ == "__main__":
    main()
