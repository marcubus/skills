# Gate

Twelve checks, mapped to the step that produces each one's evidence.

## Contents

- Step map
- Checks
- The ledger block
- The report commands

## Step map

| Step | Checks |
|---|---|
| 1 Frame the question | 1, read at step 2 |
| 2 Open the run | 1, 2, 3 |
| 3 Search in waves | 4, 5, 6 |
| 4 Validate | 7, 8, 9, 10 |
| 5 Write the report | 11, 12 |
| 6 Run the gate | 1 to 12 |
| 7 Deliver | 2, 12, and the reply items |

## Checks

| # | Check | How |
|---|---|---|
| 1 | The question and its axes | The `question:` line in `notes.md` is one sentence, `questions_asked:` records no more than two scope questions, `exclusions:` is filled or says none, `brief:` and `source_families:` are filled, and the `axes:` list holds three to six entries, each a name, the part of the question it serves, and a FINDINGS label as `EVIDENCE.md` defines it. A three-axis run meets the exception in step 1, with the fourth axis and why in `gaps:` |
| 2 | One run, one report, one path | Exactly one run directory for this topic at the base path named in `EVIDENCE.md`, holding the five entries, or six with `archive/`, with `run.lock` reading one integer, or a partial directory that is archived before a fresh one is written. The reports directory sits outside it and holds reports and nothing else. The report sits in the resolved reports directory, its name matches `YYYY-MM-DD-<slug>-report.md` or `YYYY-MM-DD-<slug>-report-<N>.md` after a collision, the slug is at most 60 characters, and the path is the one recorded in `notes.md` under `report:` |
| 3 | The skeleton came first | At step 2, the skeleton holds the header block, every label in `REPORT.md`, and one ALL CAPS label per axis, each followed by a `TO BE WRITTEN` line. `notes.md` carries `skeleton_written_at:`, and that timestamp precedes the earliest `fetched_at` in `sources.tsv` that is not `n/a`, or the run is sole-source and the timestamp alone is the evidence. At step 6, read the timestamp and the section order, since step 5 has removed the stubs |
| 4 | The tables are well formed | Block section 4 prints no complaint: each header matches exactly, every row has its column count, each table holds at least one row, and every `published` value is a date, a month, or `undated` |
| 5 | Every body matches its row | Block section 5 prints no complaint: every `sha1` matches its cached body, every file in `bodies/` is named by a row, and a body written from a transcription says so in `notes.md` |
| 6 | Every quote is in its body | Block section 6 prints no complaint: every quote occurs verbatim in the body it cites, and no quote runs over the limit in `EVIDENCE.md`. An `inference` row carries no quote and is skipped. A translated quote is in the source's language, with the translation in `note`. Read each quote against its claim, to the division `EVIDENCE.md` sets between the quote and the `note` |
| 7 | Origins are counted right | Block section 7 prints no complaint: every `origins` count matches its sources, and no one-origin claim is labelled `established`. A `contested` claim may rest on one origin when two documents from it disagree, and the report says so. A contested claim names the strongest opposing source it read, in its `note`, read by hand. Read the labels too: two pages from one vendor, or one publisher, are one origin whatever their labels say |
| 8 | Every source is tiered, originated, and current | Every row in `sources.tsv` carries a tier of 1, 2, or 3 and a non-empty `origin`, every source with an incentive has a line in `notes.md`, every fetch that took a fallback route has a `fetches:` line, the tier rule in `EVIDENCE.md` holds, and block section 7 prints no tier 3 figure in THE NUMBERS or BOTTOM LINE. A tier 3 figure in FINDINGS is named in the text as that source's own claim, read by hand. More than one source family was used, or the run is sole-source, or the run records the no-search waiver in `overrides:`, or the report says why one family carried it in WHAT COULD NOT BE VERIFIED. Every source is inside the freshness window in `SOURCING.md`, read from the source itself and not from the axis name, or is an older source the report labels with its date and why the claim still holds; a claim resting on such a source is `single-sourced` unless the report names the reason it still holds. An undated source is named as undated and may carry only a claim that does not turn on recency, unless it is a specification or standard whose version is named; otherwise it is dropped |
| 9 | No domain dominates | Block section 8 shows no domain above the concentration limit in `SOURCING.md`, or `notes.md` records the override and its reason. A sole-source run is exempt, and says so in the reply |
| 10 | The coverage bar holds | Every headline claim and every supporting claim meets the bar defined in `EVIDENCE.md`, including its axis exemption, and `sources.tsv` holds at least three rows unless the run is sole-source. Block section 7 prints the origin, tier, and confidence failures, and block section 9 prints one line per axis with no sourced claim |
| 11 | The report is complete | Every section in `REPORT.md` is present, or omitted only because it would be empty and named in WHAT COULD NOT BE VERIFIED with the reason. No `TO BE WRITTEN` line remains, no claim appears in two sections, and every `gaps:` line appears in WHAT COULD NOT BE VERIFIED. THE NUMBERS follows the never-empty rule in `REPORT.md`. Every sentence carrying a number or a date ends with one to three `[S#]` markers, which the block checks, and every sentence carrying a name or a superlative does too, read by hand; every marker names a row in `sources.tsv`. Every figure in THE NUMBERS carries its base, date, and method in the sentence or in the `note`, read by hand. A figure converted from another currency names its rate and its date, read by hand. SOURCES lists every source with its id, tier, title, publisher, date, and URL, ordered by tier then by id, and a source there but never cited carries `background` before its URL. On a sole-source run the report says one document carried it, with no outside corroboration |
| 12 | The report is clean and stands alone | The prose rules in `REPORT.md` hold, including its punctuation rule, its quotation rule, its third-person rule, its paragraph limit, and its three stand-alone rules; the quotation rule is read by hand. The three stand-alone greps print no hit outside a quotation, a date, a version, or an identifier. Each FINDINGS label is a statement, not a question, and differs from the fixed labels, read by hand. BOTTOM LINE runs to three sentences. THE LANDSCAPE runs to two to four paragraphs when it is present, each FINDINGS label to one to four paragraphs, and WHAT WOULD CHANGE THIS to two to four sentences. The word count is inside the band in `REPORT.md`, including its named-length exception, or below its floor with the reason named in WHAT COULD NOT BE VERIFIED. Every `inference` claim is marked as such in the sentence that makes it. The report states findings, not recommendations, unless the user asked for them. WHAT WOULD CHANGE THIS names the evidence that would overturn every headline claim |

