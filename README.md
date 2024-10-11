# Organize files

## An easy project, easy to understand, good to test out python and get a feel for it

> [!TIP]
> Check out Tim on youtube if you like python and projects like this. He is really good providing ideas you can do!

> [!Note]
> You will have to run the python file every time you want to clean up your downloads folder.
> I have fixed the script so the base file wont be touched. Just open the python file, with the Downloads directory and run the script and see the satisfying script take all the files get sorted and appended to folders on category. If you don't have any programming experience, the const
+ <code>SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt', '.docx', '.csv'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "EXCECUTABLES": ['.exe', '.zip', '.msi', '.gz'],
    "CODE": ['.java', '.cs', '.go', '.cpp'],
    "WEB": ['.html', '.css', '.js', '.ts']
}</code>.
1. Just change the names for example
+ <code>SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt', '.docx', '.csv'],
    "_MUSIC_": ['.m4a', '.m4b', '.mp3'],
    "_CORN_": ['.mov', _'.ogg',_ '.mp4'], **Joking**
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "EXCECUTABLES": ['.exe', '.zip', '.msi', '.gz'],
    "CORN": ['.java', '.cs', '.go', '.cpp']
    **DELETE** text if you don't want folder or this category as folder, remove the "," on the last line.
    _"WEB": ['.html', '.css', '.js', '.ts']_
}</code>
2. make another folder name, add/remove any '.file' to your liking. Easy as that. Or remove a whole line in the dict
