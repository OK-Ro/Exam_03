#!/usr/bin/env bash
set -euo pipefail
BASE="$(cd "$(dirname "$0")" && pwd)"; mode="$1"; resource="$2"; shift 2; rendu="$BASE/../../rendu"; source "$BASE/colors.sh"; source "$BASE/ui.sh"
total="$#"; n=0

test_subject() {
  local subject="$1" target="$2"
  python3 "$BASE/tester.py" "$target/$subject.py" "$subject"
}

for subject in "$@"; do
  n=$((n+1)); target="$rendu/$subject"; mkdir -p "$target"; cp "$resource/$subject/question.txt" "$target/question.txt"; [[ -e "$target/$subject.py" ]] || : > "$target/$subject.py"
  verified=0
  while true; do
    ui_title; printf "${CYAN}${BOLD}%s${RESET}\n${BLUE}Question %d of %d${RESET}" "$mode" "$n" "$total"
    [[ -n "${EXAM_STARTED_AT:-}" ]] && printf " ${BLUE}· Elapsed %s${RESET}" "$(elapsed "$(( $(date +%s)-EXAM_STARTED_AT ))")"
    printf "\n"; ui_line; printf "${GREEN}${BOLD}Your subject: %s${RESET}\n\n" "$subject"; cat "$resource/$subject/question.txt"; ui_line
    if (( verified )); then
      printf "${GREEN}${BOLD}STATUS: VERIFIED — you can continue.${RESET}\n"
    else
      printf "${YELLOW}STATUS: NOT VERIFIED — run test before continuing.${RESET}\n"
    fi
    printf "${YELLOW}test${RESET} verify   ${YELLOW}next${RESET} continue   ${YELLOW}shell${RESET} workspace   ${YELLOW}status${RESET} info   ${YELLOW}help${RESET} commands   ${YELLOW}exit${RESET} leave\n"
    read -r -p '/> ' command
    case "$command" in
      test)
        if test_subject "$subject" "$target"; then
          verified=1
          pass_banner
          ok 'All required local tests passed. You may type next.'
        else
          verified=0
          bad 'Not passed yet. Fix the solution and run test again.'
        fi
        read -r -p 'Press Enter to continue... ' _
        ;;
      next)
        if (( verified )); then break; fi
        bad 'Next is locked until this subject passes all tests.'
        read -r -p 'Press Enter to continue... ' _
        ;;
      shell) (cd "$target" && "${SHELL:-/bin/sh}");;
      status)
        printf "\n${CYAN}Workspace:${RESET} %s\n${CYAN}Progress:${RESET} %d/%d\n${CYAN}Verification:${RESET} %s\n" "$target" "$n" "$total" "$([[ $verified -eq 1 ]] && printf VERIFIED || printf PENDING)"
        read -r -p 'Press Enter to continue... ' _
        ;;
      help)
        printf "\n${YELLOW}test${RESET} runs all functional checks. ${YELLOW}next${RESET} unlocks after a pass.\n${YELLOW}shell${RESET} opens the solution folder. ${YELLOW}status${RESET} shows progress. ${YELLOW}exit${RESET} leaves without passing.\n"
        read -r -p 'Press Enter to continue... ' _
        ;;
      exit) exit 1;; *) bad 'Unknown command. Type help to see available commands.'; sleep .6;;
    esac
  done
done
ui_title
pass_banner
ok "Session complete — $total subject(s) verified."
read -r -p 'Press Enter to continue... ' _
