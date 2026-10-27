# TA-1278 research archive

Firmware, analysis, handset captures and research tools moved from the application workspace on 2026-10-27. Original relative paths are retained. `migration.json` records SHA-256 for every migrated file.

The complete pre-separation application source, uncommitted work and Git history are saved in `../backups/separation-20261027-130617/`. Existing private acquisitions remain in the other sibling directories; no existing files were overwritten. Some analysis tools expect the original full layout: use that snapshot for reproduction rather than assuming this extracted subset is standalone.

The application now keeps only the resources needed at runtime and regression fixtures. This directory is now maintained in the separate research repository; private acquisitions and recovery snapshots remain local. Review source rights and private data before selecting files for a new public repository; this local archive is not a publication allowlist.

Original resource provenance reports are retained under assets/. They describe the historical source layout; runtime files remain in the application and the complete recovery snapshot. THIRD_PARTY_NOTICES.md is the original notice document, and the ABM decoder license is retained under third-party-licenses/.
