---
title: Template Final Assignment
emoji: 🕵🏻‍♂️
colorFrom: indigo
colorTo: indigo
sdk: gradio
sdk_version: 5.25.2
app_file: app.py
pinned: false
hf_oauth: true
# optional, default duration is 8 hours/480 minutes. Max duration is 30 days/43200 minutes.
hf_oauth_expiration_minutes: 480
---

# Hugging Face Agent Course Assignment Agent

## Introduction

This project implements an intelligent AI agent designed to answer complex questions from the GAIA benchmark dataset for the **Hugging Face Agent Course**. The agent is equipped with a comprehensive toolkit of specialized functions to handle diverse question types.

The agent is capable of processing multimodal inputs including text, images, audio files, Excel spreadsheets, and web content. It can perform tasks such as:

- **Information Retrieval**: Searching Wikipedia and visiting web pages for factual information
- **Audio Processing**: Downloading YouTube videos, extracting audio, and transcribing speech
- **Chess Analysis**: Analyzing chess board images and suggesting optimal moves using Stockfish engine
- **File Processing**: Reading and analyzing various file formats (text, Excel, images)
- **Text Manipulation**: Performing operations like word reversal for puzzle-solving
- **Web Scraping**: Extracting content from web pages for analysis

This assignment was done using Google's gemini free models, a timer and also rotating models were used to work around rate limiting that the free tier has. The agent is deployed as a Gradio interface on Hugging Face Spaces, allowing users to interact with it through a web-based UI. Currently, the agent achieves a **45% success rate** on the GAIA benchmark, demonstrating strong performance across various question categories.

## Setup

### Prerequisites

- Python 3.8 or higher
- API Key for model
- Stockfish chess engine executable

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd HF_Final_Assignment
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration:**
   Create a `.env` file in the root directory and add your API keys:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Stockfish Setup:**
   - Download Stockfish chess engine from [stockfishchess.org](https://stockfishchess.org/)
   - Place the `stockfish.exe` (or appropriate binary for your OS) in the project root directory

### Dependencies

The project requires the following main dependencies:

- **gradio**: Web interface framework
- **smolagents**: Agent framework with LiteLLM integration
- **wikipedia**: Wikipedia API access
- **openai-whisper**: Audio transcription
- **librosa**: Audio processing
- **python-chess**: Chess game logic
- **openpyxl**: Excel file reading
- **requests**: HTTP requests
- **PIL (Pillow)**: Image processing

### Running the Application

1. **Local Development:**
   ```bash
   python app.py
   ```

2. **Testing the Agent:**
   ```bash
   python agent.py
   ```

### Deployment on Hugging Face Spaces

The application is configured for deployment on Hugging Face Spaces with OAuth integration. The `app.py` file includes the necessary configuration for:

- User authentication
- Question fetching from the GAIA benchmark API
- Answer submission and scoring
- Results display

## Architecture

The agent follows a modular architecture:

- **`agent.py`**: Core agent implementation using smolagents framework
- **`tools.py`**: Custom tool definitions for specialized tasks
- **`app.py`**: Gradio interface and GAIA benchmark integration
- **`requirements.txt`**: Project dependencies

## Conclusion

This project demonstrates the successful implementation of a multi-modal AI agent capable of handling diverse question types through specialized tools and reasoning. The agent's **45% success rate** on the GAIA benchmark represents a solid foundation that showcases the effectiveness of the modular tool-based approach.

The combination of Google's Gemini model with carefully crafted tools enables the agent to tackle complex problems requiring multiple steps, file processing, and cross-modal understanding. The Gradio interface provides an accessible way for users to interact with the agent, while the Hugging Face Spaces deployment ensures easy access and scalability.

## Technical Insights and Lessons Learnt

1. **Tool Design Importance**: The quality and specificity of custom tools significantly impact agent performance. Well-designed tools with clear documentation and error handling are crucial for reliable operation.

2. **Model Selection**: Using Gemini 2.5 Flash with fallback models provides a good balance between performance and cost. The model's multimodal capabilities are essential for handling diverse input types.

3. **Answer Formatting**: GAIA benchmark requires exact answer matching, making answer cleaning and formatting critical. Removing common model prefixes and normalizing responses improved accuracy significantly.

4. **Error Handling**: Robust error handling in both tools and the main agent loop prevents cascading failures and provides better user experience.

### Framework Insights

5. **smolagents Effectiveness**: The smolagents framework provides excellent abstractions for building tool-based agents, with good integration capabilities for various LLM providers.

6. **Gradio Integration**: Gradio's OAuth integration and file handling capabilities make it ideal for building agent interfaces, especially for Hugging Face ecosystem deployment.

### Performance Optimization

7. **Step Limitations**: Setting appropriate maximum steps (currently 6) prevents infinite loops while allowing complex multi-step reasoning.

8. **Timeout Management**: Implementing timeouts and delays prevents resource exhaustion and improves system stability.

9. **Multimodal Challenges**: Processing different file types requires specialized handling - chess board analysis, audio transcription, and Excel reading each needed tailored approaches.

### Areas for Improvement

10. **Score Enhancement**: The current 45% score indicates room for improvement, particularly in:
    - Better reasoning strategies for complex multi-step problems
    - Enhanced error recovery mechanisms
    - More sophisticated answer validation
    - Additional specialized tools for specific question domains

11. **Tool Expansion**: Future iterations could benefit from additional tools for mathematical computations, image analysis, and domain-specific knowledge bases.