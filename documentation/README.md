# Beats Meter

A simple yet powerful application to detect the beats per minute (BPM) of a song. This project provides two distinct interfaces for analyzing your audio files: a native desktop GUI and a local web application.

## Features

- **Accurate BPM Detection**: Utilizes the `librosa` library to perform robust beat tracking on audio files.
- **Multiple Interfaces**: Choose between a desktop application for native performance or a web interface for accessibility from your browser.
- **Broad Format Support**: Analyzes common audio formats like MP3, WAV, FLAC, and M4A (requires FFmpeg).
- **User-Friendly**: Both interfaces are designed to be simple and intuitive. Just pick a song and get the BPM instantly.

## Interfaces

### Desktop GUI

A clean and simple desktop application built with `customtkinter`. It provides a native file selection dialog and displays the BPM directly in the window. It's perfect for quick, local analysis.

### Web Application

A lightweight web interface powered by `Flask`. It runs a local server, allowing you to access the BPM analyzer from your web browser. It features a responsive design and a loading indicator during analysis.

## Technology Stack

- **Core Engine**: Python, Librosa, NumPy
- **Desktop GUI**: customtkinter
- **Web Application**: Flask

## Getting Started

To get this project running on your local machine, you'll need Python and FFmpeg installed. For a complete, step-by-step guide on setting up the project and installing all dependencies, please refer to the installation guide:

➡️ **Full Installation Guide**