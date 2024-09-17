import os
import json
import multiprocessing
import time
from random import randint

# Initialize the number of images and fits
image_number = 5  # Number of image files
fit_number = 3    # Number of fits per image

# Directory to save files (assuming current directory for simplicity)
output_dir = "outputs"
prediction_dir = "predictions"

# Create directories if they don't exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(prediction_dir, exist_ok=True)

# Function to save data to a JSON file
def save_to_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")

# Function to load data from a JSON file
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
    # Simulate some result based on fit_data
    result_data = {"fit_data": fit_data, "result": "some_calculated_result"}
    save_to_json(output_file, result_data)
    time.sleep(3)

def create_mock_prediction_files():
    for j in range(1, fit_number + 1):
        prediction_file = os.path.join(prediction_dir, f"file1_fit{j}.prediction.json")
        prediction_data = {"fit": f"some_fit_data_for_fit{j}_of_first_image"}
        save_to_json(prediction_file, prediction_data)

# Parallel processing function for fits within an image
def process_fits_for_image(image_index):
    parallel_pool = []

    for j in range(1, fit_number + 1):
        output_file = os.path.join(output_dir, f"file{image_index}_fit{j}.output.json")
        prediction_file = os.path.join(prediction_dir, f"file1_fit{j}.prediction.json")  # Prediction files are always from the first image

        print(f"Processing {output_file}...")

        # Check if prediction file exists (from first image)
        if does_prediction_file_exist(prediction_file):
            fit_data = load_previous_fit(prediction_file)
        else:
            fit_data = start_from_default_config()

        parallel_pool.append((output_file, fit_data))

    # Sequential processing of fits (inner loop), since outer loop is parallel
    for output_file, fit_data in parallel_pool:
        carry_out_magic_calculations(output_file, fit_data)

# Main workflow function to parallelize the outer loop
def main_workflow_loop():
    with multiprocessing.Pool() as pool:
        pool.map(process_fits_for_image, range(1, image_number + 1))

# Workflow start
if __name__ == "__main__":
    print("Starting X-ray diffraction workflow...")
    
    create_mock_prediction_files()

    start = time.perf_counter()
    # Enter the workflow loop
    main_workflow_loop()
    end = time.perf_counter()

    print("Workflow completed in", end - start, "seconds.")