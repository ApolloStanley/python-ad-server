# Local VAST Ad Test Server

A small, dependency-free HTTP server for testing video ad playback on Roku
(and any VAST-compatible player). It serves a VAST tag, streams a local `.mp4`
as the ad creative, and logs every tracking beacon the player fires — including
the Roku ad watermark header — so you can confirm an ad actually launched and
ran end to end.

Everything uses the Python standard library; Python 3.14 or later is required.
No `pip install` required.

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

The HTTP server is in `server.py`; VAST templates live under `media/VAST/`.

**Configuration constants**
- `PORT` — the listen port (default `8082`).
- `MEDIA_FILE` — path to the `.mp4` served as the creative (default
  `./media/ad_one.mp4`).
- `MEDIA_FILES` — maps media URLs to files. `/media.mp4` uses `MEDIA_FILE`;
  named and multi-stream examples use the bundled sample videos.

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
- `VASTS` — maps scenario names such as `"simple"`, `"custom"`, `"multiple"`,
  and `"multiview"` to their template functions.

**The request handler (`My_Server`)**
- `_server_media()` — streams the `.mp4` with Range / `206 Partial Content`
  support, including suffix ranges; returns `416` for unsatisfiable ranges and
  swallows broken-pipe errors that happen normally when a player seeks or skips.
- `_handle()` — the single entry point for `GET`, `POST`, and `HEAD`. It
  classifies each incoming request as one of four things:
  - **Media request** (path is in `MEDIA_FILES`) → serve the video.
  - **Ad request** (no query string, path is `/`, `/vast`, `/ad`, or a named
    VAST like `/custom`) → serve a VAST document.
  - **Beacon / impression** (has a query string like `/?start`) → log it and
    return an empty `200` pixel.
  - **Unknown URL** (no query and no matching route) → return `404`.

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
| `http://<IP>:<PORT>/multiple`, `/multiview`, `/stream1`, `/stream2`, `/stream3` | Multi-ad or stream-specific VAST examples |
| `http://<IP>:<PORT>/media.mp4` | The file selected by `--media-file` (Range-enabled) |
| `http://<IP>:<PORT>/ad_one.mp4`, `/ad_two.mp4`, `/640x360_1.mp4`–`/640x360_3.mp4` | Bundled sample videos (Range-enabled) |
| `http://<IP>:<PORT>/?start`, `/?complete`, etc. | Tracking beacon → empty `200` |
| Other paths without a query string | `404 Not Found` |

## Running the server

From the directory containing the script:

```bash
python3 server.py
```

On start it prints the URLs you'll need, e.g.:

```
Serving on http://192.168.1.50:8082/ (bound to 0.0.0.0; default VAST: simple) (ctrl-C to stop)
  ad-request URL for raf.force.ad_url:  http://192.168.1.50:8082/
  force a specific VAST:                http://192.168.1.50:8082/custom
  media file served at:                 http://192.168.1.50:8082/media.mp4
```

Stop it with `Ctrl-C`.

### Command-line options

| Flag | Default | Purpose |
|------|---------|---------|
| `--vast NAME` | `simple` | Which VAST is served at `/`, `/vast`, `/ad`; see `VASTS` in `server.py` for names |
| `--host ADDRESS` | `0.0.0.0` | Interface to bind; use `127.0.0.1` for local-only access |
| `--media-file PATH` | `./media/ad_one.mp4` | Local `.mp4` used by the simple VAST at `/media.mp4` |
| `--media-url URL` | (none) | Direct `.mp4` URL to download once if the media file is missing |

Examples:

```bash
# Serve the custom (quartile-tracked) VAST by default
python3 server.py --vast custom

# Use a specific local file
python3 server.py --media-file ./media/ad_one.mp4

# Auto-download a creative the first time if it's not on disk
python3 server.py --media-url https://example.com/sample.mp4

# Bind only to this computer (Roku devices on the network won't be able to connect)
python3 server.py --host 127.0.0.1
```

### Prerequisites

- Python 3.14 or later.
- An `.mp4` at `MEDIA_FILE` (or pass `--media-url` to fetch one once).
- The Roku device and the machine running this server on the **same network**,
  so the device can reach the LAN IP the server prints.

By default, the server listens on all interfaces and prints the full watermark
JWT when present. Use it only on a trusted network and avoid sharing those logs.

### Tests

Run the standard-library test suite with:

```bash
python3 -m unittest discover -s tests -v
```

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
