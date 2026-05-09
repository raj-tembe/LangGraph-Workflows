import nbformat

path = "/home/toast/Storage/AI/LangGraph-Workflows/Llama-3.2-3B-TUTOR-gsm8k.ipynb"
print(f"Fixing notebook: {path}")
with open(path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove widget metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"Fixed notebook saved: {path}")