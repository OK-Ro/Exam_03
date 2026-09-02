#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; source "$BASE/colors.sh"; source "$BASE/ui.sh"
mkdir -p "$BASE/../../rendu"
ui_title
subjects=$(find "$BASE/../rank03" -name question.txt | wc -l | tr -d ' ')
workspaces=$(find "$BASE/../../rendu" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')
printf "${BOLD}Your local Rank 03 exam simulator${RESET}\n${BLUE}%s subjects installed · %s workspaces ready${RESET}\n\n" "$subjects" "$workspaces"
printf "  ${YELLOW}1${RESET}  Commands & help\n  ${YELLOW}2${RESET}  Start Exam Rank 03\n  ${YELLOW}3${RESET}  Open rendu workspace\n  ${YELLOW}0${RESET}  Exit\n"; ui_line
read -r -p 'Enter your choice: ' choice
case "$choice" in
  1) exec bash "$BASE/help.sh";; 2) exec bash "$BASE/rank03_menu.sh";;
  3) (cd "$BASE/../../rendu" && "${SHELL:-/bin/sh}"); exec bash "$BASE/menu.sh";;
  0|exit) ui_clear; printf "${GREEN}Good luck with your exam! 🍀${RESET}\n";;
  *) bad 'Invalid choice.'; sleep .5; exec bash "$BASE/menu.sh";;
esac
