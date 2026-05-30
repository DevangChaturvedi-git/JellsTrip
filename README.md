# JellsTrip — Self-Hosted Home Infrastructure

A fully self-hosted home server built on a budget desktop PC running Proxmox VE, managing a complete stack of personal cloud services via Docker.

**Host:** `nas` | **Proxmox:** `192.168.1.200:8006` | **Docker LXC:** `192.168.1.90` | **Tailscale:** `100.88.17.70`

---

## Stack Overview

| Service | Port | Description |
|---|---|---|
| Proxmox VE | 8006 | Bare-metal hypervisor |
| AdGuard Home | 8080 | Network-wide DNS ad blocking + DHCP |
| Unbound DNS | 5335 | Recursive DNS resolver (no third-party upstream) |
| Tailscale | — | Mesh VPN, remote access, CGNAT bypass |
| Portainer | 9443 | Docker container management UI |
| Jellyfin | 8096 | Media streaming (movies, shows) |
| Navidrome (Personal) | 4533 | Music streaming — FLAC collection |
| Navidrome (Grandpa) | 4534 | Music streaming — family collection |
| Nicotine+ | 6080 | Soulseek P2P music downloader (noVNC GUI) |
| Beets | — | Automatic music library tagger |
| slskd | 5030 | Headless Soulseek engine (REST API) |
| slskd-bot | — | Telegram bot for music automation |
| Samba (SMB) | 445 | Private cloud storage (iPhone + MacBook) |
| Immich | 8083 | Photo management (Apple Photos alternative) |
| Piped Backend | 8081 | Self-hosted YouTube API backend |
| Piped Frontend | 3001 | Self-hosted YouTube PWA frontend |
| Materialious | 3000 | Material Design YouTube frontend |
| Invidious | 8080 | YouTube data extraction backend |
| CUPS | 631 | HP Ink Tank 310 network printer sharing |

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

**1. Clone the repo**
```bash
git clone https://github.com/DevangChaturvedi-git/JellsTrip.git
cd JellsTrip
```

**2. Create your .env file**
```bash
cp .env.example .env
nano .env
```
Fill in all your credentials and secrets.

**3. Start the stack**
```bash
docker compose up -d
```

---

## Environment Variables

All secrets are stored in a `.env` file (not committed to git). Create one based on `.env.example`:

| Variable | Description |
|---|---|
| `POSTGRES_PASSWORD_PIPED` | Piped PostgreSQL password |
| `SAMBA_PASS` | Samba share password |
| `IMMICH_DB_PASSWORD` | Immich PostgreSQL password |
| `TS_AUTHKEY` | Tailscale auth key |
| `SLSKD_HTTP_PASSWORD` | slskd web UI password |
| `SLSKD_SLSK_PASSWORD` | Soulseek account password |
| `SLSKD_API_KEY` | slskd REST API key |
| `SPOTIFY_CLIENT_ID` | Spotify API client ID |
| `SPOTIFY_CLIENT_SECRET` | Spotify API client secret |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token |
| `TELEGRAM_ALLOWED_USERS` | Allowed Telegram user IDs |

---

## Remote Access

All services are accessible remotely via Tailscale at `100.88.17.70:<port>` without any port forwarding on the router.

---

*Devang Chaturvedi — 23BCT0151 — VIT Vellore*
