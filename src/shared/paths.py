from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

REPORTS_DIR = PROJECT_ROOT / "reports"

ASSETS_DIR = PROJECT_ROOT / "assets"

DATA_FILE = DATA_DIR / "healthy.xlsx"