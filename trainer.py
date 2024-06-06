import os
import fitz  # PyMuPDF
import tensorflow as tf
import pandas as pd
from collections import Counter
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import json

# List of common English words
common_words = [
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren\'t', 
    'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can\'t', 
    'cannot', 'could', 'couldn\'t', 'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 
    'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 
    'having', 'he', 'he\'d', 'he\'ll', 'he\'s', 'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 
    'his', 'how', 'how\'s', 'i', 'i\'d', 'i\'ll', 'i\'m', 'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 
    'it\'s', 'its', 'itself', 'let\'s', 'me', 'more', 'most', 'mustn\'t', 'my', 'myself', 'no', 'nor', 'not', 
    'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 
    'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll', 'she\'s', 'should', 'shouldn\'t', 'so', 'some', 
    'such', 'than', 'that', 'that\'s', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 
    'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve', 'this', 'those', 'through', 
    'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll', 'we\'re', 'we\'ve', 
    'were', 'weren\'t', 'what', 'what\'s', 'when', 'when\'s', 'where', 'where\'s', 'which', 'while', 'who', 
    'who\'s', 'whom', 'why', 'why\'s', 'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll', 
    'you\'re', 'you\'ve', 'your', 'yours', 'yourself', 'yourselves'
]

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    document = fitz.open(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

# Function to scan a folder and extract text from all PDFs
def scan_folder_and_extract_text(folder_path):
    texts = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                extracted_text = extract_text_from_pdf(file_path)
                if extracted_text:  # Ensure text is not empty
                    texts.append(extracted_text)
    return texts

# Function to calculate word frequency using TensorFlow TextVectorization
def calculate_word_frequency(texts):
    if not texts:
        raise ValueError("No valid text found in the PDFs.")
        
    vectorizer = TextVectorization(output_mode='int')
    vectorizer.adapt(texts)
    
    vocabulary = vectorizer.get_vocabulary()
    word_counts = Counter()
    
    for text in texts:
        vectorized_text = vectorizer(tf.constant([text]))
        for word_index in vectorized_text[0].numpy():
            word = vocabulary[word_index]
            if word not in common_words:
                word_counts[word] += 1
    
    return word_counts

# Function to get the top N words by frequency
def get_top_n_words(word_counts, n=30):
    return dict(word_counts.most_common(n))

# Main function
def main(root_folder_path, output_json_path):
    results = {}
    for root, dirs, files in os.walk(root_folder_path):
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            texts = scan_folder_and_extract_text(subfolder_path)
            if texts:
                word_counts = calculate_word_frequency(texts)
                top_words = get_top_n_words(word_counts)
                results[subfolder] = top_words

    # Save results to JSON
    with open(output_json_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    root_folder_path = "data"
    output_json_path = 
    main(root_folder_path, output_json_path)