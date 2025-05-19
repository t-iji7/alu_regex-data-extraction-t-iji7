# Regex Formative Data Extractor
This project is a **Python-based utility** that uses **regular expressions (regex)** to extract specified data types from raw text. 
---

## 📌 Project Overview

This utility reads a text file (e.g., `sample1.txt`) and scans it using multiple regex patterns to identify and extract:

- 📧 **Email addresses**  
- 🌐 **URLs**  
- 📞 **Phone numbers**  
- 💳 **Credit card numbers**  
- 💰 **Currency amounts**  
- 🕒 **Time formats** (12-hour & 24-hour)  
- 🔖 **Hashtags**  
- 🔤 **HTML tags**

It supports various valid formats of each pattern (e.g., multiple phone formats, time styles, and card delimiters).

---

## 📁 Project Structure

```bash
your-project/
├── sample1.txt           # Your input text file containing mixed content
└── extractor.py          # Main Python script for extraction
---



