# Session storage

**Status:** accepted
**Date:** 2026-08-14
**Author:** sys-admin

## Context

The web front end has a login page and a settings page. Sessions were previously kept in a module-level dictionary. Cookies are a familiar mechanism and the framework already has a signing helper.

## Decision

1. Session state is stored in a signed cookie, not server-side.
2. The signing key comes from `SESSION_KEY` in the environment.

## Considered options

- **Server-side sessions in Redis.** This was the other candidate.

## Consequences

- Every request carries the session, so no lookup is needed.
- Restarts no longer log anyone out.
- Deployment stays stateless, so a second worker needs no shared store.
