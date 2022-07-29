## Issue "context canceled"

Using `caddy` and `ffmpeg` to try to real-time stream data to a server runs into an issue caused by `caddy` closing the connection before properly being able to be handled by `nginx` or `uwsgi`.
nginx seem to fair a bit better by only having problems with the `init.mp4` and the `m3u8` (playlist) file, but uwsgi get tons of OSErrors.
This is not really an acceptable solution, as we need this for our projects to work properly.

### How to use

- `docker compose build`
- `docker compose up -d`
- Run `ffmpeg/ll_hls.sh` in a separate console
- Check the logs of `uwsgi` or `nginx`

### Info

If you actually point the target in ll_hls.sh to the server itself (uwsgi:8002, nginx:8000), then the PUT request work totally fine, it's just when `caddy` is inbetween that it starts to cause issues.

