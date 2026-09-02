#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.resources/main"
exec bash menu.sh
