# LangGraph Workflows

A curated collection of Jupyter notebooks demonstrating LangGraph-based workflows, multi-agent orchestration patterns, and tool integrations. Includes examples with LangChain, Tavily, Google Generative API, and Groq.

## Overview

Build production-ready AI agents and multi-agent systems with LangGraph. This repository showcases:

- **Simple Chatbots & Agents**: Single-agent systems using LangGraph's StateGraph API
- **Multi-Agent Orchestration**: Supervisor/orchestrator patterns with specialized agents (researcher, analyst, writer)
- **Tool Integration**: Web search, API calls, math functions, and custom tool bindings
- **Human-in-the-Loop**: Interrupt patterns for human oversight and approval workflows
- **Memory & Persistence**: Stateful agents with short-term and long-term memory

## Key Features

- ✅ Built for **LangChain v1.0+** (all agents now use LangGraph)
- ✅ LangGraph Studio integration for visual graph design
- ✅ Examples of **durable execution** with interrupts and resumption
- ✅ Tool use patterns (web search via Tavily, LLM function calling)
- ✅ Multiple LLM provider examples (Google, Groq, OpenAI-compatible)
- ✅ Streaming and async support
- ✅ Production deployment patterns

## Prerequisites

- **Python 3.11+** (3.12 recommended)
- `pip` and a virtual environment (`venv`, `uv`, or similar)
- API keys for LLM providers and tools (see [Environment Variables](#environment-variables))

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/raj-tembe/LangGraph-Workflows.git
cd LangGraph-Workflows

# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip setuptools

# Core dependencies (compatible with LangChain v1.0)
pip install langgraph langchain langchain-google-genai langchain-tavily langchain-community groq jupyter
```

**Or** install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the repository root:

```bash
# Required
TAVILY_API_KEY="your_tavily_api_key_here"

# Choose one LLM provider:
GOOGLE_API_KEY="your_google_api_key"           # For Google Gemini
# OR
GROQ_API_KEY="your_groq_api_key"              # For Groq

# Optional
LANGSMITH_API_KEY="your_langsmith_key"         # For debugging & observability
OPENAI_API_KEY="your_openai_key"              # If using OpenAI models
```

**Load variables with `python-dotenv`:**

```bash
pip install python-dotenv
```

Then in your notebook:
```python
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
```

### 4. Run a Notebook

```bash
# Launch Jupyter
jupyter lab
# or
jupyter notebook
```

Then open any `.ipynb` file and follow the cell instructions.

## Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `TAVILY_API_KEY` | Tavily web search API | Yes (for search examples) |
| `GOOGLE_API_KEY` | Google Gemini API key | One LLM required |
| `GROQ_API_KEY` | Groq API key | One LLM required |
| `LANGSMITH_API_KEY` | LangSmith tracing & evals | Optional |
| `OPENAI_API_KEY` | OpenAI API key | Optional |

## Notebooks Overview

| Notebook | Description | Key Topics |
|----------|-------------|-----------|
| `Build_A_Basic_Chatbot_With_Langgraph.ipynb` | Minimal chatbot using StateGraph | Nodes, edges, state management |
| `Chatbot_with_Tools.ipynb` | Chatbot with tool calling (search, math) | Tool nodes, routing, conditional edges |
| `Human_In_the_Loop.ipynb` | Interrupt workflows with human approval | Breaks, resumption, state persistence |
| `Re_Act_Agent.ipynb` | ReACT-style agent loop with memory | Reasoning, acting, observation tracking |
| `simple_multi_ai_agent.ipynb` | Multi-agent workflows (researcher/writer) | Subgraphs, agent coordination |
| `Supervise_MultiAI_Agent_Architecture.ipynb` | Supervisor orchestrating specialized agents | Routing logic, agent composition, compilation |

## Running Notebooks Programmatically

### Execute with `nbconvert`

```bash
jupyter nbconvert --to notebook --execute Supervise_MultiAI_Agent_Architecture.ipynb --inplace
```

### Parameterized Execution with `papermill`

```bash
pip install papermill

# Run notebook with custom parameters
papermill input.ipynb output.ipynb \
  -p model_name "gemini-2.0-flash" \
  -p temperature 0.7
```

### Execute Python Script from Notebook

```bash
# Convert notebook to script
jupyter nbconvert --to script Build_A_Basic_Chatbot_With_Langgraph.ipynb

# Run the script
python Build_A_Basic_Chatbot_With_Langgraph.py
```

## Development Setup

### Virtual Environment with `uv` (Faster alternative)

```bash
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Generate `requirements.txt`

```bash
pip freeze > requirements.txt
```

### Pre-install Dependencies for Better Notebook Performance

Jupyter notebooks can be slow with inline `pip install` calls. Pre-install dependencies in your `.venv` before starting Jupyter to improve interactive experience.

## LangGraph Studio Integration

For visual graph design and debugging:

1. Install LangGraph CLI:
   ```bash
   pip install langgraph-cli
   ```

2. Create a `langgraph.json` config for your agents

3. Run locally:
   ```bash
   langgraph dev
   ```

4. Access at `http://localhost:8000`

See [LangGraph Studio Docs](https://docs.langchain.com/langgraph) for details.

## Deployment & Production Tips

### Local Testing
```bash
# Test graph execution with different inputs
python -m pytest tests/  # If tests directory exists
```

### Deploy to LangGraph Cloud
1. Set up LangGraph API keys
2. Configure `langgraph.json` with your graph definition
3. Deploy via LangGraph CLI or Python SDK

### Docker Deployment
```bash
docker build -t langgraph-workflows .
docker run -e TAVILY_API_KEY="..." -e GOOGLE_API_KEY="..." langgraph-workflows
```

## Best Practices

- ✅ **Use environment variables** for API keys (never commit secrets)
- ✅ **Pin package versions** in `requirements.txt` for reproducibility
- ✅ **Enable LangSmith tracing** during development for debugging complex agent flows
- ✅ **Test graphs locally** before deployment with different scenarios
- ✅ **Use streaming** for responsive user-facing applications
- ✅ **Implement error handling** with try-catch around tool calls
- ✅ **Monitor agent loops** to avoid infinite recursion; set max iterations

## Troubleshooting

### Common Issues

**Import Error: `langgraph` not found**
```bash
# Make sure venv is activated and packages installed
pip install --upgrade langgraph langchain
```

**API Key Errors**
- Verify `.env` file exists and keys are correct
- Check API quotas and billing status
- Use `echo $TAVILY_API_KEY` to confirm env vars are loaded

**Slow Notebook Execution**
- Pre-install all dependencies before starting Jupyter
- Use streaming output for faster feedback
- Monitor token usage with LangSmith

**Graph Compilation Errors**
- Ensure all nodes are defined before edges reference them
- Check state type annotations match across nodes
- Use `graph.compile().validate()` for early error detection

## Contributing

Contributions are welcome! Please:

1. **Add new notebooks** with clear examples and docstrings
2. **Include `requirements.txt`** with pinned versions for reproducibility
3. **Add unit tests** or CI workflows for key examples
4. **Update this README** with new notebook descriptions
5. **Share insights** on multi-agent patterns and orchestration strategies

**Ideas for contributions:**
- [ ] Lightweight test suite for notebook execution
- [ ] CI/CD pipeline for automated notebook testing
- [ ] Docker setup with pre-configured environments
- [ ] Deployment templates for cloud platforms
- [ ] Advanced patterns: nested graphs, memory management, monitoring

## Resources

- 📖 [LangGraph Documentation](https://docs.langchain.com/langgraph)
- 📖 [LangChain v1.0 Docs](https://docs.langchain.com/)
- 📖 [LangSmith Debugging](https://docs.langsmith.com/)
- 🎓 [LangChain Academy](https://academy.langchain.com/) — Interactive courses
- 💬 [LangChain Discord Community](https://discord.gg/langchain)

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Last Updated:** June 2026  
**Tested with:** LangChain v1.0+, LangGraph 0.2.0+, Python 3.11–3.12