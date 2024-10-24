# PhishSecure

PhishSecure is a web-based phishing website detection tool that uses machine learning models to classify whether a given URL is legitimate or phishing. The project is developed using Python, Django, and scikit-learn.

## Features

- Extracts features from a given URL using custom `FeatureExtraction`.
- Uses a pre-trained machine learning model (`GradientBoostingClassifier`) to predict the likelihood of a URL being phishing or legitimate.
- Displays the prediction along with probabilities for phishing and non-phishing classifications.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sarfaraaz97/PhishSecure.git
   cd PhishSecure
   
