import pytest
from group_by_group_name import groupByGroupName

@pytest.mark.parametrize("input,expected", [('''
user1 group1 001 /usr/bin/
user2 group3 002 /usr/bin/
user3 group2 003 /usr/bin/
user4 group1 004 /usr/bin/
user5 group2 005 /usr/bin/
''', '''
user1 group1 001 /usr/bin/
user4 group1 004 /usr/bin/
user3 group2 003 /usr/bin/
user5 group2 005 /usr/bin/
user2 group3 002 /usr/bin/
'''),])

def testValidInput(input,expected):
    assert groupByGroupName(input) == expected

@pytest.mark.parametrize("input", ["abc", "abc xyz"])
def groupByGroupName(input):
    with pytest.raises(ValueError):
        groupByGroupName(input)