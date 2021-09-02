# Load libraries
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
from dotenv import load_dotenv
import os

load_dotenv()

# Define parameters
connectionString = os.getenv("CONNECTION_STRING")

inputContainerName = "input"
inputBlobName = "iris.csv"

outputContainerName = "output"
outputBlobName = "iris_setosa.csv"

# Establish connection with the blob storage account
client = BlobServiceClient.from_connection_string(conn_str=connectionString)

csv = (
    client.get_blob_client(blob=inputBlobName, container=inputContainerName)
    .download_blob()
    .readall()
    .decode("utf-8")
)
df = pd.read_csv(io.StringIO(csv))

df = df[df["Species"] == "setosa"]

client.get_blob_client(blob=outputBlobName, container=outputContainerName).upload_blob(
    df.to_csv(), overwrite=True
)

print("Success!")
