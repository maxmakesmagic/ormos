# Ormos

Ormos is an archive of Magic: The Gathering articles and events. The builder reads the Markdown in `content/` and writes a static website.

## Build locally

Install uv, Node.js, and npm. The builder uses Pagefind to create the search index.

Run these commands from the checkout.

```sh
npm ci --ignore-scripts
uv run --locked ormos-build --output ../ormos-site
uv run --locked python -m http.server 8000 --directory ../ormos-site
```

Open http://localhost:8000/. Choose a new output directory for each build.

The builder reads redirects, Wizards URL mappings, the search shard list, and video transcripts from `data/`. The checkout contains these files.

Flash uses the pinned Ruffle package installed by `npm ci`. The Flash catalog in `data/flash.json` records the SHA-256 hashes for movies on `media.ormos.uk` and puzzle images on `i.ormos.uk`.
To place a Flash player in an article, add `![Animation name](/flash/<catalog-id>)` as a separate paragraph.
Add a `poster_url` to the catalog entry if readers open the embedded player from a preview image.

The search plan records the order of pages within each shard. Keep that order when you edit `data/search-plan.json` because Pagefind uses it to assign page numbers.
When you add a canonical page, append its path to a shard or add a shard for it.

`data/media-urls.jsonl` records public destinations for historical image and media URLs. Each line contains `original_url`, `target_url`, and `kind`. An original URL can have several entries when the archive holds different versions.

The builder uses the media map to repair historical links and prefers Ormos copies to verified Wizards or Wayback destinations. When you add a working destination, remove its original URL from `data/missing-media.jsonl`.

## Plan an upload

Compare a completed build with the inventory from the last verified deployment.

```sh
uv run --locked ormos-upload-plan --site ../ormos-site --baseline deployed.ndjson --output ../ormos-upload-plan
```

If the deployment received later updates, pass each verified inventory with `--overlay` in deployment order.

The plan writes new and changed files to `upload.ndjson`. It lists keys absent from the build in `removed.ndjson`.
If the deployment matches `inventory.ndjson`, use that file as the next baseline.

## GitHub deployment

Pushes to `main` build and deploy the site in the `production` environment. The deploy uploads new and changed files first. It then deletes files in the deployment inventory that the new build omits.

Pull requests build the site and produce a dry upload plan. Pull requests from forks and Dependabot build without R2 credentials. A follow-up workflow on `main` compares their build inventory using read-only credentials. It saves the upload list and logs the removal count.

1. Create a private R2 bucket for deployment state. Upload `deployment.zip` to its root. The ZIP must contain `inventory.ndjson` from the last verified deployment.
2. Set the repository variables `ORMOS_R2_ACCOUNT_ID` and `ORMOS_R2_STATE_BUCKET`. Set `ORMOS_R2_SITE_BUCKET` if the site bucket name differs from `ormos-site`.
3. Create an R2 Object Read token for the state bucket only. Store the key pair as the repository secrets `R2_STATE_READ_ACCESS_KEY_ID` and `R2_STATE_READ_SECRET_ACCESS_KEY`.
4. Create the `production` environment. Restrict its deployment branches to `main`. Create an R2 Object Read & Write token for the site and state buckets. Store the key pair as the environment secrets `R2_DEPLOY_ACCESS_KEY_ID` and `R2_DEPLOY_SECRET_ACCESS_KEY`.

To batch metadata checks before and after uploads, add the optional `R2_LIST_API_TOKEN` secret to `production`. Use a Cloudflare R2 Admin Read only bearer token. This token grants read access across the account's R2 buckets. The deploy uses batching for plans with at least 10,000 uploads. It uses S3 HEAD when the token is absent or the list cannot verify an object. Keep the bucket-scoped S3 key pair for deploy writes.

To pack a verified inventory for the first deployment, run this command from the checkout.

```sh
uv run --locked python -m zipfile -c ../ormos-upload-plan/deployment.zip ../ormos-upload-plan/inventory.ndjson
```

The deploy command runs up to 32 R2 requests at a time. Use `--workers` to set the concurrency when you run it locally.

If a deployment stops partway through, dry runs use the last completed inventory. The next production run checks pending uploads and deletions before it plans new changes. If you update site objects directly in R2, do it between deployments. Refresh the deployment inventory before the next run.

The default Ubuntu runner clears unused toolchains before checkout. If it lacks enough free disk, set `ORMOS_RUNNER` to a GitHub-hosted Linux runner label with at least 40 GiB free. Fork and Dependabot builds use `ubuntu-24.04`.
