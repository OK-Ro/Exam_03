#!/usr/bin/env bash
BASE="$(cd "$(dirname "$0")" && pwd)"; source "$BASE/colors.sh"; source "$BASE/ui.sh"
ui_title; printf "${CYAN}${BOLD}SESSION COMMANDS${RESET}\n\n  test   Check Python syntax\n  next   Continue to the next subject\n  shell  Open the current rendu folder\n  exit   Leave the current mode\n\n"; read -r -p 'Press Enter to return... ' _; exec bash "$BASE/menu.sh"
