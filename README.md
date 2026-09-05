# Simple AI Agent with Gemini

A simple AI agent built with **Python and the OpenAI Agents SDK**, configured to use **Google Gemini** through its OpenAI-compatible API endpoint.

This project demonstrates how to configure an external LLM provider, create an AI agent, execute it asynchronously, and display the agent's final response in the VS Code terminal.

---

## 🚀 Overview

This project is a beginner-friendly implementation of an AI agent using the **OpenAI Agents SDK**.

Instead of using OpenAI's default API directly, the project configures the SDK to communicate with **Google Gemini** through Gemini's OpenAI-compatible API.

The agent receives a prompt, processes it using the configured Gemini model, and prints the final response in the terminal.

---

## ✨ Features

* 🤖 AI agent built with OpenAI Agents SDK
* 🧠 Google Gemini model integration
* 🔄 OpenAI-compatible Gemini API configuration
* ⚡ Asynchronous agent execution
* 🔐 Environment variable-based API key configuration
* 💻 Terminal-based interaction
* ⚙️ Custom default OpenAI client configuration
* 🚫 OpenAI Agents SDK tracing disabled

---

## 🛠️ Tech Stack

| Technology        | Purpose                                  |
| ----------------- | ---------------------------------------- |
| Python 3.13+      | Programming language                     |
| OpenAI Agents SDK | Agent creation and execution             |
| Google Gemini     | AI model provider                        |
| AsyncOpenAI       | Gemini API client configuration          |
| python-dotenv     | Environment variable management          |
| uv                | Python project and dependency management |

---

## 📁 Project Structure

```text
Simple-Agent-main/
│
├── README.md
│
└── my-agent/
    └── agent1/
        ├── README.md
        ├── dotenv
        ├── pyproject.toml
        ├── uv.lock
        │
        └── src/
            └── agent1/
                ├── __init__.py
                ├── async1pro.py
                └── global_config.py
```

---

## 📌 Important File

### `global_config.py`

This is the main AI-agent implementation.

It handles:

* Loading the Gemini API key from environment variables
* Creating an `AsyncOpenAI` client
* Configuring Gemini's OpenAI-compatible API endpoint
* Setting Gemini as the default provider
* Configuring the Chat Completions API
* Disabling OpenAI Agents SDK tracing
* Creating the AI agent
* Running the agent asynchronously
* Printing the final response

---

## 🧠 How It Works

The project follows this workflow:

```text
User Prompt
     │
     ▼
OpenAI Agents SDK
     │
     ▼
Agent Configuration
     │
     ▼
AsyncOpenAI Client
     │
     ▼
Google Gemini OpenAI-Compatible API
     │
     ▼
Gemini Model
     │
     ▼
Agent Response
     │
     ▼
VS Code Terminal
```

The project configures an external Gemini provider using:

```python
external_provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
```

The configured client is then set as the default OpenAI client for the Agents SDK:

```python
set_default_openai_client(external_provider)
```

The project also configures the API communication method:

```python
set_default_openai_api("chat_completions")
```

---

## 🤖 Agent Configuration

The AI agent is created using the OpenAI Agents SDK:

```python
agent = Agent(
    name="Assistant",
    instructions="You are good agent.",
    model="gemini-2.0-flash"
)
```

The agent uses:

* **Name:** Assistant
* **Instructions:** You are good agent.
* **Model:** Gemini 2.0 Flash

The agent is then executed using:

```python
result = await Runner.run(
    agent,
    "hello how are you and what are you doing?"
)
```

The final response is displayed using:

```python
print(result.final_output)
```

---

## 🔐 Environment Configuration

The project loads the Gemini API key using `python-dotenv`.

Create a `.env` file in the `agent1` project directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### Important

Never commit your real API key to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

---

## 📋 Prerequisites

Before running the project, make sure you have:

* Python **3.13 or newer**
* Git
* `uv`
* A valid Google Gemini API key

---

## 🚀 Installation


### 1. Navigate to the Agent Project

```bash
cd Simple-Agent-main/my-agent/agent1
```

### 2. Install Dependencies

Using `uv`:

```bash
uv sync
```

This installs the dependencies defined in `pyproject.toml`.

---

## ▶️ Run the AI Agent

The project defines the following command:

```text
agent2
```

To run the configured AI agent using `uv`:

```bash
uv run agent2
```

The agent will execute the configured prompt and print the final Gemini response in the terminal.

---

## ⚙️ Project Configuration

The `pyproject.toml` defines the main project dependencies:

```toml
dependencies = [
    "dotenv>=0.9.9",
    "openai-agents>=0.0.14",
]
```

It also defines the following project commands:

```toml
[project.scripts]
agent1 = "agent1:main"
agent2 = "agent1.global_config:run_global"
```

The `agent2` command is connected to the actual AI-agent implementation in `global_config.py`.

---

## 🔄 API Provider Configuration

This project demonstrates an important concept: using the **OpenAI Agents SDK with a third-party provider**.

The project replaces the default OpenAI client with a Gemini-compatible client:

```python
set_default_openai_client(external_provider)
```

This allows the agent to communicate with Gemini using its OpenAI-compatible endpoint.

---

## 🎯 Learning Objectives

This project helps demonstrate:

* Creating AI agents with the OpenAI Agents SDK
* Configuring an external LLM provider
* Using Google Gemini with an OpenAI-compatible API
* Working with asynchronous Python functions
* Managing API keys with environment variables
* Running AI applications from the terminal
* Understanding basic agent execution flow

---

## 👨‍💻 Author

**Muhammad Zimad**

Data Analyst | AI Agent & Chatbot Developer | Python & Workflow-Automation

GitHub:
https://github.com/Muhammad-zimad
