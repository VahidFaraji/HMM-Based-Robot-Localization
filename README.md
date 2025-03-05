# Robot Localization Using HMM-Based Forward Filtering

This repository contains a project on **robot localization** using **Hidden Markov Models (HMMs)** with **forward filtering and forward-backward smoothing** techniques. The goal is to estimate a robot’s position in a grid environment while handling **sensor failures**.

## 📜 Project Overview
### **Objective**
The project aims to localize a robot using **HMM-based filtering** by:
- Implementing **Forward Filtering** for real-time localization.
- Applying **Forward-Backward Smoothing** for enhanced accuracy.
- Comparing **Uniform Failure (UF)** and **Non-Uniform Failure (NUF)** sensor models.
- Evaluating the performance of **HMM-based localization** versus **Monte Carlo Localization (MCL)**.

### **Key Concepts**
- **Hidden Markov Models (HMMs):** Used to estimate the robot’s position based on noisy sensor data.
- **Forward Filtering:** Updates the robot’s belief about its location over time.
- **Forward-Backward Smoothing:** Uses past and future observations to refine localization accuracy.
- **Sensor Failure Models:** Two types of sensor failures are considered:
  - **Non-Uniform Failure (NUF)**: Some grid positions have higher failure rates.
  - **Uniform Failure (UF)**: All positions have the same failure probability.

---

## 📂 Repository Structure

| File | Description |
|------|-------------|
| `AI_2.pdf` | Full project report explaining methods, results, and analysis. |
| `Filters.py` | Python implementation of **HMM filtering and smoothing**. |
| `TaskPart1_VisualisationAndExampleCode.ipynb` | Jupyter Notebook for **data visualization and example code**. |
| `TaskPart2_InstructionsAndCodeSkeleton.ipynb` | Notebook containing **instructions and code skeleton** for running the experiments. |

---

## 🔧 **How to Run**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/VahidFaraji/HMM-Localization.git
cd HMM-Localization
