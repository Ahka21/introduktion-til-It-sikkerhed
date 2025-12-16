#!/bin/bash
echo "Bruger: $(whoami)"
echo "Kernel: $(uname -r)"
df -h | head -n 5
