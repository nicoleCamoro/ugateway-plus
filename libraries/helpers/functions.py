import os
import hashlib
import string
import random
import datetime
import logging
import re
import base64
import cloudstorage as gcs

from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.api import images
from config import settings

def convert_key_val_pairs(keyval_array):

    result = {}
    for pair in keyval_array:
        result[pair[0]] = pair[1]
    return result

def create_random_string(n=8):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '!-_') for _ in range(n))


def create_random_gcs_filename():
    date_time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))
    filename = create_random_string()
    return 'gcs-file-' + date_time + '-' + filename


def gcs_upload(file_to_upload, bucket=settings.GCS_BUCKET):
    """Uploads a file to google cloud storage."""
    try:
        filename = create_random_gcs_filename()
        bucket_and_filename = {'bucket': bucket, 'filename': filename}
        gcs_filename = '/%(bucket)s/%(filename)s' % bucket_and_filename
        public_url = 'https://storage.googleapis.com/%(bucket)s/%(filename)s' % bucket_and_filename

        gcs_file = gcs.open(
            gcs_filename,
            mode='w',
            content_type=file_to_upload.type,
            options={'x-goog-acl': 'public-read'})
        gcs_file.write(file_to_upload.value)
        gcs_file.close()

        gs_key = blobstore.create_gs_key('/gs' + gcs_filename)
        try:
            serving_url = images.get_serving_url(gs_key)
        except:
            serving_url = public_url

        return {
            'gs_key': gs_key,
            'gcs_filename': gcs_filename,
            'serving_url': serving_url,
            'public_url': public_url,
            'filename': filename,
            'filetype': file_to_upload.type
        }

    except Exception, e:
        logging.exception(e)
        return None