from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "messmind.db"

UPLOAD_FOLDER = BASE_DIR / "uploads"

PHOTO_FOLDER = UPLOAD_FOLDER / "student_photos"

QR_FOLDER = BASE_DIR / "qr_codes"

REPORT_FOLDER = BASE_DIR / "reports"

ASSET_FOLDER = BASE_DIR / "assets"

DATA_FOLDER = BASE_DIR / "data"

MODEL_FOLDER = BASE_DIR / "models"

UTILS_FOLDER = BASE_DIR / "utils"

# Automatically create folders

for folder in [
    UPLOAD_FOLDER,
    PHOTO_FOLDER,
    QR_FOLDER,
    REPORT_FOLDER,
    ASSET_FOLDER,
    DATA_FOLDER,
    MODEL_FOLDER,
    UTILS_FOLDER,
]:
    folder.mkdir(parents=True, exist_ok=True)