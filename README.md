# Increase payout mod for Project Hospital
Increases payout for all Diagnoses by a modifier. Includes python script to generate modified files.

Tested on version 1.1.17753

## Using the mod
Put the mod folder in `ProjectHospital_Data\StreamingAssets\Addons` in the game folder.

## Requirements for script
- Project Hospital installed
- Python 3

## Running the script
- If the game is not installed from Steam to default folder, modify `gamePath` accordingly.
- Run the script with `python3 generate_xml.py`

## Publish to Steam Workshop
Using Steam CMD (https://developer.valvesoftware.com/wiki/SteamCMD, https://developer.valvesoftware.com/wiki/Command_Line_Options)

Change values in the .vdf file to match your setup.
- `appid` is the Steam ID of the game
- `publishedfileid` is the ID of the workshop file, set to 0 to upload new item.
- `contentfolder` and `previewfile` paths to mod content and preview image. Relative paths doesn't seem to work.
- `visibility` 0 = Public, 1 = Friends only, 2 = Hidden
- `title`, `description` and `changenote` is quite self explanatory.

### Run in Steam CMD
- `login <username>`
- `workshop_build_item C:\code\Mod_Increase_Payout\Increase_Payout.vdf`