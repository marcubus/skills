# Gate

The skill checking its own reply. Eighteen checks. Save the reply as `reply` and pipe it in; a check without a command is read against the reply.

## Contents

- Step map
- Checks

## Step map

| Step | Checks |
|---|---|
| 1. Decompose | 1, 2, 10, 13 |
| 2. Flag | 12 |
| 3. Verify | 5, 15 |
| 4. The bar | 6, 7, 9, 11, 16, 17, 18 |
| 5. Annotate | 3, 4, 8 |
| 6. Audit | 14 |

## Checks

**1. Numbering.** Every claim line begins `C<n>` and the numbers run from 1 without a gap. Done when the command prints nothing.

```bash
grep -oE '^C[0-9]+' | sed 's/^C//' | awk 'BEGIN{want=1} {if ($1 != want) print "expected C" want ", got C" $1; want=$1+1}'
```

**2. Tags.** Every line carries one of the three tags and no other word sits in the tag slot. Done when the line count equals the three counts summed.

```bash
awk '/^C[0-9]+/{l++; if ($0 ~ /· factual/) f++; else if ($0 ~ /· definitional/) d++; else if ($0 ~ /· opinion/) o++}
     END{print l" lines: " f+0 " factual, " d+0 " definitional, " o+0 " opinions"}'
```

**3. Enum.** Every marked line carries one of the five markers with its matching verdict word, and no line carries two. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ (✅|➗|⚠️|❌|➖) /{m=$2; w=$3; gsub(/\*/,"",w)
     ok=(m=="✅"&&w=="SUPPORTED")||(m=="➗"&&w=="CONTESTED")||(m=="⚠️"&&w=="WEAK")||(m=="❌"&&w=="BULLSHIT")||(m=="➖"&&w=="UNVERIFIED")
     if (!ok) print "unpaired: " $1 " " m " " w
     t=$0; n=0; while (match(t, /(✅|➗|⚠️|❌|➖)/)) {n++; t=substr(t, RSTART+RLENGTH)}
     if (n>1) print "two markers: " $1}'
```

**4. Quote and limit.** Every `✅`, `➗` and `⚠️` has a quote line beneath it, and every quote is 15 words or fewer. Done when the command prints nothing.

```bash
awk -F'"' '/^C[0-9]+ /{if (id != "" && want && !seen) print "no quote: " id
                      id=$0; sub(/ .*/,"",id); want=($0 ~ /(✅|➗|⚠️)/); seen=0; next}
           /^> /{if (id != "") seen=1; n=split($2,a," "); if (n>15) print "long(" n "): " $2; next}
           END{if (id != "" && want && !seen) print "no quote: " id}'
```

**5. Quote trace.** Each quote appears character for character in a tool result from this session. Compare the quote against the transcript with markdown emphasis stripped, never against the annotation, and re-verify one claim at a time: a doubt about one claim is not a reason to retract the set. Done when every quote is found in a result whose link is the one printed beside it.

**6. Contradiction.** Every `❌` either quotes a contradicting span or prints its queries in backticks. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ ❌/{id=$0; sub(/ .*/,"",id); q=0; s=0; next}
     /^> /{if (id) q=1; next}
     /^C[0-9]+|^Self-audit:/{if (id && !q && !s) print "no evidence: " id; id=""}
     /^Why:/{if (id && /`[^`]+`/) s=1}
     END{if (id && !q && !s) print "no evidence: " id}'
```

**7. Silence.** Every `➖` names its ground — `wall`, `horizon` or `generality` — and what was tried. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ ➖/{id=$0; sub(/ .*/,"",id); next}
     /^Why: /{if (id != "" && $0 !~ /(wall|horizon|generality)/) print "unnamed ground: " id; id=""}'
```

**8. Tally.** The five printed counts equal the recomputed ones, the quoted count equals the quote lines, and marked plus opinions equals the line count. Done when the arithmetic matches term by term.

```bash
awk '/^C[0-9]+ ✅/{s++} /^C[0-9]+ ➗/{c++} /^C[0-9]+ ⚠️/{w++}
     /^C[0-9]+ ❌/{b++} /^C[0-9]+ ➖/{u++} /· opinion/{o++} /^> /{q++}
     END{print "computed ✅" s+0 " ➗" c+0 " ⚠️" w+0 " ❌" b+0 " ➖" u+0 " · " o+0 " opinions, " q+0 " quoted"}'
```

**9. Origins.** Every `✅` resting on agreement names both origins, and applying the origin test to those two names shows they report different events, releases, datasets or documents. Compare the two names, not the two domains. Done when each such line names two and each pair passes.

**10. Qualifier.** Every quoted figure carries its qualifier, or the claim is `⚠️`. Done when the qualifier is readable in the quote alone.

**11. Definitions.** Every `✅` on a definitional line names the one tier-1 document that states the convention. Done when that document's title appears on the line.

**12. Flags.** Every `Why` opens with one of § 2's flag names, in any case, or with `clean`; and a claim whose own text carries a percentage, a rate, a multiple or a totaliser names both of its rung-4 queries, whatever flag it was given. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ /{id=$0; sub(/ .*/,"",id); owe=($0 ~ /%|[0-9]x|[0-9] (requests|rps|req|times|per)/ || $0 ~ /(never|always|the only|no one|every)/); next}
     /^Why: /{p=$0; n=gsub(/`[^`]+`/,"&",p); q=substr($0, index($0,":")+2, 40)
              if (q !~ /^(authority|unsourced|confidence|totalisers|named|internal|causation|quoted|clean)/) print "no flag: " id
              if (owe && n<2) print "one counter query: " id}'
```

**13. Nothing dropped.** Every sentence of the response appears in the annotation, in its original order, with the claims it split into grouped under it. Compare sentence by sentence, not line by line. Done when no sentence is missing, duplicated or reordered.

**14. Audit line.** The reply ends with one audit line, every id it names appears above at the verdict it states, its counts match the annotation, and each reason names the check that caught it — a `0 changed` line carries no reason. Done when the command prints nothing and every change reconciles.

```bash
awk '/^Self-audit:/{n++; line=$0}
     END{if (n != 1) print "audit lines: " n
         if (n == 1 && line !~ /changed/) print "no change count"
         if (n == 1 && line !~ /0 changed/ && line !~ /check [0-9]/) print "no check cited"}'
```

**15. Effort.** No claim took more than four queries, unless a specific claim's four returned nothing and the `Why` names the four that failed. Compare the queries in each `Why` against the ladder. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ /{id=$0; sub(/ .*/,"",id); next}
     /^Why: /{t=$0; n=gsub(/`[^`]+`/,"&",t); if (n>5) print "over budget: " id " " n}'
```

**16. Adversarial read.** Each quote establishes the claim it sits under rather than merely mentioning its subject. Read the quote alone, then the claim: a claim that needs its `Why` to survive is over-verdicted. Done when every quote stands on its own, and a reply marking every claim `❌` is re-read for the same failure in the other direction.

**17. Tier.** Every quote line ends `tier <n>`, the number is 1, 2 or 3, and it matches the tier its source earns. Done when the command prints nothing and no vendor claim about quality carries tier 1.

```bash
grep '^> ' | grep -v ', tier [123]$'
```

**18. Precedence.** Where two rows of § 4 could apply, the verdict is the one further from `✅`, and a credible tier-≤2 contradiction is `➗`. Compare the strongest applicable row against the verdict on each contested line. Done when no line admits a stronger row than the one it took.

