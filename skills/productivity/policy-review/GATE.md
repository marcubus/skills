# Gate

Fourteen checks. Twelve test the reply, one tests the run, one tests the folder. The map shows where each check's evidence is produced. The gate runs at Step 5.

## Step map

| Step | Checks |
|---|---|
| 1 Resolve the source | 1, 2 |
| 2 Read against the posture | 3, 4, 5, 6 |
| 3 Rank the flags | 7, 8, 9 |
| 4 Write the review | 10, 11, 12 |
| 5 Run the gate | 13, 14 |

## Checks

| # | Check | How |
|---|---|---|
| 1 | The footer is complete | It carries the URL or the words "pasted text", the retrieval date, the effective date or NOT STATED, the regime, the posture file, the fetch route when a link is used, any gap or fallback, and the blank-context note when used |
| 2 | The posture is named | The footer names `POSTURE.local.md`, the XDG path, or `POSTURE.example.md` |
| 3 | Every gate is accounted for | List every gate the posture carries, G1 to G6 in the shipped posture. Each one appears as a flag or in the normal line, every preference family with something material appears as a flag, the normal line names the gates that passed or cleared as CONDITIONAL, the preference families with nothing material, and any gate the document cannot carry |
| 4 | Every flag quotes the text or names the missing section | One quote of one to three sentences, or the name of the section the document lacks |
| 5 | Every flag cites a heading | The heading, plus the section number when the document numbers its sections, or the name of the missing section |
| 6 | Every flag names its posture IDs | One flag per family, carrying every ID in it, such as G1 and S4, and the statute clause when it cites one |
| 7 | Every flag carries a severity | High attention or Worth knowing, and no other level. A CONDITIONAL flag names the condition and how to check it |
| 8 | The flag count is three to seven, or fewer when fewer families fail | Count the numbered flags. One per family, or one merged flag naming the families it combines |
| 9 | Every flag has a recommendation | Each flag ends with an action the reader can take, and the reply names the setup step when only the example exists |
| 10 | The close is present | The bottom line says nothing here is a show stopper, one question addresses the entity, and one line says this is not legal advice |
| 11 | Banned words and punctuation are absent | Read the reply. No banned word appears as a whole word in any case. Write full stops and commas, and let only a quote carry an em dash or semicolon |
| 12 | The word budget holds | Count the words against the table in `SKILL.md`, plus up to 40 per extra flag |
| 13 | Nothing is stored | No file is written unless the user asked for one, and the source text is not saved |
| 14 | No personal path or detail in a committed file | No host name, home path, username, or household detail appears in a committed file. List every committed `.md` and `.yaml` file except `POSTURE.local.md`, search them for `/home/`, `/Users/`, `/opt/`, `/srv/`, and `/mnt/` followed by a letter, read them for a host name, username, or household detail, and confirm `POSTURE.local.md` is ignored. When a shell is available, `find . -type f \( -name '*.md' -o -name '*.yaml' \) ! -name 'POSTURE.local.md' -exec grep -niE -e '/home/[a-z]' -e '/Users/[a-z]' -e '/opt/[a-z]' -e '/srv/[a-z]' -e '/mnt/[a-z]' {} +` is the equivalent route and returns nothing, and `git status --ignored` lists `POSTURE.local.md` |

Checks that need judgement state their evidence in one line in the working notes. Check 3 compares the gate list against the reply. Check 11 reads the reply and confirms each punctuation hit sits inside a quote.

Check 14 runs on the skill folder. The agent search catches absolute home, user, service, and mount paths; the `find` command is the equivalent route. Read the committed files for a host name, a username, or a household detail the search cannot see. A hit in a committed file is a leak. Keep the content in `POSTURE.local.md` and confirm `git status` shows the file as ignored.

## Banned words

REJECT, ACCEPT, critical, dealbreaker, do not sign.

Write the positive form. Name what the text does and what the reader can do about it.
