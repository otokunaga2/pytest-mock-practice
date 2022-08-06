from os import remove
from os.path import isfile
import traceback
ERROR_MESSAGE_FILE_NOT_EXIST='ファイルが存在しません。'
ERROR_MESSAGE_FILE_DElETED='ファイルを削除しました。'
ERROR_MESSAGE='エラーが発生しました。'
def delete_file(file_path):
    try:
        if not isfile(file_path):
            return ERROR_MESSAGE_FILE_NOT_EXIST
        remove(file_path)
        return ERROR_MESSAGE_FILE_DElETED
    except:
        print(traceback.format_exc())
        return ERROR_MESSAGE
