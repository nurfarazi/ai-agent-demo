# AI Agent Demo with Google Gemini and OpenAI

This is a minimal example of an AI agent that can use either Google Gemini or OpenAI's GPT models for conversational responses.

## Features
- Supports both Google Gemini and OpenAI GPT models
- Loads API keys securely from a `.env` file
- Simple command-line chat interface

## Setup

1. **Clone this repository**
2. **Install dependencies**:
   ```sh
   pip install google-generativeai openai python-dotenv
   ```
3. **Create a `.env` file** in the project root (or copy from `.env.example`):
   ```env
   # Choose your AI provider: "google" or "openai"
   MODEL_PROVIDER=google

   # Google Gemini settings
   GOOGLE_API_KEY=your-google-api-key
   GOOGLE_MODEL_ID=gemini-pro

   # OpenAI settings (optional, if you use OpenAI)
   OPENAI_API_KEY=your-openai-api-key
   OPENAI_MODEL_ID=gpt-3.5-turbo
   ```
4. **Run the agent**:
   ```sh
   python agent.py
   ```

## Configuration

- `MODEL_PROVIDER`  
  • `google` = use Google Gemini  
  • `openai` = use OpenAI GPT  
- `GOOGLE_API_KEY` / `GOOGLE_MODEL_ID` – credentials & model for Gemini  
- `OPENAI_API_KEY` / `OPENAI_MODEL_ID` – credentials & model for OpenAI  

## Usage
Type your message at the prompt. The agent will respond using the configured model (currently set to Google Gemini by default).

## Customization
- To change models, update the respective `*_MODEL_ID` in `.env`.  
- To switch between providers, set `MODEL_PROVIDER` accordingly.  

## Security
- The `.env` file is gitignored to keep your API keys safe.

## License
MIT