## The ledger block

The block runs with `bash`, from the run directory. Sections 4 and 5 answer checks 4 and 5, and print no complaint when they pass; the `==` banners are labels, not complaints. Section 6 prints the quote failures for check 6. Section 7 prints the origin, tier, and confidence failures for checks 7, 8, and 10; check 8's incentive, fetch-route, and freshness conditions are read by hand. Section 8 prints the domain counts you read against check 9. Section 9 prints one line per axis with no sourced claim, which check 10 reads against the report's gaps. Checks 1, 2, and 3 are read from `notes.md`, the two tables, and the report path, and checks 11 and 12 read the report and what the report commands print.

```bash
echo "== 4 headers"
[ "$(head -1 sources.tsv)" = "$(printf 'id\turl\tdomain\ttitle\tpublished\tfetched_at\tsha1\ttier\torigin\tbody')" ] || echo "sources header wrong"
[ "$(head -1 claims.tsv)" = "$(printf 'id\tclaim\tsection\tsources\torigins\tconfidence\tquote\tquote_source\tnote')" ] || echo "claims header wrong"
awk -F'\t' 'NR>1 && NF!=10{print "sources line "NR}' sources.tsv
awk -F'\t' 'NR>1 && $5!~/^[0-9]{4}(-[0-9]{2}){0,2}$/ && $5!="undated"{print "source "$1": published is neither a date nor undated"}' sources.tsv
awk -F'\t' 'NR>1 && NF!=9{print "claims line "NR}' claims.tsv
[ "$(wc -l < sources.tsv)" -gt 1 ] || echo "sources.tsv is empty"
[ "$(wc -l < claims.tsv)" -gt 1 ] || echo "claims.tsv is empty"

echo "== 5 bodies"
awk -F'\t' 'NR>1{print $7"\t"$10}' sources.tsv |
while IFS=$'\t' read -r sha body; do
  [ -f "$body" ] || { echo "missing body $body"; continue; }
  [ "$sha" = "n/a" ] || [ "$sha" = "$(sha1sum "$body" | cut -c1-12)" ] || echo "sha1 mismatch $body"
done
for f in bodies/*.txt; do
  [ -e "$f" ] || continue
  cut -f10 sources.tsv | grep -qx "$f" || echo "orphan body $f"
done

echo "== 6 quotes"
awk -F'\t' 'NR>1 && $6!="inference"{print $7"\t"$8}' claims.tsv |
while IFS=$'\t' read -r quote src; do
  grep -Fq -- "$quote" bodies/"$src"-*.txt || echo "quote missing in $src: $quote"
done
awk -F'\t' 'NR>1{n=split($7,a,/[ \t]+/); if(n>15) print "quote too long: "$1}' claims.tsv

echo "== 7 origins"
awk -F'\t' 'NR==FNR{if(FNR>1) o[$1]=$9; next}
  FNR>1 && $6!="inference"{n=split($4,s,","); delete seen; c=0
    for(j=1;j<=n;j++){l=o[s[j]]; if(!(l in seen)){seen[l]=1;c++}}
    if(c!=$5) print "claim "$1": origins "$5", sources carry "c
    if(c<2 && $6!="single-sourced" && $6!="contested") print "claim "$1": one origin, "$6}' \
  sources.tsv claims.tsv
awk -F'\t' 'NR==FNR{if(FNR>1) t[$1]=$8; next}
  FNR>1 && ($3=="THE NUMBERS" || $3=="BOTTOM LINE"){n=split($4,s,",")
    for(i=1;i<=n;i++) if(t[s[i]]==3) print "tier 3 figure in "$3": "$1}' \
  sources.tsv claims.tsv
awk -F'\t' 'NR>1 && $6!~/^(established|contested|single-sourced|inference)$/{print "claim "$1": bad confidence "$6}' claims.tsv

echo "== 8 domains"
tail -n +2 sources.tsv | cut -f3 | grep -v '^local$' | sort | uniq -c | sort -rn

echo "== 9 axes"
awk '/^axes:/{f=1;next} /^[a-z_]+:/{f=0} f&&/^- /{n=split($0,a,"|"); gsub(/^[ \t]+|[ \t]+$/,"",a[3]); print a[3]}' notes.md |
while read -r lab; do
  awk -F'\t' -v l="$lab" 'NR>1 && $3==l && $4!="none"{f=1} END{exit !f}' claims.tsv || echo "axis $lab: no claim with a source, exempt if named as a gap or its claims are in THE NUMBERS"
done
```

