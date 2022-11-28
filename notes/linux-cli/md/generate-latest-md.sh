#!/bin/bash

# File: generate-latest-md.sh

# Output unified .md containing table of contents (head) with content (body)

(cat linux-cli-head.md && cat linux-cli-body.md) > ../linux-cli-latest.md
