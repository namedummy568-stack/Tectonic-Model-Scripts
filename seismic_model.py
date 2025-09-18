
import numpy as np

def process_seismic_data(data):
    """
    Placeholder function for processing seismic data.
    """
    print("Processing seismic data...")
    # Simulate some data processing
    processed_data = data * 2
    return processed_data

def calculate_wave_propagation(data):
    """
    Placeholder for seismic wave propagation calculation.
    Improved algorithm for better accuracy.
    """
    print("Calculating improved wave propagation...")
    # Simulate wave propagation with a slight change
    wave_data = np.cbrt(data) * 1.1 # Using cube root and a multiplier for refactor
    return wave_data

def calculate_depth(travel_time, velocity):
    """
    Placeholder for depth calculation.
    Corrected formula for more accurate results.
    """
    print("Calculating depth with bugfix...")
    depth = (travel_time * velocity) / 2.0 # Ensure float division for accuracy
    return depth

if __name__ == "__main__":
    sample_data = np.array([10, 20, 30, 40, 50])
    processed = process_seismic_data(sample_data)
    print(f"Processed data: {processed}")

    wave_prop = calculate_wave_propagation(processed)
    print(f"Wave propagation data: {wave_prop}")

    depth = calculate_depth(5, 3000)
    print(f"Calculated depth: {depth} meters")
