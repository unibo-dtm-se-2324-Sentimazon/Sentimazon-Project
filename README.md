````markdown
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

The original idea was to use real-time Amazon review scraping. However, due to Amazon policy limitations, a Kaggle mobile reviews sentiment dataset was used instead.

The project applies Natural Language Processing techniques to prepare raw review text for analysis. The preprocessing pipeline includes text cleaning, stop-word removal, tokenization, lemmatization, and normalization. After preprocessing, the review data is processed and analyzed to identify sentiment patterns and visualize customer opinions.

## Main Features

- Collection and preparation of product review data
- Text cleaning and preprocessing
- Stop-word removal
- Tokenization
- Lemmatization
- Part-of-speech tagging
- Aspect and noun extraction
- Sentiment analysis of customer reviews
- Model performance evaluation
- Basic visualization of review patterns and sentiment results

## Software Engineering Improvements

The original version of the project was mainly implemented inside a Jupyter Notebook. In the revised version, the project was reorganized to better follow Software Engineering practices.

The main improvements include:

- Refactored the code into a modular Python package under `src/sentimazon`
- Separated the original notebook logic into reusable Python modules
- Moved data loading, preprocessing, aspect extraction, sentiment analysis, evaluation, and visualization into separate files
- Replaced the absolute dataset path with a relative project path
- Added automated tests using `pytest`
- Updated GitHub Actions CI to run the automated test suite automatically
- Used a branch-based workflow through the `project-revision` branch
- Created and merged Pull Request #5 after CI validation
- Published release `v1.0.0`

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
10. Extract noun-based product aspects
11. Analyze the sentiment of the reviews
12. Evaluate model performance
13. Visualize the results using graphs and charts

## Text Preprocessing and Processing Steps

The preprocessing and processing stages are important parts of this project. They prepare the raw review text, transform it into a structured format, and make it suitable for sentiment analysis and visualization.

### Preprocessing Process

The preprocessing process includes:

#### Dataset selection

The original idea was to use real-time Amazon review scraping. Due to Amazon policy limitations, a Kaggle mobile reviews sentiment dataset was used instead.

The dataset was reduced to the main required columns: review text and sentiment label.

#### Text cleaning

The text cleaning stage includes:

- Removing usernames
- Removing URLs
- Removing hashtags
- Removing punctuation and special characters
- Converting all text to lowercase

#### Stop-word removal

Common English words that do not add strong meaning to sentiment analysis are removed. This helps keep the most useful words for opinion analysis.

#### Tokenization

The cleaned review text is split into individual words or tokens.

#### Lemmatization

Words are converted into their base form. This reduces word variation and improves text consistency.

## Processing Process

After preprocessing, the project continues with text processing and analysis. This stage uses the cleaned and structured review data to extract useful information from customer opinions.

The processing process includes:

### Sentiment label preparation

The available sentiment labels in the dataset are used to classify reviews into positive, negative, and neutral categories.

### Text representation

The cleaned, tokenized, and lemmatized comments are used as the main input for further Natural Language Processing tasks.

### Part-of-speech tagging

Grammatical labels are assigned to words. This helps identify word types such as nouns, verbs, adjectives, and adverbs.

### Aspect extraction

Nouns are extracted from the processed review text to identify common product-related aspects mentioned by users, such as battery, price, quality, and performance.

### Sentiment analysis

Customer opinions are analyzed using sentiment analysis methods. The project includes VADER and transformer-based sentiment models such as DistilBERT and RoBERTa.

### Result analysis

The predicted sentiment results are compared with the existing sentiment labels in the dataset. The project calculates performance metrics such as accuracy, precision, recall, and F1-score.

### Visualization

Visual outputs are created to better understand review data, frequent product aspects, and model performance.

## Tools and Technologies

- Programming Language: Python
- Core Libraries: Pandas, NumPy, Regex, NLTK
- Sentiment Analysis: VADER, DistilBERT, RoBERTa
- Evaluation: scikit-learn
- Visualization: Matplotlib
- Development Environment: Jupyter Notebook and VS Code
- Version Control: Git and GitHub
- Testing: pytest
- Automation: GitHub Actions

## Project Structure

```text
Sentimazon-Project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── Mobile_Reviews_Sentiment.csv
│
├── notebooks/
│   └── Main.ipynb
│
├── src/
│   └── sentimazon/
│       ├── __init__.py
│       ├── data_loader.py
│       ├── preprocessing.py
│       ├── aspect_extraction.py
│       ├── sentiment_analysis.py
│       ├── evaluation.py
│       └── visualization.py
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_preprocessing.py
│   ├── test_aspect_extraction.py
│   └── test_evaluation.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .gitattributes
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
jupyter notebook notebooks/Main.ipynb
```

Then run the notebook cells step by step. The notebook includes the main stages of the project, including data loading, preprocessing, aspect extraction, sentiment analysis, evaluation, and visualization.

## Automated Testing

The project includes automated tests for the main lightweight modules. The tests are written using `pytest`.

The tests cover:

- data loading
- text preprocessing
- noun/aspect extraction
- evaluation metrics

To run the tests locally on PowerShell:

```bash
$env:PYTHONPATH="src"
python -m pytest
```

Current local test result:

```text
7 passed
```

Transformer-based sentiment models such as DistilBERT and RoBERTa are not included in the automated tests because they require heavier dependencies and model downloads. This keeps the test suite fast and suitable for GitHub Actions.

## CI/CD Workflow

This project uses GitHub Actions for Continuous Integration.

In the original version, the workflow only checked whether some project files existed. In the revised version, the CI workflow runs the automated test suite using `pytest`.

The CI workflow now performs the following steps:

1. Checks out the repository
2. Sets up Python
3. Installs the required test dependencies
4. Runs the automated tests with:

```bash
PYTHONPATH=src pytest
```

This means that each push or pull request can be automatically validated. The updated CI workflow improves reliability and shows that the project is no longer only a notebook-based implementation.

## Version Control Workflow

The revised project follows a clearer Git and GitHub workflow.

The main workflow used was:

```text
branch → commits → automated tests → CI validation → pull request → merge → release
```

The improvements were developed on the `project-revision` branch and then merged into `main` through Pull Request #5 after the CI checks passed.

A release was also created:

```text
v1.0.0 - Sentimazon Refactored Version
```

## Example Output

The project can generate outputs such as:

- Cleaned review text
- Review text after stop-word removal
- Tokenized review data
- Lemmatized review text
- Part-of-speech tagged words
- Extracted noun keywords
- Sentiment classification results
- Model performance table
- Word frequency analysis
- Visual charts showing review trends, product aspects, and sentiment model performance

## Known Issues and Future Work

This project is still under development. Some limitations and possible future improvements include:

- The dataset size can be expanded
- Real-time Amazon review scraping can be added in the future if policy and technical limitations allow it
- More advanced machine learning models can be added
- Sentiment classification accuracy can be improved
- More automated tests can be added for additional functions
- More visualizations can be included
- A simple user interface or web application can be developed in the future
- The project can be extended to analyze reviews from other e-commerce platforms

## Licensing

The Sentimazon project is released under the MIT License. This license is simple, permissive, and widely used in software development. It allows users to use, modify, and distribute the project with only limited restrictions.

The MIT License was selected because it is suitable for educational and open-source projects, while still keeping the original copyright notice and license information.

## Author

This project was developed by Morteza Sheykhizadeh as part of the Software Engineering course project.
````
