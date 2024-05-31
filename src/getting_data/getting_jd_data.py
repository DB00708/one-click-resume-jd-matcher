import nltk
from nltk.corpus import stopwords
from src.constants import JD_PATH_OR_TEXT
from src.getting_data.user_data_utils import validating_input_file_path_format


def retrieving_jd_data(payload):
    jd = payload.get(JD_PATH_OR_TEXT, "")
    jd_text = validating_input_file_path_format(input_data=jd)
    return jd_text


def extract_sentences(payload):
    jd_text = retrieving_jd_data(payload)

    sentences = nltk.sent_tokenize(jd_text)
    stop_words = set(stopwords.words('english'))
    cleaned_sentences = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        cleaned_sentence = ' '.join([word for word in words if word.lower() not in stop_words])
        cleaned_sentences.append(cleaned_sentence)

    return cleaned_sentences
