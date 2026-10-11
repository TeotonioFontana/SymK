import type { ProjectModel } from './types';

export const project: ProjectModel = {
  slug: 'symk',
  name: 'SymK',
  eyebrow: 'Bounded cooperation system · jurisdiction review',
  description: 'SymK is a bounded protocol for observable and accountable cooperation among human and artificial participants. The migration narrows its jurisdiction without discarding its history, operational model or project-specific architecture.',
  statusTitle: 'Source frozen and untouched; Wave 1 diagnosis awaiting owner disposition.',
  statusDetail: 'SymK remains the authority for its current material. Imported files are review evidence only. Nothing has been moved, renamed, deleted or silently reclassified.',
  boundaryTitle: 'Source protection',
  boundary: 'SymK governance remains unchanged. Approval of this wave would authorize the next review only—not editing SymK, drafting a new Foundation or submitting concepts to VocabularyRegistry.',
  counterpartHref: '/foundation/',
  counterpartLabel: 'View the Foundation side',
  waves: [
    { id: 0, title: 'Freeze and fallback', state: 'complete', summary: 'Pin the repository state, inventory governance and test exact reconstruction.', tasks: [] },
    { id: 1, title: 'Mixed nucleus', state: 'current', summary: 'Review Product Vision, Philosophy, Engineering Principles and Foundational Concepts proposition by proposition.', tasks: [
      'Retain the DIA, value chain, users and governance tensions as SymK project material.',
      'Decide how claims describing SymK as the entire engineering discipline must be split or replaced.',
      'Retain the Philosophy as historical material while flagging fixed human/AI assignments for later revision.',
      'Separate SymK architectural choices from general engineering candidates.',
      'Keep source cleanup blocked until replacement artifacts and dependency reconciliation are approved.'
    ] },
    { id: 2, title: 'Foundation paper history', state: 'blocked', summary: 'Inspect historical discipline-level material while retaining SymK decisions and provenance.', tasks: [] },
    { id: 3, title: 'Constitution and axioms', state: 'planned', summary: 'Distinguish SymK’s internal constitution from universal claims requiring Foundation authority.', tasks: [] },
    { id: 4, title: 'Concepts and methods', state: 'planned', summary: 'Keep project primitives in SymK and route justified external candidates through proper approval.', tasks: [] },
    { id: 5, title: 'Operational governance', state: 'planned', summary: 'Route policies, registers and templates and propose source cleanup as a separate reversible operation.', tasks: [] }
  ]
};
