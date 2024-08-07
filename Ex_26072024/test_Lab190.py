import pytest

@pytest.fixture()
def sample_data_1():
    data =  [1, 2, 3, 4]
    return data
@pytest.fixture()
def sample_data_2():
    return True

def test_sample_data_1_2(sample_data_1, sample_data_2):
    print(sample_data_1)
    print(sample_data_2)
