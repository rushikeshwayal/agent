# Domain Intelligence Agent

The **Domain Intelligence Agent** is a versatile tool built using **LangChain**, which integrates multiple **LLMs** (Large Language Models) and tools to classify business domains and retrieve real-time web information. It can use models like **Google's Gemini** or **OpenAI's GPT** for conversational intelligence, and SerpAPI for web search capabilities.

## Features:

- **Real-time Web Search** using **SerpAPI** for retrieving up-to-date and relevant information from the internet.
- **Multiple LLM Integrations**: Use models from **Google** and **OpenAI** to process and classify domain data.
- **Output Parsing**: Supports multiple output parsing formats, including **String**, **JSON**, and **Pydantic**.
- **Customizable**: Easily extendable to add more models or tools.

## Technologies Used:

- **LangChain**: A framework for building applications with LLMs.
- **SerpAPI**: A tool for web search that allows agents to retrieve real-time data.
- **Langchain Generative AI**: Integrated with **Google Gemini** and **OpenAI GPT**.
- **Postgres (pgvector)**: Used for managing and storing vector embeddings.

## How to Use:

### Prerequisites:

- **PostgreSQL** with **pgvector extension** installed https://github.com/pgvector/pgvector
- **SerpAPI API Key** https://serpapi.com/
- **Hugging Face** API Key (Optional for additional models) [No need]
- **OpenAI API Key** (if using OpenAI model)

### Installation:

1. **Clone the repository**:
   ```bash
   git clone
   cd DomainIntelligenceAgent
   ```

### .env

- Create .env file in vertical_agent directory having :

```ini
GOOGLE_API_KEY= <gemini_api_key> <---! Or Whatever Model your Using !--->
SERPAPI_API_KEY = <SERPAPI_API_KEY>
```

> Note : Use Virtual Python Environment
