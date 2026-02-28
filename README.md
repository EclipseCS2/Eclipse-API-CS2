Вот готовый код для твоего `README.md`. Я добавил синие разделители-градиенты, стильные плашки (badges) и структурировал текст так, чтобы он выглядел как профессиональный Open Source проект.

Просто скопируй этот блок целиком и вставь в свой файл:

```markdown
# ExternalAPI Eclipse 💙
![Static Badge](https://img.shields.io/badge/Language-Python-0077ff?style=for-the-badge&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/Status-Active-blue?style=for-the-badge)

**ExternalAPI Eclipse** is a high-performance External Memory Interface (EMI) designed for Counter-Strike 2. This framework provides a clean abstraction layer over Source 2 engine offsets, enabling seamless interaction with game memory for research and development purposes.

![header](https://capsule-render.vercel.app/render?type=slice&color=0077ff&height=20&section=header)

## 🛠 Installation & Dependencies

To use this framework, you need to install the required low-level libraries that handle Windows API calls and process memory.

> [!IMPORTANT]
> Ensure you are running your terminal as **Administrator** to allow memory access.

**Install all dependencies using `pip`:**
It is highly recommended to use the provided `requirements.txt` file to ensure all library versions are compatible:

```bash
pip install -r requirements.txt

```

*Core dependencies include:* `Pymem` (memory manipulation), `win32api`, and `win32con` (via `pywin32`).

## 💙 API Reference & Syntax

The following four methods manage the core lifecycle of a memory intervention session:

### `api.init()`

Initializes the connection to the game process.

* **Process Attachment**: Locates `cs2.exe` and opens a process handle.
* **Module Mapping**: Identifies base addresses for `client.dll` and `engine2.dll`.

### `api.pars()`

Handles the data structures and offset mapping.

* **Offset Mapping**: Loads and links named offsets (e.g., `dwLocalPlayerPawn` or `m_iHealth`).

### `api.get()`

The primary method for **reading** data from memory (RPM).

* **Data Retrieval**: Extracts real-time values like health, coordinates, or the view matrix.

### `api.edit()`

The method for **writing** and manipulating memory (WPM).

* **Memory Modification**: Allows changing values directly inside the game process (e.g., forcing jump flags for BunnyHop).

## 💙 Technical Specifications (Core Offsets)

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

## 💙 Quick Start Example

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

## ⚠️ Disclaimer

**Educational Purpose Only.** This framework is intended for reverse engineering and software architecture research. Usage on VAC-secured servers is strictly discouraged. The developer is not responsible for any account restrictions.

```

### Что изменилось:
1.  **Синие разделители:** Добавлены через `capsule-render` (стиль `slice`, цвет `0077ff`). Они визуально разбивают текст на блоки.
2.  **Badges:** В самом верху теперь красивые синие плашки «Language: Python» и «Status: Active».
3.  **Блок Note:** Инструкция по установке теперь выделена специальным синим блоком `[!IMPORTANT]`.
4.  **Команда установки:** Я вынес `pip install -r requirements.txt` в начало, как ты и просил.

```
