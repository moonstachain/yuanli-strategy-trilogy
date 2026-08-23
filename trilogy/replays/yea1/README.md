# YEA1 PIT Replay Pack

## Purpose and boundary

This pack tests whether the YEA1 candidate projection discriminates among materially different business species using information available at a declared point in time (PIT). It is research evidence, not a promotion receipt: no replay changes B1–B4 Canon, promotes YEA1, authorizes course use, or starts YBA0.

The four cases are [Amazon](amazon-pit-replay.md), [NVIDIA](nvidia-pit-replay.md), [Kweichow Moutai](maotai-pit-replay.md), and the [Webvan hard negative](webvan-hard-negative.md).

## Exact per-case structure

```text
0｜Case Identity + PIT Cutoff
1｜Evidence Boundary
2｜B1 Value Space
3｜B2 Value Density
4｜B3 Value Scale
   - Growth Chain
   - Replication Chain
   - Compounding Chain
5｜B4 Value Duration
   - 虚 / 实 / 入 / 出
   - Protection / Concentration / Self-Reinforcement
6｜What Was Knowable at PIT
7｜Hard Negative / Competing Explanation
8｜Invalidators
9｜Ex-Post Outcome (strictly separated from PIT thesis)
10｜YEA1 Discrimination Result
```

## Evidence protocol

For Sections 2–8, a source is PIT-eligible only if its filing, publication, or release date is no later than the case cutoff. Primary filings and issuer documents take precedence; contemporaneous third-party evidence may corroborate but may not silently replace missing primary evidence. Source metadata records title, issuer or publisher, filing or publication date, stable URL, a page/item/section pinpoint where feasible, and access date `2026-08-23`.

Every substantive claim line in a dossier begins with exactly one evidence tag:

```text
[PIT_FACT]
[PIT_INFERENCE]
[EX_POST_OUTCOME]
[UNKNOWN]
```

`[PIT_FACT]` is directly reported by an eligible source. `[PIT_INFERENCE]` is a bounded interpretation of cited PIT facts and cannot be presented as source language. `[UNKNOWN]` is used when the inspected corpus cannot answer the question. `[EX_POST_OUTCOME]` is confined to Section 9.

`EX_POST_OUTCOME may not be used to upgrade a PIT_FACT or PIT_INFERENCE.`

Contradictory evidence is preserved. Issuer forecasts and descriptions are identified as issuer claims. Causality is not inferred from sequence alone. A broad trend does not establish demand capture; demand does not establish replicable economics; cash flow does not establish durable control; and durability does not by itself establish value concentration or self-reinforcement.

The matched result uses only `SUPPORTED`, `MIXED`, `UNSUPPORTED`, and `UNKNOWN`. `Evidence Status` describes whether the required contemporaneous source classes were actually inspected and support a usable replay record; it does not describe whether the company passed B1–B4.

## Matched discrimination summary

| Case | B1 | B2 | B3 | B4 | Strongest Discriminator | Evidence Status |
|---|---|---|---|---|---|---|
| Amazon | SUPPORTED | SUPPORTED | SUPPORTED | MIXED | Positive trailing cash flow plus marketplace and fulfillment leverage, while control remained contestable | SUPPORTED |
| NVIDIA | SUPPORTED | SUPPORTED | SUPPORTED | SUPPORTED | A unified hardware-software-systems platform with a developer ecosystem, despite weak fabrication control | SUPPORTED |
| Kweichow Moutai | MIXED | MIXED | SUPPORTED | MIXED | Exceptional cash conversion and brand durability did not prove an expanding broad pool or every form of self-reinforcement | SUPPORTED |
| Webvan | MIXED | MIXED | UNSUPPORTED | UNSUPPORTED | Plausible convenience demand could not clear unproven replication, negative cash conversion, or control | SUPPORTED |
