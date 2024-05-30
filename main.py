from transformers import BertTokenizer, BertModel
from src.getting_data.getting_jd_data import extract_sentences
from src.getting_data.getting_user_data import retrieving_user_data
from src.constants import FULL_NAME_KEY, JD_PATH_OR_TEXT, RESUME_PATH
from src.getting_data.user_data_utils import download_nltk_resources_if_needed
from src.preprocessing_pipeline.creating_embeddings import embed_corpus, embed_text_from_resume


def main(payload):
    download_nltk_resources_if_needed('punkt', 'tokenizers/punkt')
    download_nltk_resources_if_needed('stopwords', 'corpora/stopwords')
    resume_data = retrieving_user_data(payload)
    jd_corpus = extract_sentences(payload)

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    embedded_jd_corpus = embed_corpus(jd_corpus, tokenizer, model)
    embedded_resume_data = embed_text_from_resume(resume_data, tokenizer, model)

    # now we will do cosine similarity between the embeddings of resume and jd based on that we will assign a score,
    # if the score is above than a particular threshold we will generate the resume using llm and if it is below we will
    # ask user if user wants to update the resume and than will generate a resume


if __name__ == '__main__':
    payload = {
        FULL_NAME_KEY: "divyansh bhatia",
        RESUME_PATH: r"src/resources/RESUME.pdf",
        JD_PATH_OR_TEXT: r"src/resources/Generative AI Engineer JD (1).docx"
    }

    main(payload)
