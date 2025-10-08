# Installation Guide

Follow these steps to set up and run the Beats Meter project on your local machine.

## Prerequisites

1.  **Python**: You need Python 3.8 or newer. You can download it from [python.org](https://www.python.org/downloads/).

2.  **FFmpeg**: The `librosa` library, which this project uses for audio analysis, requires FFmpeg to decode various audio formats like MP3.
    -   **Windows**: Download the binaries from ffmpeg.org and add the `bin` directory to your system's PATH.
    -   **macOS**: Install via Homebrew: `brew install ffmpeg`
    -   **Linux**: Install using your package manager, e.g., `sudo apt-get install ffmpeg` on Debian/Ubuntu.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Beats-meter
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Install all the required Python packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

This project has two interfaces: a desktop GUI and a web app.

### To run the Desktop GUI:
```bash
python main.py
```

### To run the Web Interface:
```bash
python web_app.py
```
Then, open your web browser and go to `http://127.0.0.1:5000`.