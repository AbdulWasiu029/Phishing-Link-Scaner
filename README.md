## 🔐 Phishing Link Scanner using Python

This is a **Python-based phishing link scanner** designed for cybersecurity purposes. It uses `tldextract` to parse domain parts and `Levenshtein` distance to compare suspicious URLs against a list of known legitimate domains.

### 🧠 How It Works

The script performs the following:

* Extracts the domain, subdomain, and suffix from a given URL
* Compares it with known legitimate domains
* Uses string similarity (Levenshtein ratio) to detect:

  * **Real websites**
  * **Lookalike (phishing) domains**
  * **Suspicious or fake domains**
* Warns if the URL uses unencrypted HTTP

### 🛠️ Dependencies

Install required Python libraries:

```bash
pip install tldextract python-Levenshtein
```

### ▶️ Usage

Run the script using Python:

```bash
python phishing_scanner.py
```

By default, the script scans a **predefined list of URLs** in the code for demonstration.


### 📝 Example Output

```bash
🔍 Scanning URL: http://faceb00k.com
➡️ Protocol: HTTP | Domain: faceb00k | Suffix: com | Subdomain:
⚠️ Warning: Unsecured HTTP — no encryption used, not safe!
⚠️ Result: Domain looks similar to a real one — be cautious, could be phishing.
```


### 🧪 Optional: Accept User Input

If you want to scan a **custom URL from user input**, you can uncomment the following line in the code:

```python
# urls = input_urls()
```

Then, comment or remove the predefined list:

```python
# urls = [
#     'http://payp@l.com',
#     'https://google.com',
#     ...
# ]
```


### ✅ Add More Legitimate Domains

To enhance detection, you can add more domains to the `known_domains` list:

```python
known_domains = [
    'paypal.com',
    'google.com',
    'facebook.com',
    'amazon.com',
    'yourbank.com',
    'instagram.com',
    ...
]
```


### 📁 File Structure

```
phishing_scanner.py       # Main scanner script
README.md                 # Project documentation
```


### 📌 Disclaimer

This tool is developed for **educational and ethical use only**. Do not use it for malicious purposes.

