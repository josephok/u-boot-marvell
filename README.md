# U-Boot source for WD MyCloud gen2

## Build
```bash
./build.sh
```

## Install
1. Use kwboot to load compiled U-Boot binary to DDR and test it:
```bash
kwboot -b u-boot-a375-xx-spi.bin -t -B 115200 /dev/ttyUSB0
```

2. Load compiled U-Boot binary to DDR:
```bash
usb start; fatload usb 0:1 0x2000000 u-boot-a375-xx-spi.bin
```
or use tftp:
```bash
tftpboot 0x2000000 u-boot-a375-xx-spi.bin
```

3. Write it to SPI flash:
```bash
=> sf probe
=> sf erase 0x0 0x100000
=> sf write 0x2000000 0x0 0x100000
=> reset
```

