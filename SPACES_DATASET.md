# Step 1: Creating Your Dataset on DigitalOcean Spaces

This guide will walk you through creating a DigitalOcean Spaces object store to host the dataset for the Kubernetes AI Agent, extracting the dataset contents, and uploading the prepared data.

## 1.1 Create a Spaces Object Store

To begin, you'll need to create a DigitalOcean Spaces object store where the dataset will be stored. Follow these steps:

1. Log in to your DigitalOcean account.
2. Navigate to the [Spaces creation page](https://cloud.digitalocean.com/spaces).
3. Click **Create a Space** and configure the following:
   - Select a datacenter region closest to your target audience.
   - Choose a unique name for your Space (e.g., `kubernetes-agent-dataset`).
   - Leave the default settings for permissions unless you require public access.
4. Once the Space is created, note the endpoint URL for later use.

For more details, refer to the [Spaces Quickstart Guide](https://docs.digitalocean.com/products/spaces/getting-started/quickstart/).

## 1.2 Extract the Dataset Contents

The dataset for the Kubernetes AI Agent is available in the GitHub repository. Extract the contents of the dataset archive as follows:

1. If you haven't done this already, clone the workshop repository:

   ```bash
   git clone https://github.com/do-community/genai-launch-agent-workshop.git
   ```

2. Navigate to the dataset folder:

   ```bash
   cd genai-launch-agent-workshop/kubernetes-walkthrough
   ```

3. Extract the contents of the ZIP file:

   ```bash
   unzip kubernetes-agent.zip -d kubernetes-agent-dataset
   ```

### Note on Dataset Creation

The dataset was prepared by combining files from the following repositories:

- [Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- [Kubernetes Website](https://github.com/kubernetes/website)
- 2 Popular eBooks Found on the Public Internet

From these repositories, only the markdown (`.md`) files were retained. Below is an example of how this process was carried out:

```bash
# Clone the required repositories
git clone https://github.com/kelseyhightower/kubernetes-the-hard-way.git
git clone https://github.com/kubernetes/website.git

# Retain only markdown files and delete other contents
cd kubernetes-agent
find ./hardway -type f ! -name "*.md" -delete
find ./website -type f ! -name "*.md" -delete

# Delete empty folders
find ./hardway -type d -empty -delete
find ./website -type d -empty -delete
```

## 1.3 Upload the Dataset to the Spaces Object Store

TODO

## 1.4 (Optional) Upload the Dataset Using `s3cmd`

Once the dataset is prepared, upload it to your Spaces object store. Use the following steps:

1. Install and configure the `s3cmd` tool to interact with DigitalOcean Spaces:

   ```bash
   sudo apt-get install s3cmd
   s3cmd --configure
   ```

2. Upload the dataset folder:

   ```bash
   s3cmd sync kubernetes-agent-dataset/ s3://kubernetes-agent-dataset
   ```

3. Verify the dataset upload by checking the contents of your Space:

   ```bash
   s3cmd ls s3://kubernetes-agent-dataset
   ```

Your dataset is now ready to be accessed by the Kubernetes AI Agent!

→ [Next Up: Creating Your Dataset on DigitalOcean Spaces](./KNOWLEDGE_BASE.md) 
