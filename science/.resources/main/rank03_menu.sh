#!/usr/bin/env bash
BASE="$(cd "$(dirname "$0")" && pwd)"; source "$BASE/colors.sh"; source "$BASE/ui.sh"
ui_title; printf "${CYAN}${BOLD}EXAM RANK 03 · MODE SELECTION${RESET}\n\n  ${YELLOW}1${RESET}  ${BOLD}Level Mode${RESET}      All subjects from one selected level\n  ${YELLOW}2${RESET}  ${BOLD}Real Exam Mode${RESET}  One random subject from every level\n  ${YELLOW}3${RESET}  Back to main menu\n"; ui_line
read -r -p 'Enter your choice (1-3): ' c
case "$c" in 1) exec bash "$BASE/rank03.sh";; 2) exec bash "$BASE/rank03_real_mode.sh";; 3) exec bash "$BASE/menu.sh";; *) exec bash "$BASE/rank03_menu.sh";; esac
