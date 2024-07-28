#!/bin/bash

wget \
  --no-clobber \
  --convert-links \
  --page-requisites \
  --adjust-extension \
  --input-file=wget-urls.txt

