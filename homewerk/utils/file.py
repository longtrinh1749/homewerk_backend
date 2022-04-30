import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

UPLOAD_FOLDER = 'E:\\Projects\\Thesis\\Code\\frontend\\public\\img'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file, filename):
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return path_for_frontend(os.path.join(UPLOAD_FOLDER, filename))

def path_for_frontend(path):
    partial_paths = path.split('\\')
    partial_paths = partial_paths[6:]
    return '\\'.join(partial_paths)