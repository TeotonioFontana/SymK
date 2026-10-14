import { copyReviewPrompt, esc, sectionHead, shell, timestamp, uid, type Tab } from './protocol-ui';

type View = 'registry' | 'author' | 'combinations' | 'handoffs' | 'accountability';
type Status = 'candidate' | 'under_review' | 'accepted' | 'qualified' | 'rejected' | 'deprecated';
type RecordClass = 'participant_kind' | 'role';

interface DefinitionRecord {
  id: string; recordClass: RecordClass; nameEn: string; definitionEn: string; capabilitiesEn: string;
  limitationsEn: string; sourceEn: string; rationaleEn: string; status: Status; version: number; createdAt: string;
}
interface Combination { id: string; leftRoleId: string; rightRoleId: string; relation: 'compatible' | 'conditional' | 'incompatible'; conditionEn: string; rationaleEn: string; createdAt: string }
interface Handoff { id: string; fromParticipantEn: string; fromRoleId: string; toParticipantEn: string; toRoleId: string; contributionEn: string; governedObjectEn: string; acceptanceCriteriaEn: string; evidenceEn: string; state: 'proposed' | 'offered' | 'accepted' | 'returned' | 'completed'; createdAt: string }
interface Accountability { id: string; participantEn: string; roleId: string; accountableToEn: string; obligationEn: string; evidenceRequirementEn: string; limitationEn: string; createdAt: string }
interface Workspace { schema: 'symk.roles.v1'; definitions: DefinitionRecord[]; combinations: Combination[]; handoffs: Handoff[]; accountability: Accountability[] }

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Application mount point not found.');
const storeKey = 'knoe:symk:roles-participants:v1';
const tabs: Tab[] = [
  { id: 'registry', number: '01', label: 'Browse participant kinds and roles' },
  { id: 'author', number: '02', label: 'Create a governed definition' },
  { id: 'combinations', number: '03', label: 'Govern role combinations' },
  { id: 'handoffs', number: '04', label: 'Record contributions and handoffs' },
  { id: 'accountability', number: '05', label: 'Assign accountability obligations' }
];
const statusLabels: Record<Status, string> = { candidate: 'Candidate', under_review: 'Under review', accepted: 'Accepted', qualified: 'Qualified', rejected: 'Rejected', deprecated: 'Deprecated' };

function seed(): Workspace {
  const createdAt = '2026-10-14T00:00:00.000Z';
  const definitions: DefinitionRecord[] = [
    { id: 'SYMK-PK-001', recordClass: 'participant_kind', nameEn: 'Human participant', definitionEn: 'A natural person participating in a declared cooperation context.', capabilitiesEn: 'Can interpret, deliberate, challenge, decide and assume responsibility when legitimately authorized.', limitationsEn: 'Human identity alone does not confer decision authority or domain competence.', sourceEn: 'SymK cooperation-role migration seed', rationaleEn: 'Required to distinguish participant kind from assigned role.', status: 'candidate', version: 1, createdAt },
    { id: 'SYMK-PK-002', recordClass: 'participant_kind', nameEn: 'Artificial participant', definitionEn: 'An artificial system participating through declared capabilities, constraints and accountable supervision.', capabilitiesEn: 'Can produce, transform, compare or inspect artifacts within its granted scope.', limitationsEn: 'Must not silently claim authority, identity, competence or accountability reserved to another participant.', sourceEn: 'SymK cooperation-role migration seed', rationaleEn: 'Preserves observability and responsibility boundaries.', status: 'candidate', version: 1, createdAt },
    { id: 'SYMK-R-001', recordClass: 'role', nameEn: 'Proposer', definitionEn: 'Introduces a proposition, artifact or change for governed consideration.', capabilitiesEn: 'May submit and explain a proposal.', limitationsEn: 'Proposal authorship does not imply approval authority.', sourceEn: 'SymK proposition lifecycle', rationaleEn: 'Separates authorship from review and authority.', status: 'candidate', version: 1, createdAt },
    { id: 'SYMK-R-002', recordClass: 'role', nameEn: 'Reviewer', definitionEn: 'Examines a governed object against declared criteria and records findings.', capabilitiesEn: 'May confirm, qualify, contest or recommend disposition.', limitationsEn: 'Review does not itself enact a decision unless authority is separately granted.', sourceEn: 'SymK proposition lifecycle', rationaleEn: 'Preserves review as an inspectable contribution.', status: 'candidate', version: 1, createdAt },
    { id: 'SYMK-R-003', recordClass: 'role', nameEn: 'Challenger', definitionEn: 'Raises a reasoned contestation against a claim, decision, handoff or restriction.', capabilitiesEn: 'May submit grounds, evidence and requested remedy.', limitationsEn: 'Challenge rights do not guarantee the requested disposition.', sourceEn: 'SymK challenge obligation', rationaleEn: 'Makes dissent observable without confusing it with authority.', status: 'candidate', version: 1, createdAt }
  ];
  return { schema: 'symk.roles.v1', definitions, combinations: [], handoffs: [], accountability: [] };
}

