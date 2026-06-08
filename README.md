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

The project applies Natural Language Processing techniques to prepare raw review text for analysis. The preprocessing pipeline includes text cleaning, stop-word removal, tokenization, lemmatization, and normalization. After preprocessing, the review data is processed and analyzed to identify sentiment patterns and visualize customer opinions.

## Main Features

- Collection and preparation of product review data
- Text cleaning and preprocessing
- Stop-word removal
- Tokenization
- Lemmatization
- Part-of-speech tagging
- Sentiment analysis of customer reviews
- Basic visualization of review patterns and sentiment results

## How It Works

The workflow of the project follows these main steps:

1. Import the review dataset
2. Select the required columns for analysis
3. Clean the raw text data
4. Remove unnecessary elements such as URLs, punctuation, numbers, usernames, hashtags, and special characters
5. Convert text to lowercase
6. Remove stop words
7. Apply tokenization
8. Apply lemmatization
9. Apply part-of-speech tagging
10. Analyze the sentiment of the reviews
11. Visualize the results using graphs and charts

## Text Preprocessing and Processing Steps

The preprocessing and processing stages are important parts of this project. They prepare the raw review text, transform it into a structured format, and make it suitable for sentiment analysis and visualization.

### Preprocessing Process

The preprocessing process includes:

1. Dataset selection
   - The original idea was to use real-time Amazon review scraping.
   - Due to Amazon policy limitations, a Kaggle mobile reviews sentiment dataset was used instead.
   - The dataset was reduced to the main required columns: review text and sentiment label.

2. Text cleaning
   - Removing usernames
   - Removing URLs
   - Removing hashtags
   - Removing punctuation and special characters
   - Converting all text to lowercase

3. Stop-word removal
   - Removing common English words that do not add strong meaning to sentiment analysis
   - Keeping the most useful words for opinion analysis

4. Tokenization
   - Splitting cleaned review text into individual words or tokens

5. Lemmatization
   - Converting words into their base form
   - Reducing word variation and improving text consistency

### Processing Process

After preprocessing, the project continues with text processing and analysis. This stage uses the cleaned and structured review data to extract useful information from customer opinions.

The processing process includes:

1. Sentiment label preparation
   - Using the available sentiment labels in the dataset
   - Classifying reviews into positive, negative, and neutral categories

2. Text representation
   - Using the cleaned, tokenized, and lemmatized comments as the main input for analysis
   - Preparing the review text for further Natural Language Processing tasks

3. Part-of-speech tagging
   - Assigning grammatical labels to words
   - Identifying word types such as nouns, verbs, adjectives, and adverbs

4. Sentiment analysis
   - Analyzing customer opinions based on the processed review text
   - Understanding whether the review expresses a positive, negative, or neutral opinion

5. Result analysis
   - Comparing review text with sentiment labels
   - Identifying general patterns in customer opinions
   - Understanding how users describe product features and experiences

6. Visualization
   - Creating visual outputs to better understand the review data
   - Showing sentiment distribution and review patterns through charts

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
```

## Installation

To run this project locally, first clone the repository:

```bash
git clone https://github.com/sheykhizadeh/Sentimazon-Project.git
```

Then move into the project folder:

```bash
cd Sentimazon-Project
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

Open the Jupyter Notebook:

```bash
jupyter notebook Main.ipynb
```

Then run the notebook cells step by step. The notebook includes the main stages of the project, including data preprocessing, sentiment analysis, and visualization.

## Example Output

The project can generate outputs such as:

- Cleaned review text
- Review text after stop-word removal
- Tokenized review data
- Lemmatized review text
- Part-of-speech tagged words
- Sentiment classification results
- Word frequency analysis
- Visual charts showing review trends and sentiment distribution

## CI/CD Workflow

This project includes a basic GitHub Actions workflow. The workflow helps check the project automatically when changes are pushed to the repository.

The CI/CD workflow can be used to:

- Install project dependencies
- Check whether the Python environment is working correctly
- Support better version control and project maintenance
- Improve project reliability during development

## Known Issues and Future Work

This project is still under development. Some limitations and possible future improvements include:

- The dataset size can be expanded
- Real-time Amazon review scraping can be added in the future if policy and technical limitations allow it
- More advanced machine learning models can be added
- Sentiment classification accuracy can be improved
- More visualizations can be included
- A simple user interface or web application can be developed in the future
- The project can be extended to analyze reviews from other e-commerce platforms

## Licensing

The Sentimazon project is released under the MIT License. This license is simple, permissive, and widely used in software development. It allows users to use, modify, and distribute the project with only limited restrictions.

The MIT License was selected because it is suitable for educational and open-source projects, while still keeping the original copyright notice and license information.

## Author

This project was developed by Morteza Sheykhizadeh as part of the Software Engineering course project.