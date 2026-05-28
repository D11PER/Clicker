#  Simple Clicker Counter

![Python 3](https://img.shields.io/badge/Python-3.x-blue)
![tkinter](https://img.shields.io/badge/GUI-tkinter-green)

A minimal desktop counter built with `tkinter`. Three buttons let you increment, multiply, and divide the value — great as a starter project for learning Python GUI development.

## ✨ Features

- **+1** — increment the counter by one
- **× 10** — multiply the current value by 10
- **÷ 10** — divide the current value by 10
- Result is displayed in a large centered label

## 🚀 Getting Started

Only Python 3 is required — `tkinter` is part of the standard library.

```bash
python clicker.py
```


## 📁 Structure

```
├── clicker.py      # main app — all logic and UI in one file
└── README.md
```

## 🛠 Built With

- Python 3.x
- tkinter — built-in GUI library

## 📌 Notes

- Fixed window size: 250 × 200 px
- Counter state is stored in a global variable `count`
- Division returns a `float` — wrap with `int()` if you prefer whole numbers