function load(): Workspace {
  try { const parsed = JSON.parse(localStorage.getItem(storeKey) ?? 'null') as Workspace; if (parsed?.schema === 'symk.roles.v1') return parsed; } catch { /* use seed */ }
  const workspace = seed(); localStorage.setItem(storeKey, JSON.stringify(workspace)); return workspace;
}

let workspace = load();
let view = (new URLSearchParams(location.search).get('view') as View) || 'registry';
if (!tabs.some(({ id }) => id === view)) view = 'registry';
let selectedId = workspace.definitions[0]?.id ?? '';
let query = '';
let classFilter: 'all' | RecordClass = 'all';
let message = '';
const persist = () => localStorage.setItem(storeKey, JSON.stringify(workspace));
const roles = () => workspace.definitions.filter(({ recordClass }) => recordClass === 'role');

function head(number: string, title: string, description: string): string {
  const total = workspace.definitions.length + workspace.combinations.length + workspace.handoffs.length + workspace.accountability.length;
  return sectionHead(number, title, description, total, 'governed');
}
function roleOptions(selected = ''): string { return roles().map((item) => `<option value="${item.id}" ${selected === item.id ? 'selected' : ''}>${esc(item.id)} · ${esc(item.nameEn)}</option>`).join(''); }
function record(id: string) { return workspace.definitions.find((item) => item.id === id); }

function render(): void {
  const body = view === 'registry' ? registryView() : view === 'author' ? authorView() : view === 'combinations' ? combinationsView() : view === 'handoffs' ? handoffsView() : accountabilityView();
  app!.innerHTML = shell({ title: 'Roles and participants', eyebrow: 'Cooperation structure · governed role semantics', lead: 'Define who or what may participate, which roles can coexist, what was contributed or handed off, and who remains answerable for an obligation.', boundary: 'Participant kind, role, competence, authority and accountability are distinct. Registering a participant or role never grants authority, proves competence or transfers responsibility by itself.', version: 'Roles and Participants v0.1.0 · build 1', tabs, active: view, message, body });
  bindShell(); bindView();
}

