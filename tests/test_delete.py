import os
import src.code  as code
import pytest


@pytest.fixture(autouse=True)
def init_mock(mocker):
    #code内の関数をそれぞれmock化
    #共通処理はfixtureでまとめて記載する
    def isdelete_mock_func(file_path):
        return True
    mocker.patch('src.code.remove', isdelete_mock_func)

def is_file_mock_func_return_true(file_path):
    return True
def is_file_mock_func_return_false(file_path):
    return False

def test_file_not_exist_with_mock_func(mocker):
    #code内の関数をそれぞれmock化
    mocker.patch('src.code.isfile', is_file_mock_func_return_false)
    message = code.delete_file('test_file_path')
    assert message == 'ファイルが存在しません。'
def test_failed_file_not_exist(mocker):
    #code内の関数をそれぞれmock化
    #常にTrue
    mocker.patch('src.code.isfile', is_file_mock_func_return_true)
    # テスト対象を実行する
    message = code.delete_file('test_file_path')
    # 戻り値のメッセージを検証
    assert message == 'ファイルを削除しました。'
