+++
title = "Receipts"
subtitle = "This site's own numbers, measured, including the ones that are not flattering"
description = "What this site loads, what it weighs, what it sets on your device, what it emits, and what it cannot yet prove. Measured on 2026-10-14 against the build that includes this page, and against the live site the same day."
status_as_of = 2026-10-14
weight = 8
nav = "Receipts"
sources = [
  "web-almanac",
  "swd-emissions-model"
]
+++

Every other page here asks you to check its sources. This one turns the same standard on the site itself.

Most sites could publish a page like this. Almost none do, and the reason is not technical. The numbers below took one build command and one script, and the parts that are unflattering are here alongside the rest, because a page that only published its good numbers would be doing the thing this site complains about.

## How these numbers were taken

The site is built with `sh scripts/build.sh`, which runs four checks and then renders `public/`. Every figure on this page was then read out of that built directory rather than estimated: file sizes, request counts, and the contrast ratios, which are computed from the actual colour values in `assets/css/main.css`. The exception is "What the host sends" further down, which describes the serving rather than the files, and was therefore taken from the live site with `curl` on the same day.

Sizes are given both raw and gzipped, because gzip is what a server actually sends. Where something is a model estimate rather than a measurement, the page says so at the point where it appears.

**Measured on 2026-10-14**, against the build that includes this page. A page's weight here means everything the browser fetches for one view of it: the document, the stylesheet and the icon. Editing any page changes these figures slightly, including editing this one, so treat them as a dated snapshot rather than a constant.

The figures were re-taken after the site's real domain replaced the placeholder in `hugo.toml`, and again after the wording edits this page and `/sources/` received in the same session, because editing either page moves a row that names it. The domain edit alone adds 12 bytes to the canonical link in every page, and 24 to the home page, which also carries the RSS link. The median stayed at 9,171 bytes gzipped through all of it, and the two heaviest rows below are from the final run.

## What one page load costs

| | Measured | This site's budget | |
|---|---|---|---|
| Requests, per page | 3 (the document, one stylesheet, one icon) | under 20 | met |
| Requests to other companies | 0 | 0 | met |
| Scripts | 0 | | met |
| Cookies | 0 | 0 | met |
| Web fonts | 0, system font stack | | met |
| Median page, gzipped | 9,171 bytes | under 100 KB | met |
| Heaviest page, gzipped | 30,228 bytes (`/sources/`) | under 100 KB | met |
| Heaviest page, raw | 103,483 bytes (`/sources/`) | 100 KB, measured transferred | **over as raw bytes** |
| All 12 pages, gzipped | about 110 KB | | |

So a page here asks your browser for three files, all of them from this domain. The heaviest page on the site is the bibliography, and it is the one page deliberately exempt from the length rule, since it is a list of records rather than an argument.

**The raw row is the one place the budget does not hold, and it is printed rather than rounded away.** The 100 KB budget is written for what a page costs a reader, and what crosses the wire is compressed: 30,228 bytes, comfortably inside. Read as raw bytes instead, the heaviest page is 103,483, which is over 100 KB whether you read KB as 1,000 bytes or as 1,024, and no other page comes close, because the median is 25,343 bytes raw. So that row is marked over on the raw reading and met on the transferred one, and both numbers are here because the honest answer depends on which one the budget is about.

Nothing in the site can set a cookie: there is no JavaScript and no server-side code to do it with. The response headers used to be the one thing this page could not check, because there was nothing deployed to read them from. The site is live now, so they are measured rather than promised, in the next section.

The site-wide row is rounded, unlike the per-page figures. Editing any page moves the aggregate rows by tens of bytes, including the edit that published these numbers, which is why this page dates them and rounds the one figure that would otherwise be wrong within a day. The per-page figures have no such problem: build the site yourself from the same source and you will get exactly the numbers above.

That is this site's number. The number for the median page on the web is measured every year by the HTTP Archive for its Web Almanac, and you should read it there rather than take a figure quoted here, because a figure copied into a page like this one is out of date within a year. {{< cite "web-almanac" >}}

## What the host sends

The figures above measure the files. This section records what happens when somebody asks for them, taken with `curl` against the live site on 2026-10-14 rather than against a local build. It is the disclosure this page promised on the day it was written and could not make until there was a host to interrogate.

