# Changelog

## v1.0 — Initial Release

### Infrastructure
- Proxmox VE 9.1 installed on 256GB NVMe SSD
- Two LXC containers: CT100 (AdGuard) and CT101 (Docker workload)
- Resolved GPU framebuffer crash + NVRAM corruption incident
- Fixed subnet isolation (192.168.100.x → 192.168.1.x)
- Applied 177 pending system updates

### Network
- AdGuard Home deployed as network-wide DNS + DHCP
- Unbound recursive DNS resolver (no third-party upstream)
- Tailscale mesh VPN replacing WireGuard (CGNAT bypass)
- WPA2-AES enforced on ISP router
- Two secondary routers configured as pure access points

### Media & Entertainment
- Jellyfin deployed for movie/show streaming
- Dual Navidrome instances (personal FLAC + grandpa's collection)
- Nicotine+ Soulseek client via noVNC browser GUI
- Beets auto-tagging pipeline active
- slskd headless Soulseek engine + Telegram bot automation

### Storage & Cloud
- Seafile attempted and abandoned (circular symlink bug in LXC)
- Samba SMB deployed as private cloud (iPhone + MacBook daily use)
- Immich deployed for photo management (library population in progress)

### YouTube Alternative Stack
- Piped backend + frontend deployed and operational
- Invidious + Companion + Materialious deployed (video 500s under investigation)
- Yattee iOS client connected to Piped backend

### Printing
- CUPS + socat bridge for HP Ink Tank 310 network sharing

### Pending
- Invidious video route 500 errors
- slskd-bot Telegram conflict cleanup
- Gigabit switch procurement
