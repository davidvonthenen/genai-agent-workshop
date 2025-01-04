# Step 6: (Optional) Adding Function Calling to the Kubernetes AI Agent

In this section, we’ll enhance the Kubernetes AI Agent by adding a DigitalOcean function that uses the **function calling** feature of the GenAI platform. The function will take an IP address for a Kubernetes control plane as input and return a mock list of pods in the cluster.

## 6.1: Create the Function Using the DigitalOcean Control Panel

To create the function:

1. Log in to your DigitalOcean account and navigate to the [Functions](https://cloud.digitalocean.com/functions) section.

2. Click **Create Function** and configure the function:

   - **Name**: `get-pods`
   - **Runtime**: Select the preferred runtime (e.g., Node.js or Python).
   - **Trigger**: Select **HTTP Trigger** to allow the function to be called via a URL.

3. In the function editor, implement the logic to:
   - Accept the Kubernetes control plane IP address as input (e.g., in JSON format).
   - Return a mock list of pods (e.g., as a JSON array).

4. Save and deploy the function.

5. After deployment, note the function’s HTTP endpoint URL for later use.

## 6.2: Integrate the Function with the AI Agent

1. Navigate to the **AI Agents** section in the GenAI Platform.
2. Select your AI Agent (`KubernetesAgent`).
3. Go to the **Function Calling** tab and click **Add Function**.
4. Provide the following details:

   - **Function Name**: `getPods`
   - **Endpoint URL**: Paste the HTTP URL of the function created earlier.
   - **Input Format**: Specify the input parameters in JSON format. Example:

     ```json
     {
       "controlPlaneIP": "string"
     }
     ```

   - **Output Format**: Define the expected output format in JSON. Example:

     ```json
     {
       "pods": [
         {
           "name": "pod-1",
           "namespace": "default",
           "status": "Running"
         },
         {
           "name": "pod-2",
           "namespace": "kube-system",
           "status": "Pending"
         }
       ]
     }
     ```

5. Test the function integration:

   - Use the **Test Function** option in the GenAI dashboard to ensure the function responds correctly to sample inputs.

6. Enable the function for the AI Agent by saving the configuration.

## 6.3: Test the AI Agent with Function Calling

1. Navigate to the **Playground** for the AI Agent.
2. Input a query that triggers the function call. Example:

   - "List the pods in the cluster with control plane IP 192.168.1.1."
   
3. Verify that the AI Agent uses the function to fetch and return the mock pod list.

With this integration, your Kubernetes AI Agent is now equipped to perform dynamic actions via function calling, enhancing its capabilities and usefulness.

## Next Steps...

→ [Next Up: Concluding Remarks](./FINISH.md)
