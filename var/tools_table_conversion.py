import pandas as pd
import numpy as np
import os
import re
import frontmatter
import yaml
import requests
import sys
import argparse


def process_args():
    '''parse command-line arguments
    '''

    parser = argparse.ArgumentParser(prog='Conversions',
                                     description='This script will convert the tool and resources table to a yaml file while injecting bio.tools and FAIRsharing IDs where needed.',)
    parser.add_argument('--username',
                        help='Specify the FAIRsharing username')

    parser.add_argument('--password',
                        help='Specify the FAIRsharing password')

    parser.add_argument('--reg',
                        default=False,
                        action="store_true",
                        help='Enable TeSS, bio.tools and FAIRsharing lookup')

    args = parser.parse_args()

    return args

def remove_prefix(s, prefix):
    return s[s[:len(prefix)].index(prefix) + len(prefix):]

def client(url):
    """API object fetcher"""
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get(url)
    if r.status_code == requests.codes.ok:
        return r.json()


def correct_registry_field(registry_string, reg_arg):
    if not registry_string:
        return ''
    elif type(registry_string) is dict:
        return registry_string
    elif type(registry_string) is float:
        return ''
    elif ',' in registry_string:
        registry_list = registry_string.split(", ")
        registry_dict = {}
        for registry in registry_list:
            registry_split = registry.split(":")
            registry_dict[registry_split[0]] = registry_split[1]
    else:
        registry_split = registry_string.split(":")
        registry_dict = {registry_split[0]: registry_split[1]}
    if reg_arg:
        if "tess" not in registry_dict.keys():
            check_tess = tess_available(tool_name)
            if check_tess:
                registry_dict["tess"] = check_tess
        elif registry_dict["tess"] == "NA":
            del registry_dict["tess"]
        if "biotools" not in registry_dict.keys():
            check_biotools = biotools_available(tool_name)
            if check_biotools:
                registry_dict["biotools"] = check_biotools
        elif registry_dict["biotools"] == "NA":
            del registry_dict["biotools"]
        if "fairsharing" not in registry_dict.keys():
            if len(tool_name) > 4:
                check_fairsharing = fairsharing_available(
                    tool_name, fairsharing_token)
                if check_fairsharing:
                    registry_dict["fairsharing"] = check_fairsharing
        elif registry_dict["fairsharing"] == "NA":
            del registry_dict["fairsharing"]
    return registry_dict


def check_related_pages(page_metadata, listed_pages):
    split_pages = re.split(', |,', listed_pages)
    print(split_pages)
    pages_to_remove = []
    for page in split_pages:
        if page not in page_metadata.keys():
            print(f'ERROR: the table contains the related page "{page}", it will not be included, check the naming and re-run to include it.')
            pages_to_remove.append(page)
    related_pages = []
    for page in split_pages:
        if page not in pages_to_remove:
            related_pages.append(page)
    return related_pages  


def parse_acronym(query):
    m = re.match(r"(.*)\s\((.*)\)", query)
    if m:
        return {"fullname": m.group(1), "acronym": m.group(2)}

def tess_available(query):
    acronym = parse_acronym(query)
    def fetch_output(query):
        return client(
            f'https://tess.elixir-europe.org/materials.json_api?q="{query}"&page_number=1&page_size=30')
    if len(fetch_output(query)['data']) > 0:
        return query
    if acronym and len(fetch_output(acronym['fullname'])['data']) > 0:
        return acronym['fullname']

def biotools_available(query):
    acronym = parse_acronym(query)
    if acronym and client(f"https://bio.tools/api/tool/{acronym['acronym'].lower()}/?format=json"):
        return acronym['acronym'].lower()
    elif client(f"https://bio.tools/api/tool/{query.lower()}/?format=json"):
        return query.lower()
    elif len(query) > 4:
        json_output = client(
            f"https://bio.tools/api/t/?format=json&q='{query}'")
        if json_output['count'] != 0:
            for tool in json_output['list']:
                if tool['name'].lower() == query.strip().lower():
                    return tool['biotoolsID']
        else:
            json_output = client(
                f"https://bio.tools/api/t/?format=json&q='{query}'")
            if json_output['count'] != 0:
                for tool in json_output['list']:
                    if query.strip().lower() in tool['name'].lower():
                        return tool['biotoolsID']

def get_fairsharing_token(username, password):
    url = "https://api.fairsharing.org/users/sign_in"
    payload = "{\"user\": {\"login\":\"" + username + \
        "\",\"password\":\"" + password + "\"} }"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()["success"] != True:
            sys.exit()
        else:
            return response.json()["jwt"]
    except:
        print("Could not login into FAIRsharing")


def fairsharing_available(query, token):
    url = "https://api.fairsharing.org/search/fairsharing_records"

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    payload = {'q': query}
    try:
        response = requests.request(
            "POST", url, headers=headers, params=payload)
        output = response.json()['data']
        if len(output) >= 1:
            for fairsharing_obj in output:
                if query.lower() in fairsharing_obj['attributes']['name'].lower() and fairsharing_obj['attributes']['doi']:
                    return fairsharing_obj['attributes']['url'].split(".")[-1]
    except:
        print(response)
        sys.exit("Could not connect to FAIRsharing")


# --------- Variables ---------

google_id = "1muhgZ8xppN8tnksa97P2jcS6zS9rHvvZw8LIhd3uOn4"
gid = "1484870633"
url = f"https://docs.google.com/spreadsheets/d/{google_id}/export?format=csv&gid={gid}"
output_path = "_data/tool_and_resource_list.yml"
rootdir = 'pages/'
allowed_registries = ['biotools', 'fairsharing', 'tess', 'fairsharing-coll']


# --------- Reading out page_ids from pages ---------

print(f"----> Reading out page_id from each file")
pages_metadata = {}
for subdir, dirs, files in os.walk(rootdir):
    for file_name in files:
        if os.path.splitext(file_name)[1] == '.md':
            print(f"Opening {os.path.splitext(file_name)[0]}")
            with open(os.path.join(subdir, file_name)) as f:
                metadata, content = frontmatter.parse(f.read())
            if 'page_id' in metadata.keys() and 'search_exclude' not in metadata.keys():
                pages_metadata[metadata['page_id']] = {}
                pages_metadata[metadata['page_id']
                               ]['title'] = metadata['title']
                pages_metadata[metadata['page_id']]['type'] = remove_prefix(
                    subdir, 'pages/').replace("_", " ").capitalize()
                pages_metadata[metadata['page_id']]['url'] = os.path.splitext(file_name)[
                    0]
                if 'description' in metadata:
                    pages_metadata[metadata['page_id']
                                   ]['description'] = metadata['description']

print(f"----> Allowed related_pages: {', '.join(pages_metadata.keys())}.")

# --------- Converting the table ---------

print(f"----> Converting table {table_path} to {output_path} started.")
args = process_args()
resource_table = pd.read_csv(url)
resource_list = resource_table.to_dict("records")
clean_resource_list = []
for resource in resource_list:
    resource['registry'] = correct_registry_field(resource["registry"], args.reg)
    resource['related pages'] = check_related_pages(pages_metadata, resource['related pages'])
    
    clean_resource = {k: v for k, v in resource.items() if v}
    clean_resource_list.append(clean_resource)

if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(clean_resource_list, yaml_file)

print("----> YAML is dumped successfully")