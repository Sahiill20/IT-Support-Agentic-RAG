# Black Matter IT Service Desk Runbook

## Purpose

This runbook provides first-line triage and escalation guidance for common Black Matter IT support requests. It is intended for service-desk staff and the IT support assistant.

The assistant should use these procedures to decide what evidence to gather, which approved capability may be relevant, when human approval is required, and when to escalate. A troubleshooting suggestion in this runbook does not itself grant permission to change system state.

## General Triage Procedure

For each report:

1. Clarify the affected user, device, application, or service when that information is needed.
2. Determine whether the issue affects one user, a team, or the wider company.
3. Check available network and service-status information before recommending device-level changes.
4. Review relevant internal knowledge and existing ticket information.
5. Choose the least disruptive applicable troubleshooting step.
6. In the project's MVP, obtain explicit human approval before any action that changes system state.
7. Verify the result using an authoritative status check after an action.
8. If the issue remains unresolved, attempts are exhausted, or the needed capability is unavailable, create or update a ticket and escalate with a clear summary of findings.

Do not claim an issue is resolved based only on an action tool's success message. Check the resulting service/device state or ask the user to confirm the user-visible symptom has cleared.

## Email Troubleshooting

If an employee cannot send or receive email:

1. Determine whether the issue affects one employee or multiple employees.
2. Check network connectivity and the Black Matter service-status dashboard.
3. For a single employee, ask them to sign out and back in, verify mailbox quota, and test the approved web client.
4. If multiple employees are affected or the service dashboard indicates an incident, treat it as a suspected service incident and escalate it.

Do not ask every affected employee to reinstall email software during a widespread incident. The assistant may read service-status information and collect diagnostics when authorized. Signing users out, changing account settings, or modifying mail configuration requires an approved workflow and the applicable human approval.

## VPN Connectivity

For a VPN connection problem:

1. Confirm whether the employee can access ordinary internet sites.
2. Check the Black Matter Secure Access service status, if the status tool is available.
3. Confirm whether the issue affects one employee or multiple employees.
4. Recommend restarting the VPN client and trying another approved corporate gateway, consistent with the Internal IT Support Handbook.
5. Do not recommend disabling the firewall, endpoint protection, MFA, or other security controls.
6. If the problem persists, gather the error message and relevant non-sensitive diagnostics, then open or update an IT ticket.

If a diagnostic or service-control tool is available, the agent may use read-only checks first. A restart or other state-changing operation requires human approval in the MVP. Verify the service status after an approved operation; if verification is unsuccessful, report the issue as unresolved and escalate.

## Laptop Performance

For a slow laptop, begin with non-disruptive checks:

- CPU and memory utilization.
- Available storage space.
- Startup applications.
- Operating system update status.
- Endpoint security scan status.
- Relevant device health or hardware diagnostic results, if available.

Do not disable endpoint security agents as a troubleshooting shortcut. Escalate if hardware diagnostics report failure or repeated shutdowns continue after appropriate software remediation.

Read-only diagnostics may be performed through available authorized tools. Closing applications, restarting a device, installing software, changing configuration, or taking other actions that change state requires the applicable approval. After an approved remediation, recheck the relevant health indicators before reporting success.

## Software Requests

Verify whether the requested application is listed in the Black Matter Software Hub. If it is not listed, direct the employee to submit a request for manager approval and IT Security review.

Do not bypass those reviews, install unapproved software, or grant administrator privileges merely to complete a request. Record the request and its approval status in the ticketing process.

## Lost or Stolen Device

Treat a reported lost or stolen device as a security-sensitive incident. Promptly escalate it to the IT Service Desk, the employee's manager, and Security through the approved incident process. Capture the asset tag and last known location if available.

Do not attempt to locate or remotely recover the device using unauthorized methods. Device lock or wipe operations must be initiated by the authorized IT/Security workflow, with required approval and audit records.

## Ticket Priority

- **P1 — Critical:** Company-wide outage or critical security incident.
- **P2 — High:** A major team is blocked and no reasonable workaround is available.
- **P3 — Normal:** An individual employee is blocked or service is degraded, with a limited workaround.
- **P4 — Low:** Standard service request, information request, or low-impact issue.

Use the impact and urgency actually established from the report and available diagnostics. Do not assign a higher priority solely because a user requests it. For suspected security incidents or widespread outages, follow the applicable escalation path promptly.

## Escalation and Ticket Quality

If the issue cannot be resolved safely, the necessary action is not available, evidence is insufficient, or the verification check fails:

1. Stop automatic attempts once the configured retry limit is reached.
2. Create or update an IT ticket using the authorized ticketing capability.
3. Include the employee's problem description, affected service/device, relevant error details, evidence gathered, actions attempted, approval outcomes, and verification results.
4. Clearly mark the issue as unresolved and specify what the Service Desk should investigate next.
5. Tell the employee that the request has been escalated and provide the ticket reference when one is available.

Do not fabricate ticket IDs, claim an action was performed when it was not, or report a successful resolution without verification.
