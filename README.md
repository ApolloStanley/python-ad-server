# Local VAST Ad Test Server

A small, dependency-free HTTP server for testing video ad playback on Roku
(and any VAST-compatible player). It serves a VAST tag, streams a local `.mp4`
as the ad creative, and logs every tracking beacon the player fires — including
the Roku ad watermark header — so you can confirm an ad actually launched and
ran end to end.

Everything is standard-library Python 3. No `pip install` required.

## What it does

When a player requests an ad, the server returns a VAST XML document. That VAST
points the player back at this same server for two things:

1. **The media file** — the `.mp4` creative, served with HTTP Range support so
   the player can seek and the server can handle skips cleanly.
2. **Tracking beacons** — impression, start, quartile, and complete pixels. Each
   time the player fires one, the server logs it, so you get a live trace of how
   far playback progressed.

The server also inspects the `X-Roku-Ad-Watermark` header on every request and
prints whether it was `PRESENT` or `ABSENT`, along with the raw JWT if present
(decode it at jwt.io).

## Core layout

The whole thing is one script. The pieces, top to bottom:

**Configuration constants**
- `PORT` — the listen port (default `8082`).
- `MEDIA_FILE` — path to the `.mp4` served as the creative (default
  `./media/ad_one.mp4`).
- `MEDIA_ROUTES` — the URL paths the player may request for the video
  (`/media.mp4`, `/media`). These are just labels mapped to `MEDIA_FILE` on
  disk; they don't have to match the file's real location.

**Helpers**
- `my_ip()` — figures out the machine's LAN IP so the VAST URLs are reachable
  from the Roku device, not just localhost. It tries `ipconfig getifaddr` first,
  then falls back to opening a throwaway UDP socket toward `8.8.8.8` to ask the
  OS which local address it would route from (no packets are actually sent).
- `ensure_media_file(url)` — checks whether the creative exists; if not, and a
  `--media-url` was given, downloads it once.

**VAST templates**
- `vast_simple()` — a minimal 10-second VAST with `start` and `complete`
  tracking only.
- `vast_custom()` — a 30-second VAST with the full set of quartile beacons
  (`firstQuartile`, `midpoint`, `thirdQuartile`) plus `start` and `complete`.
- `VASTS` — a dict mapping the names `"simple"` and `"custom"` to those
  functions, used to look up which tag to serve.

**The request handler (`My_Server`)**
- `_server_media()` — streams the `.mp4` with Range / `206 Partial Content`
  support, returns `416` when the requested start is past end-of-file, and
  swallows broken-pipe errors that happen normally when a player seeks or skips.
- `_handle()` — the single entry point for `GET`, `POST`, and `HEAD`. It
  classifies each incoming request as one of three things:
  - **Media request** (path is in `MEDIA_ROUTES`) → serve the video.
  - **Ad request** (no query string, path is `/`, `/vast`, `/ad`, or a named
    VAST like `/custom`) → serve a VAST document.
  - **Beacon / impression** (has a query string like `/?start`) → log it and
    return an empty `200` pixel.

The key distinction: a request only counts as an **ad request** when it has **no
query string**. A beacon is identified *by* its query string (e.g. `/?complete`),
which is how the server tells "give me an ad" apart from "I just hit the start of
the ad."

## URL map

| URL | What it returns |
|-----|-----------------|
| `http://<IP>:<PORT>/` | The default VAST (set via `--vast`) |
| `http://<IP>:<PORT>/vast`, `/ad` | Same as `/` — the default VAST |
| `http://<IP>:<PORT>/simple` | The simple VAST, regardless of default |
| `http://<IP>:<PORT>/custom` | The custom VAST with quartile beacons |
| `http://<IP>:<PORT>/media.mp4`, `/media` | The `.mp4` creative (Range-enabled) |
| `http://<IP>:<PORT>/?start`, `/?complete`, etc. | Tracking beacon → empty `200` |

## Running the server

From the directory containing the script:

```bash
python3 server.py
```

On start it prints the URLs you'll need, e.g.:

```
Serving on http://192.168.1.50:8082/  (default VAST: simple) (ctrl-C to stop)
  ad-request URL for raf.force.ad_url:  http://192.168.1.50:8082/
  force a specific VAST:                http://192.168.1.50:8082/custom
  media file served at:                 http://192.168.1.50:8082/media.mp4
```

Stop it with `Ctrl-C`.

### Command-line options

| Flag | Default | Purpose |
|------|---------|---------|
| `--vast {simple,custom}` | `simple` | Which VAST is served at `/`, `/vast`, `/ad` |
| `--media-file PATH` | `./media/ad_one.mp4` | Local `.mp4` to serve as the creative |
| `--media-url URL` | (none) | Direct `.mp4` URL to download once if the media file is missing |

Examples:

```bash
# Serve the custom (quartile-tracked) VAST by default
python3 server.py --vast custom

# Use a specific local file
python3 server.py --media-file ./media/ad_one.mp4

# Auto-download a creative the first time if it's not on disk
python3 server.py --media-url https://example.com/sample.mp4
```

### Prerequisites

- Python 3.
- An `.mp4` at `MEDIA_FILE` (or pass `--media-url` to fetch one once).
- The Roku device and the machine running this server on the **same network**,
  so the device can reach the LAN IP the server prints.

## Setting `raf.force.ad_url`

See internal roku documentation for config_set command.

## Reading the logs

Each request prints a block. A typical successful playthrough looks like:

```
=== AD-REQUEST GET / ===          ← player fetched the VAST
=== MEDIA GET /media.mp4 ===      ← player started streaming the creative
=== BEACON GET /?start ===        ← playback began
=== BEACON GET /?complete ===     ← playback finished
```

If you only ever see the `AD-REQUEST` line and no `MEDIA` line, the player got
the tag but never started the creative — usually a media URL reachability or
format issue. If you see `MEDIA` and `start` but no `complete`, the ad was
exited or skipped before the end.