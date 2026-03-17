# Cloud-Based Active Directory Setup and User Management

## Project Overview
This project demonstrates the automated deployment and management of a simulated enterprise identity infrastructure using Microsoft Azure Entra ID (formerly Azure AD). It bridges programmatic software development with cloud security engineering by utilizing Infrastructure as Code (IaC) and the Microsoft Graph API to replace manual administrative tasks with secure, scalable pipelines.

## Architecture & Technologies
* **Cloud Platform:** Microsoft Azure (Entra ID)
* **Infrastructure as Code (IaC):** Terraform (`azuread` provider)
* **Automation & Scripting:** Python 3
* **APIs & Authentication:** Microsoft Graph API, MSAL (Microsoft Authentication Library), OAuth 2.0 Client Credentials Flow
* **Security Frameworks:** Role-Based Access Control (RBAC), Principle of Least Privilege

## Key Features & Deployments
1. **Infrastructure Provisioning (Terraform):** * Deployed standard organizational security groups.
   * Assigned built-in highly privileged roles (Security Administrator) directly to specific cloud resources.
2. **Identity Automation (Python):** * Registered a secure Enterprise Application within Azure to handle background authentication.
   * Utilized MSAL to request and process bearer tokens securely.
   * Engineered a Python script to interact with the Microsoft Graph API, successfully bulk-provisioning a dataset of simulated employee accounts with temporary credentials.
3. **Security & Access Management:** * Enforced conditional access logic and logical grouping to ensure newly generated identities were automatically bound by organizational security policies.

## Setup & Execution 
*(Note: Client secrets and tenant IDs have been omitted from this public repository for security purposes).*

**1. Terraform Deployment**
```bash
cd terraform-config
terraform init
terraform plan
terraform apply