import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? join(here, "out");
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
const bytes = statSync(dst).size;
if (bytes === 0 || bytes > 1048576) {
  throw new Error(`entry.png has unexpected size: ${bytes} bytes`);
}
console.log(`wrote ${dst} (${bytes} bytes)`);
