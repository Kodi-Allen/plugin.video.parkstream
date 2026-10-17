# ParkStream – South Park Kodi Add-on

Browse South Park seasons and watch episodes from the official South Park websites in Kodi,
with season covers, episode artwork and regional audio options.

**[Install](#installation)** ·
**[Documentation & screenshots](https://github.com/Kodi-Allen/kodi-repo/blob/main/docs/parkstream/README.md)** ·
**[Releases](https://github.com/Kodi-Allen/plugin.video.parkstream/releases)** ·
**[Report an issue](https://github.com/Kodi-Allen/plugin.video.parkstream/issues)**

| Kodi | Add-on ID | License |
|---|---|---|
| 21 (Omega) | `plugin.video.parkstream` | [GPL-2.0-only](LICENSE.txt) |

![ParkStream season list in Kodi with the season 1 cover and season description](https://raw.githubusercontent.com/Kodi-Allen/kodi-repo/main/docs/parkstream/screenshots/parkstream-kodi-season-list.jpg)

ParkStream is an unofficial, independently maintained fork of
[wargio/plugin.video.southpark_unofficial](https://github.com/wargio/plugin.video.southpark_unofficial).
It is distributed through the [Kodi Allen Repository](https://github.com/Kodi-Allen/kodi-repo).
The screenshot shows Kodi 21.1 with the Aeon Tajo skin; the appearance depends on your Kodi skin.

## Features

- Playback from the official South Park video service through Kodi's own player
- Season lists with covers, descriptions and premiere years
- Episode list with official episode stills, air dates and runtimes
- Show artwork (clear logo, clear art, banner, fan art) for Kodi skins that display it
- Random episode, optionally played directly
- Episodes with more than one audio track offer all tracks in Kodi's audio menu
- Menus in English, German, Italian, Portuguese (Brazil, Portugal), Spanish (Spain, Mexico)
  and Swedish

## Requirements

- **Kodi 21 (Omega)**, tested on a Vero 4K+ (OSMC) with Kodi 21.1.
- Access to the official South Park site for your selected region. Episode availability depends
  on your location and the regional catalogue.

Kodi 19, 20 and 22 have not been tested. No additional playback add-on is required for the
current HLS streams; `inputstream.adaptive` is not required.

## Installation

Recommended, with automatic updates:

1. Download the repository installer
   [`repository.kodiallen-1.0.1.zip`](https://github.com/Kodi-Allen/kodi-repo/raw/main/repository.kodiallen/repository.kodiallen-1.0.1.zip)
   to a location Kodi can access.
2. In Kodi, enable *Settings → System → Add-ons → Unknown sources*.
3. Open *Settings → Add-ons → Install from zip file* and select the repository ZIP.
4. Open *Install from repository → Kodi Allen Repository → Video add-ons → ParkStream* and
   select *Install*.
5. Start ParkStream from *Add-ons → Video add-ons → ParkStream*.

For manual installation without automatic updates, download the **add-on ZIP asset** from the
[releases](https://github.com/Kodi-Allen/plugin.video.parkstream/releases) and install it with
*Install from zip file*. Use the packaged `plugin.video.parkstream-….zip` asset rather than
GitHub's generated source archives. The [documentation](https://github.com/Kodi-Allen/kodi-repo/blob/main/docs/parkstream/README.md#installation)
describes both methods step by step.

## Usage

Select a season to browse its episodes, or choose **Random Episode**. Open the add-on settings
from ParkStream's context menu to configure:

| Setting | Effect |
|---|---|
| Geo Location | Selects the regional South Park site, which determines the audio and description language. *Germany* selects German, *North America[EN]* selects English. |
| Enable CC | Only applies to legacy streams; the current video service delivers no separate subtitles to the add-on. |
| Play directly the random episode | Starts a random episode instead of listing it first. |
| Show loading notification | Shows "Loading …" with the episode title while an episode starts. On by default. |
| Clear cache | Removes the cached episode lists. |

Confirm changes in the settings dialog with **OK**. Closing the dialog with *Back* discards them.
Kodi does not reload the list that is already on screen, so a new location shows up once you open
a folder or return to ParkStream.

## Known limitations

- Which episodes are available depends on your location and on the regional catalogue of the
  official site. A few episodes are not offered in every language.
- *North America[EN]* uses the English version of the official German-language site
  (`southpark.de/en`). The [documented location tests](https://github.com/Kodi-Allen/kodi-repo/blob/main/docs/parkstream/README.md#locations)
  were performed from Germany; availability elsewhere is not guaranteed. The official site
  may redirect or refuse requests from other countries.
- The official streams contain inserted advertising breaks.
- The current video service does not provide separate subtitles to the add-on.
- Season descriptions without a translation fall back to English.

## Support

For playback, language or cache problems, start with the
[troubleshooting guide](https://github.com/Kodi-Allen/kodi-repo/blob/main/docs/parkstream/README.md#troubleshooting).
For an outdated episode list, run **Clear cache** in the settings and reopen ParkStream.

If a problem persists, [open an issue](https://github.com/Kodi-Allen/plugin.video.parkstream/issues)
with your Kodi and ParkStream versions, device, selected *Geo Location*, affected episode and
steps to reproduce it.

## Data sources

- Episode lists: the `addon-data` branch of
  [wargio/plugin.video.southpark_unofficial](https://github.com/wargio/plugin.video.southpark_unofficial/tree/addon-data).
- Streams, episode stills, English and German season descriptions and runtimes: the official
  South Park websites.
- Spanish and Portuguese season descriptions: [TheTVDB](https://thetvdb.com/series/south-park).
  Locations without descriptions in their own language fall back to English.

## Development

The add-on is written in Python. Run the existing resolver tests with Python 3 from the
repository root; these tests do not need Kodi or live network requests:

```sh
python3 -m unittest discover -s tests -v
```

On Windows, use `python` in place of `python3` if that is your Python command.
The tests cover stream resolution with fixtures; they do not verify live playback or
regional availability.

`tools/generate-episode-metadata.py` regenerates `resources/data/episode-metadata.json`
from upstream episode lists and the official episode pages. It performs live requests;
see the script's help for region and worker options. Changes are recorded in
[changelog.txt](changelog.txt).

## Credits

- Original add-on *plugin.video.southpark_unofficial* by Giovanni Dante Grazioli (wargio)
- Contributors to the original add-on: anxdpanic, eldergabriel, mvn23, Niema Moshiri, serajr

## License

ParkStream is free software, licensed under the
[GNU General Public License, version 2](LICENSE.txt) (GPL-2.0-only).

- Copyright (C) 2015–2023 Giovanni Dante Grazioli (wargio) and contributors
- Copyright (C) 2026 Kodi-Allen — modifications for ParkStream, see [changelog.txt](changelog.txt)
  and the Git history for what was changed and when

The GPL applies to the source code. It does not cover the South Park artwork included for
identification (season covers, logos, fan art), which remains the property of its owners.

## Disclaimer

ParkStream is unofficial and not affiliated with or endorsed by South Park Studios,
Comedy Central or Paramount. South Park and all related titles, characters and artwork are
trademarks and copyrights of their respective owners. Check your local laws before use.
