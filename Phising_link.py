import tldextract
import Levenshtein as lv
from urllib.parse import urlparse

# Known legit domains
known_domains = [
    'paypal.com',
    'google.com',
    'facebook.com',
    'amazon.com',
    'etc.com',
]

urls = [
    'http://payp@l.com',
    'https://google.com',
    'http://faceb00k.com',
    'http://amazon.con',
    'http://etc.co',
]

def extract_domain(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or ''
    ext = tldextract.extract(hostname)
    domain = ext.domain
    subdomain = ext.subdomain
    suffix = ext.suffix
    scheme = parsed.scheme
    return domain, subdomain, suffix, scheme

def is_fake_or_similar(domain, suffix, known_domains, threshold=0.98):
    if suffix:
        full_input_domain = f"{domain}.{suffix}"
    else:
        full_input_domain = domain

    for real_domain in known_domains:
        similarity = lv.ratio(full_input_domain, real_domain)
        if similarity == 1.0:
            return "real"
        elif similarity >= threshold:
            return "similar"
    return "phishing"

def scan_url(url, known_domains):
    domain, subdomain, suffix, scheme = extract_domain(url)

    if suffix:
        full_domain = f"{domain}.{suffix}"
    else:
        full_domain = domain  # fallback in case suffix is missing

    print(f"\n🔍 Scanning URL: {url}")
    print(f"➡️ Protocol: {scheme.upper()} | Domain: {domain} | Suffix: {suffix} | Subdomain: {subdomain}")

    # Check for HTTP warning
    if scheme.lower() == "http":
        print("⚠️ Warning: Unsecured HTTP — no encryption used, not safe!")

    # Check domain match
    result = is_fake_or_similar(domain, suffix, known_domains)
    if result == "real":
        print("✅ Result: Domain is in known list — real website.")
    elif result == "similar":
        print("⚠️ Result: Domain looks similar to a real one — be cautious, could be phishing.")
    else:
        print("❌ Result: Domain is different — likely a PHISHING link!")

if __name__ == '__main__':
    # urls = input_urls()
    for url in urls:
        scan_url(url, known_domains)
