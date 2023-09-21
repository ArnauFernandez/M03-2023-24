#!/bin/bash


softPath="$(pwd)"


# Create data folders on data

mkdir -p $softPath/userdata/.cache/JetBrains

mkdir -p $softPath/userdata/.m2

mkdir -p $softPath/userdata/.gradle

mkdir -p $softPath/userdata/.config/JetBrains

mkdir -p $softPath/userdata/.jdks


# Delete current ones

rm -rf ~/.cache/JetBrains

rm -rf ~/.m2

rm -rf ~/.gradle

rm -rf ~/.config/JetBrains

rm -rf ~/.jdks


# Create links

ln -s $softPath/userdata/.cache/JetBrains ~/.cache/JetBrains

ln -s $softPath/userdata/.m2 ~/.m2

ln -s $softPath/userdata/.gradle ~/.gradle

ln -s $softPath/userdata/.config/JetBrains ~/.config/JetBrains

ln -s $softPath/userdata/.jdks ~/.jdks


#cd idea-IC-222.3739.54/bin/

cd pycharm-community-2022.2.1/bin/

./pycharm.sh