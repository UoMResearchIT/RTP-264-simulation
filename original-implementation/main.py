import os
import json

from random import randint
from time import sleep


# Initialize the number of images and fits
image_number = 5  # Number of image files
fit_number = 3    # Number of fits per image

# Directory to save files (assuming current directory for simplicity)
output_dir = "outputs"
prediction_dir = "predictions"

# Create directories if they don't exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(prediction_dir, exist_ok=True)

# Initialize lists for prediction and output file paths
prediction_files = []
output_files = []

# Generate the output files for all images and fits, and prediction files only for the first image
for i in range(1, image_number + 1):
    for j in range(1, fit_number + 1):
        output_file = os.path.join(output_dir, f"file{i}_fit{j}.output.json")
        output_files.append(output_file)
        
        # Prediction files are only generated for the first image (i=1), for all fits
        if i == 1:
            prediction_file = os.path.join(prediction_dir, f"file{i}_fit{j}.prediction.json")
            prediction_files.append(prediction_file)

# Function to save data to a JSON file
def save_to_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")

def load_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    print(f"Data loaded from {file_path}")
    return data

# Function to check if a prediction file exists
def does_prediction_file_exist(prediction_file):
    return os.path.exists(prediction_file)

# Function to start from default config
def start_from_default_config():
    print("Starting from default configuration...")
    return {"config": "default"}

# Function to load the previous fit
def load_previous_fit(prediction_file):
    print(f"Loading previous fit from {prediction_file}...")
    return load_from_json(prediction_file)

# Function to carry out calculations and save them to an output file
def carry_out_magic_calculations(output_file, fit_data):
    print(f"Carrying out magic calculations for {output_file}...")
    result_data = {"fit_data": fit_data, "result": "some_calculated_result"}
    save_to_json(output_file, result_data)
    sleep(randint(1,5))

def create_mock_prediction_files():
    print(prediction_files)
    for prediction_file in prediction_files:
        prediction_data = {"fit": "some_fit_data_for_first_image"}
        save_to_json(prediction_file, prediction_data)

# Main workflow loop to process each file
def main_workflow_loop():
    for i in range(1, image_number + 1):
        for j in range(1, fit_number + 1):
            output_file = os.path.join(output_dir, f"file{i}_fit{j}.output.json")
            prediction_file = os.path.join(prediction_dir, f"file1_fit{j}.prediction.json")  # Prediction files are always from the first image

            print(f"Processing {output_file}...")

            # Check if prediction file exists (from first image)
            if does_prediction_file_exist(prediction_file):
                fit_data = load_previous_fit(prediction_file)
            else:
                fit_data = start_from_default_config()

            # Perform calculations after loading or configuring
            carry_out_magic_calculations(output_file, fit_data)

# Workflow start
if __name__ == "__main__":
    print("Starting X-ray diffraction workflow...")

    # Create mock prediction files for the first image
    create_mock_prediction_files()

    # Enter the workflow loop
    main_workflow_loop()

    print("Workflow completed.")