# Gate

The skill checking its own reply. Twenty-two checks. Save the annotation as `reply` (checks 1–18) and the rendered reply as `render` (checks 19–22); a check without a command is read against the file. Each command reads its file on standard input: run it as `< reply`.

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
| 5. Annotate and render | 3, 4, 8, 17, 19, 20, 21, 22 |
| 6. Audit | 14 |

## Checks

**1. Numbering.** Every claim line begins `C<n>` and the numbers run from 1 without a gap, in the artifact's response order. Done when the command prints nothing.

```bash
grep -oE '^C[0-9]+' | sed 's/^C//' | awk 'BEGIN{want=1} {if ($1 != want) print "expected C" want ", got C" $1; want=$1+1}'
```

**2. Tags.** Every line carries one of the three tags and no other word sits in the tag slot. Done when the command prints nothing.

```bash
awk '/^C[0-9]+/{l++; if ($0 ~ /· claim/) c++; else if ($0 ~ /· definitional/) d++; else if ($0 ~ /· opinion/) o++}
     END{if (l != c+d+o) print l" lines: " c+0 " claims, " d+0 " definitional, " o+0 " opinions, " l-(c+d+o) " untagged"}'
```

**3. Enum.** Every marked line carries one of the five markers with its matching verdict word, and no line carries two. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ (✅|❓|⚠️|❌|🤷) /{m=$2; w=$3; gsub(/\*/,"",w)
     ok=(m=="✅"&&w=="SUPPORTED")||(m=="❓"&&w=="CONTESTED")||(m=="⚠️"&&w=="WEAK")||(m=="❌"&&w=="BULLSHIT")||(m=="🤷"&&w=="UNVERIFIED")
     if (!ok) print "unpaired: " $1 " " m " " w
     t=$0; n=0; while (match(t, /(✅|❓|⚠️|❌|🤷)/)) {n++; t=substr(t, RSTART+RLENGTH)}
     if (n>1) print "two markers: " $1}'
