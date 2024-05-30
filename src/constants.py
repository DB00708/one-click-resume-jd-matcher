# Keys for user information
RESUME_PATH = 'resume_path'
JD_PATH_OR_TEXT = "jd_path_or_text"
FULL_NAME_KEY = 'full_name'
USER_EMAIL_KEY = 'user_email'
USER_MOBILE_NO_KEY = 'user_mobile_no'
LINKEDIN_URL_KEY = 'linkedin_url'
PORTFOLIO_URL_KEY = 'portfolio_url'
KEYS_TO_SKIP = ['full_name', 'user_email', 'user_mobile_no']

# Regex patterns
EMAIL_REGEX_PATTERN = r'\b[\w\.-]+?@\w+?\.\w+?\b'
MOBILE_NO_REGEX_PATTERN = r'\b\d{10}\b'
URL_REGEX_PATTERN = r'(https?://(?:www\.)?(?:linkedin\.com/\S+|[^ ]+))'

# Keywords for resume sections
SECTIONAL_KEYWORDS = ['experience', 'education', 'responsibility', 'achievement', 'project', 'skill', 'training']

OPEN_AI_KEY = "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"
MAX_RETRIES = 3
RETRY_DELAY = 0.1
EXPERIENCE_THRESHOLD = -1
