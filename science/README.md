# Rank 03 ExamShell

A standalone, Bash-based 42-style practice shell for the Rank 03 Python
exercise bank. It follows the resource-and-mode structure of `42_examshell`,
but contains only Rank 03 practice.

```bash
cd rank03_examshell
make
```

The main menu offers **Level Mode** and **Real Exam Mode**.

- Level Mode: choose a level and practise every subject in that level in random order.
- Real Exam Mode: receive one random subject from each of Levels 1–6.

For every subject, the shell creates `rendu/<subject>/`, copies the subject,
and gives you an empty Python solution file. In a session, type `test`, `next`,
`shell`, or `exit`.
