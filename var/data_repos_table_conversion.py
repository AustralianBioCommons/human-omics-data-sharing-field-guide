
import pandas as pd
import numpy as np
import argparse 


def parse_arguments():
    parser = argparse.ArgumentParser("Generate Gen3 Schema YAMLs from a google sheet.")
    parser.add_argument('--google-id', type=str, action='store', required=True,
                        help="The alpha-numeric identifier for the sheet e.g. 1G5mVh0KGR4PvXEr1Q-Mg68bEkv8N_Usl92dCmj1yeAk")
    args = parser.parse_args()
    return args

def create_link(link_url, link_text):
    return f'<a href="{link_url}" target="_blank">{link_text}</a>'

def create_pub_link(link_url, authors):
    return f'<a href="{link_url}" target="_blank"><i class="fa-solid fa-book"></i> {authors}</a>'

def create_training_link(link_url):
    return f'<a href="{link_url}" target="_blank"><i class="fa-solid fa-chalkboard-user"></i></a>'


if __name__ == "__main__":
   args = parse_arguments()
   url = f"https://docs.google.com/spreadsheets/d/{args.google_id}/export?format=csv&gid={args.objects_gid}"
   dr_table = pd.read_csv(url)
