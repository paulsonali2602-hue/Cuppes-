CUPESS AI v1.1
==============

CUPESS AI is a phone-friendly AI coding assistant designed to run on Android using Termux.

FEATURES
--------

- Modern dark browser UI
- Mobile/Android responsive design
- Chat mode
- Coding Agent mode
- Planner -> Coder -> Reviewer workflow
- OpenRouter API support
- Workspace file creation
- Workspace protection
- Model fallback configuration
- New chat button
- Agent pipeline display
- Connection status
- Quick-start prompts


ANDROID / TERMUX SETUP
----------------------

1. Extract the CUPESS AI project into:

/storage/emulated/0/Download/

2. Open Termux.

3. Enter the CUPESS folder:

cd /storage/emulated/0/Download/CUPESS_AI_v1_1

Use the actual folder name if different.

4. Install dependencies:

pip install -r requirements.txt

5. Create the environment file:

cp .env.example .env

6. Open .env and add your OpenRouter API key:

OPENROUTER_API_KEY=YOUR_API_KEY

Never share your API key.


START CUPESS
------------

Run:

python main.py

Then open your Android browser:

http://127.0.0.1:5000

Keep Termux running while CUPESS is being used.


CONFIGURATION
-------------

Example:

OPENROUTER_API_KEY=YOUR_API_KEY

OPENROUTER_MODEL=cohere/north-mini-code:free

OPENROUTER_FALLBACK_MODELS=

HOST=127.0.0.1

PORT=5000

WORKSPACE_DIR=workspace

MAX_DEBUG_RETRIES=3


CHAT MODE
---------

Chat mode is for normal conversations and coding questions.

Example:

Explain Python classes to me.


CODING AGENT MODE
-----------------

Agent mode is designed for coding tasks.

Example:

Create a Python calculator.

CUPESS will:

1. Plan the task
2. Generate the required files
3. Write files into the workspace
4. Review the generated result


PROJECT STRUCTURE
-----------------

CUPESS_AI/
|
|-- main.py
|-- requirements.txt
|-- README.md
|-- .env
|-- .env.example
|
|-- cupess/
|   |-- __init__.py
|   |-- app.py
|   |-- agent.py
|   |-- config.py
|   |-- openrouter.py
|   |-- tools.py
|
|-- ui/
|   |-- index.html
|   |
|   |-- static/
|       |-- style.css
|       |-- script.js
|
|-- workspace/


SECURITY
--------

Never publish your API key.

Do not upload .env to GitHub.

Generated code should always be reviewed before execution.

CUPESS workspace protection prevents files from being written outside
the configured workspace.

Command execution is restricted, but these protections are not a
complete security sandbox.


TROUBLESHOOTING
---------------

If the API key is missing:

Check .env and make sure:

OPENROUTER_API_KEY=YOUR_API_KEY


If CUPESS does not start:

Run:

python main.py

Then check the Termux error.


If the browser cannot connect:

Make sure Termux is still running CUPESS.

Open:

http://127.0.0.1:5000


If the AI request fails:

Check:

1. API key
2. Selected model
3. API usage
4. Internet connection


ROADMAP
-------

Future versions can add:

- Gemini provider
- Groq provider
- DeepSeek provider
- Qwen provider
- Multiple AI models
- Automatic testing
- Automatic debugging
- Code editor
- Terminal panel
- Git integration
- Voice input
- Text-to-speech
- Project memory
- Model voting
- AI competition mode


VERSION
-------

CUPESS AI v1.1

Focus:

Modern mobile UI + OpenRouter integration + coding-agent foundation.
