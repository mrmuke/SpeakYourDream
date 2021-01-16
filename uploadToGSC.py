from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gapi-chrome-extension-bece3debbebd.json"

def Upload_blob(source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket('speakyourdream2086')
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )