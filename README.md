# 💻 Code Explainer AI

A production-ready Web Application that uses Google's latest **Gemini 3 Pro (Preview)** to analyze, explain, debug, and optimize code snippets in 30+ programming languages.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **Advanced Analysis**: Powered by the cutting-edge `gemini-3-pro-preview` model.
- **Multiple Modes**:
    - **Explain Code**: Get detailed explanations at Basic, Medium, or Advanced levels.
    - **Ask Question**: Ask specific technical questions about your code.
    - **Debug Code**: Identify syntax errors and logical bugs with fixed code solutions.
    - **Optimize Code**: Get performance and memory efficiency suggestions (Big O analysis).
    - **Compare Code**: Side-by-side comparison of two diverse implementations.
- **Analysis History**: Tracks your recent sessions in the sidebar for quick reloading.
- **Auto-Detection**: Automatically identifies programming languages using `Pygments`.
- **Clean UI**: A minimalist, dark-themed interface focused purely on code and analysis.
- **Export**: Download any analysis as a formatted Markdown file.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/app/apikey))
  - *Note: You can configure this in `.env` for local use, or enter it directly in the app sidebar.*

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd code-explainer-ai
   ```

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   - Rename `.env.example` to `.env`.
   - Add your API key:
     ```env
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

### Running the App

```bash
streamlit run app.py
```

The application will launch automatically in your browser at `http://localhost:8501`.

## 🛠️ Project Structure

- **`app.py`**: Main Streamlit application and UI logic.
- **`code_analyzer.py`**: Integration with Google Gemini API (`gemini-3-pro-preview`).
- **`prompts.py`**: Optimized prompt templates for different analysis modes.
- **`utils.py`**: Helper functions for language detection and validation.
- **`check_models.py`**: Script to verify available Gemini models for your API key.
- **`PRD.md`**: Detailed Product Requirements Document.

## 🧩 Usage

1. **Paste Code**: Copy your snippet into the main text area.
2. **Select Mode**: Choose between Explain, Debug, Optimize, etc., from the sidebar.
3. **Analyze**: Click the **🚀 Analyze Code** button.
4. **Review & History**: Read the output or reload previous analyses from the sidebar history.
5. **Download**: Save the result as a `.md` file for documentation.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
