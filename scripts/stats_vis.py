# using session-stats, this tries to combine files to make cool graphs
import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import re 
# Directory where JSON files are stored
directory = 'stats'
graphs_dir = 'graphs'

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def load_data():
    # Initialize a dictionary to collect all data
    all_data = defaultdict(lambda: defaultdict(list))

    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.startswith('stats') and filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                print(f"reading {filename}")
                data = json.load(file)
                # Collect data for each time point
                for timestamp, stats in data['data'].items():
                    for key, value in stats.items():
                        all_data[key][timestamp].append(value)
    return all_data

# Example plot code
def create_plot(data, metric, plot_name):
    plt.figure(figsize=(10, 6))
    sorted_data = sorted(data.items())

    for timestamp, value_list in sorted_data:
            avg_value = sum(value_list) / len(value_list)
            plt.plot(timestamp, avg_value, 'o-', label=metric)

    # Rotate x-axis labels
    plt.xticks(rotation=45, ha="right")

    # Set plot title and labels
    plt.title(f"{metric} Over Time")
    plt.xlabel("Time")
    plt.ylabel(metric)
    plt.tight_layout()

    # Save or show the plot
    save_or_show_plot( plot_name)

def save_or_show_plot(plot_name):
    # Ensure the 'graphs' directory exists
    os.makedirs(graphs_dir, exist_ok=True)

    # Check if the 'agg' backend is being used
    if plt.get_backend() == 'agg':
        safe_plot_name = sanitize_filename(plot_name)
        # Save the plot as a PNG file in the 'graphs' directory
        plt.savefig(os.path.join(graphs_dir, f"{safe_plot_name}.png"))
    else:
        # Show the plot
        plt.show()
    plt.close()

def extract_datetime_from_filename(filename):
    # Extract date and time from filename (format: stats_YYYY_MM_DD_HH_MM.json)
    base_name = os.path.splitext(filename)[0]
    _, year, month, day, hour, minute = base_name.split('_')
    return datetime(int(year), int(month), int(day), int(hour), int(minute))


def main():
    all_data = load_data()

    for metric, data in all_data.items():
        create_plot(data, metric, metric)

if __name__ == "__main__":
    main()
