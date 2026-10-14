import { copyReviewPrompt, esc, sectionHead, shell, timestamp, uid, type Tab } from './protocol-ui';

type View = 'registry' | 'authority' | 'escalation' | 'challenge' | 'access';
type Lifecycle = 'candidate' | 'active' | 'qualified' | 'suspended' | 'superseded' | 'rejected';
interface AuthorityBoundary { id: string; titleEn: string; holderEn: string; decisionClassEn: string; scopeEn: string; basisEn: string; limitationsEn: string; evidenceEn: string; status: Lifecycle; createdAt: string }
interface EscalationPath { id: string; triggerEn: string; fromRoleEn: string; toAuthorityEn: string; requiredRecordEn: string; deadlineEn: string; unresolvedDispositionEn: string; createdAt: string }
interface Challenge { id: string; targetEn: string; challengerEn: string; groundsEn: string; evidenceEn: string; requestedRemedyEn: string; responseAuthorityEn: string; state: 'submitted' | 'acknowledged' | 'under_review' | 'resolved' | 'deferred' | 'dismissed'; rationaleEn: string; createdAt: string }
interface AccessRestriction { id: string; resourceEn: string; protectedInterestEn: string; ruleEn: string; basisEn: string; affectedParticipantsEn: string; challengeRouteEn: string; reviewDate: string; status: Lifecycle; createdAt: string }
interface Workspace { schema: 'symk.authority.v1'; authorities: AuthorityBoundary[]; escalations: EscalationPath[]; challenges: Challenge[]; restrictions: AccessRestriction[] }

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Application mount point not found.');
const storeKey = 'knoe:symk:authority-challenge:v1';
const tabs: Tab[] = [
  { id: 'registry', number: '01', label: 'Browse boundaries and challenges' },
  { id: 'authority', number: '02', label: 'Define decision authority' },
  { id: 'escalation', number: '03', label: 'Define escalation paths' },
  { id: 'challenge', number: '04', label: 'Record a challenge' },
  { id: 'access', number: '05', label: 'Govern access restrictions' }
];

function seed(): Workspace {
  return { schema: 'symk.authority.v1', authorities: [{ id: 'SYMK-AUTH-001', titleEn: 'SymK protocol disposition authority', holderEn: 'Authorized SymK protocol steward', decisionClassEn: 'Disposition of SymK protocol propositions and protocol releases', scopeEn: 'The declared SymK jurisdiction and version only.', basisEn: 'Explicit project stewardship and the applicable ratified SymK governance record.', limitationsEn: 'No authority over Foundation discipline claims, Workbench operational policy, domain truth or external institutional decisions.', evidenceEn: 'Named decision record, rationale, applicable version and responsible identity.', status: 'candidate', createdAt: '2026-10-14T00:00:00.000Z' }], escalations: [], challenges: [], restrictions: [] };
}
function load(): Workspace { try { const parsed = JSON.parse(localStorage.getItem(storeKey) ?? 'null') as Workspace; if (parsed?.schema === 'symk.authority.v1') return parsed; } catch { /* use seed */ } const workspace = seed(); localStorage.setItem(storeKey, JSON.stringify(workspace)); return workspace; }

let workspace = load();
let view = (new URLSearchParams(location.search).get('view') as View) || 'registry';
if (!tabs.some(({ id }) => id === view)) view = 'registry';
let message = '';
let query = '';
const persist = () => localStorage.setItem(storeKey, JSON.stringify(workspace));
const total = () => workspace.authorities.length + workspace.escalations.length + workspace.challenges.length + workspace.restrictions.length;
const head = (number: string, title: string, description: string) => sectionHead(number, title, description, total(), 'governed');
const statusClass = (status: string) => ['active', 'resolved'].includes(status) ? 'accepted' : status === 'rejected' || status === 'dismissed' ? 'rejected' : '';
const values = (form: HTMLFormElement) => Object.fromEntries(new FormData(form).entries()) as Record<string, string>;

