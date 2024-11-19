API_KEY="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"
API_HOST="https://api.bionemo.ngc.nvidia.com/v1"

# Define the NGC CLI API KEY and ORG for the model download
# If these variables are not already set in the container, uncomment below
# to define and set with your API KEY and ORG
api_key = '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'
ngc_cli_org = '0559908415901577'
# Update the environment variable
import os
os.environ['NGC_CLI_API_KEY'] = api_key
os.environ['NGC_CLI_ORG'] = ngc_cli_org
os.environ['NGC_CLI_TEAM'] = 'no-team'

from bionemo.api import BionemoClient as BaseClient
from guided_molecule_gen.inference_client import BioNemoServiceClient

service_client = BioNemoServiceClient(BaseClient(api_key=API_KEY, api_host=API_HOST))
