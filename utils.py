import re
from typing import Dict, List, Optional, Any
from pygments.lexers import guess_lexer, get_lexer_by_name, ClassNotFound
from pygments.util import ClassNotFound as PygmentsClassNotFound

# Supported languages for manual selection
SUPPORTED_LANGUAGES = [
    "Auto-detect", "Python", "JavaScript", "TypeScript", "Java", "C++", "C", "C#", 
    "Go", "Rust", "Swift", "Kotlin", "PHP", "Ruby", "SQL", "HTML", "CSS", 
    "Shell", "PowerShell", "R", "Dart", "Scala", "Haskell", "Lua", "Perl", 
    "Objective-C", "Assembly", "MATLAB", "Fortran", "COBOL"
]

# Sample codes for testing
SAMPLE_CODES = {
    "Python - Bubble Sort": """def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(f"Sorted array: {sorted_numbers}")""",

    "JavaScript - Async Fetch": """async function fetchUserData(userId) {
    const url = `https://api.example.com/users/${userId}`;
    
    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("User data received:", data);
        return data;
    } catch (error) {
        console.error("Could not fetch user data:", error);
        return null;
    }
}

// Call the function
fetchUserData(12345);""",

    "Python - Fibonacci Recursive": """def fibonacci(n):
    \"\"\"
    Calculate the nth Fibonacci number using recursion.
    \"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calculate first 10 numbers
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")"""
}

def detect_language(code: str) -> str:
    """
    Detect the programming language using Pygments.
    """
    if not code.strip():
        return "Unknown"
    
    try:
        lexer = guess_lexer(code)
        # Map pygments lexer names to our supported display names if possible
        name = lexer.name
        if "Python" in name: return "Python"
        if "JavaScript" in name: return "JavaScript"
        if "TypeScript" in name: return "TypeScript"
        if "C++" in name: return "C++"
        if "Java" in name: return "Java"
        if "C#" in name: return "C#"
        if "Go" in name: return "Go"
        if "Rust" in name: return "Rust"
        if "SQL" in name: return "SQL"
        if "HTML" in name: return "HTML"
        if "CSS" in name: return "CSS"
        return name
    except Exception:
        return "Unknown"

def validate_code(code: str) -> tuple[bool, str]:
    """
    Validate input code snippet.
    """
    code = code.strip()
    if not code:
        return False, "Code snippet cannot be empty."
    if len(code) < 10:
        return False, "Code snippet is too short to analyze (minimum 10 characters)."
    if len(code) > 50000:
        return False, "Code snippet is too long (maximum 50,000 characters)."
    return True, ""

def count_lines(code: str) -> int:
    """
    Count total lines of code.
    """
    return len(code.splitlines())

def estimate_complexity(code: str) -> str:
    """
    Estimate code complexity based on common keywords.
    """
    score = 0
    # Higher score = more complex
    score += len(re.findall(r'\b(if|else|elif|switch|case)\b', code))
    score += len(re.findall(r'\b(for|while|foreach|do)\b', code)) * 2
    score += len(re.findall(r'\b(def|function|class|interface|async)\b', code)) * 3
    score += len(re.findall(r'\b(try|catch|finally|throw|raise)\b', code)) * 2
    
    if score < 5:
        return "Simple"
    elif score < 15:
        return "Moderate"
    elif score < 30:
        return "Complex"
    else:
        return "Very Complex"

def extract_functions(code: str) -> List[str]:
    """
    Extract function/method names using basic regex.
    """
    patterns = [
        r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)',           # Python
        r'function\s+([a-zA-Z_][a-zA-Z0-9_]*)',      # JS/PHP
        r'([a-zA-Z_][a-zA-Z0-9_]*)\s*\(.*?\)\s*\{', # C-style
        r'([a-zA-Z_][a-zA-Z0-9_]*)::\s*function',     # Some OOP
    ]
    
    functions = []
    for pattern in patterns:
        matches = re.findall(pattern, code)
        functions.extend(matches)
    
    return list(set(functions))

def get_code_stats(code: str) -> Dict[str, Any]:
    """
    Return a dictionary with various code metrics.
    """
    return {
        "lines": count_lines(code),
        "chars": len(code),
        "complexity": estimate_complexity(code),
        "functions": len(extract_functions(code))
    }
