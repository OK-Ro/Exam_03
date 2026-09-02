#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; source "$BASE/colors.sh"; source "$BASE/ui.sh"; export EXAM_STARTED_AT="$(date +%s)"
ui_title; printf "${CYAN}${BOLD}REAL EXAM MODE${RESET}\n\n${GREEN}Six levels. Six random subjects.${RESET}\n"; read -r -p 'Press Enter to start... ' _
for level in 1 2 3 4 5 6; do
  dir="$BASE/../rank03/level$level"; subjects=(); while IFS= read -r item; do subjects+=("$item"); done < <(find "$dir" -mindepth 1 -maxdepth 1 -type d -printf '%f\n')
  bash "$BASE/session.sh" "REAL EXAM · LEVEL $level" "$dir" "${subjects[$((RANDOM%${#subjects[@]}))]}" || exec bash "$BASE/rank03_menu.sh"
done
ui_title; ok 'Real exam complete!'; read -r -p 'Press Enter to return... ' _; exec bash "$BASE/rank03_menu.sh"
