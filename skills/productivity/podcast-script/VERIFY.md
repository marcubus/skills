# Verify

The release gate. Run every check before handing the script back. A failed check is unfinished work.

Run every check with the agent's file and search tools, using the table below for the checks that carry a command. When the host has a POSIX shell, each command is an equivalent mechanical route. The agent route is primary; the command is the fallback.

| Check | Agent route | Pass when |
|---|---|---|
| 2 | Read the source and script file metadata, or open each file and compare the modified time | The script is newer |
| 6 | Read the script, ignore every bracketed marker, and count the remaining words | The count is within 15 percent of the target, and the runtime matches the pacing sheet |
| 7 | Find every bracketed span, group them by tag and value, and check each tag against the five allowed tags | Every tag is one of the five, no bracket lacks a colon, every emotion is one of the eight, and every rate is 0.75 to 1.3 |
| 8 | Search the script for `(`, `)`, `"`, an em dash, an en dash, `--`, `/`, `!!`, and `??`, then for emoji, then for a line starting with `#`, `*`, `- `, or `\|` | No hit from any search |
| 15 | Search the script for each banlist phrase, each meta-commentary phrase, and each host `never_says` phrase, ignoring case | No hit from any search |
| 16 | Read the script and the compiled text, remove every bracketed marker from both, and compare the word sequences | Differences appear only where a marker became punctuation or a blank line, or where a name was respelt |

A timestamp needs a file tool that reports modified time. When it reports none, mark check 2 unverified rather than passing it.

## Contents

- Step map
- 1. Files exist
- 2. Source order
- 3. Profile gate
- 4. Pacing sheet
- 5. Script shape
- 6. Word count and runtime
- 7. Markers
- 8. Forbidden characters
- 9. Section breaks
- 10. Same-speaker tone changes
- 11. Speaker changes
- 12. Interjections
- 13. Emphasis and moves
- 14. Ticks
- 15. Banlist and meta-commentary
- 16. Text matches the script and the model
- 17. Text only
- 18. Pronunciation
- 19. Panel checks
- 20. Claims trace to the source
- 21. Handoff summary

## Step map

Run the checks for the step you just closed, then the full gate before delivery. For a brought-in script, run checks 7 to 21 and skip checks 1 to 4.

| Step | Checks |
|---|---|
| 1 Source | 2, 20 |
| 2 Profiles | 3 |
| 3 Model | none; read the capability table |
| 4 Beats | none; the beat map has no check of its own |
| 5 Pacing | 4 |
| 6 Script | 5, 6, 8, 15 |
| 7 Markers and ticks | 7, 9, 10, 11, 12, 13, 14 |
| 8 Pronunciation | 18 |
| 9 Compile | 16, 17 |
| 10 Verify | 1, 19, 21 |

## 1. Files exist

- `<source-stem>-podcast-script.md`
- `<source-stem>-tts-<model>.txt`, the compiled text
- `<source-stem>-script-notes.md`, or `<source-stem>-script-notes-<model>.md` for a retarget
- One host profile per host, solo included.
- `<source-stem>-panel-plan.md`, for three or more hosts.

Done when every file exists next to the source.

## 2. Source order

The source must be older than the script. Skip this check for a retarget.

```bash
python3 -c 'import os,sys; [print(int(os.path.getmtime(p)), p) for p in sys.argv[1:]]' <source> <script>
```

Done when the script's mtime is later than the source's, read from the file tool. When the host has a POSIX shell, the command returns the same value.

## 3. Profile gate

Read every profile against `PROFILE.md`. Done when every row in the profile gate passes.

Check especially:

- `pace_wpm_estimate` is numeric and agrees with the calibration line.
- `tick_inventory` has six to eight IDs, max two per type, and one `signature_tick` from it.
- No two hosts share a signature tick, opener, or bridge phrase.
- Two-host and panel: `takes_floor: waits`.
- The `show` block matches the shape: solo has no co-host fields, panel has moderator and panelists.
- No field is an adjective-only description.

