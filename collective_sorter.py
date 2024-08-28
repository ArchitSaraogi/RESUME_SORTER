from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import chardet
from bs4 import BeautifulSoup
from email import message_from_file
import json
import re
import ast



def full_sort(json_list, job_posting_text):
    def extract_text_from_json_list(json_list):
        resumes=[]
        ids=[]
        for i in json_list:
            text = ""
            def extract_text_recursive(data):
                nonlocal text
                if isinstance(data, dict):
                    for value in data.values():
                        extract_text_recursive(value)
                elif isinstance(data, list):
                    for item in data:
                        extract_text_recursive(item)
                elif isinstance(data, str):
                    text += data + " "
            extract_text_recursive(i)
            text = text.strip()
            text = text.lower()    
            text = re.sub(r'[^\w\s]', '', text)
            ids.append(i['_id']["$oid"])
            resumes.append(text)
            output = list(zip(ids,resumes))
        return output

    def calculate_similarity(job_posting, resumes ):
        if not resumes:
            print("No resumes to compare.")
            return []
        documents = [job_posting] + [resume[1] for resume in resumes]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        if tfidf_matrix.shape[0] <= 1:
            print("Insufficient data for similarity calculation.")
            return []
        
        similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()        
        resume_similarity = {resumes[i][0]: f"{similarity_scores[i]:.10f}" for i in range(len(resumes))}
        sorted_similarity = sorted(resume_similarity, key=lambda item: float(item[1]), reverse=True)
        
        return sorted_similarity
    

    def main(job_posting, json_list):
        
        resumes = extract_text_from_json_list(json_list)
        sorted_resumes = calculate_similarity(job_posting, list(resumes))
        return sorted_resumes
    main(job_posting_text, json_list)
full_sort(input_data, posting)