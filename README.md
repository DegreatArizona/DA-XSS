# DEGREATARIZONA XSS TOOL
The script iterates over a list of common XSS payloads, injecting each payload into the specified parameters of the target URL. It then makes a request to the URL and checks if the payload is reflected in the response. If a potential XSS vulnerability is found, the script outputs the details, including the parameter and payload used.


### Repository Structure

```
DA-XSS/
├── .gitignore
├── README.md
├── requirements.txt
├── xss.py
```

### `.gitignore`
Add the following to the `.gitignore` file to ignore Python bytecode and virtual environment directories:

```
__pycache__/
*.py[cod]
*.pyo
*.pyc
venv/
.env
```

### `README.md`


# XSS Scanner

A simple Python script to scan for Cross-Site Scripting (XSS) vulnerabilities in web applications.

## Features

- Tests a list of common XSS payloads on specified URL parameters.
- Supports custom cookies for authenticated scans.
- Prints potential vulnerabilities and affected parameters.

## Requirements

- Python 3.6+
- `requests`
- `bs4`
- `termcolor`

## Installation

1. Clone the repository:

```sh
git clone https://github.com/DegreatArizona/DA-XSS.git
cd DA-XSS
chmod +x xss.py
```

2. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

```sh
python xss.py <url> <params> [--cookies "key=value;key2=value2"]
```

- `<url>`: The target URL to scan.
- `<params>`: A list of parameters to test for XSS vulnerabilities (e.g., `param1 param2`).
- `--cookies`: Optional. Cookies to include in the request (format: `key=value;key2=value2`).

### Examples

```sh
python xss.py "http://example.com/search" "q"
```

```sh
python xss.py "http://example.com/search" "q" --cookies "sessionid=abcd1234"
```

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on web applications you have permission to test.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### `requirements.txt`

```txt
requests
bs4
termcolor
```

### `xss.py`

Ensure your script is saved with this name.

## Buy Me A Coffee
**Network: Bitcoin**
```
143E54wEKY11g3D7G2czfrJebf19t5S9CJ
```

### `LICENSE`

```markdown
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
