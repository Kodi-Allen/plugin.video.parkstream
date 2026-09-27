#!/usr/bin/python3
# Copyright (C) 2026 Kodi-Allen
# SPDX-License-Identifier: GPL-2.0-only
"""Regenerate resources/data/episode-metadata.json (runtimes, genres, studio).

Reads the episode lists of the selected regions and fetches each episode page
from the official South Park websites. Run from the repository root:

    python3 tools/generate-episode-metadata.py [--regions de en] [--workers 8]
"""

import argparse
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140.0 Safari/537.36"
REGIONS = {
	"de": "https://www.southpark.de",
	"eu": "https://www.southparkstudios.com",
	"en": "https://www.southparkstudios.com",
	"es": "https://www.southparkstudios.com",
	"se": "https://www.southparkstudios.nu",
	"br": "https://www.southparkstudios.com.br",
	"lat": "https://www.southpark.lat",
}
DATA_URL = "https://raw.githubusercontent.com/wargio/plugin.video.southpark_unofficial/addon-data/addon-data-{}.json"


def _get_json(url):
	request = Request(url, headers={"User-Agent": USER_AGENT})
	with urlopen(request, timeout=30) as response:
		return json.loads(response.read().decode("utf-8"))


def _video_detail(value):
	if isinstance(value, dict):
		props = value.get("props")
		if value.get("type") == "Player" and isinstance(props, dict):
			detail = props.get("videoDetail")
			if isinstance(detail, dict):
				return detail
		detail = value.get("videoDetail")
		if isinstance(detail, dict):
			return detail
		for child in value.values():
			detail = _video_detail(child)
			if detail:
				return detail
	elif isinstance(value, list):
		for child in value:
			detail = _video_detail(child)
			if detail:
				return detail
	return None


def _metadata(detail):
	result = {}
	duration = detail.get("duration")
	if isinstance(duration, dict):
		milliseconds = duration.get("milliseconds")
		if isinstance(milliseconds, int) and milliseconds > 0:
			result["duration"] = milliseconds // 1000
	genres = detail.get("genres")
	if isinstance(genres, list):
		genres = [genre for genre in genres if isinstance(genre, str) and genre]
		if genres:
			result["genres"] = genres
	channel = detail.get("channel")
	if isinstance(channel, dict):
		studio = channel.get("name")
		if isinstance(studio, str) and studio:
			result["studio"] = studio
	return result


def _episode_candidates(regions):
	candidates = {}
	for region in regions:
		data = _get_json(DATA_URL.format(region))
		for season in data.get("seasons", []):
			for episode in season:
				uuid = episode.get("uuid")
				path = episode.get("url")
				if uuid and path:
					candidates.setdefault(uuid, []).append(REGIONS[region] + path)
	return candidates


def _episode_metadata(item):
	uuid, urls = item
	for url in urls:
		try:
			detail = _video_detail(_get_json(url + ("&" if "?" in url else "?") + "json=true"))
			if detail:
				metadata = _metadata(detail)
				if metadata:
					return uuid, metadata, None
		except Exception as error:
			last_error = error
	return uuid, None, last_error if "last_error" in locals() else "no videoDetail"


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--output", default=os.path.join("resources", "data", "episode-metadata.json"))
	parser.add_argument("--workers", type=int, default=8)
	parser.add_argument("--regions", nargs="+", choices=sorted(REGIONS), default=list(REGIONS))
	args = parser.parse_args()

	candidates = _episode_candidates(args.regions)
	episodes = {}
	failures = []
	with ThreadPoolExecutor(max_workers=args.workers) as executor:
		futures = [executor.submit(_episode_metadata, item) for item in candidates.items()]
		for future in as_completed(futures):
			uuid, metadata, error = future.result()
			if metadata:
				episodes[uuid] = metadata
			else:
				failures.append((uuid, str(error)))

	with open(args.output, "w", encoding="utf-8") as output:
		json.dump({"episodes": episodes}, output, ensure_ascii=False, indent=2, sort_keys=True)
		output.write("\n")

	print("Wrote {} of {} episodes to {}".format(len(episodes), len(candidates), args.output))
	for uuid, error in sorted(failures):
		print("Missing {}: {}".format(uuid, error))


if __name__ == "__main__":
	main()
