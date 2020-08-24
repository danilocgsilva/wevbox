from wevbox.fn import create_first

def wevbox():
    folder_created = create_first('/tmp')
    print("Created folder: " + folder_created)