## 4. Pacing sheet

Read the pacing sheet in the script notes or the beat map. Done when:

- Every segment has a function, pace band, emotion, rate, effective wpm, words, duration, pause, handoff, emphasis, and move.
- The words and durations sum to the target within 15 percent.
- The script's segments match the sheet's word count and duration within 15 percent.
- Sentence lengths match the pace band.
- Rate changes are within the two to four per 10 minutes budget.
- Every emotion is one of the eight. A value the model does not carry is dropped and recorded.
- Performance moves are within their budgets.

## 5. Script shape

Read the first five lines and the last five lines.

- The first line is the cold open, not a title.
- The last line is spoken prose. No sentinel such as `END`, which the engine would speak.
- No title line, heading, episode number, or markdown.
- No bullet lists, numbered lists, tables, links, or code fences.

Done when the script starts and ends as the target pipeline expects.

## 6. Word count and runtime

```bash
sed -E 's/\[[^]]*\]//g' <script> | wc -w
```

Count spoken words, not markers. Done when the word count is within 15 percent of the declared target and the runtime matches the pacing sheet.

## 7. Markers

List every tag.

```bash
grep -oE '\[[A-Za-z_]+:[^]]*\]' <script> | sort | uniq -c
```

Done when every tag is one of:

- `[voice:]`
- `[emotion:]`
- `[rate:]`
- `[pause:]`
- `[sense:]`

Fail on any other bracket pair. Unknown tags are spoken.

Check for a bracket with no colon:

```bash
grep -oE '\[[^]]*\]' <script> | grep -v ':'
```

Expect no hit. A bare bracket such as `[wheeze]` would be spoken.

Check every emotion value against the eight in `PERFORMANCE.md`. Fail on any value outside the eight. A value the model does not carry is dropped and recorded.

Check every rate value is within 0.75 to 1.3.

Heteronym check. List every word in the script that is spelt the same as another word but said differently: record, separate, live, read, lead, close, address, does, bass, minute, wind, tear, row, bow, sewer, and so on. For each, decide the sense from the sentence. Resolve it the way the model file says. Do not rely on the engine's guess.

## 8. Forbidden characters

```bash
grep -nE '\(|\)|"|—|–|--|/|!!|\?\?' <script>
python3 -c 'import sys; [print(i+1, l.rstrip()) for i,l in enumerate(open(sys.argv[1], encoding="utf-8")) if any(0x1F300 <= ord(c) <= 0x1FAFF for c in l)]' <script>
```

Expect no hit from either search. The first checks the punctuation, and the second checks the emoji range without relying on a PCRE-enabled grep. Also check for markdown:

```bash
grep -nE '^#|^\*|^- |^\|' <script>
```

Expect no hit. The script is plain spoken prose.

No ALL CAPS for emphasis. Uppercase is for acronyms the model spells out. No stage directions. No parentheses. No bracketed notes.

## 9. Section breaks

Read the script and mark every logical section boundary. Done when every boundary has an explicit `[pause:...]` between the last turn of the section and the first turn of the next section: 800 to 1200ms, or 1000 to 1200ms for a panel.

Example: a weather update followed by local news is two sections. The boundary needs a section-break pause.

Fail if the boundary relies on the default 350ms gap.

## 10. Same-speaker tone changes

For every `[emotion:]` or `[rate:]` tag that is not the first tag for a new speaker:

- The preceding turn ends with sentence punctuation.
- The preceding line carries `[pause:...]` of at least 300ms.
- The tag is not mid-sentence.

Done when every same-speaker change has a pause and lands at a sentence boundary.

## 11. Speaker changes

For every `[voice:]` change:

- Pass if the previous turn ends with a question mark.
- Pass if the first word after the voice and rate tags is a permitted interjection or discourse marker.
- Pass if the preceding line carries `[pause:...]` of at least 300ms, or 200 to 300ms after an interjection handoff.
- Fail if none of the three is present.
- Fail if the interjection is a banned tick.
- Fail if the question is not answered by the next speaker.
- Fail if two hosts share a bridge phrase.

