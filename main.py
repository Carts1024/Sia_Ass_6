import unittest

def main():
    suite = unittest.TestLoader().discover('.', pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print("\nSummary Report:")
    print(f"Total tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    if result.failures or result.errors:
        print("\nDetails:")
        for failure in result.failures:
            print(failure[1])
        for error in result.errors:
            print(error[1])
    else:
        print("All tests passed successfully!")

if __name__ == "__main__":
    main()
