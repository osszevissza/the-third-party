+++
title = "Receipts"
subtitle = "This site's own numbers, measured, including the ones that are not flattering"
description = "What this site loads, what it weighs, what it sets on your device, what it emits, and what it cannot yet prove. Measured on 2026-10-14 against the build that includes this page."
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

The site is built with `sh scripts/build.sh`, which runs four checks and then renders `public/`. Every figure on this page was then read out of that built directory rather than estimated: file sizes, request counts, and the contrast ratios, which are computed from the actual colour values in `assets/css/main.css`.

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

Nothing in the site can set a cookie: there is no JavaScript and no server-side code to do it with. What cannot be checked yet is the response headers, because nothing is deployed. The host and the domain are both chosen, but no request to this site has been served by anything, so there is no header to read back and that is one of the failures listed below.

The site-wide row is rounded, unlike the per-page figures. Editing any page moves the aggregate rows by tens of bytes, including the edit that published these numbers, which is why this page dates them and rounds the one figure that would otherwise be wrong within a day. The per-page figures have no such problem: build the site yourself from the same source and you will get exactly the numbers above.

That is this site's number. The number for the median page on the web is measured every year by the HTTP Archive for its Web Almanac, and you should read it there rather than take a figure quoted here, because a figure copied into a page like this one is out of date within a year. {{< cite "web-almanac" >}}

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

**The canonical URL, the RSS link and the sitemap name the real domain, and nothing is published at it yet.** The placeholder went on 2026-10-14, when `hugo.toml` was pointed at `https://third-party.statichost.page/`. Every page's `rel=canonical`, the RSS `alternate` link on the home page and `sitemap.xml` now advertise the address the site is meant to live at, which is a decision rather than a mistake. The defect that remains is the deploy. The source is public on GitHub and the host is not connected to it, so until a first build is published those URLs serve nothing, and a search engine that finds them meanwhile has been told that the canonical copy of each page is somewhere it cannot fetch. That is the honest half of a one-line fix: the configuration is right and the hosting is not there.

**The name resolves, and that proves nothing, which is worth one sentence here.** `third-party.statichost.page` does have a DNS record today, pointing at the host. So does a name that cannot exist: `this-cannot-exist-9f2a.statichost.page` resolves to the same address and fails in the same way. Both refuse a TLS connection because neither has a certificate, since no site has been provisioned under either name. The record comes from a wildcard, so it is not evidence that anything is live at this address, and the check that would settle it is the one this site applies to its sources: open the page and read its own title.

**The hosting disclosure is a decision, not yet a measurement.** The site is meant to be served by statichost.eu, which builds it from the public repository, and there is no server of mine in the path. What this page cannot yet say is what that host does with a request: nothing is deployed, so no response header has been read back and there is no log to inspect. That line belongs to the first deploy, and until it is written the honest version of the claim is that a host has been chosen, not that its behaviour has been checked.

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

Three things about that number, because it is easy to overread. It is **an estimate from a model, not a measurement**. About a third of it is *embodied* emissions, the cost of manufacturing the devices and networks in the first place, which no website controls and no website can reduce by being lighter. And the grid intensity is a global average: on a grid that is cleaner or dirtier than that, the figure moves, which is why the model's own documentation tells you to substitute your own.

For scale, the honest comparison is not with other websites but with almost anything else you could do in the same second. A single page view at this weight is not the interesting number. A page that loads four megabytes of video to show you a paragraph is.

## Why publish this

Because it is checkable, and because a site arguing that claims should be checkable does not get to exempt itself.

There is a second reason, and it is the uncomfortable one. The figures above are not spectacular. Zero third-party requests is unusual; 30 kilobytes is unremarkable; and the failures listed further up are real ones, including two accessibility defects and a site configured for a domain that has nothing published at it yet. A page that published only the flattering half of this would be marketing, and this site's whole argument is that marketing is what the rest of the web already does.

Every site could publish this page. Every browser has a Network panel; every server has logs; every platform will show you the file sizes. The tools are not scarce. What is scarce is the willingness to publish the numbers when they are not good, which is why almost nobody does.

{{< source-list >}}
