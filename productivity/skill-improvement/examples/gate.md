# Example gate

An excerpt from a fictional invoice-check skill. Six checks, five steps, one brought-in path.

## Step map

| Step | Checks |
|---|---|
| 1 Read the invoice | 1 |
| 2 Read the purchase order | 1 |
| 3 Match line items | 2, 3 |
| 4 Total the variance | 4 |
| 5 Write the report | 5, 6 |

A brought-in report enters at step 5 and runs checks 5 and 6 only.

## 1. Both documents parsed

Done when every line item in the invoice and the order has a description, a quantity, and an amount.

## 2. Every line matched

Done when every invoice line has a match, or is listed as unmatched with the reason.

## 3. Tolerance applied

Done when each matched line is marked inside or outside the band in `RULES.md`, and the band used is named.

## 4. Variance totals

```bash
awk -F, 'NR>1 {s+=$4} END {print s}' lines.csv
```

Done when the reported total equals the sum of the line variances, to the cent.

## 5. Three lines

Done when the report is exactly three lines: the total, the largest variance, and the action.

## 6. No invented figure

Done when every number in the report appears in the invoice or the order, or is a sum of them.

## Retired

- 7. Currency conversion. Retired: the skill takes one currency. Number kept so old references resolve.
