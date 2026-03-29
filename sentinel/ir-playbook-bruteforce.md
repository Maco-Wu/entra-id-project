# Incident Response Playbook — Brute Force Sign-in

## Trigger
Sentinel Analytics Rule: "Brute Force Sign-in Attempt"
5+ failed sign-ins from same IP within 10 minutes.

## Severity: High

## Step 1 — Triage (first 5 minutes)
- Identify the targeted account from the incident entity
- Check if any sign-in ultimately succeeded (ResultType == 0)
- Check the source IP — is it a known corporate IP or external?

## Step 2 — Contain
- Disable the targeted user account in Entra ID
- Block the source IP via Conditional Access Named Locations

## Step 3 — Investigate
- Review full sign-in log for that account over last 24 hours
- Check audit logs for any changes if attacker got in
- Check if same IP targeted other accounts

## Step 4 — Recover
- Reset the user password
- Force MFA re-registration
- Re-enable account once password is reset

## Step 5 — Document
- Record timeline, affected accounts, source IPs
- Note whether Conditional Access Policies blocked or missed this
- Update policies if gaps identified
