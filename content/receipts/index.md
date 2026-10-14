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

Every other page here asks you to check its sources. This one turns the same standard on the site itself, and it is deliberately nothing but numbers: what a page load costs, what the host sends, what could not be measured, what is broken, and what it emits.

## How these numbers were taken

The site is built with `sh scripts/build.sh`, which runs four checks and then renders `public/`. The figures below were read out of that built directory rather than estimated, except those under "What the host sends", which were taken from the live site with `curl`. The served sizes are always a little larger than the local ones, because the host compresses at a looser setting, so the local `gzip -9` figures are the ones you can rebuild and check.

The median row leaves this page out on purpose. A page that is part of a statistic changes it whenever it is edited, so a median including this one could never be exactly right for the page reporting it.

## What one page load costs

| | Measured | This site's budget | |
|---|---|---|---|
| Requests, per page | 3 (the document, one stylesheet, one icon) | under 20 | met |
| Requests to other companies | 0 | 0 | met |
| Scripts | 0 | | met |
| Cookies | 0 | 0 | met |
| Web fonts | 0, system font stack | | met |
| Median of the other 11 pages, gzipped | 9,221 bytes | under 100 KB | met |
| Heaviest page, gzipped | 30,288 bytes (`/sources/`) | under 100 KB | met |
| Heaviest page, raw | 103,681 bytes (`/sources/`) | 100 KB, measured transferred | **over as raw bytes** |
| All 12 pages, gzipped | about 108 KB | | |

The raw row is the one place the budget does not hold. The budget is about what a page costs a reader, and what actually crosses the wire is compressed: 30,288 bytes, comfortably inside. Read as raw bytes, the heaviest page is 103,681, which is over 100 KB whether you read KB as 1,000 bytes or as 1,024, and no other page comes close, since the median is 25,927 bytes raw. Both numbers are printed because the honest answer depends on which one the budget is about.

The site-wide row is rounded, unlike the others, because it is defined as all twelve pages and so includes this page's own bytes. The per-page figures have no such problem: build the site from the same source and you get exactly the numbers above.

That is this site's number. For the median page on the web, read the HTTP Archive's Web Almanac rather than a figure copied into a page like this one, which is out of date within a year. {{< cite "web-almanac" >}}

## What the host sends

Taken with `curl` against the live site on 2026-10-14.

- **The server identifies itself as `statichost.eu`**, and it discriminates: a path that cannot exist returns `404` with a 13-byte body while a real page returns `200`. That is the same control probe this site applies to its sources, and it is why a status code from this host is worth reading.
- **HTTP/2 and HTTP/3 both work**, the second verified over QUIC rather than inferred from the `alt-svc` header.
- **TLS is a Let's Encrypt certificate for this hostname alone**, issued at 18:34 UTC on the day the site went up and valid until 12 January 2027.
- **These headers are present:** `strict-transport-security: max-age=31536000; includeSubDomains; preload`, `x-content-type-options: nosniff`, `cache-control: public, max-age=0, must-revalidate`, an `etag`, `last-modified` and `vary: Accept-Encoding`.
- **These headers are absent:** `content-security-policy`, `referrer-policy`, `permissions-policy` and `x-frame-options`. The first of those is a defect, and it is listed below with the others.
- **Compression is gzip, with no brotli**, at a looser setting than the local figures assume, which is where the roughly 3% difference above comes from. The icon is sent uncompressed.
- **Publishing is hand-triggered**, from the host's dashboard rather than by a push, so the site can sit a commit or two behind the repository. If a page here disagrees with the source on GitHub, the source is the newer of the two.
- **What the host logs is not observable from outside**, and this page does not claim to know. The disclosure on [Sources](/sources/) says there is no server of mine in the path, which is a statement about architecture rather than about logs.

## What could not be measured

**Largest Contentful Paint.** The budget says under 1.5 seconds. Measuring it needs a real browser loading the page, the browser on this machine cannot be started from the environment these numbers were taken in, and no headless audit tooling is installed. So it stays a target rather than a result, and it is the easiest thing on this page for somebody else to settle.

**No accessibility audit tool has been run**, because Lighthouse, axe and WAVE all need a browser or a third-party service. **This site therefore does not have a verified WCAG AA result.** What can be checked without one is checked: one `h1` per page, a language declared on the `html` element, a skip link before the navigation, no images and so no missing alt text, no JavaScript and so no keyboard traps, defined focus styles, and `prefers-reduced-motion` honoured. Contrast is computed from the actual colour values rather than trusted: the lowest ratio anywhere is 6.66:1, and every pair passes 4.5:1 in both colour schemes.

**The request count comes from the markup, not from a browser.** A real Network panel might show fewer requests, if something is cached, or one more, if your browser retries the icon. It cannot show a request to another company, because there is none in the markup to make.

**The HTML has not been validated.** The W3C validator is a third-party service, and running it is somebody else's five minutes.

## Known failures

Every item is a real defect, dated 2026-10-14.

**Foreign language text is not marked as such, which fails WCAG 3.1.2.** The bibliography carries French, German and Dutch titles and the prose quotes phrases in other languages, but every page declares exactly one `lang` attribute, on the `html` element, so a screen reader will read *Outil d'auto-évaluation* in an English voice.

**Citation markers are small targets, a borderline failure of WCAG 2.5.8.** At 0.75em with no line box the clickable area is a few pixels high. WCAG exempts targets set inline in a sentence and these are, so the site is arguably compliant, and it is still the weakest point here for anybody with a tremor.

**There is no `content-security-policy`.** This is the defect worth fixing first: a policy of `default-src 'self'` would make "no third-party requests" something your browser checks rather than something I assert.

**No analytics is running at all.** The plan is a cookieless counter. What the site loads today is nothing, which is a stronger statement than "analytics without cookies" and will become weaker on the day a counter is added.

## Carbon

An emissions figure cannot be measured from here, so this is a published model applied by hand, named, with its arithmetic shown. The Sustainable Web Design model gives 0.300 kWh/GB across data centres, networks and user devices, and a default grid intensity of 494 grams of CO2e per kilowatt hour, which is the global average. {{< cite "swd-emissions-model" >}}

The median page transfers 9,221 bytes gzipped, which is 0.0000086 GB, so **0.0013 grams**, about 1.3 milligrams per page view. The heaviest page works out at about 4.2 milligrams, and reading every page on the site once comes to roughly 15 milligrams. It is an estimate from a model and not a measurement, about a third of it is embodied emissions that no website can reduce by being lighter, and the grid intensity is a global average which the model itself tells you to replace with your own.

{{< source-list >}}
