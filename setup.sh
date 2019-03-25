#/bin/bash

echo "Installing PIP"
sudo apt-get install python3-pip

echo "Installing Number-Python..."
sudo pip3 install numpy

echo "Installing Science-Python..."
sudo pip3 install scipy

echo "Installing Mathematical-Plotting-Library..."
sudo pip3 install matplotlib

echo "Installing Plotly..."
sudo pip3 install plotly

echo "Installing Science-Kit Learn..."
sudo pip3 install scikit-learn

echo "Installing Science-Kit Image..."
sudo pip3 install scikit-image

echo "Installing Open Computer-Vision..."
sudo pip3 install opencv-python

echo "Done!"
