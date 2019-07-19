# Imports the Google Cloud client library
from google.cloud import storage

storage_client = storage.Client()

def upload_blob():
    """Uploads a file to the bucket."""

    bucket_name = "ketav-source"
    destination_blob_name = "teletubbies1.jpg"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(destination_blob_name)



def download_blob():
    """Downloads a blob from the bucket."""
    source_blob_name = "teletubbies1.jpg"
    destination_file_name = "/home/ketav/Downloads/teletubbies1.jpg"
    bucket_name = "ketav-source"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

def copy_blob():
    """Copies a blob from one bucket to another with a new name."""
    bucket_name = "ketav-source"
    new_bucket_name = "ketav-destination"
    blob_name = "teletubbies1.jpg"
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, blob_name)


def delete_blob():
    """Deletes a blob from the bucket."""
    bucket_name = "ketav-source"
    blob_name = "teletubbies1.jpg"
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()


def move_blob():
	"""Moves a blob from one bucket to another."""
	bucket_name = "ketav-source"
	new_bucket_name = "ketav-destination"
	blob_name = "teletubbies1.jpg"
	source_bucket = storage_client.get_bucket(bucket_name)
	source_blob = source_bucket.blob(blob_name)
	destination_bucket = storage_client.get_bucket(new_bucket_name)

	new_blob = source_bucket.copy_blob(source_blob, destination_bucket, blob_name)
	blob = source_bucket.blob(blob_name)
	blob.delete()


upload_blob()

download_blob()

copy_blob()

delete_blob()

move_blob()