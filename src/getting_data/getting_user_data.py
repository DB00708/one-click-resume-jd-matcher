import re
from src.constants import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from src.getting_data.user_data_utils import add_to_exclude_patterns, check_for_file_existence, stem_keyword, \
     validating_input_file_path_format


def extract_keywords(text, exclude_patterns):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    keywords = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    keywords = [word for word in keywords if not any(re.search(pattern, word) for pattern in exclude_patterns)]
    return keywords


def extract_sectional_keywords(keyword_list, resume_info):
    current_slice = []

    sectional_keywords = [stem_keyword(keyword) for keyword in SECTIONAL_KEYWORDS]

    for keyword in keyword_list:
        stemmed_keyword = stem_keyword(keyword.lower())
        if stemmed_keyword in sectional_keywords:
            if current_slice:
                resume_info[current_slice[0]] = current_slice[1:]
                current_slice = []
            current_slice.append(keyword.lower())
        elif current_slice:
            current_slice.append(keyword)

    if current_slice:
        resume_info[current_slice[0]] = current_slice[1:]

    return resume_info


def extract_email_from_resume(text, user_info):
    extracting_email = re.findall(EMAIL_REGEX_PATTERN, text)
    if extracting_email:
        user_info[USER_EMAIL_KEY] = extracting_email[0]
    else:
        user_info[USER_EMAIL_KEY] = ""
    return extracting_email


def extract_mobile_no_from_resume(text, user_info):
    extracting_mobile_no = re.findall(MOBILE_NO_REGEX_PATTERN, text)
    if extracting_mobile_no:
        user_info[USER_MOBILE_NO_KEY] = extracting_mobile_no[0]
    else:
        user_info[USER_MOBILE_NO_KEY] = ""
    return extracting_mobile_no


def extract_url_from_resume(text, user_info):
    extracting_url = re.findall(URL_REGEX_PATTERN, text)
    if extracting_url:
        url = extracting_url[0]
        if "linkedin" in url:
            user_info[LINKEDIN_URL_KEY] = url
        else:
            user_info[PORTFOLIO_URL_KEY] = url
    return extracting_url


def extract_resume_info(text, full_name):
    user_info = {}
    exclude_patterns = []

    user_info[FULL_NAME_KEY] = full_name
    exclude_patterns.append(full_name)

    exclude_patterns = add_to_exclude_patterns(extract_email_from_resume(text, user_info), exclude_patterns)
    exclude_patterns = add_to_exclude_patterns(extract_mobile_no_from_resume(text, user_info), exclude_patterns)
    exclude_patterns = add_to_exclude_patterns(extract_url_from_resume(text, user_info), exclude_patterns)

    return user_info, exclude_patterns


def retrieving_user_data(payload):
    full_name = payload.get(FULL_NAME_KEY, "").strip().lower()

    resume_path = payload.get(RESUME_PATH, "")
    resume_path = check_for_file_existence(resume_path)

    if not resume_path:
        print("File not exists!")
        return {}

    resume_text = validating_input_file_path_format(input_data=resume_path)
    resume_info, exclude_info = extract_resume_info(resume_text, full_name)
    resume_keywords = extract_keywords(resume_text, exclude_info)
    updated_resume_info = extract_sectional_keywords(resume_keywords, resume_info)

    # for key, value in updated_resume_info.items():
    #     print(f"{key}: {value}")

    return updated_resume_info
