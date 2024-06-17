# Data Structures and Algorithms

Welcome to the Data Structures and Algorithms repository! This repository contains implementations of various data structures and algorithms, categorized for ease of use and reference. Each implementation is written with clarity and efficiency in mind.

## Table of Contents

- [Introduction](#introduction)
- [Directory Structure](#directory-structure)
- [Implemented Algorithms](#implemented-algorithms)
  - [Sorting Algorithms](#sorting-algorithms)
  - [Searching Algorithms](#searching-algorithms)
  - [Dynamic Programming Algorithms](#dynamic-programming-algorithms)
  - [Divide and Conquer Algorithms](#divide-and-conquer-algorithms)
  - [Recursive Algorithms](#recursive-algorithms)
  - [Non-Recursive Algorithms](#non-recursive-algorithms)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository is a comprehensive collection of data structures and algorithms implemented in Python. The goal is to provide a resource for learning, reference, and application of fundamental and advanced algorithmic techniques.

## Directory Structure


## Implemented Algorithms

### Sorting Algorithms
- **Selection Sort**(`selection_sort.py`): 
  Selection Sort divides the list into a sorted and an unsorted region. It repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the end of the sorted region.

  Time Complexity: O(n^2)

  Space Complexity: O(1)
  
  Stability: Not stable

- **Quicksort** (`quicksort.py`): An efficient sorting algorithm using the divide-and-conquer approach.
- **Mergesort** (`mergesort.py`): Merge Sort is a divide-and-conquer algorithm that divides the list into two halves, recursively sorts each half, and then merges the sorted halves to produce the sorted list.

Time Complexity: O(n log n)

Space Complexity: O(n)

Stability: Stable

- **Counting Sort** (`CountingSort.py`) : Counting Sort is a non-comparison-based sorting algorithm that counts the occurrences of each element in the list. It then uses this count to place the elements in the correct position in the sorted list.

    Time Complexity: O(n + k), where k is the range of the input

    Space Complexity: O(n + k)

    Stability: Stable

### Searching Algorithms

- **Binary Search** (`binary_search.py`): A fast search algorithm for finding an element in a sorted array (non-recursive).
- **Recursive Binary Search** (`binary_search_recursive.py`): A fast search algorithm for finding an element in a sorted array (non-recursive).
- **Linear Search** (`linear_search.py`): A simple search algorithm for finding an element in an unsorted array.

### Dynamic Programming Algorithms

- **Fibonacci Sequence** (`fibonacci.py`): Calculates the nth Fibonacci number using dynamic programming (recursive).
- **Knapsack Problem** (`knapsack.py`): Solves the 0/1 knapsack problem using dynamic programming.

### Divide and Conquer Algorithms

- **Quicksort** (`quicksort.py`): As listed under sorting algorithms.
- **Mergesort** (`mergesort.py`): As listed under sorting algorithms.

### Recursive Algorithms

- **Factorial** (`factorial_recursive.py`): Calculates the factorial of a number using recursion.
- **Fibonacci Sequence** (`fibonacci_recursive.py`): Calculates the nth Fibonacci number using recursion.

### Non-Recursive Algorithms

- **Factorial** (`factorial_iterative.py`): Calculates the factorial of a number using iteration.
- **Fibonacci Sequence** (`fibonacci_iterative.py`): Calculates the nth Fibonacci number using iteration.

## Usage

To use any of the algorithms, clone the repository and navigate to the respective directory. Run the Python scripts directly to see the implementations in action. Example:

```sh
git clone https://github.com/yourusername/algorithms.git
cd algorithms/sorting
python quicksort.py