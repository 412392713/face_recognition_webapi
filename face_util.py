# -*- coding: utf-8 -*-


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return  file_ext(filename) in ALLOWED_EXTENSIONS
    
def file_ext(filename):
    if '.' in filename:
        names = filename.rsplit('.', 1)
        return names[len(names)-1].lower()
    return ''
    
