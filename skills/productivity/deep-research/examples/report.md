DEEP RESEARCH REPORT
The real cost of running a small mail server
2026-11-16

BOTTOM LINE

Self-hosted email is cheap in hardware and expensive in attention, because the cost is not the server but the ongoing work of staying off blocklists.[S1][S3] The published comparisons that make it look nearly free leave out the hours, and for one small domain the operator's own account is the only estimate of them, single-sourced.[S7] The hours decide whether it is worth doing.

THE QUESTION

The question is what it costs to run mail for one small domain, in money and in time, compared with a hosted mailbox. The scope is a domain of up to ten mailboxes with modest volume, on a virtual server the owner already pays for.[S1] Excluded are high-volume sending, marketing mail, and any setup where deliverability is somebody else's job, because those are different problems with different economics.[S3]

THE LANDSCAPE

The pieces are a server, a mail transfer agent, a spam filter, DNS records, and a reputation. The server, the transfer agent, the filter, and the DNS records are ordinary installs. The reputation is not installable at all. It is granted by the receiving side, slowly, and it can be withdrawn in a day.[S5]

The receiving side has tightened. The large providers now require authenticated sending, a published policy, and a one-click unsubscribe on bulk mail, and they enforce it by rejecting or filing mail rather than by warning the sender.[S3] A domain that was fine in 2022 can be quietly junked in 2026 without a bounce to tell anyone.[S5]

Hosting costs have fallen at the same time. A virtual server large enough for mail for ten people costs less than a streaming subscription, and the software is free.[S1] The two curves cross in an awkward place: the money has become trivial and the attention has become the constraint.

FINDINGS

THE MONEY IS NOT THE COST

The direct cost of self-hosting for ten mailboxes is a server share, a backup, and a blocklist monitoring service, and it is smaller than the hosted bill.[S1] A hosted mailbox for the same ten people is a per-seat charge that scales with headcount and does not fall when usage does.[S2]

The comparison breaks when labour enters. A practitioner account puts the steady-state work at two to four hours a quarter for a small domain, mostly reading logs and chasing a listing.[S7] Read together, the two figures make labour the deciding term: at any reasonable hourly rate it dwarfs the subscription difference, which is why the argument for self-hosting is almost never financial.

There is a second asymmetry that the price lists hide. A hosted plan bills per seat and can be cancelled in a month, while a self-hosted domain carries a fixed cost in attention that does not scale down when a mailbox is removed.[S2][S7] On the same reasoning, small domains pay proportionally more for the self-hosted route than large ones do.

DELIVERABILITY IS THE PRODUCT

The thing being bought from a hosted provider is not storage. It is a reputation pool shared across millions of senders, maintained by a team whose only job is that pool.[S6] A self-hoster joins that pool as an unknown, and the pool does not care about good intentions.

The practical consequence is that the first year is the expensive one. New domains are treated as suspect until they accumulate history, and the recovery path from a listing is documentation and patience rather than a support ticket.[S4]

THE FIRST MONTH IS THE REAL COST CENTRE

The setup itself is a weekend. The month after it is a series of small failures: a missing record, a filter that scores too aggressively, a forwarder that breaks authentication, and a receiving provider that starts filing mail without a bounce.[S3][S7]

Each of those failures costs real time and none of them is predictable from the installation guide. This is the part the vendor comparisons omit, and it is the part that decides whether a small operator keeps the setup past the first quarter.[S8]

The failures also cluster. A missing record and a filter set too aggressively produce the same symptom, mail that does not arrive, and the operator has no instrument that separates them until a receiving provider answers a support request.[S4][S7] That single diagnostic gap accounts for most of the first month in the accounts that describe it in detail, and it is the reason the guides recommend a staged cutover rather than a switch on a Friday.[S7]

THE PATTERN THAT WORKS

The pattern that works is a domain with a technical owner, low volume, and no marketing mail.[S7] The pattern that fails is a domain whose owner wants to stop thinking about mail, because the whole point of the exercise is that someone has to think about it.

