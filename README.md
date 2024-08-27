# Weather Alert System with Twilio Integration

This repository contains a Python script that uses the OpenWeatherMap API to check weather conditions and Twilio API to send SMS alerts if rain is expected. The script fetches weather data for a specified location and sends a notification if rain is predicted.

## Features

- Fetches weather forecast data from the OpenWeatherMap API.
- Checks if rain is expected based on weather conditions.
- Sends an SMS alert using the Twilio API if rain is expected.
- Configurable with environment variables for secure management of sensitive information.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `twilio`, `python-dotenv`
- OpenWeatherMap API key
- Twilio account credentials (Account SID, Auth Token, phone numbers)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/weather-alert-system.git
   cd weather-alert-system
