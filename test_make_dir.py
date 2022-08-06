import os
import pytest

# テストメソッドごとに呼び出されるフィクスチャ
@pytest.fixture(autouse=True)
def init_mock(mocker):
    mocker.patch('os.makedirs')
    mocker.patch('os.makedirs')

def test_case_1():
    os.makedirs('./a/b/c', exist_ok=True)
    assert os.makedirs.called

def test_case_2():
    os.makedirs('./a/b/c', exist_ok=True)
    assert os.makedirs.called
