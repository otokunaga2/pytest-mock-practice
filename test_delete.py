import os


# テスト対象のメソッド
def delete_file(file_path):
    try:
        if not os.path.isfile(file_path):
            return 'ファイルが存在しません。'
        
        os.remove(file_path)

        return 'ファイルを削除しました。'
    except:
        return 'エラーが発生しました。'


def test_file_not_exist_with_mock_func(mocker):
    def isfile_mock_func(file_path):
        return False
    #サイドエフェクトを利用
    mocker.patch('os.path.isfile', side_effect=isfile_mock_func)
    message = delete_file('test_file_path')
    assert message == 'ファイルが存在しません。'
def test_file_not_exist(mocker):
    # os.path.isfile をモック化する(常にFalse)
    mocker.patch('os.path.isfile', return_value=False)

    # テスト対象を実行する
    message = delete_file('test_file_path')

    # 戻り値のメッセージを検証
    assert message == 'ファイルが存在しません。'
