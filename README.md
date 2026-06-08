# Sentimazon-Project

## Description

The Sentimazon project aims to develop a tool to extract and capture the opinions of users regarding target products from Amazon reviews. The project focuses on processing textual review data, analyzing user opinions, and visualizing the results.

The main objectives of this project are:

- To visualize textual data from product reviews
- To preprocess review data for further analysis
- To apply Natural Language Processing techniques
- To analyze customer opinions and sentiment
- To present the results through basic visualizations

## Project Overview

Sentimazon is a Python-based sentiment analysis project designed to collect, clean, process, and analyze user opinions about products from Amazon reviews. The main goal of the project is to understand whether customer reviews express positive, negative, or neutral opinions about a selected product.

The project applies Natural Language Processing techniques to prepare raw review text for analysis. The preprocessing pipeline includes text cleaning, stop-word removal, tokenization, lemmatization, and normalization. After preprocessing, the review data can be used for sentiment analysis and visualization.

## Main Features

- Collection and preparation of product review data
- Text cleaning and preprocessing
- Stop-word removal
- Tokenization
- Lemmatization
- Sentiment analysis of customer reviews
- Basic visualization of review patterns and sentiment results

## How It Works

The workflow of the project follows these main steps:

1. Import the review dataset
2. Clean the raw text data
3. Remove unnecessary elements such as URLs, punctuation, numbers, usernames, and special characters
4. Remove stop words
5. Apply tokenization
6. Apply lemmatization
7. Analyze the sentiment of the reviews
8. Visualize the results using graphs and charts

## Text Preprocessing Steps

The preprocessing step is one of the most important parts of this project. It prepares the raw review text and makes it suitable for sentiment analysis.

The preprocessing process includes:

1. Text cleaning
   - URL removal
   - Punctuation removal
   - Number removal
   - Lowercasing
   - Username handling
   - Spelling correction
   - Stop-word removal

2. Removal of duplicated and unnecessary comments
   - Removing account names
   - Removing duplicate comments
   - Removing irrelevant words

3. Removal of emotional symbols
   - Removing emojis and unnecessary symbols

4. Tokenization
   - Splitting text into smaller units such as words or tokens

5. Lemmatization
   - Converting words into their base dictionary form to reduce word variation

## Tools and Technologies

- Programming Language: Python
- Core Libraries: Pandas, NumPy, Regex, NLTK
- Visualization: Matplotlib
- Development Environment: Jupyter Notebook
- Version Control: Git and GitHub
- Automation: GitHub Actions

## Project Structure

```text
Sentimazon-Project/
│
├── .github/workflows/      # GitHub Actions workflow files
├── Main.ipynb              # Main Jupyter Notebook of the project
├── README.md               # Project documentation
├── requirements.txt        # Required Python libraries
├── .gitignore              # Files ignored by Git
└── .gitattributes          # Git attributes configuration