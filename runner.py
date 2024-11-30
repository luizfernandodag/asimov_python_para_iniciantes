import sys

from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "aplicativo_web.py"]
sys.exit(stcli.main()) 