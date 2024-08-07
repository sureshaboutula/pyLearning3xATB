# Fixture - Concept in Python
# You can use the fixture - to perform multiple tasks
# Fixture basically used to provide context to the test --> Similar to Pre condition and Post condition

#setUP and TearDown --> Pre and Post condition

# Example
# test_update_negative_1
# test_update_positive_2
# Above 2 methods need token, bookingid as pre condition --> Can be done using fixture

import pytest

@pytest.fixture()
def is_married():
    return True

def test_i_need_a_confirmation(is_married):
    assert is_married == True
    print("You are married")