function registryView(): string {
  const normalized = query.toLowerCase().trim();
  const visible = workspace.definitions.filter((item) => (classFilter === 'all' || item.recordClass === classFilter) && (!normalized || JSON.stringify(item).toLowerCase().includes(normalized)));
  const selected = record(selectedId);
  return `${head('01', 'Browse participant kinds and roles', 'Inspect the governed definitions without conflating a participant kind with a role assignment.')}
    <section class="operation"><div class="filters"><label>Search<input id="query" value="${esc(query)}" placeholder="ID, name, capability or limitation"></label><label>Record class<select id="class-filter"><option value="all">All classes</option><option value="participant_kind" ${classFilter === 'participant_kind' ? 'selected' : ''}>Participant kinds</option><option value="role" ${classFilter === 'role' ? 'selected' : ''}>Roles</option></select></label></div>
    <div class="records">${visible.map((item) => `<article class="record ${item.id === selectedId ? 'selected' : ''}"><div class="record-meta"><strong>${esc(item.id)} · v${item.version}</strong><span class="status ${item.status}">${statusLabels[item.status]}</span></div><h3>${esc(item.nameEn)}</h3><p>${esc(item.definitionEn)}</p><small>${item.recordClass === 'role' ? 'Role' : 'Participant kind'} · ${esc(item.sourceEn)}</small><button class="button secondary" data-select="${item.id}">Inspect</button></article>`).join('') || '<p class="empty">No definitions match these filters.</p>'}</div>
    ${selected ? `<article class="detail"><h3>${esc(selected.id)} · ${esc(selected.nameEn)}</h3><dl><div><dt>Capabilities</dt><dd>${esc(selected.capabilitiesEn)}</dd></div><div><dt>Limitations</dt><dd>${esc(selected.limitationsEn)}</dd></div><div><dt>Rationale</dt><dd>${esc(selected.rationaleEn)}</dd></div></dl><button class="button" id="copy-review">Copy collaborative review prompt</button></article>` : ''}</section>`;
}

function authorView(): string {
  return `${head('02', 'Create a governed definition', 'Create an English-language candidate with an explicit source, scope and limitation. New records remain candidates.')}
    <section class="operation"><form id="definition-form" class="form-grid"><label>Record class<select name="recordClass" required><option value="participant_kind">Participant kind</option><option value="role">Role</option></select></label><label>Stable candidate ID<input name="id" required placeholder="SYMK-R-004"></label><label class="full">Name<input name="nameEn" required></label><label class="full">Human definition<textarea name="definitionEn" required></textarea></label><label>Capabilities<textarea name="capabilitiesEn" required></textarea></label><label>Limitations<textarea name="limitationsEn" required></textarea></label><label>Source or provenance<input name="sourceEn" required></label><label>Rationale for introducing this definition<textarea name="rationaleEn" required></textarea></label><div class="form-actions"><button class="button" type="submit">Register candidate</button><button class="button secondary" id="draft-prompt" type="button">Copy authoring prompt</button></div></form></section>`;
}

function combinationsView(): string {
  return `${head('03', 'Govern role combinations', 'Record whether two roles may be held together and under which observable conditions.')}
    <section class="operation"><form id="combination-form" class="form-grid"><label>First role<select name="leftRoleId" required><option value="">Select…</option>${roleOptions()}</select></label><label>Second role<select name="rightRoleId" required><option value="">Select…</option>${roleOptions()}</select></label><label>Relationship<select name="relation" required><option value="compatible">Compatible</option><option value="conditional">Conditionally compatible</option><option value="incompatible">Incompatible</option></select></label><label>Condition or safeguard<input name="conditionEn" required placeholder="Separation, disclosure or independent review requirement"></label><label class="full">Rationale<textarea name="rationaleEn" required></textarea></label><div class="form-actions"><button class="button" type="submit">Record combination rule</button></div></form>
    <table class="matrix"><thead><tr><th>Roles</th><th>Relationship</th><th>Condition</th><th>Rationale</th></tr></thead><tbody>${workspace.combinations.map((item) => `<tr><td>${esc(record(item.leftRoleId)?.nameEn ?? item.leftRoleId)} ↔ ${esc(record(item.rightRoleId)?.nameEn ?? item.rightRoleId)}</td><td>${esc(item.relation)}</td><td>${esc(item.conditionEn)}</td><td>${esc(item.rationaleEn)}</td></tr>`).join('') || '<tr><td colspan="4">No combination rules recorded.</td></tr>'}</tbody></table></section>`;
}

