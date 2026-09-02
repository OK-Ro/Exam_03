#!/usr/bin/env bash
BASE="$(cd "$(dirname "$0")" && pwd)"; source "$BASE/colors.sh"; source "$BASE/ui.sh"
ui_title; printf "${CYAN}${BOLD}LEVEL MODE${RESET}\n\nChoose a level; its subjects are shuffled.\n\n  1  Level 1       2  Level 2       3  Level 3\n  4  Level 4       5  Level 5       6  Level 6\n\nType menu to return.\n"
read -r -p '> ' level
[[ "$level" == menu ]] && exec bash "$BASE/rank03_menu.sh"
[[ "$level" =~ ^[1-6]$ ]] || exec bash "$BASE/rank03.sh"
exec bash "$BASE/level_base.sh" "$level"
