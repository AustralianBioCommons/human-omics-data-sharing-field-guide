
import argparse
import requests

def process_args():
    """parse command-line arguments
    """
    parser = argparse.ArgumentParser(prog='Zotero Extracter',
                                     description='Extracts the latest references from a zotero library and saves a '
                                                 'bibtex file.', )
    parser.add_argument('--zot-library-id',
                        help='Specify your personal zotero userid or the library id')
    parser.add_argument('--zot-library-type', default='group', choices=['group', 'user'],
                        help='Specify the zotero library type, "user" or "group", default "group"')
    parser.add_argument('--output-path', default='_bibliography/references.bib',
                        help='Path where the bibtex file should be saved')

    return parser.parse_args()


if __name__ == "__main__":
    args = process_args()
    library_id = args.zot_library_id
    library_type = args.zot_library_type
    api_url = "https://api.zotero.org"

    ref_strings = []
    response = requests.get(f'{api_url}/groups/{library_id}/items/top?pprint=1&limit=30&format=bibtex&start=0')
    while response.links['next']['url'] != response.links['last']['url']:
        ref_strings.append(response.text)
        response = requests.get(response.links['next']['url'])


    with open(args.output_path, "w+") as refs:
        for text in ref_strings:
            refs.write(text)