## The report commands

One block, with `R` set first. Run it from the run directory, because the marker and uncited-source loops read `sources.tsv`; when that file is absent they print one skip line. To check the worked example, run it from the skill folder with `R` unset.

```bash
R="${R:-examples/report.md}"
LAB='^[A-Z][A-Z0-9 ,-]+$'
wc -w "$R"
awk -v lab="$LAB" '$0 ~ lab && !/^SOURCES$/{s=$0; next} /^$/{next} {n=split($0,w," "); if(n>150) print "paragraph over 150 words in "s": "n}' "$R"
awk -v lab="$LAB" '/^THE LANDSCAPE$/{f=1; next} $0 ~ lab{f=0} f&&NF{p++} END{if(p>0&&(p<2||p>4)) print "landscape paragraphs: "p+0}' "$R"
awk -v lab="$LAB" '/^BOTTOM LINE$/{f=1; next} $0 ~ lab{f=0} f' "$R" | tr '\n' ' ' | awk '{n=gsub(/[.!?](\[[S0-9]+\])*( |$)/,"&"); if(n!=3) print "bottom line sentences: "n}'
awk -v lab="$LAB" '/^WHAT WOULD CHANGE THIS$/{f=1; next} $0 ~ lab{f=0} f' "$R" | tr '\n' ' ' | awk '{n=gsub(/[.!?](\[[S0-9]+\])*( |$)/,"&"); if(n<2||n>4) print "what would change this sentences: "n}'
awk -v lab="$LAB" '
  /^FINDINGS$/{inF=1; next}
  /^(THE NUMBERS|WHAT PRACTITIONERS SAY|WHAT EVERYONE GETS WRONG|WHERE THE SOURCES DISAGREE|WHAT COULD NOT BE VERIFIED|WHAT WOULD CHANGE THIS|SOURCES)$/{inF=0}
  inF && $0 ~ lab{if(lab0!="" && (pc<1||pc>4)) print "findings paragraphs under "lab0": "pc; lab0=$0; pc=0; next}
  inF && NF{pc++}
  END{if(lab0!="" && (pc<1||pc>4)) print "findings paragraphs under "lab0": "pc}' "$R"
grep -nE '[*|`]|^#|^-{3,}$|^={3,}$' "$R"
grep -nE '—|–' "$R"
grep -nE '[0-9]+-[0-9]+(%| percent)' "$R"
grep -niE '\b(podcast|episode|narration|tts|audiobook|voice-over|slide deck)\b' "$R"
grep -niE 'as you asked|earlier we|this report|this section|the research found|based on the search results|the agent' "$R"
grep -nwE 'you|your' "$R"
# every hit from the three stand-alone greps above (lines 117 to 119) must sit inside a quotation, or be a date, a version, or an identifier; check 12 reads each one
grep -n 'TO BE WRITTEN' "$R"
grep -nE '^[A-Z][A-Z0-9 ,-]+\?$' "$R"
# a label above ends in a question mark, which check 12 forbids
sed '1,3d; /^SOURCES$/,$d' "$R" | tr '\n' ' ' | sed -E 's/\.((\[S[0-9]+\])+)/\1./g' | awk '{n=split($0,s,"\\. "); for(i=1;i<=n;i++) if(s[i] ~ /[0-9]/ && s[i] !~ /\[S[0-9]+\]/) print s[i]}'
# each sentence above needs a marker, or is a date, version, or identifier; check 11 reads each one
sed '1,3d; /^SOURCES$/,$d' "$R" | tr '\n' ' ' | sed -E 's/\.((\[S[0-9]+\])+)/\1./g' | awk '{n=split($0,s,"\\. "); for(i=1;i<=n;i++){m=gsub(/\[S[0-9]+\]/,"&",s[i]); if(m>3) print "over three markers: "s[i]}}'
if [ -f sources.tsv ]; then
  grep -oE '\[S[0-9]+\]' "$R" | tr -d '[]' | sort -u |
    while read -r s; do cut -f1 sources.tsv | grep -qx "$s" || echo "marker $s not in sources.tsv"; done
  cut -f1 sources.tsv | tail -n +2 | sort -u |
    while read -r s; do
      sed '/^SOURCES$/,$d' "$R" | grep -q "\[$s\]" && continue
      grep -qE "^Tier [0-9]+\. \[$s\] .*\. background [^ ]+$" "$R" || echo "uncited source $s, needs background before the URL"
    done
else
  echo "no sources.tsv here: marker resolution skipped"
fi
```

The loop before it is the other direction: a source no marker names.
