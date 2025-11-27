# Jira/Confluence + Keycloak Connect via OIDC

Tested on Jira Server 8.10.0, Confluence 7.6.0, Keycloak 26.3.
The integration setup used the [SAML Single Sign On for Jira](https://wiki.resolution.de/doc/saml-sso/latest/jira/saml-plugin-overview) plugin by [re:solution](https://www.resolution.de/) version 6.15.2.

## References

- https://marketplace.atlassian.com/apps/1212130/saml-sso-single-sign-on-for-jira-sso-oauth-user-sync?hosting=server
- https://wiki.resolution.de/doc/saml-sso/latest/jira/setup-guides-for-saml-sso/keycloak/keycloak-with-just-in-time-provisioning?

## Jira Setup

- Install plugin `Administration > Manage Apps > Upload app`
- Setup the plugin `Administration > SAML Single Sign On`
**Identity Providers**
  - Name: `keycloak`
  - Display a button on Jira's Dashboard login gadget and login page: `On`
  **SAML IdP Metadata Settings**
  - Metadata URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml/descriptor`
  **Basic IdP Settings**
  - IdP Entity ID / Issuer: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>`
  - Login Binding: `POST`
  - IdP POST Binding URL: `https://<KEYCLOAK_HOSTNAME>/realms/<KEYCLOAK_REALM>/protocol/saml`
  **Security Settings**
  - Certificate: `Keycloak > Realm settings > SAML 2.0 Identity Provider Metadata > <ds:X509Certificate>`
  **Additional authentication (WebSudo)**
  *Request for password when accessing Administration settings will also use Keycloak*
  - Enable additional authentication: `On`
  - Hide password field for additional authentication: `On`
  - Request new authentication from IdP for additional authentication: `On`
  **User Creation and Update**
  - User Update Method: `Update from SAML-Attributes (Just-in-Time Provisioning)`
  - Reactivate inactive users during login: `Off`
  **Attribute Mapping**
  - Find user by this Jira attribute: `E-Mail Address` (this will allow implementing an error when a user is trying to access Jira without belonging to the required group, for example, jira-users)
  - Attribute as received from Keycloak:
    - ATTR_NAMEID - Username (Regex And Replacement)
    - ATTR_FULLNAME - Full Name
    - ATTR_EMAIL - E-Mail Address
    - ATTR_GROUPS - Gorups
  **User Creation and Update from SAML Attributes**
  - Create New Users: `On`
  - Update users not created by this app: `On`
  **Group Settings**
  - Always add users to these groups: `None` (this will allow implementing an error when a user is trying to access Jira without belonging to the required group, for example, jira-users)
  - Create groups if they do not exist: `Off`
  - Remove from Groups: `On` **(The setting will only apply to users created by this app, never to the group memberships of *existing users* and *administrators*)**
**Redirection**
  - Enable SSO Redirect: `Off`
  - Enable nosso: `On`

## Confluence Setup

For Confluence, I applied only one setting `Administration > Security Configuration > Secure administrator sessions: disable`. Specifically, I disabled the repeated password prompt when accessing the Administration settings. In the case of Confluence, Additional authentication (WebSudo) refuses to work.

## Keycloak Setup

Don't forget to map Keycloak groups and Client Scopes to corresponding Client Roles

### Jira Client

- Client ID: `https://<JIRA_HOSTNAME>/plugins/servlet/samlsso`
- Valid redirect URIs: `https://<JIRA_HOSTNAME>/plugins/servlet/samlsso`
- Master SAML Processing URL: `https://<JIRA_HOSTNAME>/plugins/servlet/samlsso`
- Name ID format: `username`
- Force name ID format: `On`
- Force POST binding: `On`
- Sign documents: `On`
- Sign assertions: `On`
- Signature algorithm: `RSA_SHA256`
- SAML signature key name: `KEY_ID`
- Canonicalalization method: `Exclusive`
- Client Roles:
  - `jira-access`

### Confluence Client

- Client ID: `https://<CONFLUENCE_HOSTNAME>/plugins/servlet/samlsso`
- Valid redirect URIs: `https://<CONFLUENCE_HOSTNAME>/plugins/servlet/samlsso`
- Master SAML Processing URL: `https://<CONFLUENCE_HOSTNAME>/plugins/servlet/samlsso`
- Name ID format: `username`
- Force name ID format: `On`
- Force POST binding: `On`
- Sign documents: `On`
- Sign assertions: `On`
- Signature algorithm: `RSA_SHA256`
- SAML signature key name: `KEY_ID`
- Canonicalalization method: `Exclusive`
- Client Roles:
  - `confluence-access`

### Client Scope Mappers

- **Jira**
  - `aud`: Audience
  - `email` (`ATTR_EMAIL`): User Property
  - `groups` (`ATTR_GROUPS`): Group list
  - `fullname` (`ATTR_FULLNAME`): User Property (firstName)
  - Scope: `jira-access`

- **Confluence**
  - `aud`: Audience
  - `email` (`ATTR_EMAIL`): User Property
  - `groups` (`ATTR_GROUPS`): Group list
  - `fullname` (`ATTR_FULLNAME`): User Property (firstName)
  - Scope: `confluence-access`
