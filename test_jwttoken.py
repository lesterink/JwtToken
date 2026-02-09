# test_jwttoken.py
"""
Tests for JwtToken module.
"""

import unittest
from jwttoken import JwtToken

class TestJwtToken(unittest.TestCase):
    """Test cases for JwtToken class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JwtToken()
        self.assertIsInstance(instance, JwtToken)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JwtToken()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
