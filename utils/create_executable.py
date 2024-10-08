import streamlit.web.cli as stcli
import os, sys
import shutil

def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

if __name__ == "__main__":
    script_path = resolve_path("lofam.py")
    os.system(f"streamlit run {script_path} --global.developmentMode=false")

    sys.exit(stcli.main())