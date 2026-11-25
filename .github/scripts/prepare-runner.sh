#!/usr/bin/env bash
set -euo pipefail

workspace=${GITHUB_WORKSPACE:?}
build_dir=${RUNNER_TEMP:?}
gib=$((1024 ** 3))
workspace_gib=40
build_gib=0

if [[ $(stat -c '%d' -- "$workspace") != $(stat -c '%d' -- "$build_dir") ]]; then
    workspace_gib=17
    build_gib=23
fi

available_bytes() {
    df --block-size=1 --output=avail -- "$1" | tail -n 1
}

has_space() {
    (( $(available_bytes "$workspace") >= workspace_gib * gib )) &&
    (( $(available_bytes "$build_dir") >= build_gib * gib ))
}

if ! has_space && [[ ${GITHUB_ACTIONS:-} == true && ${RUNNER_ENVIRONMENT:-} == github-hosted ]]; then
    # These toolsets are preinstalled on the hosted runner and unused by Ormos.
    sudo rm -rf -- /usr/local/lib/android /usr/share/dotnet /opt/ghc \
        /usr/local/.ghcup /opt/hostedtoolcache/CodeQL /usr/share/swift
    sudo docker image prune --all --force
fi

if ! has_space; then
    printf 'The runner needs %s GiB free at %s and %s GiB free at %s.\n' \
        "$workspace_gib" "$workspace" "$build_gib" "$build_dir" >&2
    df -h -- "$workspace" "$build_dir" >&2
    exit 1
fi
