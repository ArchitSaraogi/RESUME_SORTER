from sorter import sorter
from sorter import common_words
import os
import json
import re
import math
import spacy

nlp = spacy.load('en_core_web_sm')
def extract_organization(text):
    doc = nlp(text)
    organizations = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    return organizations


def super_sort(resume_json_array, job_posting_location):
    word_count = {}
    shortlist = {}

    def process_json_files(folder_path, category):
        if not os.path.isdir(folder_path):
            print(f"Error: {folder_path} is not a valid directory.")
            return

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if filename.endswith('.json'):
                print(f"Processing JSON file: {filename}")
            
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    sorter1 = sorter(data)
                    for i in sorter1.final_result():
                        if i[0] == category:
                            shortlist[filename] = i[1]




    def filter(text):
        for line in text.split():
            if line not in common_words:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
    

    def split_text(text):
        # Use regular expression to split by spaces and commas
        words = re.split(r'[ ,]+', text)
        return words

    
    def cosine_similarity(dict1, dict2):
        all_words = set(dict1.keys()).union(set(dict2.keys()))
        
        vector1 = [dict1.get(word, 0) for word in all_words]
        vector2 = [dict2.get(word, 0) for word in all_words]
        
        dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
        
        magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
        magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        else:
            return dot_product / (magnitude1 * magnitude2)


    def calculate_score(data):
        try:
            sort1 = sorter(data)
            text = sort1.extract_text_from_json()
            text = split_text(text)
            word_frequency = sort1.calculate_word_frequency(text)
            score = cosine_similarity(word_frequency, word_count)

            organizations = extract_organization(text)
            organization_weight = len(organizations) * 0.1  

            internship_weight = data.get('internships', 0) * 0.2
            project_weight = data.get('projects', 0) * 0.2
            weighted_score = score + internship_weight + project_weight + organization_weight

            return weighted_score
    def sort_json_by_score(json_list):

         scores = [(json_obj, calculate_score(json_obj)) for json_obj in json_list]
         sorted_json = sorted(scores, key=lambda x: (x[1] is None, x[1]), reverse=True)
         return [json_obj['_id'] for json_obj, _ in sorted_json]


    
    filter(job_posting_location)
    return sort_json_by_score(resume_json_array)

    
