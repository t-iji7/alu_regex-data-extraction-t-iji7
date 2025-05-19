import re  #imports regex modules for python

#opens file and reads
with open('sample.txt', 'r') as file:
    text = file.read()

#checking for regex patterns
patterns = {
    'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    'urls': r'https?://\S+',
    'phone_numbers': r'\(\d{3}\) \d{3}-\d{4}',
    'credit_cards': r'\d{4} \d{4} \d{4} \d{4}',
    'currency': r'\$\d+\.\d{2}',
    'time': r'\d{1,2}:\d{2} [AP]M',
    'hashtags': r'#\w+',
    'html_tags': r'<[^>]+>',
}

#storing and printing match results
for pattern_name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{pattern_name}: {matches}")




