# East African Music Data Analyzer

## Overview

The East African Music Data Analyzer is a Python application that analyzes
music data from East African artists.

The program uses Pandas to load, clean, filter, organize, and analyze the
dataset. Matplotlib is used to create a chart showing one of the analysis
results.

The project focuses on artists, countries, genres, and streaming performance.

## Analysis Questions

The program answers the following questions:

1. Which East African countries have the most artists in the dataset?

2. Which music genres have the highest average streaming numbers?

3. Which artist has the highest number of streams?

## Dataset

The development dataset is stored in:

`data/music_data.csv`

For the final version, this file should be replaced with a free dataset
selected by the student.

Dataset source:

[ADD THE REAL DATASET SOURCE HERE]

Dataset license or usage information:

[ADD THE DATASET LICENSE INFORMATION HERE]

## Data Analysis Methods

The program demonstrates several data analysis techniques:

- Filtering
- Counting
- Grouping
- Aggregation
- Calculating averages
- Sorting
- Data conversion
- Finding the highest value
- Data cleaning
- Data visualization

## Question 1 Analysis

The program filters the dataset to selected East African countries and counts
the number of artists associated with each country.

This allows the program to identify which countries have the most artists in
the dataset.

## Question 2 Analysis

The program groups the East African records by music genre and calculates the
average number of streams for each genre.

The results are then sorted from the highest average streaming number to the
lowest.

## Question 3 Analysis

The program sorts artists according to their number of streams and identifies
the artist with the highest streaming number.

## Visualization

The program creates a bar chart showing the number of artists in each
East African country.

The chart is saved in:

`charts/artists_by_country.png`

## Development Environment

The project was developed using:

- Python 3
- Visual Studio Code
- Pandas
- Matplotlib
- Git
- GitHub

## How to Run

First install the required Python libraries:

```text
python -m pip install -r requirements.txt