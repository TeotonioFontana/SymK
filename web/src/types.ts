export type WaveState = 'complete' | 'current' | 'blocked' | 'planned';

export interface Wave { id: number; title: string; state: WaveState; summary: string; tasks: string[]; }

export interface ProjectModel {
  slug: string; name: string; eyebrow: string; description: string;
  statusTitle: string; statusDetail: string; boundaryTitle: string; boundary: string;
  counterpartHref: string; counterpartLabel: string; waves: Wave[];
}
