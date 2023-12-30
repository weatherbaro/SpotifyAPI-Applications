# Spotify MBTI Predictor

## Overview
Spotify MBTI Predictor is a Flask-based web application that integrates with the Spotify API to guess a user's Myers-Briggs Type Indicator (MBTI) personality type based on their recently played tracks. It analyzes various musical attributes like danceability, energy, and tempo to make predictions.

## Features
- **Spotify Authentication**: Allows users to log in with their Spotify account and grant access to their recently played tracks. Understanding OAuth 2.0 and session management is beneficial.
- **Musical Analysis**: Analyzes the user's musical tastes based on recent tracks to predict the MBTI type. Involves knowledge of data handling and algorithmic logic.
- **MBTI Guess**: Displays the guessed MBTI type to the user based on the analyzed musical attributes. Requires understanding of user interface design and web development.
- **API Integration**: Interacts with the Spotify API to fetch user data. Knowledge of RESTful services and HTTP protocol is necessary.

## Installation

### Prerequisites
- Python 3.6 or above
- Flask
- Requests library
- Spotify Account that you've been listening to music on

### Setting Up

1. **Clone the repository**
2. **Navigate to the project directory**
3. **Install dependencies**
4. **Set environment variables**
5. **Run the application**


## Usage
1. **Start the Application**: Run the Flask server using the command above.
2. **Open Web Browser**: Navigate to `http://localhost:5000` or the configured port.
3. **Log in with Spotify**: Use the 'Login' feature to authenticate with your Spotify account.
4. **View Your Predicted MBTI**: After the analysis, your predicted MBTI type will be displayed.