function render(): void {
  const body = view === 'registry' ? registryView() : view === 'authority' ? authorityView() : view === 'escalation' ? escalationView() : view === 'challenge' ? challengeView() : accessView();
  app!.innerHTML = shell({ title: 'Authority and challenge', eyebrow: 'Authority boundary · contestable protocol governance', lead: 'Declare who may decide what, how unresolved matters escalate, how decisions may be challenged, and when access restrictions are legitimate.', boundary: 'Authority must be explicit, scoped, attributable, reviewable and challengeable. Neither expertise, authorship, technical capability, directory placement nor system access grants decision authority by itself.', version: 'Authority and Challenge v0.1.0 · build 1', tabs, active: view, message, body });
  bindShell(); bindView();
}

function registryView(): string {
  const normalized = query.trim().toLowerCase();
  const cards = [
    ...workspace.authorities.map((item) => ({ type: 'Authority boundary', id: item.id, title: item.titleEn, body: `${item.holderEn} · ${item.scopeEn}`, state: item.status })),
    ...workspace.escalations.map((item) => ({ type: 'Escalation path', id: item.id, title: item.triggerEn, body: `${item.fromRoleEn} → ${item.toAuthorityEn}`, state: 'recorded' })),
    ...workspace.challenges.map((item) => ({ type: 'Challenge', id: item.id, title: item.targetEn, body: `${item.challengerEn} · ${item.groundsEn}`, state: item.state })),
    ...workspace.restrictions.map((item) => ({ type: 'Access restriction', id: item.id, title: item.resourceEn, body: `${item.ruleEn} · ${item.basisEn}`, state: item.status }))
  ].filter((item) => !normalized || JSON.stringify(item).toLowerCase().includes(normalized));
  return `${head('01', 'Browse authority, escalation, challenge and access records', 'Inspect every authority-related record class together while preserving their distinct meanings.')}
    <section class="operation"><div class="filters"><label>Search<input id="query" value="${esc(query)}" placeholder="ID, holder, target, grounds or scope"></label></div><div class="records">${cards.map((item) => `<article class="record"><div class="record-meta"><strong>${esc(item.id)}</strong><span class="status ${statusClass(item.state)}">${esc(item.state)}</span></div><h3>${esc(item.title)}</h3><p>${esc(item.body)}</p><small>${esc(item.type)}</small></article>`).join('') || '<p class="empty">No governed records match the search.</p>'}</div><div class="form-actions"><button class="button" id="copy-review" type="button">Copy cross-record review prompt</button></div></section>`;
}

function authorityView(): string {
  return `${head('02', 'Define decision authority', 'Register a candidate authority boundary with an explicit basis, scope, limitation and evidence requirement.')}
    <section class="operation"><form id="authority-form" class="form-grid"><label>Stable candidate ID<input name="id" required placeholder="SYMK-AUTH-002"></label><label>Boundary title<input name="titleEn" required></label><label>Authority holder or role<input name="holderEn" required></label><label>Decision class<input name="decisionClassEn" required></label><label class="full">Scope<textarea name="scopeEn" required></textarea></label><label>Authority basis<textarea name="basisEn" required></textarea></label><label>Limitations<textarea name="limitationsEn" required></textarea></label><label class="full">Required decision evidence<textarea name="evidenceEn" required></textarea></label><div class="form-actions"><button class="button" type="submit">Register candidate boundary</button><button class="button secondary" id="authority-prompt" type="button">Copy boundary-review prompt</button></div></form>
    <div class="records">${workspace.authorities.map((item) => `<article class="record"><div class="record-meta"><strong>${item.id}</strong><span class="status ${statusClass(item.status)}">${item.status}</span></div><h3>${esc(item.titleEn)}</h3><p>${esc(item.holderEn)} may decide ${esc(item.decisionClassEn)} within ${esc(item.scopeEn)}</p><small>Limitation: ${esc(item.limitationsEn)}</small></article>`).join('')}</div></section>`;
}

