import re  #imports regex modules for python

#opens and reads file
with open('sample.txt', 'r') as file:
    text = file.read()

#checking for regex patterns by group to accomodate various formats
patterns = {
    'emails': r'\b[\w.-]+@[\w.-]+\.\w{2,}\b',
    'urls': r'https?://\S+',
    'phone_numbers': r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})',
    'credit_cards': r'\b(?:\d{4}[- ]?){3}\d{4}\b',
    'currency': r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?',
    'time': r'\b((?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)|(?:[01]?\d|2[0-3]):[0-5]\d)\b',
    'hashtags': r'#\w+',
    'html_tags': r'<[^>]+>',
}

#storing and printing matched results by each category
for pattern_name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{pattern_name}: {matches}")




