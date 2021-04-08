cmake_minimum_required(VERSION 3.6)

include(ExternalProject)

project(NVM-Controller C)

# The default C Flags
set(CMAKE_C_FLAGS
"${CMAKE_C_FLAGS} \
-O2 \
-std=c99 \
-Wall \
-g \
-fstrict-aliasing \
-Wstrict-aliasing \
"
)

# Compile the source
add_subdirectory(src)

