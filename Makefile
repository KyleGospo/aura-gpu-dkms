obj-m += aura-gpu.o

aura-gpu-objs := asic/asic-polaris.o asic/asic-vega.o asic/asic-navi.o atom/atom.o aura-gpu-reg.o aura-gpu-i2c.o aura-gpu-bios.o aura-gpu-hw.o main.o

ccflags-y := -std=gnu99 -Wno-declaration-after-statement
KERNEL_SOURCE_DIR := /lib/modules/$(shell uname -r)/build

all:
	make -C "$(KERNEL_SOURCE_DIR)" M="$(PWD)" modules EXTRA_CFLAGS="-g -DDEBUG"

clean:
	make -C "$(KERNEL_SOURCE_DIR)" M="$(PWD)" clean