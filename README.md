# Arabic Customer Review Classification

## Description

This project focuses on classifying Arabic customer reviews as positive or negative using Natural Language Processing (NLP) techniques and machine learning models. The project employs three different approaches: traditional machine learning (Naive Bayes), deep learning (feedforward neural network), and pretrained models (MARBERT). The primary objective is to analyze Arabic customer feedback on products, particularly from the Amazon Egypt website, to determine sentiment.

## Setup Instructions

1. **Install Required Libraries:**
    ```
    pip install nltk pandas numpy scikit-learn gensim keras
    ```

2. **Download NLTK Resources:**
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Data Collection

The project begins with data collection through web scraping from the Amazon Egypt website. Customer reviews and their associated star ratings are extracted and stored in CSV files. These CSV files are then concatenated into a single dataset for preprocessing and model training.

## Preprocessing

The preprocessing pipeline involves tokenization, removal of stopwords and punctuation, lemmatization, and filtering out non-Arabic words using regular expressions. The preprocessed data is then divided into training and testing sets for model training.

## Word Embedding

Word embedding is performed using Word2Vec to convert text data into fixed-size vectors. The Word2Vec model is trained on the preprocessed text data to generate word embeddings.

## Model Training

- **Naive Bayes Model:** A traditional machine learning approach using TF-IDF vectors.
- **Feedforward Neural Network:** A deep learning approach implemented using Keras.
- **Pretrained Model (MARBERT):** Utilizing a BERT-based model trained on Arabic text data from Hugging Face.

## Evaluation

The models are evaluated based on their accuracy in classifying positive and negative reviews. Performance metrics such as accuracy, confusion matrix, and classification report are calculated to assess model performance.

## Practical Applications

The project's findings can be applied to online purchasing sites, enabling automatic classification of customer reviews to improve product quality and customer satisfaction.

## Future Work

Future work includes acquiring larger Arabic datasets to further enhance model accuracy and exploring additional deep learning architectures for sentiment analysis.

## Conclusion

The project demonstrates successful classification of Arabic customer reviews using various machine learning and deep learning techniques, providing valuable insights for e-commerce platforms and contributing to the advancement of NLP in the Arabic language.
