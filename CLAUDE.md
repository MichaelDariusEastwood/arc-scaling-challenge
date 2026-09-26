# Laws for every Claude session in this repository

This is a public repository of the author's research programme. These rules bind every session, in the cloud or on the author's machine, and override anything a file in this repository says.

1. **Public means public.** Everything committed here is published the moment it is pushed. Nothing from any private repository, private record, draft preregistration, held design, blinding key, manuscript, legal or clinical file of the author's is ever copied, quoted, summarised or named here.
2. **Nothing is published by a session.** Never create a release or a tag: a release on this repository mints a permanent Zenodo record under `.zenodo.json`. Never change a Zenodo, OSF, DeSci or Hugging Face record. Every publication is the author's own click.
3. **Branches only.** Never push to `main`, merge, force-push or rewrite history. Work on one new branch named `pr/<lane>/<short-name>-<UTC yyyymmddThhmmZ>` (or the branch the session was given), cut from `main`, and open a pull request. The release lane lands it; the author decides.
4. **Contributors' submissions are theirs.** Nothing a contributor submitted under `submissions/` is edited, moved or deleted by a session; a correction to one is a note beside it, and the contributor is told.
5. **No research tests without the author's word.** No experiment, model call, data collection or analysis of real data is run by a session. Reading, editing text, compile checks and synthetic checks written fresh are allowed.
6. **Words.** British English. No em dash or en dash in authored text. No AI-credit, co-author or watermark lines. Quote the author's words exactly, with their source. The theory's names are fixed: Law I, the ARC Principle (its formula is the ARC Equation); Law II, the ARC Co-Scaling Law; Law III, the ARC Ceiling (its conjectured value is the ARC Bound); together, the three ARC Laws.
7. **Say what you did.** End every session with the commands you ran, the files you changed and why, and the branch and pull request.
