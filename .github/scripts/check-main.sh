#!/usr/bin/env bash
set -euo pipefail

if [[ ${GITHUB_REF:?} != refs/heads/main ]]; then
    printf 'Deployment requires the main branch.\n' >&2
    exit 1
fi

current_sha=$(gh api "repos/${GITHUB_REPOSITORY:?}/git/ref/heads/main" --jq .object.sha)
if [[ ${GITHUB_SHA:?} != "$current_sha" ]]; then
    printf 'Main now points to %s. This build is for %s.\n' "$current_sha" "$GITHUB_SHA" >&2
    exit 1
fi
