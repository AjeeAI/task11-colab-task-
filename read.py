# import file_ops
from participant_pkg import file_ops
from pathlib import Path
workspace = Path("workspace")

path = workspace / "contacts.csv"
file_ops.load_participants(path)