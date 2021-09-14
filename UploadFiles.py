import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)

                with open(localPath, "rb") as f:
                    dbx.files_upload(f.read().dropboxPath, mode=WriteMode("overwrite"))


def main():
    accessToken = "qB-2QXu6Q8UAAAAAAAAAAS9aieNCS29S1Jk-k1GfHIi0w2YaeMZ67m0wax_Hnqax"
    transferData = TransferData(accessToken)

    fileFrom = str(input("Enter the folder path to transfer: "))
    fileTo = input("Enter the full path to upload to DropBox: ")

    transferData.uploadFile(fileFrom, fileTo)
    print("Moved!")


main()
