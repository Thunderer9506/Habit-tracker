# Habit Tracker – Pixela API Integration

This is a Python-based habit-tracking tool that uses the [Pixela API](https://pixe.la/) to visualize your daily progress in a beautiful, shareable graph.  
It’s designed for simplicity — you run the script, log your habit data, and Pixela takes care of the visualization.

---

## Overview

The script connects to Pixela’s API to:

1. **Register a new user** *(only needs to be done once)*.
2. **Create a habit graph** — defining the name, unit, type, and color.
3. **Log daily progress** — for example, the number of kilometers cycled or minutes studied.
4. **Update past data** — correct mistakes if you’ve entered the wrong value.
5. **Delete data** — remove entries for a specific date if needed.

All your progress is stored and visualized by Pixela, so you can see your habit streaks grow over time.

---

## How It Works

### 1. **Environment Variables**
Your Pixela credentials are stored securely in a `.env` file:
```env
USERNAME=your_pixela_username
TOKEN=your_secret_token
```
These are loaded in the script using `python-dotenv` to avoid exposing sensitive data in code.

---

### 2. **User Registration** *(Step 1)*
The first step (commented out in the code) sends a `POST` request to Pixela’s `/v1/users` endpoint with:
- `username`
- `token` (your chosen API key)
- Agreement flags for terms of service and age requirements.

---

### 3. **Graph Creation** *(Step 2)*
You define:
- **Graph ID** (`graph1` in this example)
- **Name** (e.g., `"Cycling Graph"`)
- **Unit** (`Km`, `Minutes`, etc.)
- **Type** (`float` or `int`)
- **Color** (Pixela’s theme colors, e.g., `"shibafu"` for green)

This creates a dedicated visual graph for your habit.

---

### 4. **Logging Data** *(Step 3)*
The script:
- Gets the current date in `YYYYMMDD` format.
- Sends a `POST` request to log the quantity for that date (e.g., `"5"` kilometers).

Pixela instantly updates the graph with the new data point.

---

### 5. **Updating Data** *(Step 4)*
If you entered the wrong number for a day, you can send a `PUT` request to change it.

Example: changing `"5"` to `"2"` kilometers for today.

---

### 6. **Deleting Data** *(Step 5)*
If an entry is incorrect or unnecessary, you can remove it with a `DELETE` request.

---

## Why Use This?
- **Visual Motivation** — Progress is displayed in an interactive graph.
- **Easy Habit Tracking** — Just run the script and log your daily habit.
- **Pixela Integration** — Your data is stored securely and can be accessed from anywhere.
- **Secure Credentials** — Uses `.env` files to protect your API token.

---

## Example Use Case
You’re cycling daily and want to track your distance.  
Run the script, log today’s distance, and check your Pixela graph to see your streaks and improvements over time.
