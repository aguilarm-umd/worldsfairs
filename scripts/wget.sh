#!/bin/bash

wget \
  --no-clobber \
  --convert-links \
  --page-requisites \
  --adjust-extension \
  --input-file=data/wget-urls.txt

