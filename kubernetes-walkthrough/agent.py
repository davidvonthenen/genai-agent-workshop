# Install pyjwt openai httpx libraries.
import httpx
from openai import OpenAI
import jwt

# Make sure to set these values as environment variables.
API_BASE = "https://cloud.digitalocean.com/gen-ai"  # production environment
agent_id = "XXXXXX"  # replace with `data-agent-id` from the chatbot code snippet
agent_key = "XXXXXX"  # replace with `data-chatbot-id` from the chatbot code snippet
agent_endpoint = "XXXXXX + "/api/v1/"  # replace with your agent's endpoint URL and make sure to keep the "/api/v1" suffix.


def get_refresh_token(agent_key: str) -> str:
    response = httpx.post(
        f"{API_BASE}/auth/agents/{agent_id}/token",
        headers={
            "Content-Type": "application/json",
            "X-Api-Key": agent_key,
        },
        json={},
    )
    if not response.is_success:
        raise Exception("Failed to issue refresh token")

    data = response.json()
    return data["refresh_token"]


def get_access_token(refresh_token: str) -> str:
    response = httpx.put(
        f"{API_BASE}/auth/agents/{agent_id}/token?refresh_token={refresh_token}",
        headers={
            "Content-Type": "application/json",
            "X-Api-Key": agent_key,
        },
        json={},
    )
    if not response.is_success:
        raise Exception("Failed to refresh access token")

    data = response.json()
    access_token = data["access_token"]
    return access_token

def is_expired(access_token: str) -> bool:
    try:
        jwt.decode(
            access_token,
            options={
                "verify_signature": False,
                "verify_exp": True,
            },
        )
    except jwt.exceptions.ExpiredSignatureError:
        return True
    except Exception as e:
        raise e

    return False

if __name__ == "__main__":
    refresh_token = ""
    access_token = ""

    # Refresh tokens expire every few days, so you need to refresh them for long running processes.
    if not refresh_token or is_expired(refresh_token):
        refresh_token = get_refresh_token(agent_key)
        print(f"Refreshed refresh token!")

    # Access tokens expire every few minutes, so you need to refresh them for long running processes.
    if not access_token or is_expired(access_token):
        access_token = get_access_token(refresh_token)
        print(f"Refreshed access token!")

    client = OpenAI(
        base_url=agent_endpoint,
        api_key=access_token,
    )

    response = client.chat.completions.create(
        model="n/a",
        messages=[{"role": "user", "content": "I am attempting to debug a pod that isn't starting in a Kubernetes cluster. What can I do to debug this?"}],
        stream=True,
    )

    for message in response:
        print(message.choices[0].delta.content, end="")
