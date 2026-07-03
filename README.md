# U-Boot source for WD MyCloud gen2

## Build
```bash
./build.sh
```

## Install
1. Use kwboot to load compiled U-Boot binary to DDR and test it:
```bash
kwboot -b u-boot-wd.bin -t -B 115200 /dev/ttyUSB0
```

2. Load compiled U-Boot binary to DDR:
```bash
usb start; fatload usb 0:1 0x2000000 u-boot-wd.bin
```
or use tftp:
```bash
tftpboot 0x2000000 u-boot-wd.bin
```

3. Write it to SPI flash:
```bash
=> sf probe
=> sf erase 0x0 0xf0000
=> sf write 0x2000000 0x0 0xf0000
=> reset
```

## Supported Commands

### Boot
| Command | Description |
|---------|-------------|
| `bootm` | Boot application image from memory |
| `bootz` | Boot Linux zImage from memory |
| `bootd` | Boot default image (run `bootcmd`) |
| `boot_menu` | Display interactive boot menu |
| `stage_boot` | Staged boot support |
| `pxe` | Boot from PXE server |

### Network
| Command | Description |
|---------|-------------|
| `tftpboot` | Load file via TFTP |
| `dhcp` | Obtain IP via DHCP and boot |
| `ping` | Send ICMP echo request |
| `nfs` | Boot image via NFS |

### Storage
| Command | Description |
|---------|-------------|
| `sf probe/read/write/erase` | SPI Flash operations |
| `nand read/write/erase` | NAND Flash operations |
| `ide reset/info/read/write` | SATA disk operations (via Marvell IDE/SATA interface) |
| `mmc rescan/info/read/write` | MMC/SD card operations |
| `usb start/info/read` | USB storage operations |

### Filesystem
| Command | Description |
|---------|-------------|
| `ext2load / ext2ls` | Load file / list directory from ext2 |
| `ext4load / ext4ls / ext4write` | Load file / list / write to ext4 |
| `fatload / fatls` | Load file / list directory from FAT |
| `ubifsmount / ubifsload / ubifsls` | Mount and access UBIFS |
| `ubi part/readvol/writevol` | UBI volume operations |
| `jffs2 dump/ls` | Access JFFS2 filesystem |
| `mtdparts` | Manage MTD partitions |

### Memory
| Command | Description |
|---------|-------------|
| `md` | Memory display |
| `mm` | Memory modify (auto-incrementing) |
| `mw` | Memory write |
| `cp` | Memory copy |
| `cmp` | Memory compare |
| `crc32` | Checksum calculation |

### Environment
| Command | Description |
|---------|-------------|
| `printenv` | Print environment variables |
| `setenv` | Set environment variable |
| `editenv` | Edit environment variable |
| `saveenv` | Save environment to SPI Flash |
| `run` | Run commands in environment variable |
| `importenv / exportenv` | Import/export environment |

### Hardware
| Command | Description |
|---------|-------------|
| `i2c` | I2C bus operations |
| `spi` | SPI bus operations |
| `eeprom read/write` | EEPROM access via I2C |
| `date` | Get/set RTC date and time |
| `pci` | PCI bus enumeration and access |
| `sar` | Sample At Reset register read/write |

### Misc
| Command | Description |
|---------|-------------|
| `bdinfo` | Print board information |
| `coninfo` | Print console devices |
| `echo` | Print arguments to console |
| `sleep` | Delay execution |
| `itest` | Integer/string test |
| `source` | Execute script from memory |
| `go` | Start application at address |
| `elf` | Load and run ELF image |
| `rcvr` | Enter recovery mode |
| `sys_restore` | Restore system to factory defaults |

### Loading Linux from SATA example
```bash
ide reset
ext4load ide 0:1 0x2000000 /boot/uImage
setenv bootargs 'console=ttyS0,115200 root=/dev/sda1 rw rootwait'
bootm 0x2000000
```
