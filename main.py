# Load libraries
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
from dotenv import load_dotenv
import os

# Load environmental variables from .env file if running locally
load_dotenv()

# Define parameters
connectionString = os.getenv("CONNECTION_STRING")

inputContainerName = "input"
inputBlobName = "iris.csv"

outputContainerName = "output"
outputBlobName = "iris_setosa.csv"

# Establish connection with the blob storage account
client = BlobServiceClient.from_connection_string(conn_str=connectionString)

# Read CSV as a string
csv = (
    client.get_blob_client(blob=inputBlobName, container=inputContainerName)
    .download_blob()
    .readall()
    .decode("utf-8")
)

# Load CSV as a string to a dataframe. Note the convertion to io.String
df = pd.read_csv(io.StringIO(csv))

# Filtering by column value
df = df[df["Species"] == "setosa"]

# Uploading resulting CSV
new_csv = df.to_csv()

client.get_blob_client(blob=outputBlobName, container=outputContainerName).upload_blob(
    new_csv, overwrite=True
)

print("Success!")
