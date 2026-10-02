# EDITH - Personal Voice Assistant 🤖

EDITH is a Python-based personal voice assistant that combines voice interaction with a web-based dashboard. The project uses a Flask backend and REST APIs to connect the assistant functionality with a browser-based interface.

## 🚀 Features

- Voice-based interaction
- Text-to-speech responses
- Flask backend
- REST API integration
- Web-based dashboard
- Frontend and backend communication
- Audio processing
- Assistant command handling
- Setup and configuration documentation

## 🛠️ Technologies Used

- Python
- Flask
- REST APIs
- HTML
- CSS
- JavaScript
- Text-to-Speech
- Voice / Audio Processing

## 🏗️ Architecture

```text
                 ┌──────────────────────┐
                 │    Web Dashboard     │
                 │   HTML / JS / CSS    │
                 └──────────┬───────────┘
                            │
                         REST API
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Flask Server      │
                 │  edith_server.py     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   EDITH Assistant    │
                 │       Python         │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Voice / Audio Layer  │
                 │  Speech Processing   │
                 └──────────────────────┘

⚙️ Installation 
1. Clone the repository
git clone https://github.com/HemanthVadakattu1342/EDITH.git
2. Navigate to the project
cd EDITH
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
5. Install dependencies
pip install -r requirements.txt
6. Start the Flask server
python edith_server.py

Open the local address provided by Flask in your browser.

🖥️ How It Works
The user interacts with the EDITH assistant.
Voice/audio input is processed by the Python application.
The Flask server provides communication between the assistant and the web dashboard.
REST API endpoints allow the frontend to communicate with the backend.
EDITH processes the requested operation and provides a response.
Text-to-speech functionality is used for voice responses where configured.
🔧 Configuration

Depending on the current implementation, some components may require additional configuration such as:

Python dependencies
Audio input/output configuration
Text-to-speech configuration
API configuration
Environment variables

Refer to the project files and setup instructions before running the application.

🧪 Troubleshooting
Audio or Text-to-Speech Issues

Check that:

Required Python packages are installed.
The system has access to the required audio devices.
The configured text-to-speech engine is available.
Python has the required permissions to access audio devices.
Flask Server Issues

Verify that:

The virtual environment is activated.
All dependencies are installed.
The correct Python file is being executed.
The configured port is available.
🔮 Future Improvements
Add more voice commands
Improve natural-language interaction
Add authentication to the web dashboard
Improve error handling
Add persistent user preferences
Add additional APIs and integrations
Improve the user interface
Add automated testing
