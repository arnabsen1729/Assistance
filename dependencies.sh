#!/bin/bash

#Speech Recognition
sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
pip3 install pyaudio # pip install pyaudio
pip3 install SpeechRecognition

# For testing you can run
# python3 -m speech_recognition