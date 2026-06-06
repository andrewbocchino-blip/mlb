# MLB Model — flat, upload-proof layout

Only THREE files to upload (no folders to mangle): `run.py`, `requirements.txt`,
and `README.md`. The entire model is embedded inside `run.py`. The daily
scheduler (`daily.yml`) is added through GitHub's own "create file" box so the
folder path is created correctly — see step 3.

This runs the midnight-pull experiment: every run locks each PLAY/LEAN with the
line it was taken at into `docs/locked_picks.jsonl`. Paper only. No real money.

## Setup (browser only)

### 1. Use a fresh empty repo
If your current repo has loose files, easiest is: repo → Settings → scroll to
bottom → Delete this repository, then make a new empty one (Public). Or just
make a new repo with a different name.

### 2. Upload the three files
On the empty repo: **Add file → Upload files**. Drag in `run.py`,
`requirements.txt`, and `README.md`. Commit. (No folders, so nothing can flatten.)

### 3. Add the scheduler at the correct path
- **Add file → Create new file**
- In the filename box type EXACTLY:  `.github/workflows/daily.yml`
  (typing the slashes creates the folders automatically)
- Paste the entire contents of `daily.yml` (included in this download) into the editor
- Commit

### 4. Turn on Pages
- Settings → Pages → Source: **Deploy from a branch** → Branch **main**, folder **/docs** → Save
- (The /docs folder appears after the first run; if Pages says it can't find it,
  run the workflow once first — step 6 — then set Pages.)

### 5. Allow the workflow to publish
- Settings → Actions → General → Workflow permissions → **Read and write** → Save

### 6. Run once to test
- Actions tab → **Daily MLB Dashboard** → **Run workflow**
- Wait ~1 min. Then set Pages (step 4) if you hadn't. Open your page at
  `https://<your-username>.github.io/<repo>/`

After this it runs itself at 12:05 AM ET daily and locks picks. Just open the page.