Done when every voice change has a pause, a question, or an interjection.

## 12. Interjections

For every interjection handoff:

- One to four words.
- `[rate:1.05]` to `[rate:1.1]`.
- A short pause after it: 200 to 300ms.
- The next turn resets to `[rate:1.0]`, the host's baseline, or the rate the host used before the interjection.
- The interjection is a permitted tick with `Pace: faster`, or the host's `bridge_in` phrase.

Done when every interjection is fast and the rate resets.

## 13. Emphasis and moves

- Level 5: only where the model carries `angry`.
- Underline: three to six words, 150 to 250ms between words, zero or one per episode.
- Deadpan aside: one to two lines at `[rate:0.95]`, and the next line sets its own rate. Two to three per 10 minutes.
- Build: zero or one per episode.
- Drop: zero to two per episode.
- Direct address: zero to two per episode.
- Quote: zero to two per episode.
- Confession: zero or one per episode.
- Rapid-fire list: zero or one per episode.
- Callback: zero or one per episode.
- Warning: zero or one per episode.
- Relief: zero or one per episode.

Done when every move is within budget and every underline and deadpan aside fits its shape. A move that needs an emotion the model does not carry is recorded as dropped.

## 14. Ticks

Read `TICKS.md`. Done when:

- Every tick in the script is a row with `Banned: no`.
- Every tick is in the host's `tick_inventory`, or in that host's `emotion_behaviour.ticks_under_load`, or is one of the host's `bridge_in` or `bridge_out` literals.
- The tick density is at or below the host's `tick_density` for the segment's state: baseline, or strained when the segment carries `angry` or `excited`. A panel uses 2.0 baseline, 3.5 strained, 5.0 ceiling.
- No tick is inside a sentence under six words. A tick that is its own sentence is allowed.
- No more than two ticks are in any 20-word window.
- A sign-off appears once.
- A phrase tic appears no more than three times.
- Backchannels are one per turn and within the per-host budget.
- Regional ticks match the host's nationality.
- Eye-roll and understatement ticks pair with the deadpan aside.
- Curiosity ticks pair with the curious follow-up.

## 15. Banlist and meta-commentary

Collect every row in `TICKS.md` with `Banned: yes`. The table is authoritative. The grep below covers the common literals and is a starting set.

```bash
grep -inF \
  -e "that's a really great point" \
  -e "absolutely, one hundred percent" \
  -e "couldn't agree more" \
  -e "that's a really good question" \
  -e "let's unpack that" \
  -e "in today's episode" \
  -e "dive into" \
  -e "at the end of the day" \
  -e "it's important to note that" \
  -e "when it comes to" \
  -e "the fact of the matter is" \
  -e "needless to say" \
  -e "as we discussed earlier" \
  -e "as i mentioned" \
  -e "in conclusion" \
  -e "to sum up" \
  -e "without further ado" \
  -e "thanks for watching" \
  -e "stay tuned" \
  -e "i hear you" \
  -e "let's take this offline" \
  -e "let's circle back" \
  -e "touch base" \
  -e "close the loop" \
  -e "keep me in the loop" \
  -e "reach out" \
  -e "heads up" \
  -e "ping me" \
  -e "sync up" \
  -e "level set" \
  -e "pulse check" \
  -e "parking lot" \
  -e "double-click on that" \
  -e "deep dive" \
  -e "move the needle" \
  -e "low-hanging fruit" \
  -e "boil the ocean" \
  -e "think outside the box" \
  -e "paradigm shift" \
  -e "game changer" \
  -e "best-in-class" \
  -e "value add" \
  -e "mission critical" \
  -e "stakeholder alignment" \
  -e "it is what it is" \
  -e "when push comes to shove" \
  <script>
```

Expect no hit. Also check the host's `never_says` list.

Then check for meta-commentary that describes the process rather than the content:

