#!/bin/sh

chmod 755 tts.sh

speakword=$1

espeak -ven+f3 -k10 -s150 "$speakword"