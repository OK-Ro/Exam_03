#!/usr/bin/env bash
ui_clear() { printf '\033[2J\033[H'; }
ui_line() {
  local n i
  n=$(tput cols 2>/dev/null || printf 72)
  (( n > 100 )) && n=100
  (( n < 40 )) && n=40
  for ((i = 0; i < n; i++)); do printf '─'; done
  printf '\n'
}
ui_title() { ui_clear; printf "${CYAN}${BOLD}  EXAMSHELL${RESET} ${BLUE}· Rank 03 Python Practice${RESET}\n"; ui_line; }
ok() { printf "${GREEN}✓ %s${RESET}\n" "$1"; }
bad() { printf "${RED}✗ %s${RESET}\n" "$1"; }
pass_banner() {
  printf "\n${GREEN}${BOLD}╔══════════════════════════════════════════════╗${RESET}\n"
  printf "${GREEN}${BOLD}║             ✓  SUBJECT PASSED  ✓             ║${RESET}\n"
  printf "${GREEN}${BOLD}╚══════════════════════════════════════════════╝${RESET}\n"
}
elapsed() { local s="$1"; printf '%02d:%02d' "$((s/60))" "$((s%60))"; }
