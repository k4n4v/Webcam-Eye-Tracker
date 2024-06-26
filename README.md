# Early Alzheimer's Detection Project Using Eye Tracking

## Background
Alzheimer's disease (AD) is the most common form of dementia, a neurodegenerative disease that causes brain damage and ultimately death. Currently, diagnosis usually does not occur until the disease is in the late stages and behavioral changes begin to occur. Most pathophysiological changes are difficult to detect until after death, but research indicates that the eyes can be used as a "window into the brain" to help with earlier detection. This can be done through the observation of eye saccades which are the which are quick, simultaneous movements of the eyes in a given direction.

## About
This project aims to create an inexpensive eye tracking system for the observation of eye saccades. From there, connections can be made to data about regular eye saccades and eye saccades in patients with AD to assist in diagnosis. The program analyzes video recordings of participants' eyes during an eye test, generating a detailed PDF report that includes the percentage of irregular saccadic movements based on established academic criteria.

This project includes a prototype head-chin rest stand, 3D printed for flexibility and cost-effectiveness, equipped with a computer webcam for precise eye movement recording.

## Features
- **Eye Tracking**: Utilizes video input to track eye movements
- **Saccade Detection**: Analyzes eye movement data to identify and report saccades.
- **Report Generation**: Generates a detailed PDF report based on the eye tracking analysis, including metrics on saccade movements.
- **Customizable Exam Setup**: Allows users to configure parameters for different test scenarios.

## Built With
- Python
- OpenCV
- MATLAB

## Installation

### Prerequisites
- Python 3.x
- Pip

Note: The program is configured to the physical prototype designed specifications. For accurate results, use the example videos provided in `\samples`. If you would like to run your own trials or adapt the software to different setups, please contact me.

### Set Up
1. Clone the repository to your local machine.
   ```sh
   git clone https://github.com/k4n4v/Early-AD-Detection-Capstone
   ```
2. Enter folder
   ```sh
   cd Early-AD-Detection-Capstone
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
Enter the following command in the terminal:
   ```sh
   python main.py
   ```

## Disclaimer
This project is a prototype developed for educational purposes as part of the University of Guelph's ENGG41x0 capstone project. It is not intended to be used as real medical software or provide medical advice. Users should exercise caution and not rely on this software for any medical or diagnostic purposes.
