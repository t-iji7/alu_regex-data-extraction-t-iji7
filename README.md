# Regex Formative Data Extractor
This project is a **Python-based application** that uses **regular expressions (regex)** to extract specified data types from raw text. 
---

## Project Overview

This utility reads a text file (e.g., `sample1.txt`) and scans it using multiple regex patterns to identify and extract:

- 📧 **Email addresses**
- 📞 **Phone numbers**
- 🕒 **Time formats** (12-hour & 24-hour) 
- 🌐 **URLs**  
- 🔖 **Hashtags**  
- 💰 **Currency amounts**    
- 💳 **Credit card numbers**  
- 🔤 **HTML tags**

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


