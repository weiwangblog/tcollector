#!/bin/bash
grep -q ":" /proc/mounts && /opt/tcollector/nfsiostattsd 10
