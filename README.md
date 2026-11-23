# The World in One Day — 23 November 2026

A front page that sums up Monday 23 November 2026 in one image: 1 big
headline + 13 small panels, 14 stories across 8 regions, every number and
name taken from dual-sourced verified reports of that day.

## The image

`entry.png` (1024×1024, PNG) is drawn by `draw.py` from the verified story
set — no invented numbers, no hype, no speculation shown as fact. The date
**23 November 2026** is printed in the masthead and on every panel.

Headline: Russian overnight strike on Dymer kills up to 15 in Kyiv region
(11 dead in one apartment block; a boy aged 7 and a woman aged 79 rescued
after 22 hours).

Small panels: COP31 ends with no climate deal · Ukraine sinks Russian
corvette Merkury off Libya · NATO meets on Polish airspace violation ·
China cuts stock margin floor to 80% · Tata Steel buys 26.4% of APL Apollo
for $1.67bn · Iran vows "every means" to break Hormuz blockade · Report
blames Israel for toxic pollution in 99% of Gaza · Record FAA ground stop ·
Senate GOP open to cutting Iran war funds · AI stock rout: Nikkei -4.8%,
KOSPI -4.7% · WHO urges calm as Ebola-hit DR Congo fighting grows ·
India 720-9 declared; Test vs NZ ends in draw · OpenAI chief proposes
"perplexity" limits on frontier AI.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. Running it
twice writes identical bytes. Regenerate the image with
`python3 draw.py entry.png` (Pillow + DejaVu fonts).

## Entry

Competition: news-image-20261123 — "Sum up 23 November's world news in
one image" (make.fun).
