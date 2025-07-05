import unittest

# Discover and run all tests in the current directory
if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir=".", pattern="test*.py")

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
