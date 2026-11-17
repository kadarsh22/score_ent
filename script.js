'use strict';

// Both original videos are available without JavaScript; tabs progressively enhance them.
const tabs = [...document.querySelectorAll('[role="tab"]')];
const captions = {
  'tab-overview': 'From a collapsed subspace to diverse representations, while keeping views aligned.',
  'tab-explained': 'Follow the objective: align views, smooth the density, estimate the score, and update the encoder.'
};

function selectTab(selected) {
  tabs.forEach(tab => {
    const active = tab === selected;
    tab.setAttribute('aria-selected', String(active));
    tab.tabIndex = active ? 0 : -1;
    const panel = document.getElementById(tab.getAttribute('aria-controls'));
    if (!active) panel.querySelector('video').pause();
    panel.hidden = !active;
  });
  document.getElementById('demo-caption').textContent = captions[selected.id];
}

tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
    if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = tabs.length - 1;
    if (next === undefined) return;
    event.preventDefault();
    tabs[next].focus();
    selectTab(tabs[next]);
  });
});

selectTab(tabs[0]);

const copyButton = document.getElementById('copy-citation');
let statusTimer;
copyButton.addEventListener('click', async () => {
  const citation = document.getElementById('bibtex');
  const status = document.getElementById('copy-status');
  clearTimeout(statusTimer);
  try {
    if (!navigator.clipboard) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(citation.textContent.trim());
    copyButton.querySelector('span').textContent = 'Copied!';
    status.textContent = 'Citation copied to clipboard.';
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(citation);
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy, or download the .bib file below.';
  }
  statusTimer = setTimeout(() => {
    copyButton.querySelector('span').textContent = 'Copy citation';
    status.textContent = '';
  }, 7000);
});

if ('IntersectionObserver' in window) {
  const navLinks = [...document.querySelectorAll('nav a')];
  const sections = [...document.querySelectorAll('main section[id]')];
  const visibleSections = new Set();
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) visibleSections.add(entry.target.id);
      else visibleSections.delete(entry.target.id);
    });
    const current = sections.find(section => visibleSections.has(section.id));
    navLinks.forEach(link => {
      if (current && link.hash === `#${current.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
}
