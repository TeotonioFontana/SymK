import './styles.css';
import { project } from './project';
import type { Wave, WaveState } from './types';

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Application mount point not found.');

const stateLabel: Record<WaveState, string> = { complete: 'Completed', current: 'Awaiting decision', blocked: 'Blocked', planned: 'Planned' };
const storageKey = `${project.slug}:wave-checklist`;
const checked = new Set<string>(JSON.parse(localStorage.getItem(storageKey) ?? '[]') as string[]);
let selected = Number(location.hash.replace('#wave-', ''));
if (!project.waves.some((wave) => wave.id === selected)) selected = project.waves.find((wave) => wave.state === 'current')?.id ?? 0;

const escapeHtml = (value: string) => value.replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' })[character]!);
const visualState = (state: WaveState) => state === 'blocked' || state === 'planned' ? 'future' : state;

function waveCard(wave: Wave): string {
  return `<button class="wave ${wave.state} ${wave.id === selected ? 'selected' : ''}" data-wave="${wave.id}" aria-pressed="${wave.id === selected}">
    <span class="badge ${visualState(wave.state)}">${stateLabel[wave.state]}</span>
    <h3>Wave ${wave.id} · ${escapeHtml(wave.title)}</h3><p>${escapeHtml(wave.summary)}</p>
  </button>`;
}

function render(): void {
  const wave = project.waves.find((item) => item.id === selected)!;
  const done = wave.tasks.filter((_, index) => checked.has(`${wave.id}:${index}`)).length;
  const percent = wave.tasks.length ? Math.round(done / wave.tasks.length * 100) : wave.state === 'complete' ? 100 : 0;
  app!.innerHTML = `<main>
    <header class="topbar"><a class="back" href="/knowledge-engineering.html">← Knowledge Engineering</a><span class="version">SymK Web v0.2.0 · build 2</span></header>
    <p class="eyebrow">${escapeHtml(project.eyebrow)}</p><h1>${escapeHtml(project.name)}</h1><p class="lead">${escapeHtml(project.description)}</p>
    <aside class="notice"><strong>Current status: ${escapeHtml(project.statusTitle)}</strong><p>${escapeHtml(project.statusDetail)}</p></aside>
    <h2>Migration waves</h2><section class="waves" aria-label="Migration waves">${project.waves.map(waveCard).join('')}</section>
    <section class="workspace" aria-live="polite"><div class="workspace-header"><div><h2>Wave ${wave.id} · ${escapeHtml(wave.title)}</h2><p>${escapeHtml(wave.summary)}</p></div><span class="badge ${visualState(wave.state)}">${stateLabel[wave.state]}</span></div>
      <div class="progress" aria-label="Task progress"><span style="width:${percent}%"></span></div><p>${done} of ${wave.tasks.length} current tasks marked for local follow-up (${percent}%).</p>
      <div class="checklist">${wave.tasks.length ? wave.tasks.map((task, index) => `<label class="check"><input type="checkbox" data-task="${wave.id}:${index}" ${checked.has(`${wave.id}:${index}`) ? 'checked' : ''}><span>${escapeHtml(task)}</span></label>`).join('') : '<p class="empty">No actionable checklist is open for this wave.</p>'}</div>
    </section>
    <h2>Boundary</h2><aside class="boundary"><h3>${escapeHtml(project.boundaryTitle)}</h3><p>${escapeHtml(project.boundary)}</p></aside>
    <nav class="actions"><a class="action primary" href="${project.counterpartHref}">${escapeHtml(project.counterpartLabel)}</a><a class="action" href="/knowledge-engineering.html">Return to program</a></nav>
  </main>`;
  bind();
}

function bind(): void {
  document.querySelectorAll<HTMLElement>('[data-wave]').forEach((element) => element.addEventListener('click', () => {
    selected = Number(element.dataset.wave); history.replaceState(null, '', `#wave-${selected}`); render();
  }));
  document.querySelectorAll<HTMLInputElement>('[data-task]').forEach((input) => input.addEventListener('change', () => {
    const key = input.dataset.task!; input.checked ? checked.add(key) : checked.delete(key);
    localStorage.setItem(storageKey, JSON.stringify([...checked])); render();
  }));
}

render();
