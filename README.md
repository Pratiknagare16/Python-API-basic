# Consuming Real-World Data via APIs

A hands-on practice repository for learning how to fetch live data using Python and APIs.

## Overview

An **API (Application Programming Interface)** is a bridge between two applications. We use the Python `requests` library to "ask" a server for data, which usually comes back in **JSON** format (similar to Python dictionaries).

## Key Concepts

| Concept | Description |
|---------|-------------|
| **HTTP GET** | Fetching/retrieving data from a server |
| **HTTP POST** | Sending data to a server |
| **Status 200** | Success - request completed |
| **Status 404** | Not Found - resource doesn't exist |
| **Status 401** | Unauthorized - API key missing/invalid |
| **JSON** | Data format that looks like Python dictionaries |

## Setup

```bash
# Install required library
pip install requests

# Or use requirements.txt
pip install -r requirements.txt
```

## Practice Files (Progressive Difficulty)

| File | Difficulty | Topic |
|------|------------|-------|
| `part1_basic_request.py` | Beginner | Simple GET request |
| `part2_status_codes.py` | Beginner+ | Understanding response codes |
| `part3_user_input.py` | Intermediate | Dynamic queries with input() |
| `part4_error_handling.py` | Intermediate+ | Robust error handling |
| `part5_real_api.py` | Advanced | Real-world API (Weather/Crypto) |

## How to Run

```bash
python part1_basic_request.py
python part2_status_codes.py
python part3_user_input.py
python part4_error_handling.py
python part5_real_api.py
```

## Testing APIs Before Coding

### Using cURL (Command Line)
```bash
# Test a simple API
curl https://api.coinpaprika.com/v1/coins/btc-bitcoin

# Test with headers
curl -H "Accept: application/json" https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
```

### Using Postman
1. Download Postman from https://www.postman.com/downloads/
2. Create a new GET request
3. Enter the API URL
4. Click "Send" and observe the JSON response
5. Check for `200 OK` status

## Free APIs Used (No API Key Required)

| API | Description | Documentation |
|-----|-------------|---------------|
| JSONPlaceholder | Fake REST API for testing | https://jsonplaceholder.typicode.com/ |
| Open-Meteo | Weather data | https://open-meteo.com/ |
| CoinPaprika | Cryptocurrency data | https://api.coinpaprika.com/ |

## Activity Submission Checklist

- [ ] Screenshot 1: Python code in VS Code
- [ ] Screenshot 2: Terminal output with live data
- [ ] Screenshot 3: Postman showing 200 OK status
- [ ] Screenshot 4: cURL command result

## Caption Template
> "Today I fetched live data for [Your Chosen Topic]! I learned how to handle GET requests in Python."

## Resources

- [Requests Library Documentation](https://docs.python-requests.org/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [JSON Format](https://www.json.org/)