THE NUMBERS

Server share for ten mailboxes on a shared virtual server runs about four to six dollars a month, measured from published list prices in November 2026 and excluding any server the owner already runs.[S1]

A hosted business mailbox lists at about seven dollars per user per month on an annual plan, so ten mailboxes is about seventy dollars a month at list price before any discount.[S2]

No figure for operator time appears here, because none came from a primary or reputable secondary source.

The receiving providers' authentication requirements apply to all senders above five thousand messages a day, measured against the published thresholds in February 2026.[S3]

The accounts that read as marketing describe a single afternoon and no ongoing work; they are written by people selling a hosting product or a guide.[S8]

WHAT PRACTITIONERS SAY

The accounts that read as honest share a shape. The setup is described as a weekend, the first month as a series of small failures, and the steady state as quiet until it is not.[S7]

One practitioner detail is worth repeating because it contradicts the guides. The recurring work is not maintenance in the software sense. It is correspondence with receiving providers and blocklist operators, which is a support job rather than an engineering one.[S7]

WHAT EVERYONE GETS WRONG

The common belief is that self-hosting email is now easy because the software improved. The software did improve. The receiving side changed faster, and in the opposite direction, so the net difficulty rose while the installation got simpler.[S3]

The second common belief is that a blocklist listing is a rare accident. For a new domain it is close to a rite of passage, and the recovery is a documented process rather than an emergency.[S4]

The third is that a paid blocklist monitoring service removes the work. It removes the detection delay and leaves the correspondence, which is the larger half.[S7]

WHERE THE SOURCES DISAGREE

The cost per mailbox differs by an order of magnitude between the two published comparisons. One puts self-hosting at under a dollar per mailbox per month, the other at eleven dollars.[S1][S8] The gap is labour. The low figure counts only the server, the high figure includes an estimate of administration time at a commercial rate. Both are arithmetically correct and they answer different questions, so the money is treated here as settled and the time as the open variable.

The two sources also disagree about how long setup takes, by a factor of ten. That disagreement has the same cause, since the fast estimate is written by a vendor and the slow one by an operator.[S7][S8]

WHAT COULD NOT BE VERIFIED

No independent measurement was found of how often a small new domain is silently junked rather than rejected, so the frequency is unknown and the direction is inferred from provider guidance. The phrasings tried were junk folder rates, false positive small sender, and delivery failure silent.

No survey was found that measures operator time, so the two to four hour figure rests on one account and is labelled single-sourced throughout.

WHAT WOULD CHANGE THIS

The finding turns on labour being the dominant cost. A tool that automated blocklist monitoring and reputation recovery to the point where the quarterly work fell under an hour would invert the comparison for anyone whose time is billed. Evidence of that would be a documented setup with a year of logs and no manual intervention, which none of the sources provides.

The deliverability finding would change if a receiving provider began offering a shared reputation pool to small senders on the same terms as a hosted provider, and no source suggests that is planned.

SOURCES

Tier 1. [S1] Northwind Hosting, Cloud server price list, November 2026. https://northwind.example/cloud
Tier 1. [S2] Bluepeak, Workspace pricing, November 2026. https://bluepeak.example/workspace-pricing
Tier 1. [S3] Bluepeak, Email sender guidelines, February 2024, updated 2026. https://bluepeak.example/sender-guidelines
Tier 1. [S4] The Blocklist Council, Removal procedure, 2026. https://blocklist-council.example/removal
Tier 2. [S5] The Mail Ledger, Providers tighten sender rules again, 14 May 2026. https://mail-ledger.example/sender-rules
Tier 2. [S6] Sender Practice Forum, Best practices, 2025. https://sender-forum.example/best-practices
Tier 3. [S7] A practitioner, A write-up on running mail for a small domain, undated. https://notes.example/self-hosting-mail
Tier 3. [S8] A hosting vendor, Self-hosted versus hosted comparison, undated. https://vendor.example/self-hosted-vs-hosted

Illustrative example. The figures are invented and the URLs are placeholders.
