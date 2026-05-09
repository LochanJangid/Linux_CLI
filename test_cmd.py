import os
from check_cmd import check_command


def test_pwd():
    pwd = check_command(["pwd"])
    assert pwd == os.getcwd()

def test_mkdir():
    new_folder = check_command(["mkdir", "good_dir"])
    assert os.path.exists(new_folder) == True

def test_cd():
    past_pwd = check_command(["pwd"])
    work = check_command(["cd", "good_dir"])
    new_pwd = check_command(["pwd"])
    dir_name = new_pwd.replace(past_pwd, "")
    assert dir_name == "/good_dir"
    work2 = check_command(["cd", ".."])
    new_pwd = check_command(["pwd"])
    assert new_pwd == past_pwd

def test_ls():
    items = check_command(["ls"])
    assert items == os.listdir(os.getcwd())

def test_rmdir():
    old_folders = check_command(["rmdir", "good_dir"])
    assert os.path.exists(next(old_folders)) == False

def test_touch():
    old_files = check_command(["touch", "snake.py", "rockstar_file.txt"])
    assert os.path.exists(next(old_files)) == True
    assert os.path.exists(next(old_files)) == True

def test_cat():
    files = check_command(["cat", "non_existance_file.txt" "rockstar_file.txt"])
    for file in files:
        if file is not None:
            with open(file, "r") as f:
                content = f.read()
            assert file == content
        
def test_rm():
    removed_files = check_command(["rm", "rockstar_file.txt", "snake.py"])
    for file in removed_files:
        assert os.path.exists(file) == False

def test_cp():
    new_none_file = check_command(["cp", "file.txt", "new_file.txt"])
    make_file = check_command(["touch", "file.txt"]) # Making file with testing it 
    assert os.path.exists(next(make_file)) == True
    new_file = check_command(["cp", "file.txt", "new_file.txt"])
    assert new_none_file == None
    assert new_file == "new_file.txt"
    assert os.path.exists("file.txt") == True
    assert os.path.exists(new_file) == True

    # Clean the mess
    removed_files = check_command(["rm", "file.txt", "new_file.txt"])
    for file in removed_files:
        assert os.path.exists(file)  == False

def test_mv():
    new_none_file = check_command(["mv", "file.txt", "new_file.txt"])
    make_file = check_command(["touch", "file.txt"]) # Making file with testing it 
    assert os.path.exists(next(make_file)) == True
    new_file = check_command(["mv", "file.txt", "new_file.txt"])
    assert new_none_file == None
    assert new_file == "new_file.txt"   
    assert os.path.exists("file.txt") == False
    assert os.path.exists(new_file) == True

    # Clean the mess
    removed_files = check_command(["rm", "file.txt", "new_file.txt"])
    assert os.path.exists(next(removed_files))  == False
    assert os.path.exists(next(removed_files))  == False
    