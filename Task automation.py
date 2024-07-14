import os
import shutil
from collections import defaultdict
def organize_files(directory):
    file_types = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'xlsx', 'ppt', 'pptx', 'csv'],
        'Audio': ['mp3', 'wav', 'aac', 'flac'],
        'Video': ['mp4', 'mkv', 'mov', 'avi', 'flv'],
        'Archives': ['zip', 'tar', 'gz', 'rar'],
        'Scripts': ['py', 'js', 'sh', 'bat'],
    }
    extension_to_category = defaultdict(lambda: 'Others')
    for category, extensions in file_types.items():
        for extension in extensions:
            extension_to_category[extension] = category
    for category in file_types.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1].lower()
            category = extension_to_category[file_extension]
            destination_folder = os.path.join(directory, category)
            shutil.move(os.path.join(directory, filename), os.path.join(destination_folder, filename))
    print(f"Files in '{directory}' have been organized.")
organize_files('/path/to/your/directory')