function escalationView(): string {
  return `${head('03', 'Define escalation paths', 'Declare the trigger, destination, required record, timing and safe unresolved disposition.')}
    <section class="operation"><form id="escalation-form" class="form-grid"><label>Trigger condition<textarea name="triggerEn" required></textarea></label><label>Originating role or participant<input name="fromRoleEn" required></label><label>Escalation destination<input name="toAuthorityEn" required></label><label>Required record or evidence<input name="requiredRecordEn" required></label><label>Response deadline or timing rule<input name="deadlineEn" required></label><label>Disposition if unresolved<input name="unresolvedDispositionEn" required></label><div class="form-actions"><button class="button" type="submit">Record escalation path</button></div></form>
    <table class="matrix"><thead><tr><th>Trigger</th><th>Path</th><th>Required record</th><th>Unresolved disposition</th></tr></thead><tbody>${workspace.escalations.map((item) => `<tr><td>${esc(item.triggerEn)}</td><td>${esc(item.fromRoleEn)} → ${esc(item.toAuthorityEn)}</td><td>${esc(item.requiredRecordEn)} · ${esc(item.deadlineEn)}</td><td>${esc(item.unresolvedDispositionEn)}</td></tr>`).join('') || '<tr><td colspan="4">No escalation paths recorded.</td></tr>'}</tbody></table></section>`;
}

function challengeView(): string {
  return `${head('04', 'Record a challenge', 'Preserve a contestation, its grounds and evidence without assuming that challenge or response authority decides the merits.')}
    <section class="operation"><form id="challenge-form" class="form-grid"><label>Target claim, decision or restriction<input name="targetEn" required></label><label>Challenger identity or role<input name="challengerEn" required></label><label>Grounds<textarea name="groundsEn" required></textarea></label><label>Evidence or pointer<textarea name="evidenceEn" required></textarea></label><label>Requested remedy<input name="requestedRemedyEn" required></label><label>Responsible response authority<input name="responseAuthorityEn" required></label><label>State<select name="state"><option value="submitted">Submitted</option><option value="acknowledged">Acknowledged</option><option value="under_review">Under review</option><option value="resolved">Resolved</option><option value="deferred">Deferred</option><option value="dismissed">Dismissed</option></select></label><label>Current rationale or qualification<textarea name="rationaleEn" required></textarea></label><div class="form-actions"><button class="button" type="submit">Record challenge</button></div></form>
    <div class="records">${workspace.challenges.map((item) => `<article class="record"><div class="record-meta"><strong>${item.id}</strong><span class="status ${statusClass(item.state)}">${item.state}</span></div><h3>${esc(item.targetEn)}</h3><p>${esc(item.challengerEn)}: ${esc(item.groundsEn)}</p><small>Requested remedy: ${esc(item.requestedRemedyEn)} · Response authority: ${esc(item.responseAuthorityEn)}</small></article>`).join('') || '<p class="empty">No challenges recorded.</p>'}</div></section>`;
}

function accessView(): string {
  return `${head('05', 'Govern legitimate access restrictions', 'Record the protected interest, rule, basis, affected participants, review date and challenge route.')}
    <section class="operation"><form id="access-form" class="form-grid"><label>Protected resource or evidence<input name="resourceEn" required></label><label>Protected legitimate interest<input name="protectedInterestEn" required></label><label class="full">Restriction rule<textarea name="ruleEn" required></textarea></label><label>Legal, ethical or protocol basis<textarea name="basisEn" required></textarea></label><label>Affected participants<textarea name="affectedParticipantsEn" required></textarea></label><label>Challenge or exception route<input name="challengeRouteEn" required></label><label>Mandatory review date<input name="reviewDate" type="date" required></label><div class="form-actions"><button class="button" type="submit">Register candidate restriction</button><button class="button secondary" id="restriction-prompt" type="button">Copy proportionality-review prompt</button></div></form>
    <div class="records">${workspace.restrictions.map((item) => `<article class="record"><div class="record-meta"><strong>${item.id}</strong><span class="status ${statusClass(item.status)}">${item.status}</span></div><h3>${esc(item.resourceEn)}</h3><p>${esc(item.ruleEn)}</p><small>Basis: ${esc(item.basisEn)} · Review: ${esc(item.reviewDate)} · Challenge: ${esc(item.challengeRouteEn)}</small></article>`).join('') || '<p class="empty">No access restrictions recorded.</p>'}</div></section>`;
}

