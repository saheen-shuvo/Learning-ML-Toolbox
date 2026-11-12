# Learning ML Toolbox

An open learning journey through the Python tools and concepts that support machine learning. This repository contains notes, small experiments, and practice code that I am building while learning data analysis, visualization, and AI programming.

> Learning in public: the code is intentionally simple, practical, and continuously evolving. You are welcome to explore the notes, learn from them, and suggest improvements.

## What you will find here

- **NumPy fundamentals**: arrays, data types, indexing, slicing, iteration, and array generation.
- **Advanced NumPy**: arithmetic and logical operations, sorting, searching, counting, statistics, linear algebra, and array manipulation.
- **Pandas for data analysis**: Series, DataFrames, indexing, filtering, sorting, loading data, grouping, statistics, dates, and applying functions.
- **Data cleaning practice**: duplicate detection, missing-value checks, filling and dropping null values, and preparing data for analysis.
- **Data visualization**:
  - **Matplotlib**: line plots, bar charts, histograms, pie charts, and scatter plots.
  - **Seaborn**: count/bar plots, line plots, histograms, KDE plots, scatter plots, facet plots, pair plots, and joint plots.
- **AI Programming with Python**: a Jupyter notebook containing final-exam practice and Python programming exercises.

## Repository structure

```text
.
├── AI_Programming_With_Python_Final_Exam_Ans.ipynb
├── Advanced Data Analysis NumPy/
├── Data Analysis with NumPy/
├── Data Analysis with Pandas/
├── Matplotlib Data Visualization/
├── Pandas for Machine Learning/
└── Seaborn Data Visualization/
```

Each folder contains focused `.py` examples. The filenames describe the concept being practiced, so you can open a topic directly without following a strict order.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/saheen-shuvo/Learning-ML-Toolbox.git
cd Learning-ML-Toolbox
```

### 2. Install the main Python libraries

```bash
python -m pip install numpy pandas matplotlib seaborn jupyter
```

### 3. Run an example

```bash
python "Data Analysis with NumPy/numpy-intro.py"
```

For the notebook, start Jupyter and open `AI_Programming_With_Python_Final_Exam_Ans.ipynb`:

```bash
jupyter notebook
```

Some examples use inline sample data, while others may be intended for interactive exploration. Read each file before running it and adjust paths or inputs when needed.

## Suggested learning path

1. Start with **Data Analysis with NumPy** to understand arrays and vectorized operations.
2. Continue with **Advanced Data Analysis NumPy** for manipulation, statistics, and linear algebra.
3. Learn **Data Analysis with Pandas** and then practice cleaning data in **Pandas for Machine Learning**.
4. Use **Matplotlib** and **Seaborn** to visualize patterns in data.
5. Revisit the notebook exercises and apply these tools to small datasets.
6. Continue toward core machine-learning topics such as feature engineering, model training, evaluation, and deployment.

## Learning in public

This is a personal study repository, not a finished course or production library. Notes may be incomplete, examples may be refactored, and new topics will be added as I learn. If you spot an error or have a clearer explanation, feel free to open an issue or submit a pull request.

## License

No license has been added yet. Until a license is provided, please treat the contents as personal learning material and ask before redistributing or reusing them.