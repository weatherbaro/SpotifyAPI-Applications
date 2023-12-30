# Spotify MBTI Predictor

## Overview
Spotify MBTI Predictor is a Flask-based web application that integrates with the Spotify API to guess a user's Myers-Briggs Type Indicator (MBTI) personality type based on their recently played tracks. It analyzes various musical attributes like danceability, energy, and tempo to make predictions.

## Features

### Spotify Authentication
- Allows users to log in with their Spotify account and grant access to their recently played tracks. Understanding OAuth 2.0 and session management is beneficial.

### Musical Analysis
- Analyzes the user's musical tastes based on recent tracks to predict the MBTI type. Involves knowledge of data handling and algorithmic logic.

### MBTI Guess
- Displays the guessed MBTI type to the user based on the analyzed musical attributes. Requires understanding of user interface design and web development.

### API Integration
- Interacts with the Spotify API to fetch user data. Knowledge of RESTful services and HTTP protocol is necessary.

## Installation

### Prerequisites
- Python 3.6 or above
- Flask
- Requests library
- Spotify Account that you've been listening to music on

### Setting Up
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies
4. Set environment variables
5. Run the application

## Usage

1. **Start the Application:** Run the Flask server using the command above.
2. **Open Web Browser:** Navigate to http://localhost:5000 or the configured port.
3. **Log in with Spotify:** Use the 'Login' feature to authenticate with your Spotify account.
4. **View Your Predicted MBTI:** After the analysis, your predicted MBTI type will be displayed.

## Understanding the MBTI Prediction Process

The MBTI prediction process analyzes the musical attributes of a user's recently played tracks and maps them to the MBTI dimensions. Here's how the traits relate to each MBTI letter in the prediction logic:

### Introversion (I) / Extraversion (E)
- Extraversion is associated with higher levels of danceability, energy, and liveness. Predominantly high values in these traits lean towards "E" (Extraversion).
- Otherwise, it leans towards "I" (Introversion).

### Sensing (S) / Intuition (N)
- Intuition is related to a higher level of instrumentalness and tempo, and lower speechiness. Predominantly high or low values in these traits lean towards "N" (Intuition).
- Otherwise, it leans towards "S" (Sensing).

### Thinking (T) / Feeling (F)
- Feeling is associated with higher valence and lower speechiness. High value in valence or low in speechiness leans towards "F" (Feeling).
- Otherwise, it leans towards "T" (Thinking).

### Judging (J) / Perceiving (P)
- Judging is related to higher acousticness and speechiness, but lower tempo. Predominantly high or low values in these traits lean towards "J" (Judging).
- Otherwise, it leans towards "P" (Perceiving).

The MBTI type is formed by combining the individual predictions from each dimension. This is a novel way to engage users with music and psychology, providing a unique insight into how music preferences might reflect personality traits. Please note, the accuracy of this prediction might vary widely among individuals and is meant for entertainment and engagement purposes.
