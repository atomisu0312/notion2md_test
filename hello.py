from notion2md.exporter.block import MarkdownExporter, StringExporter
from dotenv import load_dotenv

import os

def main():
    load_dotenv('.env')
    key = os.environ['NOTION_API_TOKEN']    
    print("Yout API KEY is {}".format(key))
    
if __name__ == "__main__":
    main()
