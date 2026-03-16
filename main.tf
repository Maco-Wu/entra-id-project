# 1. Define the required provider
terraform {
  required_providers {
    azuread = {
      source  = "hashicorp/azuread"
      version = "~> 2.47.0" # Uses a stable version of the provider
    }
  }
}

# 2. Configure the Azure AD Provider
provider "azuread" {
  # We leave this block empty to use the authentication from 'az login'
}

# 3. Create a test Security Group
resource "azuread_group" "cloud_sec_admins" {
  display_name     = "Cloud Security Admins"
  security_enabled = true
  description      = "Security group for Cloud Administration"
}

# 4. Fetch your unique default Azure domain name (e.g., @yourtenant.onmicrosoft.com)
data "azuread_domains" "default" {
  only_initial = true
}

# 5. Create a simulated employee
resource "azuread_user" "test_admin" {
  user_principal_name = "jdoe@${data.azuread_domains.default.domains.0.domain_name}"
  display_name        = "John Doe"
  mail_nickname       = "jdoe"
  password            = "SuperSecretSecurePass123!" 
  account_enabled     = true
}

# 6. Add the simulated employee to your Security Group
resource "azuread_group_member" "admin_membership" {
  group_object_id  = azuread_group.cloud_sec_admins.object_id
  member_object_id = azuread_user.test_admin.object_id
}

# 7 & 8. Activate the built-in role directly by its name
resource "azuread_directory_role" "sec_admin" {
  display_name = "Security Administrator"
}

# 9. Assign the Security Administrator role to John Doe
resource "azuread_directory_role_assignment" "john_admin_rights" {
  role_id             = azuread_directory_role.sec_admin.template_id
  principal_object_id = azuread_user.test_admin.object_id
}