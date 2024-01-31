# MLOps Deployment on Azure Container Apps

_Maximize the potential of instantaneous scaling for real-time inference_

## Generate a Personal Access Token (PAT)

To be added as an Action secret, create an [access token](https://github.com/settings/tokens/new?description=Azure+Container+Apps+access&scopes=write:packages) with sufficient permissions for writing to packages.

## Create an Azure Service Principal

You'll need:

1. An Azure subscription ID [locate it here](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade) or follow [this guide](https://docs.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id).
2. A Service Principal with AppID, password, and tenant information. Create one with: `az ad sp create-for-rbac -n "REST API Service Principal"` and assign the IAM role for the subscription. Alternatively, set the proper role access using the command below (replace with your subscription id):

```bash
az ad sp create-for-rbac --name "CICD" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID --sdk-auth
```

## Azure Container Apps

Ensure you have one instance created, noting the name and resource group for use in the workflow file.

## Modify Defaults

Make sure to use 2 CPU cores and 4GB of memory per container, as loading HuggingFace with FastAPI requires significant upfront memory.

## Potential Issues

Here are potential pitfalls leading to deployment failures:

- Inadequate RAM per container.
- Lack of authentication for accessing the remote registry (ghcr.io). Authentication is mandatory.
- Incorrect or insufficient permissions for the PAT (Personal Access Token).
- Using a port other than 80 in the container. Azure Container Apps defaults to port 80. Adjust to match the container.

If encountering issues, check logs in the portal or use the Azure CLI command:

```bash
az containerapp logs show --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP_NAME --follow
```

Ensure to update both variables to match your environment.

## API Best Practices

While there are specific best practices for the FastAPI framework, many general HTTP API best practices are widely applicable. 

### Utilize HTTP Error Codes

Leverage the HTTP specification's error codes to convey specific conditions effectively. For instance, use `401 Unauthorized` when access lacks proper authorization and `404 Not Found` when a resource doesn't exist.

### Accept Request Types Sparingly

Each HTTP method has a distinct purpose:

- `GET`: Read-only operations
- `POST`: Write-only operations
- `PUT`: Update existing resources
- `HEAD`: Check if a resource exists

Adhering to these best practices ensures a robust and maintainable HTTP API.
