#!/bin/bash

wget \
  --no-clobber \
  --convert-links \
  --page-requisites \
  --adjust-extension \
  --input-file=- << 'END'
https://digital.lib.umd.edu/worldsfairs
https://digital.lib.umd.edu/worldsfairs/about
https://digital.lib.umd.edu/worldsfairs/essays
https://digital.lib.umd.edu/worldsfairs/exhibits
https://digital.lib.umd.edu/worldsfairs/documentation
https://digital.lib.umd.edu/worldsfairs/rights
https://digital.lib.umd.edu/worldsfairs/browse
END
