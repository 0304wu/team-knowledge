# Team tools

## Install the research skills

Run PowerShell from this repository:

```powershell
.\tools\install-skills.ps1
```

This installs `team-knowledge-base`, `paper-reading`, and `experiment-record` into the current user's Codex skills directory. It does not copy credentials or upload files.

## Scan and check duplicates

```powershell
python .\tools\scan_knowledge_base.py .
python .\tools\check_duplicates.py .
```

The duplicate checker reports exact hashes and repeated DOI values. It never deletes files.
