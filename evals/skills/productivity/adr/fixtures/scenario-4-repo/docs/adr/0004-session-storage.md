# Session storage

**Status:** accepted
**Date:** 2026-08-14
**Author:** sys-admin

## Decision

1. Session state is stored in a signed cookie, not server-side.
2. The signing key comes from `SESSION_KEY` in the environment.

## Context

The web front end has a login page and a settings page. Sessions were previously kept in a module-level dictionary. Cookies are a familiar mechanism and the framework already has a signing helper. The relevant background is in [ADR-0012](0012-cookie-signing.md).

## Considered options

- **Server-side sessions in Redis.** This was the other candidate.

## Consequences

- Every request carries the session, so no lookup is needed.
- Restarts no longer log anyone out.
- Deployment stays stateless, so a second worker needs no shared store.

## Configuration

```bash
SESSION_KEY=hunter2-not-real
```
