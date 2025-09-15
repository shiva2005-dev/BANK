import pytest
import project
def test_choice():
    with pytest.raises(TypeError):
        project.choice("a")
    with pytest.raises(TypeError):
        project.choice(6)
def test_add():
    assert project.add(100)=="After adding balance is 1100"
    with pytest.raises(SystemExit):
        project.add("a")
def test_sub():
    assert project.sub(100)=="After subtracting balance is 1000"
    with pytest.raises(SystemExit):
        project.sub("a")
def test_bal():
    assert project.bal()=="The balance is 1000"