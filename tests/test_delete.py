import os
import src.code  as code



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
    message = code.delete_file('test_file_path')

    # 戻り値のメッセージを検証
    assert message == 'ファイルが存在しません。'
