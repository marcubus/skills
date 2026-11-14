# Product sync, 9 March

**Ana:** Start with the export bug. Where are we?

**Ben:** The CSV export drops the last row when the file has no trailing newline. I can have a fix by Thursday.

**Ana:** Do it. We ship it as a patch.

**Cleo:** Do we tell the customer?

**Ana:** Not yet. We wait until the patch is out.

**Ben:** The import path has the same bug, probably. I haven't checked.

**Ana:** Check it next week.

**Cleo:** I'd rather rewrite the parser than patch it twice.

**Ana:** Not now. We patch.

**Ben:** Fine.

**Ana:** Second thing. The dashboard is slow for accounts over 10,000 rows.

**Cleo:** That's the count query. I can cache it, but the cache has to be invalidated on import.

**Ana:** Cache it. We revisit the parser after the patch ships.

**Ben:** Who owns the customer note?

**Ana:** Cleo.

**Cleo:** I'll draft it by Friday, but it doesn't go out until the patch is live.

**Ben:** Someone should update the changelog.

**Ana:** Yes, do that.

**Ana:** Good. That's everything.
