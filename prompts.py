def get_code_explanation_prompt(code_snippet: str, programming_language: str, detail_level: str) -> str:
    """
    Generates a prompt for code explanation based on the detail level.
    """
    
    requirements = ""
    if detail_level == "Basic":
        requirements = """
1. **Overview**: Simple overview of what this code does (2-3 sentences)
2. **Main Purpose**: Explain the main goal in plain English
3. **Key Components**: List the most important parts
4. **Simple Analogy**: Use a relatable analogy
5. **Output**: Describe what the code outputs or achieves
"""
    elif detail_level == "Medium":
        requirements = """
1. **Overview**: Explain what this code does overall (2-3 sentences)
2. **Step-by-Step Breakdown**: Go through the code section by section
3. **Key Concepts**: Identify important programming concepts used
4. **Logic Flow**: Describe how data flows through the code
5. **Analogies**: Use 1-2 real-world analogies
6. **Potential Issues**: Identify any bugs or edge cases
7. **Improvements**: Suggest 2-3 improvements
8. **Complexity Analysis**: Time and Space complexity (Big O)
"""
    else:  # Advanced
        requirements = """
1. **Executive Summary**: High-level technical summary
2. **Line-by-Line Analysis**: Deep dive into every logical unit
3. **Design Patterns**: Identify any patterns or architecture styles
4. **Performance Analysis**: In-depth Big O analysis and potential bottlenecks
5. **Code Quality Assessment**: Evaluate readability, maintainability, and idioms
6. **Security Considerations**: Highlight potential vulnerabilities
7. **Refactoring Suggestions**: Concrete examples of how to rewrite for better quality
8. **Testing Recommendations**: How would you unit test this code?
"""

    prompt = f"""
You are an expert programming tutor explaining code to students. Analyze and explain the following {programming_language} code.

CODE TO ANALYZE:
```{programming_language}
{code_snippet}
```

EXPLANATION REQUIREMENTS (Level: {detail_level}):
{requirements}

FORMAT YOUR RESPONSE:
- Use markdown headers (##, ###) for sections
- Use bullet points for lists
- Use code blocks with syntax highlighting for code examples
- Use **bold** for important terms
- Use *italic* for emphasis
- Keep paragraphs concise and readable
"""
    return prompt

def get_specific_question_prompt(code_snippet: str, programming_language: str, question: str) -> str:
    """
    Generates a prompt to answer a specific question about the code.
    """
    prompt = f"""
You are an expert developer. Answer a specific question about this {programming_language} code.

CODE:
```{programming_language}
{code_snippet}
```

QUESTION: {question}

INSTRUCTIONS:
- Provide a direct, accurate answer to the question
- Reference specific lines or sections of the code
- Explain the "why" behind the answer
- If the question is irrelevant to the code, politely point that out
- Use markdown formatting for clarity
"""
    return prompt

def get_debugging_prompt(code_snippet: str, programming_language: str, error_message: str = "") -> str:
    """
    Generates a prompt to debug and fix issues in the code.
    """
    error_info = f"ERROR MESSAGE/SYMPTOM: {error_message}" if error_message else "SYMPTOM: The code is not working as expected."
    
    prompt = f"""
You are a senior debugger. Identify bugs, logical errors, or performance issues in this {programming_language} code.

CODE:
```{programming_language}
{code_snippet}
```

{error_info}

INSTRUCTIONS:
1. **Issue Identification**: Clearly list the bugs or errors found
2. **Root Cause**: Explain why these issues are occurring
3. **Fixed Code**: Provide the corrected version of the code
4. **Explanation of Changes**: Explain what was changed and why
5. **Prevention**: How to avoid such mistakes in the future

FORMAT: Use clear markdown sections.
"""
    return prompt

def get_optimization_prompt(code_snippet: str, programming_language: str) -> str:
    """
    Generates a prompt for code optimization suggestions.
    """
    prompt = f"""
You are a performance engineer. Suggest optimizations for this {programming_language} code to make it faster or more memory-efficient.

CODE:
```{programming_language}
{code_snippet}
```

INSTRUCTIONS:
1. **Bottleneck Analysis**: Identify where the code is slow or inefficient
2. **Optimized Version**: Provide an optimized version of the code
3. **Comparison**: Explain the improvements in terms of Time/Space complexity
4. **Trade-offs**: Mention any trade-offs (e.g., readability vs. speed)

FORMAT: Use clear markdown sections.
"""
    return prompt

def get_comparison_prompt(code1: str, code2: str, programming_language: str) -> str:
    """
    Generates a prompt to compare two code snippets.
    """
    prompt = f"""
You are an expert code reviewer. Compare these two {programming_language} snippets.

CODE SNIPPET 1:
```{programming_language}
{code1}
```

CODE SNIPPET 2:
```{programming_language}
{code2}
```

INSTRUCTIONS:
1. **Functionality**: Do they do the same thing?
2. **Performance**: Which one is more efficient?
3. **Readability**: Which one is easier to understand and maintain?
4. **Best Practices**: Which one follows {programming_language} idioms better?
5. **Recommendation**: Which one would you recommend using and why?

FORMAT: Use a comparison table if applicable and clear sections.
"""
    return prompt
