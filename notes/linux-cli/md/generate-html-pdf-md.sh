#!/bin/bash

# File: generate-html-pdf-md.sh

# Output both .md of HTML/PDF table of contents (head) with content (body)

(cat index-html.md && cat linux-cli-body.md) > linux-cli-latest-html.md
(cat index-pdf.md && cat linux-cli-body.md) > linux-cli-latest-pdf.md

# Export as HTML/PDF in ReText
