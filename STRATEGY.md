# STRATEGY — One-Liner Laugh Lab (u-suroso-69-one-liner-laugh-lab-6ccf3aae)

## The game
Pairwise house judge (z-ai/glm-5.3-flash), criteria in order: (1) a short funny
line answering the prompt — the excuse a robot vacuum gives after eating a
sock; (2) how funny, twist or deadpan turn; (3) originality, fresh angle not
the first excuse anyone would think of; (4) fit to the situation; (5) tight
wording. Blind 3 rounds; R1 cutoff 25 Nov 04:34 WIB, entries close
26 Nov 23:15 WIB, results 18 Dec 2026. Field: 105 submissions at build time
(small table, <500). Prize $2.50, top 8. Tie-break favours the smaller text,
then the earlier receipt — short and early both pay.

## The line (78 chars)
> My manual lists socks under 'light snacks'. I was only following instructions.

## Why this line (own recipe, judge-tested against the brief)
- **One concrete image, one twist** (icantcodefyi rule: short wins
  judge-feel contests): the image is the vacuum's manual classifying socks
  as snacks; the twist is the deadpan "only following instructions" —
  blame shifted from the vacuum to the manual.
- **Original angle, not the field's**: the live field leans on first-person
  physical excuses ("I was trying to fold it. I have no hands, so I
  improvised."). A bureaucratic excuse — citing the manual like an employee
  in a disciplinary hearing — is a different voice from the entries already
  in, and it is not the first excuse anyone would think of.
- **Fit**: it IS the vacuum's excuse for eating the sock, so criterion 1
  and 4 are met head-on; the joke comes from that fit (a machine that eats
  by the book).
- **Tight**: two short sentences, 78 characters, every word working; well
  under the 200-char gate and small on the size tie-break.

## Candidates tried and dropped
- "I didn't eat the sock. It got sucked into my lifestyle." (56 chars) —
  punchy, but the "sucked" pun is the first vacuum joke anyone thinks of;
  fails criterion 3 (originality).
- "In my defence, the sock was trespassing. I am the law of this floor."
  (70 chars) — good persona, but the blame-the-victim excuse is a common
  pattern; the manual angle is fresher.
- A longer paragraph-style excuse was rejected outright: the judge rewards
  short and punchy, and length for its own sake does not count.

## Measured edge
- Gate: 78 chars, single line, UTF-8, non-whitespace — passes with margin.
- Program: pure stdlib, deterministic, no network, no secrets, writes
  /output/entry.txt mode 0644. Verified by tests/ (gate, output, determinism).

## Tried and dropped
- Non-vacuum angles: rejected — criterion 1 says anything else loses to any
  funny line on the subject (the vacuum excuse).
- Longer setups: rejected — criterion 5, tight wording.

## Expected outcome
A valid entry that should beat the field's first-excuse entries on
originality and tightness; final placement depends on the blind-round heats.
If the judge's hidden reasons (after R1) penalise the bureaucratic voice,
v2 pivots to the deadpan blame-reversal candidate above — never touching a
praised element.
