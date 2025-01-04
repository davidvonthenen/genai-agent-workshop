# STEP 3: Creating the Kubernetes AI Agent

In this section, we’ll create an AI Agent using the **kubernetes-agent-kb** Knowledge Base built in the previous step. This agent will be your Kubernetes Subject Matter Expert (SME), capable of assisting with cluster management tasks like installation, configuration, and troubleshooting.

## Prerequisites

Ensure you have:
- A working Knowledge Base named **kubernetes-agent-kb**.
- Access to the GenAI Platform in your DigitalOcean account.

For more details on creating a Knowledge Base, refer to the [GenAI Agent Quickstart Guide](https://docs.digitalocean.com/products/genai-platform/how-to/manage-ai-agent/create-agent/).

## 3.1: Access the AI Agents Section

1. Log in to your DigitalOcean account.
2. Navigate to the GenAI Platform dashboard.
3. Select **AI Agents** from the side menu.

## 3.2: Create a New AI Agent

1. Click **Create AI Agent**.
2. Fill in the following fields:
   - **Agent Name**: `KubernetesAgent`
   - **Description**: "An AI-powered Kubernetes SME for cluster management, troubleshooting, and best practices."
   - **Knowledge Base**: Select `kubernetes-agent-kb` from the dropdown menu.

3. Choose a model for your agent:
   - **Model**: Select the recommended model for your use case (e.g., `gpt-4` or another supported LLM).
   - **Compute**: Choose a GPU-enabled instance to optimize performance.

## 3.3: Configure Agent Settings

1. **System Prompt**:
   - Define a system prompt to guide the agent's behavior. Example:
     ```
     You are a Kubernetes Subject Matter Expert. Provide detailed and accurate guidance for installing, configuring, managing, and troubleshooting Kubernetes clusters.
     ```

2. **Endpoints**:
   - Select whether the agent will have a public or private endpoint based on your use case.
   - Note down the endpoint URL for later integration.

3. **Guardrails**:
   - Enable default guardrails for:
     - Content moderation.
     - Handling sensitive information.
     - Blocking jailbreak attempts.
   - Add custom guardrails if necessary.

## 3.4: Test the AI Agent

1. Navigate to the **Playground** section of your agent.
2. Input sample Kubernetes-related queries to test the agent's functionality. Example queries:
   - "How do I troubleshoot a CrashLoopBackOff error in Kubernetes?"
   - "What are the best practices for configuring Kubernetes ingress?"

3. Evaluate the agent’s responses and refine settings as needed.

## 3.5: Deploy the AI Agent

1. Save your configurations and deploy the agent.
2. Use the provided endpoint URL to integrate the AI Agent into applications or workflows.

→ [Next Up: Function Calling With Your AI Agent](./STEP4_FUNCTION_CALLING.md)
