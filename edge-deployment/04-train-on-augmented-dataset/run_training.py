""" Script to train a new model. """
from data_utils import *
from model_utils import *
from train_utils import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--learning-rate", type=float, default=5e-4)
    parser.add_argument("--output", type=str, default="model.pth")
    parser.add_argument("--synthetic", action="store_true", help="Include synthetic data in training set")
    args = parser.parse_args()

    # Load data
    classes = get_classes()
    train_loader, val_loader = get_loaders(batch_size=args.batch_size, include_synthetic=args.synthetic)

    # Create model
    model = create_model(len(classes))

    # Train model
    train_model(model, train_loader, learning_rate=args.learning_rate, epochs=args.epochs)

    # Evaluate
    accuracy = evaluate_model(model, val_loader)
    print(f"Validation accuracy: {accuracy:.2%}")

    # Save model
    save_model(model, args.output)
    print(f"Model saved to {args.output}")

if __name__ == "__main__":
    main()
