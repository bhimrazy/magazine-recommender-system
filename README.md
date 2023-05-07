# Magazine Recommender System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project implements a magazine recommender system using [Amazon review data from 2018](https://nijianmo.github.io/amazon/) . The system calculates similarity scores between magazines and recommends the most similar magazines to the user.

## Table of Contents

- [Magazine Recommender System](#magazine-recommender-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Data Preprocessing](#data-preprocessing)
  - [Recommendation Algorithm](#recommendation-algorithm)
  - [Web Interface](#web-interface)
  - [Future Work](#future-work)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This project implements a magazine recommender system using Amazon review data from 2018. The system is designed to recommend magazines to users based on their interests and preferences. The recommender system calculates similarity scores between magazines using the cosine similarity metric and recommends the most similar magazines to the user.

The project also includes a web interface that allows users to enter their ratings for magazines and receive recommendations for similar magazines. The web interface was implemented using FastAPI and Tailwind CSS.

## Getting Started

### Prerequisites

To run this project, you need to have Python 3.7 or later installed on your system. You also need to have the following packages installed:

- pandas
- scikit-learn
- numpy
- fastapi
- uvicorn
- tailwind

### Installation

1. Clone the repository

```sh
git clone https://github.com/bhimrazy/magazine-recommender-system.git
cd magazine-recommender-system
cd web
```

2. Install the required packages using pip

```sh
pip install -r requirements.txt
```

### Usage

To run the web interface, use the following command:

```sh
uvicorn main:app --reload
```

The web interface should now be accessible in your web browser at `http://localhost:8000/`.

## Data Preprocessing

The Amazon review data was preprocessed as follows:

1. Filtered the data to only include reviews for magazines.
2. Removed duplicate reviews.
3. Tokenized the review text and removed stop words.
4. Used the TF-IDF algorithm to calculate the similarity scores between magazines.

## Recommendation Algorithm

The recommender system uses the cosine similarity metric to calculate the similarity scores between magazines. The most similar magazines are recommended to the user based on their ratings of other magazines.

## Web Interface

The web interface was implemented using FastAPI and Tailwind CSS. The user can enter their ratings for magazines and receive recommendations for similar magazines. The recommendations are updated dynamically as the user enters their ratings.

## Future Work

Some potential areas for future work on this project include:

- Evaluating the performance of the recommender system using metrics such as precision, recall, and F1 score.
- Implementing a collaborative filtering algorithm to improve the accuracy of the recommendations.
- Scaling the system to handle larger datasets using techniques such as MapReduce.

## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
