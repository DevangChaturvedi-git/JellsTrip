# JellsTrip — Self-Hosted Home Infrastructure

A fully self-hosted home server built on a budget desktop PC running Proxmox VE, running three LXC containers that together host 55+ Docker services spanning media, AI orchestration, personal cloud, and network infrastructure.

**Host:** `nas` | **Proxmox:** `192.168.1.200:8006` | **Docker LXC:** `192.168.1.90` | **Tailscale:** `100.88.17.70`

---

## Proxmox Layout

| VMID | Name | Status | Purpose |
|------|------|--------|---------|
| 100 | PiHole | Running | Network-wide DNS ad blocking |
| 101 | docker | Running | Main Docker host — 55+ containers (see below) |
| 102 | print-server | Stopped | HP printer sharing (CUPS) — currently offline |

*(Correction from earlier docs: DNS ad-blocking runs on **Pi-hole**, not AdGuard Home.)*

---

## Stack Overview (LXC 101 — Docker)

### AI Orchestration — Peanut
A self-hosted personal AI orchestrator: one conversational entry point with memory, capability routing, and an approval gate for anything that writes/changes/spends, sitting in front of every other service below. Built from scratch — deterministic agent routing, deterministic model routing, a policy engine, an approval engine, and an execution coordinator, all wired to real self-hosted services through the Model Context Protocol (MCP).

| Service | Port | Description |
|---|---|---|
| peanut | — | Core orchestrator — routing, reasoning, policy, execution |
| omniroute | 20128 | Multi-provider LLM gateway/router (Gemini, OpenRouter, OpenCode, and 400+ models) |
| open-webui | 8081 | Web chat client, phone/browser access to Peanut |
| morphic + morphic-db + morphic-redis | 3000 | AI-answer search frontend over SearXNG |
| homelab-mcp | 18000 | MCP server — Docker/host inspection capability |
| workspace-mcp | 18002 | MCP server — internal file/workspace capability |
| memory-mcp | 18003 | MCP server — long-term memory store |
| jellyfin-mcp | 18004 | MCP server — Jellyfin library capability |
| searxng-mcp | 18005 | MCP server — private web search capability |
| navidrome-mcp | 18006 | MCP server — music library capability |
| arr-mcp | 18007 | MCP server — Radarr/Sonarr/Lidarr/Prowlarr capability (read + gated write) |
| jellyseerr-mcp | 18008 | MCP server — media request capability (read + gated write) |
| slskd-mcp | 18009 | MCP server — Soulseek search/download capability (read + gated write) |
| github-mcp | 18082 | MCP server — GitHub repo/code capability |
| docker-socket-proxy | — | Scoped Docker API access for MCP servers |

### Media Streaming
| Service | Port | Description |
|---|---|---|
| jellyfin | 8096 | Movie/TV streaming |
| navidrome | 4533 | Music streaming (FLAC library) |
| immich_server / immich_machine_learning / immich_postgres / immich_redis | 8083 | Self-hosted photo management (Apple Photos alternative) |
| invidious + invidious-db + invidious-companion | 3015 | Self-hosted YouTube frontend/backend |
| materialious | — | Material Design YouTube frontend (over Invidious) |
| monochrome | 5555 | Manga/comic reader |

### Media Acquisition
| Service | Port | Description |
|---|---|---|
| radarr | 7878 | Movie tracking/acquisition |
| sonarr | 8989 | TV tracking/acquisition |
| lidarr | 8686 | Music tracking/acquisition |
| prowlarr | 9696 | Indexer management for the *arr stack |
| jellyseerr | 5055 | Media request/availability frontend |
| slskd | 5030 | Headless Soulseek client (REST API) |
| qbittorrent-nox | 8080 / 6881 | Torrent client |
| beets | — | Automatic music library tagger |
| octorr | 5274 | *arr stack utility |
| spotiflac-api / spotiflac-test | 8010 / 5800 | Spotify → FLAC download tooling |
| yt-dlp-shim | — | Internal yt-dlp API wrapper |
| dab-downloader | — | Known issue — currently restart-looping |
| flaresolverr | 8191 | Cloudflare-bypass proxy for indexers |

### Networking & Security
| Service | Port | Description |
|---|---|---|
| unbound-dns | 53 | Recursive DNS resolver |
| tailscale-audio | — | Mesh VPN container |
| wg-easy | 51820 / 51821 | WireGuard VPN with web UI |
| vaultwarden | 3012 / 8085 | Self-hosted password manager (Bitwarden-compatible) |
| homestack-proxy-1 (Caddy) | 8090 / 8443 | Reverse proxy |
| portainer | 9000 / 9443 | Docker management UI |

### Communication
| Service | Port | Description |
|---|---|---|
| matrix-synapse + matrix-postgres | 8008 | Self-hosted Matrix chat server |
| mautrix-whatsapp | — | WhatsApp bridge for Matrix |
| firefox-sync (syncserver) | 5000 | Self-hosted Firefox Sync |
| samba | 445 | Private cloud file storage (iPhone + MacBook) |

### Productivity & Dev (Google replacement)
| Service | Port | Description |
|---|---|---|
| filebrowser (Quantum) | 8094 | Web file manager over the Samba tree (`/mnt/data`) — search, previews, share links |
| stirling-pdf | 8097 | PDF toolkit — merge, split, OCR, sign, convert, redact |
| forgejo | 3030 / 2222 | Self-hosted Git (GitHub mirror target), SSH on 2222 |
| threadfin | 34400 | IPTV M3U/EPG proxy feeding Jellyfin Live TV |

### Search & Data
| Service | Port | Description |
|---|---|---|
| searxng | 8888 | Privacy-respecting metasearch engine |
| vectordb (pgvector) | — | Vector database (available for future semantic search/memory upgrades) |

---

## Hardware

| Component | Spec |
|---|---|
| CPU | Intel Core i3 10th Gen (F-Series) |
| RAM | 16 GB DDR4 |
| GPU | NVIDIA GeForce GT 730 4GB |
| Primary Storage | 256 GB NVMe SSD (Proxmox + containers) |
| Secondary Storage | 1.5 TB HDD (media, music, photos) |
| Network | Gigabit Ethernet |

---

## Setup

### Prerequisites
- Proxmox VE installed on bare metal
- Docker LXC container running Debian 13
- 1.5TB HDD mounted at `/mnt/data`

### Deployment
```bash
git clone https://github.com/DevangChaturvedi-git/JellsTrip.git
cd JellsTrip
cp .env.example .env
nano .env   # fill in your credentials
docker compose up -d
```

---

## Remote Access
All services are accessible remotely via Tailscale at `100.88.17.70:<port>` without any port forwarding on the router.

---

## Known Issues
- `dab-downloader` is currently restart-looping — not yet root-caused.
- Print server (LXC 102) is currently stopped.

---

*Devang Chaturvedi — 23BCT0151 — VIT Vellore*
