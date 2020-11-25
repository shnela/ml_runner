# Instruction to copy

## Run flask shell
```bash
# Go to WorkingDir
cd /cygdrive/c/Users/NobleProg/WorkingDir/
# activate environment
source ./virtualenvs/cygin_env/bin/activate
# go to project dir
cd ./ml_runner

# run flask shell
FLASK_APP='main.py' SECRET_KEY='123' flask shell
```

## Update virtual env in cygwin
```bash
# Go to WorkingDir
cd /cygdrive/c/Users/NobleProg/WorkingDir/
# activate environment
source ./virtualenvs/cygin_env/bin/activate

# install all missing requirements
pip install -r ./ml_runner/requirements.txt
```