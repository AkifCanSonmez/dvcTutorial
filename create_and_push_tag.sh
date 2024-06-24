#!/bin/bash

# En son tag'i bul, yoksa v0 olarak başlat
latest_tag=$(git describe --tags `git rev-list --tags --max-count=1`)

if [ -z "$latest_tag" ]; then
    latest_tag="v0"
fi

tag_number=$(echo $latest_tag | grep -o -E '[0-9]+')
new_tag_number=$((tag_number + 1))
new_tag="v${new_tag_number}"

export NEW_TAG=$new_tag

echo $NEW_TAG

# Dataset'i DVC ve Git'e ekle, yeni tag oluştur ve push et
dvc remote add mygdrive gdrive://1DF5EZJzttjrHyuIW7dmwYeJsY0XmjJx4
dvc remote default mygdrive
dvc add dataset
dvc push
git add dataset.dvc .dvcignore
git commit -m "Update dataset with new images"
git tag $new_tag
git push origin $new_tag

# Yeni tag'i train script'ine parametre olarak geçir
echo $new_tag > new_tag.txt