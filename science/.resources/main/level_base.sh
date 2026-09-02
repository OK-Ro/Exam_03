#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; level="$1"; dir="$BASE/../rank03/level$level"
subjects=(); while IFS= read -r item; do subjects+=("$item"); done < <(find "$dir" -mindepth 1 -maxdepth 1 -type d -printf '%f\n')
for ((i=${#subjects[@]}-1;i>0;i--)); do j=$((RANDOM%(i+1))); t="${subjects[$i]}"; subjects[$i]="${subjects[$j]}"; subjects[$j]="$t"; done
bash "$BASE/session.sh" "LEVEL $level MODE" "$dir" "${subjects[@]}" || true
exec bash "$BASE/rank03_menu.sh"
