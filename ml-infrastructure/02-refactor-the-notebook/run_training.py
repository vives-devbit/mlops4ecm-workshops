""" Script to train a new model. """
from data_utils import *
from model_utils import *
from train_utils import *
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--learning-rate", type=float, default=1e-3)
    parser.add_argument("--output", type=str, default="model.pth")
    args = parser.parse_args()

    # TODO Write code to train and save a model
    # Use the args parameters:
    # - args.batch_size
    # - args.learning_rate
    # - args.epochs
    # - args.output

    # TODO Load data and model

    # TODO Train model and print accuracy

    # TODO Save model to disk

if __name__ == "__main__":
    main()
