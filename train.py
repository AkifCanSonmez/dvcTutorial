import argparse
import os
from architecture import create_model

def train_model(model, version):
    # Add your training logic here
    # For demonstration, let's assume the model training is complete

    # Save the trained model in a versioned directory
    model_save_path = os.path.join("models", version)
    print(model_save_path)
    os.makedirs(model_save_path, exist_ok=True)
    #model.save(os.path.join(model_save_path, 'model.h5'))
    print(f"Model saved in {model_save_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a model and save it with versioning.')
    parser.add_argument('version', type=str, help='Version tag for the model and dataset.')

    args = parser.parse_args()
    model = create_model()
    # Create and compile the model
    train_model(model, args.version)