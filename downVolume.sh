#!/bin/bash

echo "hello"

amixer sset Master 10%-

sudo amixer cset numid=3 1

amixer cset numid=1 400

