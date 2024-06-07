from sorter import sorter
from sorter import common_words
import os
import sys
import json
import re
import math


def super_sort(resume_json_array,job_posting_location):
    word_count = {}
    shortlist={}



    def process_json_files(folder_path,category):
        # Check if the provided path is a directory
        if not os.path.isdir(folder_path):
            print(f"Error: {folder_path} is not a valid directory.")
            return

        # Iterate through all files in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # Check if the file is a JSON file
            if filename.endswith('.json'):
                print(f"Processing JSON file: {filename}")
            
                # Open and read the JSON file
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    sorter1=sorter(data)
                    for i  in sorter1.final_result():
                        if i[0] == category:
                            shortlist[filename]=i[1]


    def filter_common_words(file, common_words=common_words):
        with open(file, 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    word = word.lower()
                    if word not in common_words:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    def filter(text):
        word_count={}
        for line in text:
            if line not in common_words:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
        return word_count

    def split_text(text):
        # Use regular expression to split by spaces and commas
        words = re.split(r'[ ,]+', text)
        return words
    def cosine_similarity(dict1, dict2):
        # Get the set of all unique words in both dictionaries
        all_words = set(dict1.keys()).union(set(dict2.keys()))
        
        # Create vectors from the dictionaries
        vector1 = [dict1.get(word, 0) for word in all_words]
        vector2 = [dict2.get(word, 0) for word in all_words]
        
        # Compute the dot product
        dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
        
        # Compute the magnitudes
        magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
        magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))
        
        # Compute the cosine similarity
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        else:
            return dot_product / (magnitude1 * magnitude2)


    def calculate_score(data):
        try:
            sort1 = sorter(data)
            # Extract text from JSON data using the Sorter object
            text = sort1.extract_text_from_json(data)
            # Split the text into words
            text = split_text(text)
            # Calculate word frequency
            word_frequency = sort1.calculate_word_frequency(text)
            # Calculate cosine similarity with a predefined word count
            score = cosine_similarity(word_frequency, word_count)
            return score
        except Exception as e:
            print(f"Error calculating score: {e}")
            return 0
        

    def sort_json_by_score(json_list):
        # Calculate scores for each JSON object
        scores = [(json_obj, calculate_score(json_obj)) for json_obj in json_list]
        
        # Sort the JSON objects based on the scores
        sorted_json = sorted(scores, key=lambda x: x[1], reverse=True)
        
        return [json_obj for json_obj, _ in sorted_json]

    filter_common_words(job_posting_location)
    return sort_json_by_score(resume_json_array)

    