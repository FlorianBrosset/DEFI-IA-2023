# DEFI-IA-2023

We have developed an algorithm that estimates the prices of nights in hotels of a travel agency. 
This algorithm was trained on the prices displayed during simulated bookings made on the agency's website with different features (hotel city, hotel brand, date of the request etc.). 
Once trained on these data, our algorithm takes as input the features of the booking request, and can predict the prices of the internal algorithm of the travel agency on unknown days.


## Features

- train our model your self with "train.py "
- select the features of your choice, and predict the prices of the internal algorithm of the travel agency on unknown days with "app.py"

see Usage section for commands
## Installation

To install our project run the following commands:

$git clone https://github.com/FlorianBrosset/DEFI-IA-2023


## Usage

Then , to train our model or launch the gradio application from the docker container, run the following commands:

$cd DEFI-IA-2023

$sudo docker build - < Dockerfile --tag [nom du dock]

$sudo docker run -it --name [nom du conteneur] -v [path actuel]:/workspace/[nom du dossier dans le conteneur] [nom du docker]

$cd workspace/[nom du dossier dans le conteneur]

$python app.py 

$python train.py 
