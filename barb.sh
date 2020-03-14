#!/usr/bin/env zsh
JSON=$(youtube-dl -j --flat-playlist 'https://www.youtube.com/user/VideoGameSeppuku/videos')
echo $JSON | jq 'select(.title | match("SMM")) | .title' 
