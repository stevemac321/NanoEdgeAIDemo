

## ✅ **NanoEdgeAI EKG Anomaly Detection (STM32 + Python Serial Host)**

### 🔧 Overview

This project implements a **real-time EKG anomaly detector** using:

* An STM32H723ZG Nucleo board
* NanoEdgeAI anomaly detection library (generated via NanoEdgeAI Studio)
* A Python host script that sends 141 float values (simulated EKG signals) over UART
* The MCU runs inference on received signals and returns a 2-byte result:

  * `status` (enum from NanoEdge)
  * `similarity` (0–100%)

---

### 📂 Project Structure

| File                                       | Description                                                        |
| ------------------------------------------ | ------------------------------------------------------------------ |
| `Core/Src/main.c`                          | Main firmware loop, model training, UART receive logic             |
| `training_data.c`                          | Normal training set (extracted from `normal_signals.csv`)          |                    |
| `EKG_Simulalator.py`                       | Python script that sends float arrays over UART and prints results |
| `NanoEdgeAI.h`, `knowledge.h`, `libneai.a` | NanoEdgeAI model files                                             |
| `.ioc`                                     | STM32CubeMX project configuration                                  |

---

### ⚙️ Firmware Flow

1. **NanoEdgeAI model is initialized** in `train_model()`
2. **Model is trained** using \~500 signals from `normal_signals.csv`

   * `neai_anomalydetection_learn()` is called in nested loop
   * Training completes when `NEAI_MINIMAL_RECOMMENDED_LEARNING_DONE` is returned
3. **Interrupt-based UART receive** starts via `HAL_UART_Receive_IT()`
4. Each **incoming float** (4 bytes) is:

   * Reconstructed from bytes
   * Appended to `EKG_Input[]`
5. When 141 floats are received:

   * `neai_anomalydetection_detect()` is called
   * Result is returned to Python via `HAL_UART_Transmit()`

---

### 🖥️ Python Script Flow (`EKG_Simulalator.py`)

```python
for each float in signal:
    ser.write(pack_float(f))
wait_for(2_bytes_response)
print(status, similarity)
```

---

### 📈 Output Examples

```bash
✅ All floats sent. Port is held open. Waiting for MCU response...
📬 Report bytes: b'\x00d'
Status: 0
Similarity: 100  # Normal

✅ All floats sent. Port is held open. Waiting for MCU response...
📬 Report bytes: b'\x00\x00'
Status: 0
Similarity: 0    # Anomaly
```

---

### 🛠️ Requirements

#### Firmware:

* STM32CubeIDE 1.18+
* STM32H7 HAL drivers
* NanoEdgeAI Studio-generated static lib with embedded knowledge

#### Host:

* Python 3.x
* `pyserial`

```bash
pip install pyserial
```

---

### 🚀 To Run the Project

1. **Open STM32CubeIDE**, build and flash the project
2. Run:

```bash
python EKG_Simulalator.py
```

3. MCU will return:

   * `status` (0 = OK)
   * `similarity` (0–100)

---

License: GPL v.2
