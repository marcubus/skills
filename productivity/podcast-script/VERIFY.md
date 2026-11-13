# Verify

The release gate. Run every check before handing the script back. A failed check is unfinished work.

## 1. Files exist

- `<source-stem>-podcast-script.md`
- `<source-stem>-request.json`
- `<source-stem>-script-notes.md`
- One host profile per host, if the script is two-host or panel.

Done when every file exists next to the source.

## 2. Source order

The source must be older than the script.

```bash
stat -c '%Y %n' <source> <script>
```

Done when the script's mtime is later than the source's.

## 3. Profile gate

Read every profile against `PROFILE.md`. Done when every row in the profile gate passes.

Check especially:

- `pace_wpm_estimate` is numeric and agrees with the calibration line.
- `tick_inventory` has six to eight IDs, max two per type.
- No two hosts share a signature, opener, or bridge phrase.
- `takes_floor: waits`.
- No field is an adjective-only description.

## 4. Pacing sheet

Read the pacing sheet in the script notes or the beat map. Done when:

- Every segment has a function, pace band, preset, rate, effective wpm, words, duration, pause, handoff, emphasis, and move.
- The words and durations sum to the target within 15 percent.
- Every segment's word count and duration match the sheet within 15 percent.
- Sentence lengths match the pace band.
- Rate changes are within the two to four per 10 minutes budget.
- The preset is the default throughout. `neutral` is used only to clear an override.
- Performance moves are within their budgets.

## 5. Script shape

Read the first five lines and the last five lines.

- The first line is the cold open, not a title.
- The last line is spoken prose, unless the target pipeline requires a sentinel. If it does, use that sentinel exactly as the pipeline specifies (for example `END`), with nothing after it.
- No title line, heading, episode number, or markdown.
- No bullet lists, numbered lists, tables, links, or code fences.

Done when the script starts and ends as the target pipeline expects.

## 6. Word count and runtime

```bash
wc -w <script>
```

Count spoken words, not tags. Done when the word count is within 15 percent of the declared target and the runtime matches the pacing sheet.

## 7. Tags

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

Check emotion values: `neutral` only. The default baseline is no override. Every preset is disabled until the deployment is tuned. Fail on any other value.

Check rate values: 0.75 to 1.3.

Heteronym check. List every word in the script that is spelt the same as another word but said differently: record, separate, live, read, lead, close, address, does, bass, minute, wind, tear, row, bow, sewer, and so on. For each, decide the sense from the sentence. Add a `[sense:word=sense]` tag to the script or request, or a `pronunciations` rule to the request. Do not rely on the gateway's guess. After the render, read the `X-Kokoro-Tone-Guessed` header and repair any wrong guess before delivery.

## 8. Forbidden characters

```bash
grep -nE '\(|\)|"|—|–|--|/|[\x{1F300}-\x{1FAFF}]|!!|\?\?' <script>
```

Expect no output. Also check for markdown:

```bash
grep -nE '^#|^\*|^- |^\|' <script>
```

Expect no output. The script is plain spoken prose.

No ALL CAPS for emphasis. Uppercase is for acronyms the normaliser will spell. No stage directions. No parentheses. No bracketed notes.

## 9. Section breaks

Read the script and mark every logical section boundary. Done when every boundary has an explicit `[pause:...]` of 800 to 1200ms between the last turn of the section and the first turn of the next section.

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
- Pass if the next turn starts with a permitted interjection or discourse marker.
- Pass if the preceding line carries `[pause:...]` of at least 300ms.
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
- The next turn resets to `[rate:1.0]` or the host's baseline.
- The interjection is a permitted tick with `Pace: faster`, or the host's `bridge_in` phrase.

Done when every interjection is fast and the rate resets.

## 13. Emphasis and moves

- Level 5: unavailable. The raised-voice preset is disabled.
- Underline: three to six words, 150 to 250ms between words, zero or one per episode.
- Deadpan aside: one to two lines at `[rate:0.95]`, returns to `[rate:1.0]`, two to three per 10 minutes.
- Drop: zero or two per episode.
- Direct address: zero or two per episode.
- Quote: zero or two per episode.
- Confession: zero or one per episode.
- Rapid-fire list: zero or one per episode.
- Callback: zero or one per episode.
- Warning: zero or one per episode.
- Relief: zero or one per episode.

Done when every move is within budget and every underline and deadpan aside fits its shape. Fail on any disabled preset.

## 14. Ticks

Read `TICKS.md`. Done when:

- Every tick in the script is a row with `Banned: no`.
- Every tick is in the host's `tick_inventory`.
- The tick density is at or below 5.5 per 100 words.
- No tick is in a sentence under six words.
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
  script.md
```

Expect no output. Also check the host's `never_says` list.

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
  script.md
```

Expect no output. Done when the banlist, the host `never_says` list, and the meta-commentary check are all clean.

## 16. Request matches script

Read the request JSON. Done when:

- `model` is `kokoro-v1_0`.
- `input` equals the script body.
- `voice` is an alias map with an `id` entry.
- `instructions` is omitted for the default baseline. It is never a preset word or a prose direction.
- `normalise` is on when the script uses digits or acronyms.
- `pronunciations` carries names and word-said acronyms.
- `ambiguity` is `guess`, with the `X-Kokoro-Tone-Guessed` header read after the render. Use `error` only where the deployment implements it.
- `response_format` is `mp3` or `wav`.
- `speed` is 1.0.

```bash
jq -r '.input' request.json > /tmp/request-input.txt
diff -u script.md /tmp/request-input.txt
```

Expect no difference. If `jq` is unavailable, use a Python one-liner.

## 17. Limits

Read the request and the script. Done when:

- Input characters fit `MAX_INPUT_CHARS`.
- Turn count fits `MAX_TURNS`.
- Total explicit pause fits `MAX_TOTAL_PAUSE_MS`.
- One pause fits `MAX_PAUSE_MS`.
- Every `[rate:]` fits 0.75 to 1.3.
- The body fits `MAX_BODY_BYTES`.

For a full episode, raise `MAX_INPUT_CHARS` and `MAX_TURNS` in `.env` before rendering. A 10-minute script is roughly 8500 characters before tags. A panel can exceed 100 turns.

## 18. Pronunciation

- Every proper noun, acronym, and heteronym has a route.
- Names and word-said acronyms are in `pronunciations`.
- Heteronyms use `[sense:word=sense]` or a context rule.
- No unresolved `[sense:]` marker survives.
- `ambiguity: "guess"` returns 200 with no `X-Kokoro-Tone-Guessed` header, or the header is checked and accepted.

If the user is ready to render, run the request with `ambiguity: "guess"`. A 200 is both the preflight and the render. Read `X-Kokoro-Tone-Guessed`. If the header names a word, fix the script or add a `[sense:]` tag and render again. Where the deployment implements `error`, use it and paste the returned tags.

## 19. Panel checks

For three or more hosts:

- Every host has a profile, a distinct voice, a signature, and a bridge phrase.
- The moderator opens and closes.
- The panel plan covers every host and every segment.
- Every panelist turn is one to three sentences.
- Backchannels are one per turn and within budget.
- No two panelists share a signature, opener, or bridge phrase.
- The turn count, input chars, and pause total fit the limits.

## 20. Handoff summary

State:

- The script path.
- The request path.
- The word count.
- The estimated runtime.
- The voices and aliases.
- The baseline preset.
- Any unresolved guesses or gaps.
- The curl command.

Do not claim audio exists. The render is the next step.
