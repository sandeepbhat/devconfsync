# devconfsync

`devconfsync` helps you backup your favorite developer settings.

## Usage
```bash
python3.7 devconfsync/main.py -c config.json
```
You can use the `config.json` under `sample` folder to get started.

## Config breakdown
Refer `sample/config.json` for details.

```
"destination" -> This needs to be a git repository with remote added.
```
```
"tools" -> devconfsync provides support to backup the configuration files for the following tools (as of today). Refer devconfsync/popular.py for the supported tools.
1. zsh
2. git
3. vscode
4. tmux
5. bash
```
```
"files" -> Any other files which are not covered by the list above.
```

## Publishing changes
`devconfsync` uses `gitpython`. It basically does the following (as of today).
1. Check if destination path is a git repo. If no fail.
2. Check if the git repo is dirty.
3. If yes, add all changes (equivalent of `git add --all` is used).
4. Make a commit.
5. Push changes to remote.
