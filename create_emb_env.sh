#!/bin/zsh

DIRS=("app" "middleware" "hal" "driver" "bsp")

for DIR_NAME in ${DIRS}; do
    mkdir -p "src/$DIR_NAME"
    mkdir -p "inc/$DIR_NAME"
done

mkdir -p thirdparty/freertos
mkdir -p thirdparty/seggar

mkdir tests
mkdir -p docs/adr
mkdir -p docs/pottery
mkdir build

mkdir -p stm32_cubemx/Core
mkdir -p stm32_cubemx/Drivers

echo "Folders created successfully!"

