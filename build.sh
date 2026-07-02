#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE="uboot-marvell-builder"
DOCKERFILE="$SCRIPT_DIR/Dockerfile.build"

# Build container image if not exists
if ! podman image exists "$IMAGE"; then
    echo "==> Building container image..."
    podman build -t "$IMAGE" -f "$DOCKERFILE"
fi

# Build u-boot
echo "==> Building U-Boot..."
podman run --rm -v "$SCRIPT_DIR:/build:Z" "$IMAGE" ./build.pl -f spi -b armada_375 "$@"
