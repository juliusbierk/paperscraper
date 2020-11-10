"""Dump chemRxiv data in JSONL format."""
import os

from datetime import datetime
from paperscraper.get_dumps.utils.chemrxiv import ChemrxivAPI, download_full, parse_dump

HERE = os.path.abspath(os.path.dirname(__file__))
today = datetime.today().strftime('%Y-%m-%d')
save_folder = os.path.abspath(os.path.join(HERE, '..', '..', 'server_dumps'))
save_path = os.path.join(save_folder, f'chemrxiv_{today}.jsonl')


def chemrxiv(save_path: str = save_path, token=None):
    """Fetches all papers from biorxiv until current date, stores them in jsonl
    format in save_path.

    Args:
        save_path (str, optional): Path where the dump is stored.
            Defaults to save_path.
    """
    # create API client
    api = ChemrxivAPI(token=token)
    # Download the data
    download_full(save_folder, api)
    # Convert to JSONL format.
    parse_dump(save_folder, save_path)
