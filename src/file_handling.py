import os


def create_folder(caminho):
    os.makedirs(caminho, exist_ok=True)
    return