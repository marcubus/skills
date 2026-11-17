# Moving the home lab to one box

Internal note, 9 November 2026. Written by the person who runs it.

## Why

Four machines, three power supplies, and a switch that fails when the study gets above 30 degrees. The lab runs a media server, a photo library, a DNS resolver, a password vault, and a small web app. Two of the machines are eight years old and one has a failing drive bay. The goal is one machine that can be replaced in an afternoon and backed up in an hour.

## What we learned

The workload is not compute bound. Over a week the busiest container used 12 percent of one core, and the whole stack peaked at 41 watts. Memory is the constraint: the photo library indexer and the media transcoder together want 9 gigabytes at peak, and the transcoder is bursty enough that swapping makes playback stutter.

Storage is the second constraint. The photo library is 1.4 terabytes and grows by about 40 gigabytes a month. The media library is replaceable and does not need to be on the fast pool. Backups currently go to an external drive that is rotated weekly by hand, which is the weakest part of the setup.

Networking was the surprise. The DNS resolver needs a fixed address and a low latency path to the router, and moving it to a virtual machine behind a bridge added about 4 milliseconds to every lookup. That is invisible in normal use and noticeable when a page opens twenty subresources.

## What we decided

One machine, 64 gigabytes of memory, two mirrored drives for the fast pool, and one large drive for media. Everything runs as containers under a single compose file per service, so a rebuild is a git clone and one command.

The DNS resolver stays on the router. It is the one service where a reboot of the host should not take the network down, and the router already has the uptime.

Backups move to a nightly job that writes to a second machine in another room, with a monthly restore test. The restore test is the part that matters. An untested backup is a belief.

## What we did not settle

Whether the photo library should move to object storage. The cost is unclear because the library would need a second copy for the index, and the index is the part that is expensive to rebuild.

Whether the transcoder should move to a separate machine. The burst is short and the rest of the stack is idle, so a second machine is 30 watts for a problem that lasts four minutes.

How long the rebuild actually takes. The estimate is an afternoon, and the estimate comes from the person who built the current setup, which is not a neutral source.