- **The server names itself** as `statichost.eu`, and it discriminates: a path that cannot exist returns `404` with a 13-byte body, while a real page returns `200`. That is the same control probe this site applies to its sources, and it is why a status code from this host is worth something.
- **HTTP/2 and HTTP/3 both work.** The `alt-svc` header advertises `h3`, and a request over QUIC returns the page with HTTP/3, so the advertisement is not decoration.
- **TLS is a Let's Encrypt certificate for this hostname alone**, issued at 18:34 UTC on the day the site went up and valid until 12 January 2027. It carries one name rather than a wildcard, which is the detail that makes the control probe above meaningful.
- **These headers are present:** `strict-transport-security: max-age=31536000; includeSubDomains; preload`, `x-content-type-options: nosniff`, `cache-control: public, max-age=0, must-revalidate`, an `etag`, `last-modified`, `vary: Accept-Encoding`, and `accept-ranges: bytes`.
- **These headers are absent:** `content-security-policy`, `referrer-policy`, `permissions-policy` and `x-frame-options`. A site with no scripts, no forms, no cookies and no third-party requests has little for them to protect, and that is an explanation rather than a defence. A policy of `default-src 'self'` would let your browser enforce this site's central claim instead of taking my word for it, so the absence is a defect and it is listed below.
- **Compression is gzip, and it is looser than the tables above.** Those figures are a local measurement, `gzip -9` on the machine the site was built on, reproducible by anybody who builds it. The host compresses at a lower setting and sends the icon uncompressed, so **what crosses the wire is about 3% larger than this page reports**: the heaviest page is 31,253 bytes as served against the 30,228 published above, and the median page is about 9,460 against 9,171. The published numbers stay as they are because they are the reproducible ones, and this bullet is the correction that keeps them honest.
- **What the host logs is not observable from outside**, and this page does not claim to know. The disclosure on [Sources](/sources/) says there is no server of mine in the path, which is a statement about architecture, and it is the accurate form of the claim.
- **Only the IPv4 address answered from the machine this was measured on.** The domain has both an `A` and an `AAAA` record, and the IPv6 attempt failed immediately with "network unreachable", which is a local condition rather than a statement about the host. So this page reports the IPv4 result and says nothing about IPv6 either way.

## What could not be measured

**Largest Contentful Paint is not measured.** The site's budget says under 1.5 seconds. Measuring it needs a real browser loading the page. A browser is installed on the machine this was built on, but it cannot be started from the environment these numbers were taken in, and no headless audit tooling is installed. So that line stays a target and not a result, and it is the easiest thing on this page for somebody else to settle: open the site, run Lighthouse, and the number is either inside the budget or it is not.

**No accessibility audit tool has been run.** Lighthouse, axe and WAVE all need a browser or a third-party service. The browser here cannot be launched from this environment and no headless audit tooling is installed, so none of them has been used. **This site therefore does not have a verified WCAG AA result.** This is the gap on this page that a reader can close in five minutes, and it is the one most likely to change the numbers above. What can be checked without a browser is checked, and here it is:

- one `h1` per page, 12 of 12 pages
- a language declared on the `html` element, 12 of 12
- a skip link before the navigation, 12 of 12
- images: none, so there is no missing alt text to find
- keyboard traps: none possible, because there is no JavaScript and no custom widget on the site
- focus styles: defined, and the focus ring measures 8.42:1 against its background in light mode and 9.35:1 in dark
- `prefers-reduced-motion`: honoured in the stylesheet

**Contrast is computed, not trusted.** The lowest ratio anywhere on the site is 6.66:1, on secondary text against the light background. Every text pair passes 4.5:1 in both colour schemes, and the highest is 17.6:1 on body text.

**The request count comes from the markup, not from a browser.** A real Network panel might show fewer requests, if something is cached, or one more, if your browser retries the icon. It cannot show a request to another company, because there is none in the markup to make.

**The HTML has not been validated.** The W3C validator is a third-party service. It could be run by hand without affecting the pages, and it has not been.

## Known failures

This is the section that makes the page worth publishing. Every item is a real defect, dated 2026-10-14.

**Foreign language text is not marked as such, which fails WCAG 3.1.2.** The bibliography contains French, German and Dutch titles, and the prose quotes phrases in other languages. Every page carries exactly one `lang` attribute, on the `html` element, so a screen reader will read *Outil d'auto-évaluation* in an English voice. This is a genuine failure, found while writing this page, and it is not fixed yet.

**Citation markers are small targets, which is a borderline failure of WCAG 2.5.8.** They are set at 0.75em with no line box, so the clickable area is a few pixels high. WCAG exempts targets set inline in a sentence, and these are, so the site is arguably compliant. It is still the weakest point here for anybody with a tremor, and it is on the list.

**The canonical URL pointed at a domain with nothing published at it, and the deploy closed it.** The placeholder went on 2026-10-14, when `hugo.toml` was pointed at `https://third-party.statichost.page/`, and the site went up the same evening. The change was then checked the way this site checks a source rather than the way it checks a status code: all twelve pages were fetched and each one's own title and `rel=canonical` were read off the response. Every page answers `200` with the title it should have, so the canonical copy of each page is now the page itself.

