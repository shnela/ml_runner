# README

## Tworzenie środowiska wirtualnego

### Cygwin
[Instrukcja](https://docs.python.org/3/library/venv.html#creating-virtual-environments) z dokumentacji pythona.

```bash
# przejście do WorkingDir
cd /cygdrive/c/Users/NobleProg/WorkingDir/
# stworzenie środowiska wirtualnego
python3.8.exe -m venv ./virtualenvs/cygin_env
# aktywacja środowiska
source ./virtualenvs/cygin_env/bin/activate
```

### pyCharm
```
File | Settings | Project: ml_runner | Python Interpreter
```
Klikamy w gearbox w prawym górnym rogu i `Add...`, tworzymy `Virtualenv Environment`


## Nowe zależności
* flask

### Cygwin

```bash
# przejście do WorkingDir
cd /cygdrive/c/Users/NobleProg/WorkingDir/
# aktywacja środowiska
source ./virtualenvs/cygin_env/bin/activate
# sprawdzenie zainstalowanych paczek
pip freeze
# instalacja flaska
pip install flask
# sprawdzenie zainstalowanych paczek
pip freeze
# stworzenie pliku requirements.txt z zainstalowanymi zależnościami
pip freeze > ml_runner/requirements.txt
```

### pyCharm
```
File | Settings | Project: ml_runner | Python Interpreter
```
Dodanie `flask`.

## Uruchomienie aplikacji

### Cygwin
```bash
# set location to working directory
$ cd /cygdrive/c/Users/NobleProg/WorkingDir/

# activate env
$ source ./virtualenvs/cygwin_flask_env/bin/activate

# go to project dir
cd ./ml_runner/
 
# run application
$ FLASK_APP='main.py' flask run
```

### Pycharm
1. `Add configuration...` na górze po prawej
2. New `Python` configuration
3. Script path: file `main.py`
4. Add `app.run()` inside `main.py`
5. Click run (green play button)
