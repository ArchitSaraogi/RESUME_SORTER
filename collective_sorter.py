from sorter import sorter
from sorter import common_words
import os
import sys
import json
import tensorflow as tf
import re
import math


word_count = {}
shortlist={}
final_shortlist={}



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


def process_json_files2(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    # Iterate through all files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                sort1 = sorter(data)
                text = sort1.extract_text_from_json(data)
                text = split_text(text)
                word_frequency = sort1.calculate_word_frequency(text)
                final_shortlist[filename]= cosine_similarity(word_frequency,word_count)
try:
    if sys.argv[1].lower()=="filter":
        filter_common_words(sys.argv[2])
        process_json_files2(sys.argv[3])
        final_shortlist = dict(sorted(final_shortlist.items(), key=lambda item: item[1], reverse=True))
        print(final_shortlist)
    elif sys.argv[1].lower()=="categorize":
        process_json_files(sys.argv[3],sys.argv[2].upper())
        shortlist=dict(sorted(shortlist.items(), key=lambda item: item[1], reverse=True))
        print(shortlist)
except IndexError:
    print("IndexError : Arguements missing- collective_sorter.py <Operation_to_Perform(filter/categorize)> <category(categorize)//Job_posting.txt(filter)> <folder_path with all resumes>")

