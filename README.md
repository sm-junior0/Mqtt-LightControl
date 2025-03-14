# MQTT Light Control Web Application

## Overview

The MQTT Light Control project simulates a simple light control system using the MQTT protocol. Users can control a light (simulated by an ESP8266 device) through a web interface, sending MQTT messages to turn the light on or off.

## Features

- **Real-time Control**: Control the light in real-time using MQTT messages.
- **User-Friendly Interface**: A web-based interface for easy interaction.
- **Dark Mode**: Toggle between light and dark themes for better visibility.
- **Connection Status**: Visual indicators for connection status to the MQTT broker.

## How to Run

### Prerequisites

- Python 3.x installed on your machine.
- Internet connection for accessing the public MQTT broker.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sm-junior0/Mqtt-LightControl.git
   ```

2. **Install Dependencies**:    
   Make sure to install the required Python library:
   ```bash
   pip install paho-mqtt
   ```

3. **Run the Simulation**:
   Execute the `light_simulation.py` script to simulate the IoT device:
   ```bash
   python light_simulation.py
   ```

4. **Open the Web Interface**:
   Open `index.html` in your web browser to control the light.

## MQTT Broker

The application connects to a public MQTT broker at `ws://broker.hivemq.com:8000/mqtt`. You can change the broker URL in the JavaScript code if you want to use a different broker.

## Dependencies

- **Python Libraries**:
  - `paho-mqtt`: A Python library for MQTT.

- **Web Technologies**:
  - HTML
  - CSS
  - JavaScript
  - MQTT.js (for MQTT protocol)
  - Bootstrap (for styling)
  - Font Awesome (for icons)

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report issues, please feel free to submit a pull request or open an issue.

## Acknowledgments

- [MQTT.js](https://github.com/mqttjs/MQTT.js) for the MQTT client implementation.
- [Bootstrap](https://getbootstrap.com/) for responsive design.
- [Font Awesome](https://fontawesome.com/) for icons.
- [Paho MQTT](https://www.eclipse.org/paho/) for the Python MQTT client library.

---

This version of the README retains the original structure and content while ensuring clarity and simplicity. No additional features or complexities have been added. Let me know if you need further adjustments!