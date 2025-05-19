# Regex Formative Data Extractor
This project is a **Python-based application** that uses **regular expressions (regex)** to extract specified data types from raw text. 
---

## Project Overview

This utility reads a text file (e.g., `sample1.txt`) and scans it using multiple regex patterns to identify and extract:

- **Email addresses**
- **Phone numbers**
- **Time formats** (12-hour & 24-hour) 
- **URLs**  
- **Hashtags**  
- **Currency amounts**    
- **Credit card numbers**  
- **HTML tags**

It supports various valid formats of each pattern (e.g., multiple phone formats, time styles, and card delimiters).

---

## Project Structure

```bash
your-project/
├── sample1.txt           # Your input text file containing mixed content
└── filter.py             # Main Python script for extraction
```
--- 

## Setup Instructions
- Clone the Repository 
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
- Create Your Text Sample

- Run the Script
```bash
python filter.py
```
---

## How it works
- Opens and reads a text file
- Matches each pattern category found in the text to a specified Regex Pattern
- Outputs each match based on the category

## Sample 1 output test
```bash
emails: ['hello@novaengine.io', 'emily.clark@neuronet.co.uk', 'hello@novaengine.io', 'emily.clark@neuronet.co.uk']
urls: ['https://www.novaengine.io', 'https://docs.novaengine.io/guides', 'https://assets.novaengine.io/images/ai-lab.jpg"', 'https://www.novaengine.io,', 'https://docs.novaengine.io/guides', 'https://assets.novaengine.io/images/ai-lab.jpg"']
phone_numbers: ['(628) 321-7745', '917-645-3322', '404.903.8881', '(628) 321-7745', '917-645-3322', '404.903.8881']
credit_cards: ['5198 3321 6654 7832', '4012-8866-9981-2245', '5198 3321 6654 7832', '4012-8866-9981-2245']
currency: ['$24.50', '$3,499.00', '$24.50', '$3,499.00']
time: ['09:15', '5:45 PM', '09:15', '5:45 PM']
hashtags: ['#NovaLaunch', '#CodeTheFuture', '#NovaLaunch', '#CodeTheFuture']
html_tags: ['<p>', '</p>', '<div class="example">', '</div>', '<img src="https://assets.novaengine.io/images/ai-lab.jpg" alt="AI Laboratory Banner">', '<p>', '<div class="example">', '<img src="https://assets.novaengine.io/images/ai-lab.jpg" alt="AI Laboratory Banner">']
```
