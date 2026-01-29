# 💻 Code Explainer AI

A production-ready Web Application that uses Google's latest **Gemini** models to analyze, explain, debug, and optimize code snippets in 30+ programming languages.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **Multi-Mode Analysis**:
    - **Explain**: Detailed code walkthroughs (Basic/Medium/Advanced).
    - **Debug**: Auto-detect bugs and provide fixed code.
    - **Optimize**: Performance improvements and Big O analysis.
    - **Compare**: Compare two snippets side-by-side.
    - **Ask**: Chat with your code.
- **Bring Your Own Key**: Securely use the app with your own API key via the UI.
- **History**: Sidebar session history for quick access.
- **Export**: Download analysis as Markdown.

## 🚀 How to Run

### Local Installation
1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd code-explainer-ai
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

### Configuration
You can provide your Google Gemini API Key in two ways:
1.  **UI (Recommended for Demo)**: Enter it directly in the app sidebar.
2.  **.env File**: Create a `.env` file and set `GOOGLE_API_KEY=your_key`.

## ☁️ Deployment

This app is optimized for **Streamlit Community Cloud**.
👉 **[Read the Deployment Guide](DEPLOYMENT.md)** for step-by-step instructions.

## 📂 Project Structure

- `app.py`: Main application entry point.
- `code_analyzer.py`: Gemini API integration.
- `prompts.py`: System prompts for different analysis modes.
- `utils.py`: Helper functions (language detection, file processing).

## 📄 License
This project is licensed under the MIT License.
