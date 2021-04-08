
include_directories(
    "${PROJECT_SOURCE_DIR}/include"
    "${PROJECT_BINARY_DIR}/include"
    )

set(ELF_FILE ${PROJECT_NAME}.elf)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR})

add_executable(${ELF_FILE}
    "${PROJECT_SOURCE_DIR}/src/main.c"
    "${PROJECT_SOURCE_DIR}/src/debug.c"
    "${PROJECT_SOURCE_DIR}/src/ports.c"
    "${PROJECT_SOURCE_DIR}/src/mpy_comm.c"
    "${PROJECT_SOURCE_DIR}/src/checkpoint.c"
    "${PROJECT_SOURCE_DIR}/src/checkpoint_ctrl.c"
    "${PROJECT_SOURCE_DIR}/MSP430FR5xx_6xx/eusci_b_spi.c"
    "${SOURCE_FILES}"
    )
