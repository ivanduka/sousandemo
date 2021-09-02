Clone the repository in VSCode

Open the console and run the following commands:
- `python -m venv env1` # creating a new clean environment
- `.\env1\Scripts\activate` # activating the environment's Python
- `pip install -r requirements.txt` # installing the requirements for the project

Create a storage account in Azure
Add two containers to it: `input` and `output`
Upload to `input` `iris.csv` from https://github.com/Azure-Samples/batch-adf-pipeline-tutorial/blob/master/iris.csv

Copy `.env.example` to `.env`
and enter your Connection String for the storage account to .env 
(Storage account -> Access Keys -> Show Keys -> Key1 -> Connection String)