function handoffsView(): string {
  return `${head('04', 'Record contributions and handoffs', 'Preserve what moved between participants, under which roles, with acceptance criteria and evidence.')}
    <section class="operation"><form id="handoff-form" class="form-grid"><label>From participant<input name="fromParticipantEn" required></label><label>From role<select name="fromRoleId" required><option value="">Select…</option>${roleOptions()}</select></label><label>To participant<input name="toParticipantEn" required></label><label>To role<select name="toRoleId" required><option value="">Select…</option>${roleOptions()}</select></label><label class="full">Contribution or governed object<input name="governedObjectEn" required></label><label class="full">Description of contribution/handoff<textarea name="contributionEn" required></textarea></label><label>Acceptance criteria<textarea name="acceptanceCriteriaEn" required></textarea></label><label>Evidence pointer<textarea name="evidenceEn" required></textarea></label><label>State<select name="state"><option value="proposed">Proposed</option><option value="offered">Offered</option><option value="accepted">Accepted</option><option value="returned">Returned</option><option value="completed">Completed</option></select></label><div class="form-actions"><button class="button" type="submit">Record handoff</button></div></form>
    <div class="records">${workspace.handoffs.map((item) => `<article class="record"><div class="record-meta"><strong>${item.id}</strong><span class="status ${item.state === 'completed' ? 'completed' : ''}">${item.state}</span></div><h3>${esc(item.governedObjectEn)}</h3><p>${esc(item.fromParticipantEn)} (${esc(record(item.fromRoleId)?.nameEn ?? item.fromRoleId)}) → ${esc(item.toParticipantEn)} (${esc(record(item.toRoleId)?.nameEn ?? item.toRoleId)})</p><small>${esc(item.contributionEn)}</small></article>`).join('') || '<p class="empty">No handoffs recorded.</p>'}</div></section>`;
}

function accountabilityView(): string {
  return `${head('05', 'Assign accountability obligations', 'Record answerability and required evidence without confusing it with decision authority.')}
    <section class="operation"><form id="accountability-form" class="form-grid"><label>Participant or system<input name="participantEn" required></label><label>Role<select name="roleId" required><option value="">Select…</option>${roleOptions()}</select></label><label>Accountable to<input name="accountableToEn" required></label><label>Evidence requirement<input name="evidenceRequirementEn" required></label><label class="full">Obligation<textarea name="obligationEn" required></textarea></label><label class="full">Limitation or exception<textarea name="limitationEn" required></textarea></label><div class="form-actions"><button class="button" type="submit">Record obligation</button><button class="button secondary" id="accountability-prompt" type="button">Copy consistency-review prompt</button></div></form>
    <div class="records">${workspace.accountability.map((item) => `<article class="record"><div class="record-meta"><strong>${item.id}</strong><span>${esc(record(item.roleId)?.nameEn ?? item.roleId)}</span></div><h3>${esc(item.participantEn)} → ${esc(item.accountableToEn)}</h3><p>${esc(item.obligationEn)}</p><small>Evidence: ${esc(item.evidenceRequirementEn)} · Limitation: ${esc(item.limitationEn)}</small></article>`).join('') || '<p class="empty">No accountability obligations recorded.</p>'}</div></section>`;
}

