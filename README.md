# ice_breaker

## Project setup

Clone the project
```bash
git clone -b 1-start-here https://github.com/khongks/ice_breaker
```

Open terminal, run pipenv shell
```bash
pipenv shell
```
Output:
```bash
Creating a virtualenv for this project...
Pipfile: /Users/kskhong/Documents/Dev/ice_breaker/Pipfile
Using default python from /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 (3.11.1) to create virtualenv...
⠸ Creating virtual environment...created virtual environment CPython3.11.1.final.0-64 in 276ms
  creator CPython3Posix(dest=/Users/kskhong/.local/share/virtualenvs/ice_breaker-y8_IJaW-, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/kskhong/Library/Application Support/virtualenv)
    added seed packages: pip==23.2.1, setuptools==68.2.2, wheel==0.41.2
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment!
Virtualenv location: /Users/kskhong/.local/share/virtualenvs/ice_breaker-y8_IJaW-
Creating a Pipfile for this project...
Launching subshell in virtual environment...
 . /Users/kskhong/.local/share/virtualenvs/ice_breaker-y8_IJaW-/bin/activate                                                                   
kskhong ~/Documents/Dev/ice_breaker [1-start-here] $  . /Users/kskhong/.local/share/virtualenvs/ice_breaker-y8_IJaW-/bin/activate
```

Note that the environment name created is `ice_breaker-y8_IJaW-`.

A pipfile is created
```[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.11"
```

Install langchain
```bash
pipenv install langchain
```
Output:
```bash
Installing langchain...
Resolving langchain...
Added langchain to Pipfile's [packages] ...
✔ Installation Succeeded
Pipfile.lock not found, creating...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (59562ce621fd68cbd9ce3e95f6a0608aa50beaf2ddd86881247be6f557e62ae9)!
Installing dependencies from Pipfile.lock (e62ae9)...
```

Switch interpreter to the environment.

Create a launch.json file and add the envFile:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Ice Breaker Runner",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true,
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```
---

Install black

```bash
pipenv install black
```

Install Google Search when using SerpAPI
```bash
pipenv install google-search-results
```


---

Install openai

```bash
pipenv install openai
pip install openai
```
Output:
```bash
Loading .env environment variables...
Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Installing openai...
Resolving openai...
Added openai to Pipfile's [packages] ...
✔ Installation Succeeded
Pipfile.lock (e62ae9) out of date, updating to (f13e5a)...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success!
Locking [dev-packages] dependencies...
Updated Pipfile.lock (759265c0a65a48af2dbaf704e313babe755b43f99dabfd1482ed9e0673f13e5a)!
Installing dependencies from Pipfile.lock (f13e5a)...
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```


