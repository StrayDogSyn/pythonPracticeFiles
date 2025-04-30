"""
Unit tests for sorting algorithms.

This module contains unit tests for all the sorting algorithms 
in the src/week3/examples directory.
"""
import sys
import os
import unittest
import copy
import random
from pathlib import Path

# Add the src directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import sorting algorithms
from src.week3.examples.bubble_sort import bubble_sort
from src.week3.examples.insertion_sort import insertion_sort
from src.week3.examples.selection_sort import selection_sort
from src.week3.examples.merge_sort import merge_sort
try:
    from src.week3.examples.heap_sort import heap_sort
    HEAP_SORT_AVAILABLE = True
except ImportError:
    HEAP_SORT_AVAILABLE = False

# Import test cases
from src.week3.examples.test_cases import test_cases, is_sorted, generate_test_array


class TestSortingAlgorithms(unittest.TestCase):
    """Base class for testing sorting algorithms."""
    
    def setUp(self):
        # Create test arrays
        self.empty_array = []
        self.single_element = [42]
        self.sorted_array = list(range(10))
        self.reversed_array = list(range(10, 0, -1))
        self.random_array = random.sample(range(100), 20)
        self.duplicate_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    def _test_sort_algorithm(self, sort_func, array=None):
        """Test a sorting algorithm with various test cases."""
        if array is None:
            arrays = [
                self.empty_array,
                self.single_element,
                self.sorted_array,
                self.reversed_array,
                self.random_array,
                self.duplicate_array
            ]
        else:
            arrays = [array]
            
        for arr in arrays:
            # Make a copy since some sort functions modify the array in-place
            original = copy.deepcopy(arr)
            sorted_arr = sort_func(copy.deepcopy(arr))
            
            # Check that the array is sorted
            self.assertTrue(is_sorted(sorted_arr), 
                        f"Array not sorted correctly: {sorted_arr}")
            
            # Check that all elements from the original array are in the sorted array
            self.assertEqual(sorted(original), sorted(sorted_arr),
                         f"Elements changed during sorting. Original: {original}, Sorted: {sorted_arr}")
            
            # Check that the array has the same length
            self.assertEqual(len(original), len(sorted_arr),
                         f"Length changed during sorting. Original: {len(original)}, Sorted: {len(sorted_arr)}")


class TestBubbleSort(TestSortingAlgorithms):
    """Tests for bubble sort algorithm."""
    
    def test_bubble_sort(self):
        """Test the bubble sort algorithm."""
        self._test_sort_algorithm(bubble_sort)
        
    def test_bubble_sort_large(self):
        """Test bubble sort with a larger array."""
        large_array = generate_test_array(200, "random")
        self._test_sort_algorithm(bubble_sort, large_array)


class TestInsertionSort(TestSortingAlgorithms):
    """Tests for insertion sort algorithm."""
    
    def test_insertion_sort(self):
        """Test the insertion sort algorithm."""
        self._test_sort_algorithm(insertion_sort)
        
    def test_insertion_sort_almost_sorted(self):
        """Test insertion sort with an almost sorted array."""
        almost_sorted = copy.deepcopy(self.sorted_array)
        if len(almost_sorted) > 1:
            almost_sorted[0], almost_sorted[-1] = almost_sorted[-1], almost_sorted[0]
        self._test_sort_algorithm(insertion_sort, almost_sorted)


class TestSelectionSort(TestSortingAlgorithms):
    """Tests for selection sort algorithm."""
    
    def test_selection_sort(self):
        """Test the selection sort algorithm."""
        self._test_sort_algorithm(selection_sort)
    
    def test_selection_sort_duplicate(self):
        """Test selection sort with an array containing many duplicates."""
        duplicates = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        self._test_sort_algorithm(selection_sort, duplicates)


class TestMergeSort(TestSortingAlgorithms):
    """Tests for merge sort algorithm."""
    
    def test_merge_sort(self):
        """Test the merge sort algorithm."""
        self._test_sort_algorithm(merge_sort)
    
    def test_merge_sort_large(self):
        """Test merge sort with a larger array."""
        large_array = generate_test_array(500, "random")
        self._test_sort_algorithm(merge_sort, large_array)


if HEAP_SORT_AVAILABLE:
    class TestHeapSort(TestSortingAlgorithms):
        """Tests for heap sort algorithm."""
        
        def test_heap_sort(self):
            """Test the heap sort algorithm."""
            self._test_sort_algorithm(heap_sort)
        
        def test_heap_sort_reversed(self):
            """Test heap sort with a reversed array."""
            self._test_sort_algorithm(heap_sort, list(range(100, 0, -1)))


if __name__ == "__main__":
    unittest.main()