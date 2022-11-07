import pandas as pd
import os
import re
import frontmatter
import yaml

def remove_prefix(s, prefix):
    return s[s[:len(prefix)].index(prefix) + len(prefix):]

# --------- Variables ---------

table_path = "_data/main_tool_and_resource_list.csv"
table_url = f"https://docs.google.com/spreadsheets/d/1muhgZ8xppN8tnksa97P2jcS6zS9rHvvZw8LIhd3uOn4/export?format=csv&gid=1484870633"
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
main_list = []
if args.reg:
    fairsharing_token = get_fairsharing_token(args.username, args.password)

tools_table = pd.read_csv(table_url)
tools_dict = tools_table.to_dict()

with open(table_path, 'r') as read_obj:
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Check file as empty
    if header != None:
        # Looping over rows and adding its contents to the main dict
        for row_index, row in enumerate(csv_reader):
            tool = {}
            tool_name = row[0]
            for col_index, cell in enumerate(row):
                # Only include keys if there are values:
                if header[col_index] == 'related_pages' and cell:
                    output = re.split(', |,', cell)
                    for tag in output:
                        if tag not in pages_metadata.keys():
                            print(
                                f'ERROR: The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check if the tag you are using is declared in the metadata of one of the pages using the "page_id" attribute.')
                            sys.exit(
                                f'The table contains the tag "{tag}" in row {row_index} which is not allowed.\n-> Check if the tag you are using is declared in the metadata of one of the pages using the "page_id" attribute.')
                # Only include keys if there are values:
                elif header[col_index] == 'country' and cell:
                    output = re.split(', |,', cell)
                elif header[col_index] == 'registry':
                    output = {}
                    if cell:  # Only include keys if there are values
                        for registry in re.split(', |,', cell):
                            reg, identifier = re.split(':|: ', registry)
                            if reg in allowed_registries:
                                output[reg] = identifier
                            else:
                                print(
                                    f'ERROR: The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                                sys.exit(
                                    f'The table contains the registry "{reg}" in row {row_index} which is not allowed.\n' + f"Allowed registries are {', '.join(allowed_registries)}.\n")
                    if args.reg:
                        if "tess" not in output:
                            check_tess = tess_available(tool_name)
                            if check_tess:
                                output["tess"] = check_tess
                        elif output["tess"] == "NA":
                            del output["tess"]
                        if "biotools" not in output:
                            check_biotools = biotools_available(tool_name)
                            if check_biotools:
                                output["biotools"] = check_biotools
                        elif output["biotools"] == "NA":
                            del output["biotools"]
                        if "fairsharing" not in output:
                            if len(tool_name) > 4:
                                check_fairsharing = fairsharing_available(
                                    tool_name, fairsharing_token)
                                if check_fairsharing:
                                    output["fairsharing"] = check_fairsharing
                        elif output["fairsharing"] == "NA":
                            del output["fairsharing"]
                else:
                    # Return the normal form for the Unicode string
                    output = unicodedata.normalize("NFKD", cell).strip()
                if output:
                    tool[header[col_index]] = output
            main_list.append(tool)
            print(f"{row_index}. {tool['name']} is parsed.")

with open(output_path, 'w') as yaml_file:
    documents = yaml.dump(main_list, yaml_file)

print("----> YAML is dumped successfully")