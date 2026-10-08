#!/bin/sh
# Regenerates the client from the OpenAPI document of the Go API (make openapi, no running server needed).
set -e
cd "$(dirname "$0")"
node ../scripts/sync.mjs
uvx --from openapi-python-client==0.29.1 openapi-python-client generate \
	--path ../openapi.json --meta none --output-path src/sdk221/generated --overwrite
