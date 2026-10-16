# Black Matter Internal IT Support Handbook

## Purpose and Scope

This handbook describes Black Matter's employee IT policies and the approved first-line troubleshooting guidance available to the IT support assistant. It is an internal reference for common workplace technology issues.

The assistant may explain these policies and perform read-only checks through authorized tools. In this project's MVP, any operation that changes system state must receive explicit human approval before execution. The assistant must never claim an operation succeeded until it has checked the resulting system state.

## VPN Access

Employees working outside a Black Matter office must use the company VPN before accessing internal systems. Install the **Black Matter Secure Access** VPN client from the internal **Black Matter Software Hub**.

To connect:

1. Confirm that the device has a working internet connection.
2. Open Black Matter Secure Access.
3. Sign in using the employee's Black Matter account.
4. Complete multi-factor authentication (MFA).
5. Select the recommended corporate gateway, usually the closest available gateway.

If the connection fails, confirm internet connectivity, restart the VPN client, and try another approved corporate gateway. Do not disable endpoint protection, the firewall, or other security controls to make the VPN work.

If the problem persists, contact the IT Service Desk and include the exact error message or a screenshot that does not expose passwords, MFA codes, access tokens, or other secrets.

The support assistant may inspect available VPN or service diagnostics. Restarting a service, changing device/network settings, or modifying security controls is not an automatically authorized action. In this project's MVP, state-changing actions require human approval, and security controls must not be disabled as a workaround.

## Password Reset Policy

Black Matter passwords must be at least 14 characters long. Employees should use the self-service identity portal for ordinary password resets.

After five failed login attempts, an account may be temporarily locked. If self-service recovery fails or the account remains locked, contact the IT Service Desk.

Employees must never share passwords, one-time passcodes, MFA codes, recovery codes, or session tokens with support personnel or the support assistant. The assistant must not ask users to disclose these secrets. Password resets or account-unlock operations may only be performed through an explicitly authorized workflow and must follow its approval requirements.

## Multi-Factor Authentication (MFA)

MFA is mandatory for email, VPN, cloud administration, and other protected Black Matter systems.

Approved methods are:

- The company-approved authenticator app.
- Registered hardware security keys.

SMS may be used only when it is explicitly enabled as a recovery method. Employees should never approve an MFA request they did not initiate. If an employee suspects MFA fatigue, account compromise, or unauthorized sign-in attempts, the issue should be escalated promptly to the IT Service Desk and Security.

The assistant must never request or store MFA codes. It must not bypass MFA or recommend disabling it to restore access.

## Software Installation and Access

Employees should install business software only from the Black Matter Software Hub.

Requests for software not listed in the portal require both manager approval and IT Security review before installation. Administrator access is not granted simply to install unapproved applications.

The assistant may check whether an application is listed in the approved software catalog or help an employee submit a request. It must not install unapproved software, grant administrator privileges, or bypass the approval process. Any installation or access change must use an authorized tool and follow the required human-approval process.

## Lost or Stolen Devices

Immediately report a lost or stolen Black Matter laptop or mobile device to the IT Service Desk and the employee's manager. Provide the device asset tag, if available, and its last known location. Do not include passwords or authentication codes in the report.

IT will coordinate device-lock or wipe procedures with Security according to incident policy. Employees must not attempt to remotely recover the device themselves.

The assistant should treat a lost or stolen device as a security-sensitive incident: gather only the information needed to create an incident report, promptly escalate it, and avoid independently initiating a lock or wipe action. Such actions must be handled through the authorized security workflow and its approval requirements.

## Handling Unresolved Issues

If the approved troubleshooting steps do not resolve an issue, the employee should contact the IT Service Desk or open a ticket. Include a concise problem description, the relevant error message, affected service/device, and troubleshooting steps already attempted.

The assistant must distinguish between a recommendation, an action that was attempted, and an action that was verified successful. If verification fails or the required tool is unavailable, it must clearly state that the issue remains unresolved and provide the ticket/escalation path.
