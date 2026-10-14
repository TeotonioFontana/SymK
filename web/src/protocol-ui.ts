import './protocol-management.css';

export interface Tab { id: string; number: string; label: string }
export const esc = (value: string) => value.replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[character]!);
export const timestamp = () => new Date().toISOString();
export const uid = (prefix: string) => `${prefix}-${crypto.randomUUID().slice(0, 8).toUpperCase()}`;

export async function copyReviewPrompt(text: string): Promise<boolean> {
  try { await navigator.clipboard.writeText(text); return true; } catch { return false; }
}

export function shell(options: {
  title: string; eyebrow: string; lead: string; boundary: string; version: string;
  tabs: Tab[]; active: string; message: string; body: string;
}): string {
  return `<main class="protocol-app">
    <header class="topbar"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/knowledge-engineering.html">Knowledge Engineering</a><span>›</span><a href="management.html">SymK Management</a><span>›</span><a href="management-protocol.html">Protocol governance</a><span>›</span><strong>${esc(options.title)}</strong></nav><span class="version">${esc(options.version)}</span></header>
    <p class="eyebrow">${esc(options.eyebrow)}</p><h1>${esc(options.title)}</h1><p class="lead">${esc(options.lead)}</p>
    <aside class="boundary"><strong>Protocol boundary</strong><p>${esc(options.boundary)}</p></aside>
    <nav class="tabs" aria-label="Management operations">${options.tabs.map((tab) => `<button type="button" data-tab="${tab.id}" class="${tab.id === options.active ? 'active' : ''}"><span>${tab.number}</span>${esc(tab.label)}</button>`).join('')}</nav>
    ${options.message ? `<div class="message" role="status">${esc(options.message)}</div>` : ''}${options.body}
    <nav class="actions"><a class="button secondary" href="management-protocol.html">Back to Protocol governance</a><a class="button secondary" href="management.html">All SymK groups</a><a class="button secondary" href="/symk/">Migration workspace</a></nav>
  </main>`;
}

export function sectionHead(number: string, title: string, description: string, count: number, noun: string): string {
  return `<section class="head"><div><p class="eyebrow">Function ${esc(number)}</p><h2>${esc(title)}</h2><p>${esc(description)}</p></div><strong>${count} ${esc(noun)} record(s)</strong></section>`;
}
