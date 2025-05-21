# Spot the Bot

## Overview
**Spot the Bot** is a project focused on detecting bot-generated texts by analyzing semantic trajectories of natural language texts. This research primarily investigates the Kanuri and Miskito languages using advanced word embedding techniques and clustering algorithms. The goal is to develop effective mechanisms to distinguish between human-authored and bot-generated content, addressing the rising concerns of misinformation in digital communications.

## Features
- **Data Collection and Pre-processing**: Collection of text corpora for Kanuri and Miskito languages, followed by extensive cleaning and preprocessing.
- **Text Generation**: Generation of bot-like texts using ChatGPT 3.5 to simulate bot-generated content.
- **Word Embeddings**: Implementation of Word2Vec and FastText models to create meaningful vector representations of words.
- **Clustering**: Application of the Wishart clustering algorithm to identify distinct clusters of human and bot-generated texts.
- **Statistical Analysis**: Use of Mann-Whitney statistical tests and Holm-Bonferroni corrections to validate the significance of clustering results.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Libraries: `numpy`, `pandas`, `scikit-learn`, `gensim`, `scipy`, `matplotlib`, `nltk`
- Access to ChatGPT 3.5 for text generation

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/username/spot-the-bot.git
   cd spot-the-bot
## Usage
Data Collection and Pre-processing
Collect text corpora from available sources, focusing on the Kanuri and Miskito languages. Clean and preprocess the data by removing irrelevant characters, tokenizing, and lemmatizing the text. Ensure all preprocessing scripts are run before moving to the next steps.

### Text Generation
Use ChatGPT 3.5 to generate bot-like texts based on specific prompts. These texts will serve as a comparison to human-generated texts in further analyses.

### Word Embeddings
Train Word2Vec and FastText models on the preprocessed text data:
   ```sh
   from gensim.models import Word2Vec, FastText
   # Training Word2Vec model
   word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
   word2vec_model.save("word2vec.model")
   # Training FastText model
   fasttext_model = FastText(sentences, vector_size=100, window=5, min_count=1, workers=4)
   fasttext_model.save("fasttext.model")
 ```

## Statistical Analysis
Perform statistical analysis to validate the clustering results:
   ```sh
   from scipy.stats import mannwhitneyu
   # Example comparison of two distributions
   stat, p = mannwhitneyu(data1, data2)
   print(f'Statistics={stat}, p={p}')
```
Apply Holm-Bonferroni correction for multiple testing.
 
## Results
Analyze the results using the Calinski-Harabasz index and visualize the clustering with t-SNE and PCA plots:
   ```sh
   from sklearn.decomposition import PCA
   import matplotlib.pyplot as plt
   
   # PCA for dimensionality reduction
   pca = PCA(n_components=2)
   principalComponents = pca.fit_transform(embeddings)
   plt.scatter(principalComponents[:, 0], principalComponents[:, 1], c=clustering.labels_)
   plt.show()
```

## Acknowledgements
- **Tajamul Sheikh**: Original research and dissertation
- **Majid Sohrabi**: Supervisory guidance and support





