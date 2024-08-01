import os
import subprocess

def paths(directory: str):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

filepaths: list[str] = paths(os.getcwd())       
for file in filepaths:
    if file.endswith(".flac"):
        name = os.path.basename(file)
        subprocess.run(f'ffmpeg -nostdin -i "{file}" -c:a alac -c:v copy "{name}.m4a"')
        os.remove(file)
