# remove-all-discord-messages-client
A simple Discord client for removing all user messages from the specified server written in Python

## Usage
In order to run this client you must have Python installed on your machine: https://www.python.org/downloads/  
Also, you will need Git for downloading the project: https://git-scm.com/downloads. If you do not want to install Git, just download repository manually as an archive.

1. Install `discord.py` Python library for accessing the Discord API:
```sh
pip install discord.py
```
2. Clone the client repository:
```sh
git clone git@github.com:shevtsiv/remove-all-discord-messages-client.git
```
3. Modify the `remove-all-discord-messages-client/main.py` script by inserting your Discord token and Server ID, from which you want delete all your messsages:  
  3.1 Go to Google Chrome Developer Tools, switch to mobile view, open Local Storage and copy "token"'s value. Replace the placeholder in main.py for the value you copied.  
  3.2 Go to Discord Settings -> Advanced Tab, enable Developer Mode. Then right click on Server name in the left upper corner and hit "Copy ID". Replace the placeholder in main.py for the value you copied.  
4. Run the script:
```sh
python ./remove-all-discord-messages-client/main.py
```
