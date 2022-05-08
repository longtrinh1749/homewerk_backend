import os
import base64
import random
import string

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

RANDOM_FILENAME_LENGTH = 50

UPLOAD_FOLDER = 'E:\\Projects\\Thesis\\Code\\frontend\\public\\img'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, filename, work_id):
    file.save(os.path.join(UPLOAD_FOLDER, get_work_filename(work_id, result=False)))
    return path_for_frontend(os.path.join(UPLOAD_FOLDER, filename))

def path_for_frontend(path):
    partial_paths = path.split('\\')
    partial_paths = partial_paths[6:]
    return '\\'.join(partial_paths)

def save_b64_file(data: str, work_id: int):
    b64_data = data.replace('data:image/png;base64,', '')
    img_data = base64.b64decode(b64_data)
    filename = get_work_filename(work_id, result=True)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, 'wb') as f:
        f.write(img_data)

    return path_for_frontend(file_path)

def get_work_filename(work_id, result=False):
    filename = 'file_' + str(work_id)
    if result:
        filename += '_result'
    filename += '.png'
    return filename
