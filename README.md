# Lottery AI / Analysis Collection

This repository collects five open-source lottery analysis / AI projects and provides quick-start notes and one-click fork links so you can examine and run them from your GitHub account.

IMPORTANT: These projects are third-party open-source repositories. Some have explicit open-source licenses (e.g., MIT), others do not include a LICENSE file or use non-standard licensing. Before redistributing or copying source code into your own public repo, review each project's license and, if needed, contact the original author for permission.

## Included projects (5)

1. CorvusCodex / LotteryAi
   - URL: https://github.com/CorvusCodex/LotteryAi
   - Summary: Python-based lottery prediction project implementing multiple ML approaches. (License: MIT)
   - Quick run notes:
     - Clone: `git clone https://github.com/CorvusCodex/LotteryAi.git`
     - Create venv and install: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` (if requirements exist)
     - Read README in upstream for training / inference commands (Jupyter notebooks or scripts).
   - One-click fork: https://github.com/CorvusCodex/LotteryAi/fork

2. bartoszclapinski / LotteryLAB
   - URL: https://github.com/bartoszclapinski/LotteryLAB
   - Summary: Web app for statistical lottery analysis (FastAPI / HTMX / SQLite). Good for visualizing trends and randomness tests.
   - Quick run notes:
     - Clone: `git clone https://github.com/bartoszclapinski/LotteryLAB.git`
     - See upstream README for how to run the FastAPI app (likely `pip install -r requirements.txt` then `uvicorn`).
   - One-click fork: https://github.com/bartoszclapinski/LotteryLAB/fork
   - License: No LICENSE file detected in the upstream metadata — check upstream LICENSE or contact author before redistributing.

3. JeffMv / Lofea
   - URL: https://github.com/JeffMv/Lofea
   - Summary: Tools to convert historical draws into ML-ready features (feature engineering for lottery data).
   - Quick run notes:
     - Clone: `git clone https://github.com/JeffMv/Lofea.git`
     - Inspect notebooks / scripts in repo; set up Python env and run feature generation scripts.
   - One-click fork: https://github.com/JeffMv/Lofea/fork
   - License: Upstream lists license as "Other" — inspect LICENSE or contact author for reuse terms.

4. Ahmad-Alam / Lottery-Prediction
   - URL: https://github.com/Ahmad-Alam/Lottery-Prediction
   - Summary: Jupyter Notebook showing LSTM (RNN) approaches for Powerball / Mega Millions forecasting. Good for learning and experimentation.
   - Quick run notes:
     - Clone: `git clone https://github.com/Ahmad-Alam/Lottery-Prediction.git`
     - Open notebooks: `jupyter notebook` and run example notebooks after installing dependencies.
   - One-click fork: https://github.com/Ahmad-Alam/Lottery-Prediction/fork
   - License: No explicit license file in metadata — check upstream before redistributing.

5. Callam7 / LottoPipeline
   - URL: https://github.com/Callam7/LottoPipeline
   - Summary: Modular data pipeline for historical draw ingestion, frequency/decay analysis, clustering, Monte Carlo, and deep learning experiments.
   - Quick run notes:
     - Clone: `git clone https://github.com/Callam7/LottoPipeline.git`
     - Follow upstream README for pipeline steps (likely Python-based: venv + requirements + run scripts).
   - One-click fork: https://github.com/Callam7/LottoPipeline/fork
   - License: Check LICENSE in upstream (not all metadata show license) before redistribution.

---

## How to use this collection

Option A — Inspect & Fork individually (recommended):
- Click any of the one-click fork links above (or open the upstream URL and press Fork). After forking, the project will appear under your account and you can run it or modify it there.

Option B — Clone upstream locally and run:
- Example for a Python-based project:
  ```bash
  git clone https://github.com/CorvusCodex/LotteryAi.git
  cd LotteryAi
  python -m venv .venv
  source .venv/bin/activate    # or `.venv\Scripts\activate` on Windows
  pip install -r requirements.txt
  # follow upstream README to train or run notebooks
  ```

Option C — Add upstream as a submodule in this repo (keeps upstream link):
- If you want each project visible inside this repository as a submodule, run locally and push:
  ```bash
  git clone https://github.com/US3456H/3456.git
  cd 3456
  git submodule add https://github.com/CorvusCodex/LotteryAi.git external/LotteryAi
  git submodule add https://github.com/bartoszclapinski/LotteryLAB.git external/LotteryLAB
  git submodule add https://github.com/JeffMv/Lofea.git external/Lofea
  git submodule add https://github.com/Ahmad-Alam/Lottery-Prediction.git external/Lottery-Prediction
  git submodule add https://github.com/Callam7/LottoPipeline.git external/LottoPipeline
  git commit -m "Add lottery projects as submodules"
  git push
  ```

## Submodules — automated helper script

I added a helper script `add-submodules.sh` to this repository that you can run locally or in a Codespace to add and initialize the five submodules automatically.

Usage (local):

```bash
chmod +x add-submodules.sh
./add-submodules.sh
# then commit the .gitmodules and submodule pointers
git add .gitmodules external/*
git commit -m "Add lottery projects as submodules"
git push
```

This script only prepares the submodule pointers locally. Because adding submodules modifies Git metadata (the gitlinks), you must run the script in your local clone and push the commit that the script creates. Alternatively you can manually run the git submodule commands shown above.

## License & redistribution note
- I created this collection README; the included upstream projects keep their own licenses. Before copying upstream source into this repository or redistributing, please confirm each upstream project's LICENSE file or contact the authors. If you want, I can help check each repo for a LICENSE file and list which are safe to copy (MIT/Apache/GPL) and which require confirmation.

## Next steps I can do for you (reply with the option you want):
- Add these upstream repos as git submodules into this repo (I will create the .gitmodules and commit) — reply "submodules".
- Fork all 5 projects into your account (I will prepare one-click links for you to confirm) — reply "forks".
- Import source code of only the projects that have explicit permissive licenses (I will check license files and import those) — reply "import-licensed".
- Expand README with step-by-step run commands for each project (I will inspect each upstream README and extract exact commands) — reply "expand-steps".

If you want me to proceed with one of the tasks above, reply with the corresponding keyword.
