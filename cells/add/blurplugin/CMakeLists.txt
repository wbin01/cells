cmake_minimum_required(VERSION 3.22)
project(blurplugin LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Encontre os pacotes do Qt6
find_package(Qt6 REQUIRED COMPONENTS Core Gui Quick WaylandClient)


# Inclua os diretórios do Qt e do Wayland
include_directories(
    ${Qt6Core_INCLUDE_DIRS}
    ${Qt6Gui_INCLUDE_DIRS}
    ${Qt6Quick_INCLUDE_DIRS}
    ${Qt6WaylandClient_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}  # Para o blur-client-protocol.h
)

# Arquivo gerado por wayland-scanner
set(BLUR_PROTOCOL_SRC
    ${CMAKE_CURRENT_SOURCE_DIR}/blur-client-protocol.h
)

# Adicione o arquivo-fonte do plugin
add_library(blurplugin SHARED
    blurplugin.cpp
    ${BLUR_PROTOCOL_SRC}
)

# Link com bibliotecas Qt e Wayland necessárias
target_link_libraries(blurplugin
    Qt6::Core
    Qt6::Gui
    Qt6::Quick
    Qt6::WaylandClient
    wayland-client
)

# Defina include dirs privados se necessário
target_include_directories(blurplugin PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    /usr/include/x86_64-linux-gnu/qt6/QtGui/6.8.3/QtGui/private
)

# Defina a pasta de saída do plugin
set_target_properties(blurplugin PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)
