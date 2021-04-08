# CMAKE toolchain for the MSP430FR microcontroller

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR msp430)

set(DEVICE "msp430fr5994" CACHE STRING "")
string(TOUPPER ${DEVICE} DEVICE_DEFINE)
set(DEVICE_DEFINE "__${DEVICE_DEFINE}__")

# MSP430 support files (installation dependent)
set(PATH_MSP430_SUPPORT "/opt/msp430-gcc-support-files/include" CACHE STRING "")
set(PATH_MSP430_LIB "/opt/msp430/msp430-elf" CACHE STRING "")
set(PATH_MSP430_BIN "/opt/msp430/bin" CACHE STRING "")
set(PATH_MSP430_INCLUDE "/opt/msp430/lib/gcc/msp430-elf/8.2.0/include" CACHE STRING "")

# Device specific driverlib
set(PATH_MSP430_DRIVERS "${PROJECT_SOURCE_DIR}/MSP430FR5xx_6xx" CACHE STRING "")

# default linkersctip
set(LINKER_SCRIPT
    "${PROJECT_SOURCE_DIR}/${DEVICE}.ld"
    CACHE
    FILEPATH "linkerscript"
    )

set(CMAKE_C_COMPILER    "${PATH_MSP430_BIN}/msp430-elf-gcc")
set(CMAKE_CXX_COMPILER  "${PATH_MSP430_BIN}/msp430-elf-g++")
set(CMAKE_AR            "${PATH_MSP430_BIN}/msp430-elf-ar")
set(CMAKE_LINKER        "${PATH_MSP430_BIN}/msp430-elf-ld")
set(CMAKE_NM            "${PATH_MSP430_BIN}/msp430-elf-nm")
set(CMAKE_OBJDUMP       "${PATH_MSP430_BIN}/msp430-elf-objdump")
set(CMAKE_STRIP         "${PATH_MSP430_BIN}/msp430-elf-strip")
set(CMAKE_RANLIB        "${PATH_MSP430_BIN}/msp430-elf-ranlib")
set(CMAKE_SIZE          "${PATH_MSP430_BIN}/msp430-elf-size")


# Compiler flags
set(COMMON_FLAGS "-gdwarf-3 -gstrict-dwarf -I${PATH_MSP430_SUPPORT} -I${PATH_MSP430_LIB} -I${PATH_MSP430_DRIVERS} -I${PATH_MSP430_INCLUDE}" CACHE STRING "")

#set(MCU_SPECIFIC_CFLAGS "-mmcu=msp430fr5994 -mhwmult=f5series -mcode-region=none -mdata-region=none -mlarge" CACHE STRING "")
set(MCU_SPECIFIC_CFLAGS "-MD -mhwmult=f5series -mmcu=${DEVICE} -D${DEVICE_DEFINE} -mlarge -fno-builtin" CACHE STRING "")

set(CMAKE_C_FLAGS "${MCU_SPECIFIC_CFLAGS} ${COMMON_FLAGS}" CACHE STRING "")

# Linker flags
set(MCU_SPECIFIC_LINKER_FLAGS "-L${PATH_MSP430_LIB}/lib/large" CACHE STRING "")
set(CMAKE_EXE_LINKER_FLAGS "${MCU_SPECIFIC_LINKER_FLAGS} -L${PATH_MSP430_SUPPORT} -T${LINKER_SCRIPT} -Wl,--gc-sections -Wl,-Map,\"${PROJECT_NAME}.map\" -Wl,-lgcc -Wl,-lc" CACHE STRING "")

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