**Before the deploy, this domain behaved exactly like a name that cannot exist, and the reason this page gave for that was wrong.** `third-party.statichost.page` and `this-cannot-exist-9f2a.statichost.page` have identical DNS records, both pointing at the host through a wildcard, so a resolving name is not evidence that anything is live. The real name also refused a TLS connection with `tlsv1 alert internal error`, which is the same error the impossible name still gives today. This page originally read that as "neither has a certificate". **That was an inference, and the certificate contradicts it**: the one now serving this site was issued at 18:34 UTC, before the probe was taken, so what failed was the name answering rather than a certificate existing. An error you can observe is not the same thing as a cause you can name. This page made that mistake about its own domain, which is the mistake it exists to warn about everywhere else.

**There is no `content-security-policy`, and it is the defect here worth fixing first.** The full header set the host sends is listed above. A site with no scripts, no forms, no cookies and no third-party requests has almost nothing for a policy to restrict, which is precisely why its absence went unnoticed, and it is still a missing enforcement of the claim this whole site is built on: `default-src 'self'` would make "no third-party requests" something your browser checks rather than something I assert.

**No analytics is running at all.** The plan is a cookieless counter. Right now the site loads no analytics of any kind, which is a stronger statement than "analytics without cookies", and it will become weaker on the day a counter is added. When that happens, this page will say so.

**The bibliography is the heaviest page, and it is where the budget breaks on one reading of it.** `/sources/` is 3.3 times the median page, and it is mostly generated from `data/sources.yaml`. Compressed it is 30,228 bytes, well inside the budget; raw it is 103,483, which is over the 100 KB line, as the table above records.

**The two `/sources/` blockers were closed while this page was being written**, which is worth recording rather than quietly deleting: the route for reporting an error is published, and so is the disclosure of which recommended tools its author actually runs. What was a defect in the last draft of this page is a sentence in this one.

## Carbon

An emissions figure cannot be measured from here, and inventing one would be the exact failure this site documents elsewhere. What can be done honestly is to apply a published model by hand, name it, and show the arithmetic so you can check it.

The Sustainable Web Design model gives energy intensities per gigabyte transferred, split by segment, and a default grid intensity of 494 grams of CO2e per kilowatt hour, which is the global average for electricity. {{< cite "swd-emissions-model" >}} Its constants add up like this:

- operational: 0.055 kWh/GB for data centres, 0.059 for networks, 0.080 for user devices
- embodied: 0.012, 0.013 and 0.081 kWh/GB for the same three segments
- total: **0.300 kWh/GB**, which at 494 gCO2e/kWh is **148 grams of CO2e per gigabyte** transferred

The median page here transfers 9,171 bytes gzipped, which is 0.0000085 GB, so:

> 0.0000085 GB × 148 gCO2e/GB = **0.0013 grams**, about 1.3 milligrams per page view

The heaviest page works out at about 4.2 milligrams, and reading every page on the site once comes to roughly 15 milligrams.

These three figures use the local gzip measurement, which is the reproducible one. The host sends about 3% more than that, as the section above records, which would move them to roughly 1.3, 4.3 and 16 milligrams. The difference is small enough to be within the model's own error, and it is printed here rather than quietly applied so that both readings are on the page.

Three things about that number, because it is easy to overread. It is **an estimate from a model, not a measurement**. About a third of it is *embodied* emissions, the cost of manufacturing the devices and networks in the first place, which no website controls and no website can reduce by being lighter. And the grid intensity is a global average: on a grid that is cleaner or dirtier than that, the figure moves, which is why the model's own documentation tells you to substitute your own.

For scale, the honest comparison is not with other websites but with almost anything else you could do in the same second. A single page view at this weight is not the interesting number. A page that loads four megabytes of video to show you a paragraph is.

## Why publish this

Because it is checkable, and because a site arguing that claims should be checkable does not get to exempt itself.

There is a second reason, and it is the uncomfortable one. The figures above are not spectacular. Zero third-party requests is unusual; 30 kilobytes is unremarkable; and the failures listed further up are real ones, including two accessibility defects and a missing `content-security-policy` on a site whose claim a policy could enforce. A page that published only the flattering half of this would be marketing, and this site's whole argument is that marketing is what the rest of the web already does.

Every site could publish this page. Every browser has a Network panel; every server has logs; every platform will show you the file sizes. The tools are not scarce. What is scarce is the willingness to publish the numbers when they are not good, which is why almost nobody does.

{{< source-list >}}
