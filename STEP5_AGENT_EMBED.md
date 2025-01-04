# Step 5: Embed Your AI Agent In A Web Page

Once your Kubernetes AI Agent is deployed, embedding it into an existing webpage is straightforward. DigitalOcean's GenAI platform provides a pre-generated script that introduces a chat-style interface, allowing seamless interaction with your agent.

## 5.1 Embedding the Chatbot

Follow these steps to embed the chatbot into your webpage:

1. **Locate the Embed Code:**

   - After creating and deploying your AI Agent, navigate to the **Agent Dashboard**.
   - Look for the **Chatbot Integration** section, where you will find a pre-generated embed code.

2. **Insert the Embed Code into Your HTML:**

   - Copy the provided script and paste it into your webpage's HTML, typically before the closing `<body>` tag.
   - Here’s a sample script for reference:

   ```html
   <script async
     src="https://agent-8ab8ecee3cab483ce778-r637w.ondigitalocean.app/static/chatbot/widget.js"
     data-agent-id="b1953dd2-b3dc-11ef-bf8f-4e013e2ddde4"
     data-chatbot-id="5VkEXRJQSchUUMa9rdR-SyUdtyCWGl9V"
     data-name="dvonthenen-agent-kubernetes Chatbot"
     data-primary-color="#031B4E"
     data-secondary-color="#E5E8ED"
     data-button-background-color="#0061EB"
     data-starting-message="Hello! How can I help you today?"
     data-logo="/static/chatbot/icons/default-agent.svg">
   </script>
   ```

3. **(Optional) Customize the Embed Code**

    - Update the following attributes to tailor the chatbot to your preferences:

        - `data-name`: The display name of your chatbot.
        - `data-primary-color`, `data-secondary-color`, and `data-button-background-color`: Adjust the colors to match your website’s branding.
        - `data-starting-message`: Set a custom greeting message for users.
        - `data-logo`: Specify the URL of your custom logo (if any).

4. Save Your Webpage:

    - Save the changes to your HTML file.
    - Ensure the file is hosted on a web server for the chatbot to function correctly.

After embedding the chatbot, open your webpage in a browser to verify the integration. The chatbot should appear as an interactive widget, ready to assist with Kubernetes-related queries.

→ [Next Up: Call Your AI Agent Using An API Call](./STEP6_AGENT_API.md)
