// News image for Tuesday 17 November 2026 (make.fun news-image-20261117).
// The entry image is entry.png beside this file, drawn by draw.py from
// verified 17 November 2026 reporting (Reuters / BBC): the Crimea Bridge
// collapse, tanker fires in the Strait of Hormuz, Trump landing in Manila
// ahead of the Xi-Putin summit, the US losing measles elimination status,
// Nvidia in turmoil, and the EU Rwanda return-hub plan.
// The program copies it to /output/entry.png, deterministically, with no
// network. Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);
if (!existsSync(source)) {
  throw new Error('entry.png is missing from the repository root');
}
mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, 'entry.png'));
