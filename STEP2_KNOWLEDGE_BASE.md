# Step 2: Building a Knowledge Base for the Kubernetes AI Agent

In this section, we’ll create a Knowledge Base (KB) using DigitalOcean's GenAI Platform, leveraging the dataset stored in your DigitalOcean Spaces object store, named `kubernetes-agent-dataset`, from the previous step.

## Prerequisites

Ensure you have:

- The dataset uploaded to a Spaces object store (e.g., `kubernetes-agent-dataset`).
- The endpoint URL and credentials for your Space.

For more details on creating a Knowledge Base, refer to the [Knowledge Base Quickstart Guide](https://docs.digitalocean.com/products/genai-platform/how-to/manage-kb/create/).

## 2.1: Access the GenAI Platform

1. Log in to your DigitalOcean account.
2. Navigate to the GenAI Platform dashboard.
3. Select **Knowledge Base** from the side menu.

## 2.2: Create a New Knowledge Base

1. Click **Create Knowledge Base**.
2. Enter a name for your Knowledge Base (e.g., `kubernetes-agent-kb`).
3. Specify the source as **Spaces Object Store** and provide the following details:
   - Space name: `kubernetes-agent-dataset`
   - Space endpoint URL: (e.g., `https://nyc3.digitaloceanspaces.com/kubernetes-agent-dataset`)
   - Credentials: Use your DigitalOcean Spaces API keys.

4. Configure the ingestion options:
   - File formats: Ensure `.md` is enabled.
   - Indexing mode: Select **Initial Dataset Index** to process the full dataset.

5. Click **Save** to create the Knowledge Base.

## 2.3: Monitor the Indexing Process

1. Once created, the Knowledge Base will begin indexing the dataset files.
2. Navigate to the **Knowledge Base Overview** page to monitor progress.
3. Verify that all files have been indexed successfully. Any errors will be displayed in the logs.

## 2.4: (Optional) Test the Knowledge Base

1. Navigate to the **Test Your Knowledge Base** section.
2. Enter sample queries related to Kubernetes to test the retrieval accuracy of your KB.
3. Refine indexing or dataset contents as needed based on the test results.

Congratulations! Your Knowledge Base is now live and ready to empower your Kubernetes AI Agent.

→ [Next Up: Creating Your AI Agent](./STEP3_GENAI_AGENT.md)