function bindShell(): void { document.querySelectorAll<HTMLButtonElement>('[data-tab]').forEach((button) => button.addEventListener('click', () => { view = button.dataset.tab as View; message = ''; history.replaceState(null, '', `authority.html?view=${view}`); render(); })); }
function bindView(): void {
  document.querySelector<HTMLInputElement>('#query')?.addEventListener('input', (event) => { query = (event.currentTarget as HTMLInputElement).value; render(); });
  document.querySelector<HTMLButtonElement>('#copy-review')?.addEventListener('click', async () => { const ok = await copyReviewPrompt(`Review this SymK authority-and-challenge registry for gaps, conflicts, overlaps and authority leakage. Distinguish protocol authority from Foundation, Workbench, domain and external authority. Verify escalation, contestability, evidence and access-review obligations.\n\n${JSON.stringify(workspace, null, 2)}`); message = ok ? 'Cross-record review prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLButtonElement>('#authority-prompt')?.addEventListener('click', async () => { const ok = await copyReviewPrompt('Help define a candidate SymK decision-authority boundary in English. Require a named holder or role, decision class, jurisdiction, scope, authority basis, limitations, evidence, challenge route, escalation and counterexamples. Expertise, authorship, system access and technical capability must not be treated as authority by themselves.'); message = ok ? 'Boundary-review prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLButtonElement>('#restriction-prompt')?.addEventListener('click', async () => { const ok = await copyReviewPrompt(`Assess these candidate SymK access restrictions for necessity, proportionality, least privilege, time limitation, affected participants, exception handling and contestability. Access restrictions must not erase evidence or shield authority from legitimate challenge.\n\n${JSON.stringify(workspace.restrictions, null, 2)}`); message = ok ? 'Proportionality-review prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLFormElement>('#authority-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); if (workspace.authorities.some(({ id }) => id === data.id.trim())) { message = 'That stable ID already exists.'; render(); return; } workspace.authorities.push({ id: data.id.trim(), titleEn: data.titleEn.trim(), holderEn: data.holderEn.trim(), decisionClassEn: data.decisionClassEn.trim(), scopeEn: data.scopeEn.trim(), basisEn: data.basisEn.trim(), limitationsEn: data.limitationsEn.trim(), evidenceEn: data.evidenceEn.trim(), status: 'candidate', createdAt: timestamp() }); persist(); message = 'Candidate authority boundary registered; no authority was granted.'; render(); });
  document.querySelector<HTMLFormElement>('#escalation-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); workspace.escalations.push({ id: uid('SYMK-ESC'), triggerEn: data.triggerEn.trim(), fromRoleEn: data.fromRoleEn.trim(), toAuthorityEn: data.toAuthorityEn.trim(), requiredRecordEn: data.requiredRecordEn.trim(), deadlineEn: data.deadlineEn.trim(), unresolvedDispositionEn: data.unresolvedDispositionEn.trim(), createdAt: timestamp() }); persist(); message = 'Escalation path recorded.'; render(); });
  document.querySelector<HTMLFormElement>('#challenge-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); workspace.challenges.push({ id: uid('SYMK-CH'), targetEn: data.targetEn.trim(), challengerEn: data.challengerEn.trim(), groundsEn: data.groundsEn.trim(), evidenceEn: data.evidenceEn.trim(), requestedRemedyEn: data.requestedRemedyEn.trim(), responseAuthorityEn: data.responseAuthorityEn.trim(), state: data.state as Challenge['state'], rationaleEn: data.rationaleEn.trim(), createdAt: timestamp() }); persist(); message = 'Challenge recorded without predetermining its merits.'; render(); });
  document.querySelector<HTMLFormElement>('#access-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); workspace.restrictions.push({ id: uid('SYMK-AR'), resourceEn: data.resourceEn.trim(), protectedInterestEn: data.protectedInterestEn.trim(), ruleEn: data.ruleEn.trim(), basisEn: data.basisEn.trim(), affectedParticipantsEn: data.affectedParticipantsEn.trim(), challengeRouteEn: data.challengeRouteEn.trim(), reviewDate: data.reviewDate, status: 'candidate', createdAt: timestamp() }); persist(); message = 'Candidate access restriction registered with a review date and challenge route.'; render(); });
}

render();
