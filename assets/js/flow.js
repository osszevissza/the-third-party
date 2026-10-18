/*
  flow.js: the one script the site ships, and everything it does is an addition.

  Two jobs:

  1. It adds d-run to the inline diagrams as they reach the viewport, which is what
     starts the CSS packet animation in main.css. Without a script the diagrams render
     complete and still.

  2. It builds the receipt on /one-page-load/: a small fixed card that fills in as the
     reader scrolls the request ledger. Every fact the card shows is already in the
     prose of the ledger; the card is a running summary and not a second copy of the
     content, and it can be dismissed, because a fixed un-dismissable box is the thing
     this site argues against.

  The rules this file serves (AGENT.md section 8):

  - The ledger prose is the source of truth. The script reads the ledger's own heading
    sequence and walks away if the count does not match what it expects, rather than
    summarise a page that has changed underneath it.
  - prefers-reduced-motion ends the whole file: the receipt is motion by construction.
  - Nothing leaves the browser: no fetch, no beacon, no storage, no third party.
*/

(function () {
  "use strict";

  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (!("IntersectionObserver" in window)) return;

  // --- 1. the diagrams ------------------------------------------------------
  // d-run is the class that lets the CSS animations start. Without JavaScript it is
  // never added, and a diagram that never animates is a complete diagram.

  var diagrams = document.querySelectorAll("figure.diagram svg");
  var dio = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("d-run");
        dio.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  diagrams.forEach(function (svg) { dio.observe(svg); });

  // --- 2. the receipt on /one-page-load/ ------------------------------------
  // One array per ledger heading, in page order. Each label is a compression of a fact
  // the prose states in full; the count is the count of this list, not a measurement
  // of anything, which is why the card never presents it as one.

  var LEDGER_ITEMS = [
    ["which hostname you asked for"],
    ["your IP address", "your User-Agent", "Accept-Language", "the Referer header"],
    ["a first-party cookie ID"],
    ["your IP and User-Agent, sent to a font company"],
    ["your viewport and screen size"],
    ["a request to the consent vendor"],
    ["an ad tag request"],
    ["your ID, matched to their ID"],
    ["one bid request, broadcast to every bidder"],
    ["device, user and geo, taken from your IP"],
    ["impression and conversion pixels"],
    ["your scrolling, hesitation and keystrokes"],
    ["embeds, each phoning home"],
    ["and you never clicked anything"]
  ];

  var wrap = document.querySelector("[data-flow-ledger]");
  if (!wrap) return;

  var steps = wrap.querySelectorAll("h3");
  if (steps.length !== LEDGER_ITEMS.length) return;

  var card = document.createElement("aside");
  card.className = "flow-receipt";
  card.hidden = true;

  var head = document.createElement("p");
  head.className = "flow-receipt-head";

  var label = document.createElement("span");
  label.className = "flow-receipt-label";
  label.textContent = "Left your browser so far";

  var chip = document.createElement("span");
  chip.className = "flow-receipt-count";
  chip.textContent = "0 items";

  head.appendChild(label);
  head.appendChild(chip);

  var close = document.createElement("button");
  close.type = "button";
  close.className = "flow-receipt-close";
  close.textContent = "Hide";
  head.appendChild(close);

  var list = document.createElement("ul");
  list.className = "flow-receipt-list";

  var latest = document.createElement("p");
  latest.className = "flow-receipt-latest";

  card.appendChild(head);
  card.appendChild(list);
  card.appendChild(latest);
  document.body.appendChild(card);

  // The "active" step is the one crossing a band just above the middle of the
  // viewport, which is where a reader is looking when they read a section.
  var stepIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) revealThrough(Number(entry.target.dataset.flowStep));
    });
  }, { rootMargin: "-35% 0px -55% 0px", threshold: 0 });

  steps.forEach(function (step, index) {
    step.dataset.flowStep = String(index);
    stepIO.observe(step);
  });

  // When the ledger has scrolled above the viewport the receipt goes away until the
  // reader comes back. A ledger not yet reached keeps the card hidden anyway.
  var wrapIO = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting && entry.boundingClientRect.top < 0) card.hidden = true;
    });
  }, { threshold: 0 });
  wrapIO.observe(wrap);

  close.addEventListener("click", function () {
    card.hidden = true;
    stepIO.disconnect();
    wrapIO.disconnect();
  });

  var revealed = -1;

  function revealThrough(stepIndex) {
    for (var s = revealed + 1; s <= stepIndex; s++) {
      LEDGER_ITEMS[s].forEach(function (text) {
        var li = document.createElement("li");
        li.textContent = text;
        list.appendChild(li);
      });
    }
    if (stepIndex > revealed) revealed = stepIndex;
    var count = list.children.length;
    chip.textContent = count + (count === 1 ? " item" : " items");
    latest.textContent = list.lastChild.textContent;
    if (card.hidden) card.hidden = false;
  }
})();
