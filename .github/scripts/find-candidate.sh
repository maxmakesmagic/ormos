#!/usr/bin/env bash
set -euo pipefail

artifact_name=candidate-inventory-${SOURCE_RUN_ATTEMPT:?}
artifact_id=$(gh api --method GET \
    "repos/${GITHUB_REPOSITORY:?}/actions/runs/${SOURCE_RUN_ID:?}/artifacts" \
    -f "name=$artifact_name" \
    --jq '.artifacts[] | select(.expired == false) | .id')

if [[ -n $artifact_id && ! $artifact_id =~ ^[0-9]+$ ]]; then
    printf 'Expected one candidate inventory artifact.\n' >&2
    exit 1
fi

printf 'artifact_id=%s\n' "$artifact_id" >> "${GITHUB_OUTPUT:?}"
