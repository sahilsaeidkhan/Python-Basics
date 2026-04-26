import urllib.request
import json

API_KEY = "AIzaSyDvaD-Q3aVWrxt8IxyarVlCFfeZQf3fsHk"  # Paste new key here

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [{"parts": [{"text": "Say hello in one word"}]}]
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read())
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        print("✅ API Key is WORKING!")
        print(f"Response: {text}")
except urllib.error.HTTPError as e:
    error = json.loads(e.read())
    print("❌ API Key FAILED!")
    print(f"Error: {error['error']['message']}")

# Question (medium)
# Given a string, return the length of its longest substring that contains no repeating
# characters.

import sys

def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    Uses a sliding window with a hash map to store the latest index of each character.
    """
    last_seen = {}
    start = 0
    max_len = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - start + 1)

    return max_len

if __name__ == "__main__":
    test_cases = [
        "abcabcbb",   # expected 3 ("abc")
        "bbbbb",      # expected 1 ("b")
        "pwwkew",     # expected 3 ("wke")
        "",           # expected 0
        "au",         # expected 2 ("au")
        "dvdf",       # expected 3 ("vdf")
    ]

    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: '{s}' -> Length of longest non-repeating substring: {result}")
