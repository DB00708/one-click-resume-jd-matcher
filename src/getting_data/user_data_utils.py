import os
import nltk
import pymupdf
import docx2txt
from nltk.stem import PorterStemmer


def download_nltk_resources_if_needed(resource_name, resource_path):
    try:
        nltk.data.find(resource_path)
    except LookupError:
        nltk.download(resource_name)


def check_for_file_existence(file_path):
    if not os.path.exists(file_path):
        return ""
    return file_path


def is_file_path(input_str):
    return os.path.isfile(input_str)


def read_pdf(file_path):
    text = ""
    doc = pymupdf.open(file_path)
    for page in doc:
        text = page.get_text()
    return text


def read_docx(file_path):
    text = docx2txt.process(file_path)
    return text


def stem_keyword(keyword):
    stemmer = PorterStemmer()
    return stemmer.stem(keyword)


def add_to_exclude_patterns(extracted_items, exclude_patterns):
    if isinstance(extracted_items, list) and extracted_items:
        exclude_patterns.extend(extracted_items)
    return exclude_patterns


def validating_input_file_path_format(input_data):
    text = ""

    if is_file_path(input_data):
        file_path = input_data
        if file_path.endswith('.pdf'):
            text = read_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = read_docx(file_path)
        else:
            print("Unsupported file format. Please upload a PDF or a DOCX file.")
    else:
        text = input_data

    return text
