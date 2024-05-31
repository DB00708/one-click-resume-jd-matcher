import json
import time
from src.constants import RETRY_DELAY, MAX_RETRIES


def extract_json_from_response(response_text, retries=1):
    try:
        start_index = response_text.find('{')
        end_index = response_text.rfind('}') + 1
        json_data = response_text[start_index:end_index]
        parsed_data = json.loads(json_data)
        return parsed_data
    except json.JSONDecodeError as e:
        if retries < MAX_RETRIES:
            print(f"Error decoding JSON: {e}. Retrying after {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
            return extract_json_from_response(response_text, retries + 1)
        else:
            raise ValueError(f"Max retries reached. Unable to extract JSON after {MAX_RETRIES} attempts.")

