import os
import base64
import random
import string
import uuid

from dotenv import load_dotenv
from google.cloud import storage

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

RANDOM_FILENAME_LENGTH = 50

UPLOAD_FOLDER = 'E:\\Projects\\Thesis\\Code\\frontend\\public\\img'

GCLOUD_KEY_PATH = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
GCLOUD_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, filename, work_id):
    # file.save(os.path.join(UPLOAD_FOLDER, gen_work_filename(work_id, result=False)))
    # return path_for_frontend(os.path.join(UPLOAD_FOLDER, filename))
    image_url = upload_gcloud_file(file=file)
    return image_url

def path_for_frontend(path):
    partial_paths = path.split('\\')
    partial_paths = partial_paths[6:]
    return '\\'.join(partial_paths)

def save_b64_file(data: str, work_id: int):
    b64_data = data.replace('data:image/png;base64,', '')
    img_data = base64.b64decode(b64_data)
    # filename = gen_work_filename(work_id, result=True)
    # file_path = os.path.join(UPLOAD_FOLDER, filename)
    # with open(file_path, 'wb') as f:
    #     f.write(img_data)
    #
    # return path_for_frontend(file_path)

    # with open('tmp.png', 'wb') as f:
    #     f.write(img_data)
    # with open('tmp.png', 'rb') as f:
    #     img_path = upload_gcloud_file(file=f, result=True)
    #     return img_path

    # with open("my_file.png", "wb") as binary_file:
    #     binary_file.write(img_data)
    return upload_gcloud_file(data=img_data, result=True)

def gen_work_filename(work_id, result):
    filename = 'file_' + str(work_id)
    if result:
        filename += '_result'
    filename += '.png'
    return filename

def upload_gcloud_file(file=None, data=None, result=False):
    load_dotenv()
    storage_client = storage.Client().from_service_account_json(GCLOUD_KEY_PATH)
    bucket = storage_client.get_bucket(GCLOUD_BUCKET)
    blob = bucket.blob('%s/%s/%s' % ('image', 'submit', uuid.uuid4()))
    blob.content_type = "image/png"
    if file:
        blob.upload_from_file(file, rewind=True)
    elif data:
        blob.upload_from_string(data, content_type='image/png')
    # blob.make_public()
    return blob.public_url

def upload_gcloud_doc(name, file=None, data=None):
    load_dotenv()
    storage_client = storage.Client().from_service_account_json(GCLOUD_KEY_PATH)
    bucket = storage_client.get_bucket(GCLOUD_BUCKET)
    name = name.replace(' ', '_')
    blob = bucket.blob('%s/%s/%s' % ('doc', 'assigment', name + '_' + str(uuid.uuid4())))
    if file:
        blob.upload_from_string(file.read(), content_type=file.content_type)
    elif data:
        blob.upload_from_string(data, content_type='image/png')
    # blob.make_public()
    return blob.public_url
