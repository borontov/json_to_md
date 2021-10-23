# The purpose of this script
To convert your data from json format to the markdown (.md files) format. 

For example if you want to move your notes from your Telegram messages/channels/groups to the Zettelkasten system in [Obsidian](https://obsidian.md/).

# Install
Just install [poetry](https://python-poetry.org/) and update script dependencies.

# Usage
1. Put your settings in `settings.py` and .json files with data (optionally, with attachments) in the appropriate data folder (`data/` by default, change in the `settings.py` file).
2. Add your Mako template in the `templates/` folder.
3. Create your template variable in the `templates.py` file.
4. Write your own handler and put it in the `handlers/` folder.
5. Change the `main.py` file using your template and handler.

# Participating in the development of this program
Contributions to this repo are warmly welcomed! Create issues and send pull requests!
