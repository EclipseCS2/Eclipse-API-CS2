# ExternalAPI Eclipse 💙

> [!NOTE]
>**ExternalAPI Eclipse** is a high-performance External Memory Interface (EMI) designed for Counter-Strike 2. This framework provides a clean abstraction layer over Source 2 engine offsets, enabling seamless interaction with game memory for research and development purposes.

---

## 🔵 Installation & Dependencies

To use this framework, you need to install the required low-level libraries that handle Windows API calls and process memory.

**1. Clone the repository or copy the project files.**

**2. Install all dependencies using `pip`:**
It is highly recommended to use the provided `requirements.txt` file to ensure all library versions are compatible:

```bash
pip install -r requirements.txt

```

> [!NOTE]
> The core dependencies include `Pymem` (for memory manipulation) and `pywin32` (for low-level Windows API access).

---

## 🔵 API Reference & Syntax

The following four methods manage the core lifecycle of a memory intervention session:

### `api.init()`

Initializes the connection to the game process.

* **Process Attachment**: Locates `cs2.exe` in the system and opens a process handle with the necessary access rights.
* **Module Mapping**: Identifies the base addresses for `client.dll` and `engine2.dll`.

### `api.pars()`

Handles the data structures and offset mapping.

* **Offset Mapping**: Loads and links named offsets (e.g., `dwLocalPlayerPawn` or `m_iHealth`) to their specific memory addresses.
* **Configuration**: Prepares the API to correctly read specific data members.

### `api.get()`

The primary method for **reading** data from memory (RPM — ReadProcessMemory).

* **Data Retrieval**: Extracts real-time values of game variables like health, coordinates, or the view matrix.

### `api.edit()`

The method for **writing** and manipulating memory (WPM — WriteProcessMemory).

* **Memory Modification**: Allows changing values directly inside the game process (e.g., forcing jump flags for BunnyHop).

---

## 🔵 Technical Specifications (Core Offsets)

The API supports a comprehensive list of offsets categorized by their function:

### 1. Global & Engine Access

* **General:** `dwEntitySystem`, `dwEntityList`, `dwLocalPlayerPawn`, `dwLocalPlayerController`, `dwGlobalVars`, `dwGameRules`, `dwGameResourceService`.
* **Rendering & Input:** `dwViewMatrix`, `dwViewAngles`, `dwViewRender`, `dwCSGOInput`, `dwGlowManager`, `dwSoundSystem`.

### 2. Player Pawn & Data Members

* **Combat & Stats:** `m_iHealth`, `m_ArmorValue`, `m_bHasHelmet`, `m_iShotsFired`, `m_aimPunchAngle`, `m_lifeState`.
* **Movement:** `m_vecVelocity`, `m_fFlags`, `m_vOldOrigin`, `m_pMovementServices`.
* **Status:** `m_bIsScoped`, `m_bIsDefusing`, `m_flFlashBangTime`, `m_flFlashDuration`, `m_iIDEntIndex`.

### 3. World & Objects

* **C4 Dynamics:** `dwPlantedC4`, `m_flC4Blow`, `m_bBombPlanted`, `dwWeaponC4`.
* **Equipment:** `m_pClippingWeapon`, `m_iItemDefinitionIndex`, `m_iClip1`, `m_hMyWeapons`.

---

## 🔵 Quick Start Example

```python
import ExternalAPI

# Initialize the interface
api = ExternalAPI
api.init()
api.pars()

# Simple data monitoring loop
while True:
    # Read current health
    current_health = api.get("m_iHealth")
    print(f"Player Health: {current_health}")
    
    # Simple BunnyHop implementation
    if api.get("m_fFlags") & (1 << 0): # Check if on ground
        api.edit("jump", 65537)

```

---

> [!CAUTION]
> ### Disclaimer
> **Educational Purpose Only.** This framework is intended for reverse engineering and software architecture research. Usage on VAC-secured servers is strictly discouraged. The developer is not responsible for any account restrictions.

