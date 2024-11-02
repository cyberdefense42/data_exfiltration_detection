# Data Exfiltration Detection System

A machine learning-powered system for detecting potential data exfiltration attempts in network traffic. This project uses Random Forest classification to identify suspicious network activities and provides a real-time monitoring interface.

## Table of Contents
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Real-time Detection: Analyze network traffic patterns in real-time
- High Accuracy: 94% precision in detecting potential data exfiltration attempts
- User-friendly Interface: Web-based dashboard for easy monitoring
- Visualizations: Interactive charts showing traffic patterns and threat probabilities
- Easy Integration: RESTful API for seamless integration with existing security systems

## System Architecture

The system consists of three main components:

1. Data Generation & Training Module
   - Simulates network traffic data
   - Trains Random Forest model
   - Performs feature engineering

2. Detection Engine
   - Processes incoming network logs
   - Makes real-time predictions
   - Calculates threat probabilities

3. Web Interface
   - Real-time monitoring dashboard
   - Interactive visualizations
   - Alert system

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. Clone the repository
```bash
git clone https://github.com/vishalsharma1987/data_exfiltration_detection.git
cd data_exfiltration_detection
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

```bash
python src/train_model.py
```

This will:
- Generate synthetic network traffic data
- Train the Random Forest model
- Save the model and necessary files

### Running the Application

```bash
python src/app.py
```

Access the web interface at: `http://localhost:5000`

### Using the Dashboard

1. Input network log data:
   - Source/Destination IP
   - Ports
   - Protocol
   - Bytes transferred
   - Action taken

2. View Results:
   - Real-time prediction
   - Threat probability
   - Historical trend chart

## Model Performance

Our model achieves the following metrics:

- Precision: 0.94
- Recall: 0.92
- F1-Score: 0.93
- Accuracy: 0.99

Top predictive features:
1. Bytes sent
2. Destination port
3. Time of day
4. Protocol type
5. Source port

## API Reference

### Prediction Endpoint

```http
POST /predict
```

Request body:
```json
{
    "timestamp": "2023-11-02T10:30:00",
    "source_ip": "192.168.1.100",
    "destination_ip": "203.0.113.1",
    "source_port": 54321,
    "destination_port": 443,
    "protocol": "TCP",
    "bytes_sent": 1500,
    "bytes_received": 500,
    "action": "allow"
}
```

Response:
```json
{
    "prediction": 0,
    "probability": 0.12
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Vishal Sharma - [your.email@example.com](mailto:vishal.sharma@whu.edu)

Project Link: [https://github.com/vishalsharma1987/data_exfiltration_detection](https://github.com/vishalsharma1987/data_exfiltration_detection)

## Acknowledgments

- Scikit-learn team for their excellent machine learning library
- Flask team for the web framework
- All contributors who spend time to help improve this project
