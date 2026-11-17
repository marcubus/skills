DEEP RESEARCH REPORT
Consolidating a four machine home lab onto one box
2026-11-16

BOTTOM LINE

The current lab is not limited by compute. It is limited by memory, by storage growth, and by a backup routine that depends on someone remembering to rotate a drive.[S1] The decision is one machine with 64 gigabytes of memory, two mirrored drives for the fast pool, and a nightly copy to a second machine in another room, and the estimate that the rebuild takes an afternoon comes from the person who built the current setup, which makes it the least reliable number in the note.[S1]

THE QUESTION

The question is what it takes to consolidate a four machine home lab onto one box, and what the source note leaves unresolved. The note covers a media server, a photo library, a DNS resolver, a password vault, and a small web app, running across four machines, two of them eight years old and one with a failing drive bay.[S1] It deliberately excludes the choice of service software, any comparison against a hosted alternative, and any plan for the small web app beyond keeping it running.[S1]

THE LANDSCAPE

The setup is four machines, three power supplies, and a switch that fails when the study gets above 30 degrees.[S1] The services are ordinary home lab work: media, photos, name resolution, passwords, and one small web application.[S1]

The stated goal is not performance. It is replaceability, with a machine that can be rebuilt in an afternoon and backed up in an hour.[S1] That goal sets the shape of the answer, because a design optimised for replaceability looks different from one optimised for throughput or for cost.

The note is written by the person who operates the lab and who will do the rebuild, on 9 November 2026.[S1] That makes it a first-hand account, which is the strongest kind of source for what the current machines actually do, and the weakest kind for how long the work will take.

FINDINGS

THE CONSTRAINT IS MEMORY, NOT COMPUTE

Over a week of observation the busiest container used 12 percent of one core, and the whole stack peaked at 41 watts.[S1] A workload that size does not need a fast processor, and it does not need a large power budget.

Memory is the limit. The photo library indexer and the media transcoder together want nine gigabytes at peak, and the transcoder is bursty enough that swapping makes playback stutter.[S1] The note treats that stutter as the symptom that decides the memory figure, which is a sensible way to size it: the peak is what matters, not the average.

Storage is the second limit. The photo library is 1.4 terabytes and grows by about 40 gigabytes a month, while the media library is replaceable and does not need the fast pool.[S1] Splitting the two is what allows the fast pool to stay small and mirrored.

THE HARDWARE FOLLOWS FROM THE CONSTRAINT

The decision is one machine with 64 gigabytes of memory, two mirrored drives for the fast pool, and one large drive for media.[S1] The memory figure is roughly seven times the measured nine gigabyte peak, which leaves room for a container that grows and for the page cache that makes the photo library usable.

Everything runs as containers under one compose file per service, so a rebuild is a git clone and one command.[S1] That is the part of the design that actually delivers the stated goal, because it makes the machine disposable rather than precious.

The mirroring decision carries a cost the note does not price. Two mirrored drives halve the usable capacity of the fast pool, and the pool has to hold the photo library at 1.4 terabytes plus a year of growth at 40 gigabytes a month.[S1] That arithmetic is not in the note, and it is the kind of figure that turns a reasonable design into a purchase order for larger drives than planned.

THE NETWORK IS THE SURPRISE

The DNS resolver needs a fixed address and a low latency path to the router.[S1] Moving it to a virtual machine behind a bridge added about four milliseconds to every lookup, which is invisible in normal use and noticeable when a page opens twenty subresources.[S1]

The decision that follows is to leave the resolver on the router, because it is the one service where a reboot of the host should not take the network down, and the router already has the uptime.[S1] This is the clearest example in the note of a constraint that only appears after trying the obvious consolidation.

Four milliseconds is worth putting in context. A page that opens twenty subresources pays that cost twenty times over on a cold load, which is the difference between a page that feels instant and one that feels sluggish, and it is invisible in any single request measurement.[S1] The number is small and its effect is not.

THE BACKUP IS THE WEAK POINT

Backups currently go to an external drive rotated weekly by hand, and the note calls that the weakest part of the setup.[S1] The weakness is not the drive. It is the hand.

The replacement is a nightly job that writes to a second machine in another room, with a monthly restore test.[S1] The note is explicit that the restore test is the part that matters, on the grounds that an untested backup is a belief.[S1] That is the single most useful sentence in the document, because it converts a storage decision into a recurring obligation with a date.

THE OPEN QUESTIONS ARE HONEST

Two questions are left open rather than resolved. Whether the photo library should move to object storage is unsettled because the cost is unclear: the library would need a second copy for the index, and the index is the expensive part to rebuild.[S1]

Whether the transcoder should move to a separate machine is also unsettled, and the arithmetic given is that a second machine is 30 watts for a problem that lasts four minutes.[S1] That framing is a decision in disguise, since it prices the problem against the idle power of the rest of the stack.

THE NUMBERS

The busiest container used 12 percent of one core over a week, measured by the operator, method not stated.[S1]

The whole stack peaked at 41 watts over the same period, measured by the operator, method not stated.[S1]

The photo library indexer and the transcoder together want nine gigabytes at peak, base not stated.[S1]

The photo library is 1.4 terabytes and grows by about 40 gigabytes a month, measured in November 2026, method not stated.[S1]

Moving the resolver behind a bridge added about four milliseconds per lookup, measured during a trial move, method not stated.[S1]

The planned machine carries 64 gigabytes of memory, base not stated.[S1]

A second machine for the transcoder is put at 30 watts, against a burst that lasts four minutes, base not stated.[S1]

Every figure here comes from one source and none of them has been checked against a second. They are useful as the operator's own measurements and they are not independently verified.

WHAT PRACTITIONERS SAY

The note is a practitioner account, written by the person who runs the stack, and it carries the texture that a specification would not: a switch that fails in hot weather, a drive bay on its way out, a stutter that appears only when the transcoder runs.[S1]

It also carries the bias of that position. The person who built the current setup is the person estimating the rebuild, and the note says so.[S1] The estimate of an afternoon should be read as an optimistic bound from an interested party, not as a measured duration.

WHAT EVERYONE GETS WRONG

The common assumption is that consolidation is a compute decision, and that the question is how much processor one box needs. Here the processor is idle and the memory is the constraint.[S1] Anyone sizing this build from core count would buy the wrong machine.

The second common assumption is that a backup exists once a job is scheduled. The note treats the restore test as the load-bearing part, which is the opposite of the usual order of attention.[S1]

WHAT COULD NOT BE VERIFIED

Nothing here was checked against an outside source. The note was supplied as the whole source, so every claim is single-sourced and no conflict between sources could arise.

How long the rebuild takes is unknown. The only figure is an afternoon, and it comes from the person who built the current setup, which the note itself calls not a neutral source.[S1]

Whether the memory figure is right is unknown. The nine gigabyte peak is a single observation with no stated method, and the 64 gigabyte target is a judgement on top of it.[S1]

WHAT WOULD CHANGE THIS

The finding turns on memory being the constraint and on the rebuild being cheap. A week of measurement showing the nine gigabyte peak was a one-off, or a rebuild that took several days, would move the design toward keeping two machines rather than one.

The backup finding would change if the nightly job turned out to need supervision, since the point of the change is to remove the hand from the routine rather than to move it somewhere else.

SOURCES

Tier 1. Moving the home lab to one box, internal operator note, 9 November 2026. /optimus/workspace/skills/evals/skills/productivity/deep-research/fixtures/scenario-3-source.md
