import os

# Path
ROOT_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
ASSETS_VHP_DIR = os.path.join(ASSETS_DIR, "VisibleHumanProject")

# Dataset
DATASET_VHP_ORIGINAL = os.path.join(ASSETS_VHP_DIR, "original")
DATASET_VHP_AUGMENTED = os.path.join(ASSETS_VHP_DIR, "augmented")