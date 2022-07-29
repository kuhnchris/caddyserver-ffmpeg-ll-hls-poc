#!/bin/bash

ffmpeg -re -stream_loop -1 \
-f lavfi -i "mptestsrc=t=dc_luma" \
-c:v libx264 -b:v 5000k \
-c:a aac -b:a 128k -preset:v fast \
-filter:v "settb=AVTB,setpts='trunc(PTS/1K)*1K+st(1,trunc(RTCTIME/1K))-1K*trunc(ld(1)/1K)',drawtext=fontfile=bbb.ttf:text='%{localtime}.%{eif\:1M*t-1K*trunc(t*1K)\:d}':fontsize=48:x=100:y=50:box=1" \
-x264-params keyint=15:min-keyint=15 -g 2 -hls_time 2 \
-hls_segment_type fmp4 \
-method PUT -hls_list_size 10 -http_persistent 0 -f hls \
http://localhost:8888/example.m3u8
#http://localhost:8002/example.m3u8
