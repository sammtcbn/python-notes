#!/bin/bash
version=$(cat ./jsonfile1.json | python3 -c "import sys, json; print(json.load(sys.stdin)['version'])")
echo version is $version
