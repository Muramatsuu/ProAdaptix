# test_proadaptix.py
"""
Tests for ProAdaptix module.
"""

import unittest
from proadaptix import ProAdaptix

class TestProAdaptix(unittest.TestCase):
    """Test cases for ProAdaptix class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProAdaptix()
        self.assertIsInstance(instance, ProAdaptix)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProAdaptix()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
