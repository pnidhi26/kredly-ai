import shutil

shutil.rmtree("data/chroma", ignore_errors=True)
print("Vector DB reset")
