import json
from collections import Counter
import sys
import re

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

# Function to extract relevant text from the JSON file
class sorter:
    def __init__(self,dictn):
        self.user_json= dictn
        self.text=""
        self.categories_json_path = "data.json"
        self.common_words=common_words

    def extract_text_from_json(self, json_data):
        text = ""

        # Extracting data from the appliedBy section
        applied_by = json_data.get('appliedBy', {})
        
        text += applied_by.get('firstName', '') + " "
        text += applied_by.get('lastName', '') + " "
        text += applied_by.get('institute', '') + " "
        text += applied_by.get('program', '') + " "
        text += applied_by.get('year', '') + " "
        
        # Extracting internship details
        for internship in applied_by.get('resumeInterships', []):
            text += internship.get('title', '') + " "
            text += internship.get('company', '') + " "
            text += internship.get('description', '') + " "
        
        # Extracting project details
        for project in applied_by.get('resumeProjects', []):
            text += project.get('title', '') + " "
            text += project.get('company', '') + " "
            text += project.get('description', '') + " "

        self.text = text.strip()
        return self.text

    # Function to calculate word frequency using TensorFlow TextVectorization
    def preprocess_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation and special characters
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def calculate_word_frequency(self, texts):
        if not texts:
            raise ValueError("No valid text found in the input.")
        
        word_counts = Counter()
        
        for text in texts:
            preprocessed_text = self.preprocess_text(text)
            words = preprocessed_text.split()
            for word in words:
                if word not in self.common_words:
                    word_counts[word] += 1
        
        return word_counts

    # Function to categorize the text based on JSON data
    def categorize_text(self,text, json_path):
        texts = [text]
        text_word_counts = self.calculate_word_frequency(texts)

        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)

        scores = []
        for category, word_counts in json_data.items():
            score = sum(text_word_counts[word] for word in word_counts)
            scores.append((category, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        top_3_categories = scores[:5]
        return top_3_categories

    def final_result(self):
        input_json_data = self.user_json
        input_text = self.extract_text_from_json(input_json_data)
        top_5_categories = self.categorize_text(input_text, self.categories_json_path)
        return top_5_categories