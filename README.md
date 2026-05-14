 # LangGraph Workflows

 A curated collection of Jupyter notebooks that demonstrate LangGraph-based workflows, multi-agent orchestration patterns, and tool integrations (LangChain, Tavily, Google Generative API, Groq examples).

 ## Features

 - Examples of building simple chatbots and multi-agent systems using `langgraph`.
 - Demonstrations of tool integrations (web search, math helpers, human-in-the-loop interrupts).
 - Supervisor / orchestrator examples showing multi-agent sequencing (researcher, analyst, writer).

 ## Prerequisites

 - Python 3.10 or newer
 - `pip` and a virtual environment manager (`venv`, `virtualenv`, or similar)

 ## Setup

 1. Create and activate a virtual environment:

 ```bash
 python3 -m venv .venv
 source .venv/bin/activate
 ```

 2. Install core dependencies used across the notebooks (most of the dependencies are pre-installed in google colab)

 ```bash
 pip install --upgrade pip
 pip install langchain-google-genai langchain_tavily langchain_community langgraph
 ```

 3. Optional: create a `requirements.txt` for reproducible installs:

 ```bash
 pip freeze > requirements.txt
 ```

 ## Environment variables

 Some notebooks require API keys. Common variables used in the repo:

 - `TAVILY_API_KEY` — Tavily search API key
 - `GEMINI_API_KEY` or `GOOGLE_API_KEY` — Google/Gemini API key (notebooks use one or the other)
 - `LANGSMITH_API_KEY` — Optional, used in tracing examples
 - `GROQ_API_KEY` — Optional, for Groq-based examples if you enable them

 Example (Linux/macOS):

 ```bash
 export TAVILY_API_KEY="your_tavily_key"
 export GEMINI_API_KEY="your_gemini_key"
 export LANGSMITH_API_KEY="your_langsmith_key"   # optional
 ```

 Tip: For local development consider using a `.env` file and `python-dotenv` to load keys.

 ## Running the notebooks

 - Start Jupyter Lab/Notebook and open the .ipynb files:

 ```bash
 jupyter lab
 # or
 jupyter notebook
 ```

 - Execute a notebook headlessly (for CI or testing) using `nbconvert`:

 ```bash
 jupyter nbconvert --to notebook --execute Supervise_MultiAI_Agent_Architecture.ipynb --inplace
 ```

 - For parameterized runs, you can use `papermill`:

 ```bash
 pip install papermill
 papermill input.ipynb output.ipynb -p some_param value
 ```

 ## Notebooks (summary)

 - [Build_A_Basic_Chatbot_With_Langgraph.ipynb](Build_A_Basic_Chatbot_With_Langgraph.ipynb) — Minimal LLM chatbot built with LangGraph; shows basic StateGraph usage.
 - [Chatbot_with_Tools.ipynb](Chatbot_with_Tools.ipynb) — Chatbot demonstrating tool calls (web search, math functions) and tool-condition routing.
 - [Human_In_the_Loop.ipynb](Human_In_the_Loop.ipynb) — Demonstrates interruptible tool execution and human-in-the-loop resume via `interrupt`/`Command`.
 - [Re_Act_Agent.ipynb](Re_Act_Agent.ipynb) — ReACT-style loop with tool usage and memory tracing.
 - [simple_multi_ai_agent.ipynb](simple_multi_ai_agent.ipynb) — Simple multi-agent workflow with researcher/writer roles and ToolNode examples.
 - [Supervise_MultiAI_Agent_Architecture.ipynb](Supervise_MultiAI_Agent_Architecture.ipynb) — Supervisor/Orchestrator example showing researcher → analyst → writer sequencing, and how to compile a StateGraph.

 ## Development tips

 - Install notebook dependencies ahead of time (many notebooks run `pip install` inline which can slow interactive use).
 - Use a consistent virtual environment and pin versions in `requirements.txt` when sharing or running in CI.
 - Replace placeholder API keys in notebooks with environment variables for safety.

 ## Contributing

 - Contributions, bug reports, and PRs welcome. Suggested improvements:
	 - Add `requirements.txt` with pinned versions
	 - Add lightweight runner scripts to execute key notebooks
	 - Add unit tests or CI workflows for reproducibility

 ## License

 - See the repository [LICENSE](LICENSE) for license terms.

