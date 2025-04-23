# AI Agent Demo with agno and OpenAI

This is a minimal example of an AI agent using the [agno](https://github.com/agno-agi/agno) framework and OpenAI's GPT model.

## Features
- Uses agno for agent structure
- Integrates with OpenAI's GPT-3.5-turbo for responses
- Loads API key securely from a `.env` file

## Setup

1. **Clone this repository**
2. **Install dependencies**:
   ```sh
   pip install agno openai python-dotenv
   ```
3. **Create a `.env` file** in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. **Run the agent**:
   ```sh
   python agent.py
   ```

## Usage
Type your message at the prompt. The agent will respond using OpenAI's GPT model.

## Security
- The `.env` file is gitignored to keep your API key safe.

## License
MIT
