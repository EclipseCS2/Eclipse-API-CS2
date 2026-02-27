

---

# CS2 Eclipse API 🌑

**CS2 Eclipse** is a high-performance External Memory Interface (EMI) designed for Counter-Strike 2. This framework provides a clean abstraction layer over Source 2 engine offsets, enabling seamless interaction with game memory for research and development purposes.

---

## 🌑 Installation & Dependencies

The project relies on low-level libraries to handle process memory and Windows API calls. To set up your environment, ensure you have Python installed and run the following command:

```bash
python -m pip install -r requirements.txt

```

> **Core Dependencies:** `Pymem`, `pywin32`.

---

## 🌑 Technical Specifications (Core Offsets)

The API is architected to support all critical memory addresses, categorized by their function within the game engine:

### 1. Global & Engine Access

Primary entry points within `client.dll`:

* **`dwEntitySystem` / `dwEntityList**` — Global entity registry management.
* **`dwLocalPlayerController`** — Local player metadata and network state.
* **`dwViewMatrix`** — $4 \times 4$ transformation matrix for World-to-Screen calculations.
* **`dwGameRules`** — Internal match state and round parameters.

### 2. Player Pawn & Data Members

Specific offsets for real-time entity state monitoring:

* **Combat:** `m_iHealth`, `m_ArmorValue`, `m_iShotsFired`, `m_aimPunchAngle`.
* **Movement:** `m_vecVelocity`, `m_fFlags`, `m_vOldOrigin`.
* **Status:** `m_bIsScoped`, `m_bIsDefusing`, `m_flFlashDuration`, `m_lifeState`.

### 3. World & Objects

Environment-specific offsets:

* **C4 Dynamics:** `dwPlantedC4`, `m_flC4Blow`, `m_bBombPlanted`.
* **Equipment:** `m_pClippingWeapon`, `m_iItemDefinitionIndex`, `m_iClip1`.

---

## ⚠️ Disclaimer

**Educational Purpose Only.** This framework is intended for reverse engineering and software architecture research.

* The developer is not responsible for any account restrictions or bans.
* Usage on VAC-secured (Valve Anti-Cheat) servers is strictly discouraged.

---