function values(form: HTMLFormElement): Record<string, string> { return Object.fromEntries(new FormData(form).entries()) as Record<string, string>; }
function bindShell(): void { document.querySelectorAll<HTMLButtonElement>('[data-tab]').forEach((button) => button.addEventListener('click', () => { view = button.dataset.tab as View; message = ''; history.replaceState(null, '', `roles.html?view=${view}`); render(); })); }
function bindView(): void {
  document.querySelector<HTMLInputElement>('#query')?.addEventListener('input', (event) => { query = (event.currentTarget as HTMLInputElement).value; render(); });
  document.querySelector<HTMLSelectElement>('#class-filter')?.addEventListener('change', (event) => { classFilter = (event.currentTarget as HTMLSelectElement).value as typeof classFilter; render(); });
  document.querySelectorAll<HTMLButtonElement>('[data-select]').forEach((button) => button.addEventListener('click', () => { selectedId = button.dataset.select!; render(); }));
  document.querySelector<HTMLButtonElement>('#copy-review')?.addEventListener('click', async () => { const item = record(selectedId); if (!item) return; const ok = await copyReviewPrompt(`Collaborative SymK review\n\nRecord: ${item.id} v${item.version}\nClass: ${item.recordClass}\nName: ${item.nameEn}\nDefinition: ${item.definitionEn}\nCapabilities: ${item.capabilitiesEn}\nLimitations: ${item.limitationsEn}\nStatus: ${item.status}\n\nReview jurisdiction, clarity, hidden assumptions, role/participant-kind confusion, authority leakage, accountability gaps, incompatible combinations and downstream consequences. Ask clarifying questions before recommending a disposition.`); message = ok ? 'Collaborative review prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLButtonElement>('#draft-prompt')?.addEventListener('click', async () => { const ok = await copyReviewPrompt('Help draft a candidate SymK participant-kind or role definition in English. Keep participant kind, role, competence, authority and accountability distinct. Require capabilities, limitations, provenance, rationale, compatibility considerations and counterexamples. Do not grant authority or acceptance.'); message = ok ? 'Authoring prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLButtonElement>('#accountability-prompt')?.addEventListener('click', async () => { const ok = await copyReviewPrompt(`Review these SymK accountability records for gaps, overlaps and contradictions. Distinguish answerability from decision authority and verify that each obligation has an observable evidence requirement.\n\n${JSON.stringify(workspace.accountability, null, 2)}`); message = ok ? 'Consistency-review prompt copied.' : 'Clipboard access was unavailable.'; render(); });
  document.querySelector<HTMLFormElement>('#definition-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); if (workspace.definitions.some(({ id }) => id === data.id.trim())) { message = 'That stable ID already exists.'; render(); return; } workspace.definitions.push({ id: data.id.trim(), recordClass: data.recordClass as RecordClass, nameEn: data.nameEn.trim(), definitionEn: data.definitionEn.trim(), capabilitiesEn: data.capabilitiesEn.trim(), limitationsEn: data.limitationsEn.trim(), sourceEn: data.sourceEn.trim(), rationaleEn: data.rationaleEn.trim(), status: 'candidate', version: 1, createdAt: timestamp() }); persist(); selectedId = data.id.trim(); message = 'Candidate definition registered without granting authority or acceptance.'; view = 'registry'; render(); });
  document.querySelector<HTMLFormElement>('#combination-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); if (data.leftRoleId === data.rightRoleId) { message = 'Choose two distinct roles.'; render(); return; } workspace.combinations.push({ id: uid('SYMK-RC'), leftRoleId: data.leftRoleId, rightRoleId: data.rightRoleId, relation: data.relation as Combination['relation'], conditionEn: data.conditionEn.trim(), rationaleEn: data.rationaleEn.trim(), createdAt: timestamp() }); persist(); message = 'Role-combination rule recorded.'; render(); });
  document.querySelector<HTMLFormElement>('#handoff-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); workspace.handoffs.push({ id: uid('SYMK-HO'), fromParticipantEn: data.fromParticipantEn.trim(), fromRoleId: data.fromRoleId, toParticipantEn: data.toParticipantEn.trim(), toRoleId: data.toRoleId, contributionEn: data.contributionEn.trim(), governedObjectEn: data.governedObjectEn.trim(), acceptanceCriteriaEn: data.acceptanceCriteriaEn.trim(), evidenceEn: data.evidenceEn.trim(), state: data.state as Handoff['state'], createdAt: timestamp() }); persist(); message = 'Contribution and handoff recorded with evidence and acceptance criteria.'; render(); });
  document.querySelector<HTMLFormElement>('#accountability-form')?.addEventListener('submit', (event) => { event.preventDefault(); const data = values(event.currentTarget as HTMLFormElement); workspace.accountability.push({ id: uid('SYMK-ACC'), participantEn: data.participantEn.trim(), roleId: data.roleId, accountableToEn: data.accountableToEn.trim(), obligationEn: data.obligationEn.trim(), evidenceRequirementEn: data.evidenceRequirementEn.trim(), limitationEn: data.limitationEn.trim(), createdAt: timestamp() }); persist(); message = 'Accountability obligation recorded; no decision authority was inferred.'; render(); });
}

render();
