"""Save Trained models"""

import os

import dill as pickle


def load_model(file_path):

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Check if the file is a piccle file
    if not file_path.endswith(".pkl"):
        raise ValueError("The file is not a pickle file.")

    with open(file_path, "rb") as file_name:
        model = pickle.load(file_name)

    return model


def run(
    model_load_dir: str,
    ranking_model_path: str,
    cross_encoder_path: str,
    bm25_es_path: str,
    bm25_us_path: str,
    bm25_jp_path: str,
) -> None:

    """
    This function load the trained models: ranking model, cross-encoder model, and bm25 models.
    """

    # Define file names where the models are saved
    ranking_model_file = os.path.join(model_load_dir, ranking_model_path)
    cross_encoder_file = os.path.join(model_load_dir, cross_encoder_path)
    bm25_es_file = os.path.join(model_load_dir, bm25_us_path)
    bm25_us_file = os.path.join(model_load_dir, bm25_es_path)
    bm25_jp_file = os.path.join(model_load_dir, bm25_jp_path)

    # Save cross encoder model
    cross_encoder_model = load_model(file_path=cross_encoder_file)
    ranking_model = load_model(file_path=ranking_model_file)
    bm25_model_us = load_model(file_path=bm25_us_file)
    bm25_model_es = load_model(file_path=bm25_es_file)
    bm25_model_jp = load_model(file_path=bm25_jp_file)

    return (
        cross_encoder_model,
        ranking_model,
        bm25_model_us,
        bm25_model_es,
        bm25_model_jp,
    )
