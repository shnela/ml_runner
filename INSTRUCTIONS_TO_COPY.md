# Instruction to copy

## Create virtualenv

### Ubuntu
```bash
np@jakub-ch3j:/mnt/c/Users/NobleProg/WorkingDir$ python3 -m venv ./virtualenvs/ubuntu_env
np@jakub-ch3j:/mnt/c/Users/NobleProg/WorkingDir$
```

### Cygwin
```bash
NobleProg@jakub-ch3j /cygdrive/c/Users/NobleProg/WorkingDir
$ python3.8.exe -m venv ./virtualenvs/cygwin_env

NobleProg@jakub-ch3j /cygdrive/c/Users/NobleProg/WorkingDir
$
```

## Update virtual (Ubuntu)
```bash
# activate environment
source ./virtualenvs/ubuntu_env/bin/activate

# install all missing requirements
pip install -r ./ml_runner/requirements.txt
```

## Run flask shell
```bash
# activate environment
source ./virtualenvs/cygin_env/bin/activate
# go to project dir
cd ./ml_runner
# export variables
source ./environment.env

# run flask shell
flask shell
```
