# Audio Book

Audio Books are audio files. Basically a conversion tool of text (book) to audio (mp3).

## Features

Users have an option to either play the audio file on the spot or can be downloaded for future hearing.

## Prerequisites

- pyttsx3 (text to speech converter, used to play the audio on the spot)
- pypdf (pdf related library)
- gtts (text to speech converter, used to download the audio file)
- espeak (Linux OS)

## Installation

- First, install all the prerequisites as mentioned above.
    ```
    pip install pypdf
    pip install pyttsx3
    pip install gtts
    ```
    Creating a virtual environment and then installing all the prerequisites is recommended.
- For linux os, install espeak for pyttsx3 functionality.
