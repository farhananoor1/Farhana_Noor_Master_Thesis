# Analyzing the Complexity of Natural Languages for Bot Detection

This repository contains code and resources for the thesis "Analyzing the Complexity of Natural Languages for Bot Detection" by Noor Farhana.

## Overview

This project presents an entirely unsupervised pipeline to distinguish between human-authored and bot-generated texts in two under-resourced, morphologically rich languages: **Yoruba** and **Kashmiri**. The framework integrates:

* Language-specific preprocessing (stop-word removal, diacritic normalization, stemming, lemmatization)
* Dense vector embeddings (Word2Vec and FastText)
* Density-based clustering (Wishart algorithm)
* Visualization (t-SNE, PCA)
* Information-theoretic analysis (entropy–complexity plane)


## Getting Started

### Prerequisites

* Python 3.8+
* pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/bot-detection-thesis.git
cd bot-detection-thesis

# Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Results

Detailed results, plots, and statistical evaluations are provided in the colab.ipynb file and in the final thesis PDF.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use this work, please cite:

> Noor Farhana. *Analyzing the Complexity of Natural Languages for Bot Detection*. Master's thesis, National Research University Higher School of Economics, 2025.

---

*Maintained by Noor Farhana. For questions or comments, please contact \[[noorfarhana878@gmail.com](noorfarhana878@gmail.com)].*