```

**4. Quote and limit.** Every `✅`, `❓` and `⚠️` has an evidence blockquote above it, and every quoted fragment in that blockquote is 15 words or fewer. A context block, whose lines begin `> agent:` or `> you:`, is exempt: it quotes whole sentences. Done when the command prints nothing.

```bash
awk -F'"' '
/^> (agent|you):/{next}
/^> /{pend=1; s=$0; while (match(s, /"[^"]*"/)) { f=substr(s, RSTART+1, RLENGTH-2); c=split(f,a," "); if (c>15) print "long(" c "): " f; s=substr(s, RSTART+RLENGTH) } next}
/^C[0-9]+ /{id=$0; sub(/ .*/,"",id); if (($0 ~ /(✅|❓|⚠️)/) && !pend) print "no quote: " id; pend=0; next}
'
```

**5. Quote trace.** Each fragment appears character for character in a tool result from this session, the context fragments in the response under test, the evidence fragments in their cited source, and the fragments keep their source order. Split on `…` and check each part; never compare a quote against the annotation. Done when every fragment is found in a result whose link is printed beside it.

**6. Contradiction.** Every `❌` and `❓` has a blockquote above it, or prints its queries in backticks. Done when the command prints nothing.

```bash
awk '/^> /{q=1}
     /^C[0-9]+ (❌|❓)/{id=$0; sub(/ .*/,"",id); found[id]=q; q=0; next}
     /^C[0-9]+ /{q=0}
     /^Why:/{if (id != "" && !found[id] && $0 !~ /`[^`]+`/) print "no evidence: " id; id=""}
     END{if (id != "" && !found[id]) print "no evidence: " id}'
```

**7. Silence.** Every `🤷` names its ground — `wall`, `horizon` or `generality` — and what was tried. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ 🤷/{id=$0; sub(/ .*/,"",id); next}
     /^Why: /{if (id != "" && $0 !~ /(wall|horizon|generality)/) print "unnamed ground: " id; id=""}'
```

**8. Tally.** The five printed counts equal the recomputed ones, marked plus opinions equals the line count, and the opinion count equals the tagged opinion lines. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ ✅/{s++} /^C[0-9]+ ❓/{c++} /^C[0-9]+ ⚠️/{w++}
     /^C[0-9]+ ❌/{b++} /^C[0-9]+ 🤷/{u++} /· opinion/{o++}
     /^✅ [0-9]+ · ❓/{split($0, p, /[^0-9]+/); ps=p[2]; pc=p[3]; pw=p[4]; pb=p[5]; pu=p[6]; pm=p[7]; po=p[8]}
     END{
       if (ps == "") { print "no tally line"; exit }
       bad = 0
       if (ps+0 != s+0) { print "✅ printed " ps ", computed " s+0; bad=1 }
       if (pc+0 != c+0) { print "❓ printed " pc ", computed " c+0; bad=1 }
       if (pw+0 != w+0) { print "⚠️ printed " pw ", computed " w+0; bad=1 }
       if (pb+0 != b+0) { print "❌ printed " pb ", computed " b+0; bad=1 }
       if (pu+0 != u+0) { print "🤷 printed " pu ", computed " u+0; bad=1 }
       if (pm+0 != s+c+w+b+u) { print "marked " pm ", marked lines " s+c+w+b+u; bad=1 }
       if (po+0 != o+0) { print "opinions printed " po ", tagged " o+0; bad=1 }
       if (bad) printf "computed ✅ %d ❓ %d ⚠️ %d ❌ %d 🤷 %d · %d opinions\n", s, c, w, b, u, o
     }'
```

**9. Origins.** Every `✅` resting on agreement names both origins, and applying the origin test to those two names shows they report different events, releases, datasets or documents. Compare the two names, not the two domains. Done when each such line names two and each pair passes.

**10. Qualifier.** Every quoted figure carries its qualifier, or the claim is `⚠️`. A figure with no quote at all is judged by the absence test, not by this check. Done when the qualifier is readable in the quote alone.

**11. Definitions.** Every `✅` on a definitional line names the one tier-1 document that states the convention. Done when that document's title appears on the line.

**12. Flags.** Every `Why` opens with one of § 2's flag tokens — the parenthesised word beside each name — in any case, or with `clean`; and a claim whose own text carries a percentage, a rate, a multiple or a totaliser names both of its rung-4 queries, whatever flag it was given. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ /{id=$0; sub(/ .*/,"",id); body=$0; sub(/^.*— (agent|you): /,"",body)
              owe=(body ~ /%/ || body ~ /one in/ || body ~ /[0-9][0-9,.]* ?(x|×|k|K|M|B|GB|MB|TB|ms|ns|rps|req|requests|per|times|users|people|percent)/ || body ~ /(never|always|the only|no one|nobody|none|every|most)/)
              next}
     /^Why: /{p=$0; n=gsub(/`[^`]+`/,"&",p); q=substr($0, index($0,":")+2, 40)
              if (q !~ /^(authority|unsourced|confidence|totalisers|named|internal|causation|quoted|clean)/) print "no flag: " id
              if (owe && n<2) print "one counter query: " id}'
```

**13. Nothing dropped.** Every sentence of the response appears in the annotation, in its original order, with the claims it split into grouped under it. Compare sentence by sentence, not line by line. Done when no sentence is missing, duplicated or reordered.

**14. Audit line.** Every id the audit line names appears above at the verdict it states, its own line and change counts match the marked lines, and each reason names the check that caught it — a `0 changed` line carries no reason. Done when the command prints nothing and every change reconciles.

```bash
awk '/^Self-audit:/{audit=$0; next}
     {body=body $0 "\n"}
     END{
       if (audit == "") { print "no audit line"; exit }
       n=split(audit, w, /[^A-Za-z0-9]+/)
       for (i=1;i<=n;i++) if (w[i] ~ /^C[0-9]+$/ && index(body, w[i] " ") == 0) print "audit names missing " w[i]
     }'
```

**15. Effort.** No claim took more than four queries. A specific claim may take a fifth only when the four returned nothing and its `Why` says so. Compare the queries in each `Why` against the ladder. Done when the command prints nothing.

```bash
awk '/^C[0-9]+ /{id=$0; sub(/ .*/,"",id); next}
     /^Why: /{t=$0; n=gsub(/`[^`]+`/,"&",t)
              if (n>5) print "over budget: " id " " n
              else if (n==5 && t !~ /(four|4).*(fail|nothing|empty|no result|zero)/) print "fifth without the failed four: " id}'
```

**16. Adversarial read.** Each quote establishes the claim it sits under rather than merely mentioning its subject. Read the quote alone, then the claim: a claim that needs its `Why` to survive is over-verdicted. Done when every quote stands on its own, and a reply marking every claim `❌` is re-read for the same failure in the other direction.

**17. Tier.** Every blockquote line carrying a source ends `tier <n>`; the number is 1, 2 or 3, and it matches the tier its source earns. Done when the command prints nothing and no vendor claim about quality carries tier 1.

```bash
grep '^> ' | grep -e '—' | grep -v ', tier [123]$'
```

**18. Precedence.** Each line takes the only row its evidence fits: `❌` has a contradicting tier ≤2 span, a quote that does not establish the claim, or a passed absence test; `✅` has support and no contradiction at equal or higher tier; `❓` quotes both sides at comparable tier; `⚠️` quotes a partial span; `🤷` has a wall, horizon or generality. Read the verdict against its evidence, and against the nearest row it did not take. Done when no line could take a nearer row than the one it took.

**19. Render order.** Groups run `❌` → `❓` → `🤷` → opinions; the counts line is the last non-empty line, carrying no `C` ids, and the audit line sits directly above it. Done when the command prints nothing.

```bash
awk '
/^C[0-9]+ ❌/{r=0} /^C[0-9]+ ❓/{r=1} /^C[0-9]+ 🤷/{r=2} /^C[0-9]+ · opinion/{r=3}
/^C[0-9]+ /{if (r < rk) print "order: " $1; rk=r; next}
NF{prev2=prev; prev=$0}
END{if (prev !~ /(WEAK|SUPPORTED)/) print "counts line not last: " prev
    if (prev ~ /C[0-9]+/) print "ids in counts line"
    if (prev2 !~ /^Self-audit:/) print "audit not above counts: " prev2}
'
```

**20. Context block.** Every `❌`, `❓` and `🤷` opens with a blockquote whose fragments are each prefixed `agent:` or `you:`. Done when the command prints nothing.

```bash
awk '
/^> /{if (!inb) {blocks++; inb=1}
      if (blocks==1 && $0 !~ /^> (agent|you): "/) print "unprefixed context: " $0; next}
/^$/{inb=0; next}
/^C[0-9]+ (❌|❓|🤷)/{if (blocks<1) print "no context block: " $1; blocks=0; inb=0; next}
/^C[0-9]+ /{blocks=0; inb=0; next}
{inb=0}
'
```

**21. Claim line.** Every `❌`, `❓` and `🤷` names its author after the dash and states the claim in prose, not as a quotation. Done when the command prints nothing.

```bash
awk -F'—' '/^C[0-9]+ (❌|❓|🤷) /{c=$2
      if (c !~ /^ (agent|you): /) print "no attribution: " $1
      if (c ~ /"/) print "quoted claim: " $1}'
```

**22. Blank lines.** A blockquote sits above every `❌`, `❓` and `🤷` claim, with exactly one blank line between the quote and the claim, so the renderer does not absorb the claim. Done when the command prints nothing.

```bash
awk '/^> /{q=NR; next}
     /^C[0-9]+ (❌|❓|🤷)/{if (q != NR-2) print "no blank line above: " $1; q=0; next}
     /^C[0-9]+ /{q=0}'
```
