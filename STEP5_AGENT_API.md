# Step 5: Calling Your Kubernetes AI Agent Using an API

In this final exercise, you will learn how to interact with your AI Agent via an API call. This enables you to programmatically send queries to your AI Agent and retrieve responses. A pre-configured Python script (`agent.py`) is provided in the GitHub repository to simplify this process.

## Prerequisites

Before proceeding, ensure you have:

- Python 3.7 or later installed.
- (Optional, but highly recommended) A virtual environment like [conda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) or [venv](https://docs.python.org/3/library/venv.html).
- The `agent.py` script, available in the repository under `./kubernetes-walkthrough/agent.py`.
- Installed the required Python libraries: `pyjwt`, `openai`, and `httpx`.

  ```bash
  pip install pyjwt openai httpx
  ```

- Your AI Agent's credentials:

  - Agent ID: Found in your chatbot embed code under `data-agent-id`.
  - Agent Key: Found in your chatbot embed code under `data-chatbot-id`.
  - Agent Endpoint URL: Found in your chatbot embed code (src value in the embed script).

## 5.1: Update agent.py

1. Open the `agent.py` file in a text editor.
2. Replace the placeholders with your agent’s details:

  - `agent_id`: Replace XXXXXX with your Agent ID.
  - `agent_key`: Replace XXXXXX with your Agent Key.
  - `agent_endpoint`: Replace XXXXXX with your Agent Endpoint URL. Ensure it ends with /api/v1/.

## 5.2: Test the Script

1. Run the script:

  ```bash
  python ./kubernetes-walkthrough/agent.py
  ```

2. The script will:

  - Generate or refresh tokens as needed.
  - Send a query to your AI Agent. The default query is:

    ```
    I am attempting to debug a pod that isn't starting in a Kubernetes cluster. What can I do to debug this?
    ```

3. The agent's response will be printed to the terminal.

### How the Script Works

Key Functions

- Token Management:

  - `get_refresh_token(agent_key)`: Generates a refresh token.
  - `get_access_token(refresh_token)`: Generates an access token.
  - `is_expired(token)`: Checks if a token has expired.

- API Call:

  - The script uses the OpenAI client to make chat completions requests to the agent.

## 5.3: Customize the Script

1. Modify the messages parameter in the script to include your desired query:

  ```python
  messages=[{"role": "user", "content": "Your custom query here"}]
  ```

2. Adjust the response handling as needed.

## Next Steps...

Here is an optional module:

→ [Next Up: Function Calling With Your AI Agent](./STEP6_FUNCTION_CALLING.md)

Or let's wrap up here...

→ [Next Up: Concluding Remarks](./FINISH.md)
