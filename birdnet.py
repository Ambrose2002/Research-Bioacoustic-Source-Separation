from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import sys
import os
import csv

# Load and initialize the BirdNET-Analyzer models.

curr_date = datetime.today()
analyzer = Analyzer()

def analyze():
    """
    Analyze a recording file and print the detected bird species.
    
    Precondition: 
    - The recording file path must be provided as a command-line argument
    
    
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError("incorrect number of arguments")
        
        file_path = sys.argv[1]
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        recording = Recording(
            analyzer,
            file_path,
            lat=42.454803,
            lon=-76.473666,
            # date=datetime(year=curr_date.year, month=curr_date.month, day=curr_date.day), 
            min_conf=0.1,
        )
        recording.analyze()

        print(recording.detections)
    
        fields = recording.detections[0].keys()
        fields = [val for val in fields]
        print(fields)
        with open(file_path[:-4] + ".csv", "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = fields)
            
            writer.writeheader()
            writer.writerows(recording.detections)
        
    except FileNotFoundError as fe:
        print("File not found")
            
analyze()
