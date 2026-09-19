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

## v2.0 — Infrastructure Refresh (Sept 2026)

### Infrastructure
- Corrected container layout: CT100 = PiHole (not AdGuard Home), CT101 = Docker workload (58+ containers), CT102 = print-server (currently stopped)
- Full re-audit of running services against live `docker ps -a` output

### AI Orchestration (new)
- Deployed Peanut: self-hosted personal AI orchestrator (deterministic agent routing, model routing, policy/approval engine, MCP-based tool execution)
- Deployed OmniRoute as a multi-provider LLM gateway/router (400+ models via Gemini, OpenRouter, OpenCode)
- Deployed Open WebUI and LibreChat as chat frontends to Peanut
- Deployed Morphic as an AI-answer search frontend over SearXNG
- Deployed 9 MCP servers (homelab, workspace, memory, Jellyfin, SearXNG, Navidrome, arr-stack, Jellyseerr, slskd) plus a GitHub MCP server and a scoped docker-socket-proxy

### YouTube Alternative Stack
- Retired Piped backend/frontend
- Invidious + Companion + Materialious is now the primary YouTube-alternative stack

### Networking & Security
- Corrected DNS documentation: PiHole (CT100) handles network-wide ad-blocking, not AdGuard Home
- Added Vaultwarden (self-hosted Bitwarden-compatible password manager)
- Added wg-easy (WireGuard VPN with web UI) alongside Tailscale
- Added Portainer for Docker management

### Communication
- Added Matrix Synapse + mautrix-whatsapp bridge
- Added self-hosted Firefox Sync

### Known Issues
- dab-downloader currently restart-looping, not yet root-caused
- Print server (CT102) currently stopped
