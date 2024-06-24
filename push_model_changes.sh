#!/bin/bash

# Model dosyalarını ve yapılandırmaları Git ile takip altına al
git add models/$NEW_TAG/*.h5
git commit -m "Add trained model for version $(cat new_tag.txt)"

# Değişiklikleri uzak repoya push et
git push origin master