```bash
grep -inE \
  -e "let me explain" \
  -e "i'?ll walk you through" \
  -e "first,? i'?ll" \
  -e "next,? i'?ll" \
  -e "as i said" \
  -e "as we discussed" \
  -e "in this episode" \
  -e "the next section" \
  -e "this section" \
  -e "let'?s break this down" \
  -e "let'?s get into it" \
  -e "here'?s what we'?ll cover" \
  -e "by the end of this episode" \
  -e "i'?m going to tell you" \
  -e "i want to talk about" \
  -e "today we'?re going to" \
  -e "the point of this episode" \
  -e "before we begin" \
  -e "let'?s start with" \
  -e "let'?s move on" \
  -e "as mentioned" \
  -e "as discussed" \
  -e "to recap" \
  -e "to summarise" \
  -e "in this section" \
  -e "in the next section" \
  -e "the source says" \
  -e "the report says" \
  -e "the document says" \
  -e "the research shows" \
  -e "according to the report" \
  -e "according to the document" \
  -e "according to the source" \
  -e "the script says" \
  -e "the instructions say" \
  -e "the prompt says" \
  <script>
```

Expect no hit. Done when the banlist, the host `never_says` list, and the meta-commentary check are all clean.

## 16. Text matches the script and the model

Read the compiled text and the model file. Done when:

- The model is named in the notes and matches the text file name.
- Every marker is resolved: none survives unless the model reads it as text.
- The spoken words equal the script body after the compile rules.
- Every difference from the script is one the model file allows.

Compare the text to the script body after removing every marker the model resolves:

```bash
sed -E 's/\[[^]]*\]//g' <script-body> > "${TMPDIR:-${TEMP:-/tmp}}/script-words.txt"
sed -E 's/\[[^]]*\]//g' <compiled-text> > "${TMPDIR:-${TEMP:-/tmp}}/text-words.txt"
diff -u "${TMPDIR:-${TEMP:-/tmp}}/script-words.txt" "${TMPDIR:-${TEMP:-/tmp}}/text-words.txt"
```

Expect differences only where a marker became punctuation or a blank line, or where a name was respelt. Every other word matches.

Then apply the model file's own text rules. It is the authority on the dialect.

## 17. Text only

Read the compiled text. Done when:

- It holds the spoken words and the model's inline controls, and nothing else.
- No front matter, headings, comments, or code fences.
- No payload: no JSON, no keys, no endpoint, no header, no command.
- No marker the model does not read.

The skill delivers text. A payload belongs to the tool that renders it.

## 18. Pronunciation

- Every proper noun, acronym, and heteronym has a route.
- The model file says how to resolve a name or a heteronym.
- Every `[sense:]` tag is resolved. None is left ambiguous.

If a word is still ambiguous, add a `[sense:]` marker or respell it, then compile again.

## 19. Panel checks

For three or more hosts:

- Every host has a profile, a distinct voice, a signature tick, and a bridge phrase.
- The moderator opens and closes.
- The panel plan covers every host and every segment.
- Every panelist turn is one to three sentences.
- Backchannels are one per turn and within budget.
- No two panelists share a signature tick, opener, or bridge phrase.
- Every speaker change has a pause, a question, or an interjection.

## 20. Claims trace to the source

Read every spoken claim against the source. Done when:

- Every number, name, date, and quotation appears in the source.
- Every causal claim is one the source makes, not one the script infers.
- An inference the script draws from the source is stated as an inference, not as a fact.
- A rounded figure is the source's figure, rounded, and is not presented as exact.
- No margin, deadline, or count is invented.

A figure the source does not carry is a failure, even when it is plausible. Cut it, or say what the source does say.

## 21. Handoff summary

State:

- The script path.
- The compiled text path.
- The model and its text dialect.
- The word count.
- The estimated runtime.
- The voices and casting.
- The turn map, when the model drops `[voice:]`.
- Every dropped marker.
- Any unresolved guesses or gaps.

Do not claim audio exists. The render is the next step.
