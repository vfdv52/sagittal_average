import numpy as np

from sagittal_brain.sagittal_brain import run_averages


def test_run_averages(tmp_path):
    """
    Test that run_averages correctly calculates row averages.
    Uses tmp_path fixture to avoid interfering with the repository.
    """
    # 1. Create input dataset
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1  # Last row is all ones

    # 2. Save it into a file in temporary directory
    file_input = tmp_path / "brain_sample.csv"
    np.savetxt(file_input, data_input, fmt="%d", delimiter=",")

    # 3. Create expected result
    # The expected result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    # 4. Call the function with the files
    file_output = tmp_path / "brain_average.csv"
    run_averages(file_input=str(file_input), file_output=str(file_output))

    # 5. Load the result
    result = np.loadtxt(file_output, delimiter=",")

    # 6. Compare the result with the expected values
    np.testing.assert_array_equal(result, expected)


def test_run_averages_all_ones(tmp_path):
    """
    Additional test: if all values are 1, all averages should be 1.
    """
    # Create input dataset with all ones
    data_input = np.ones((10, 10))

    # Save to temporary file
    file_input = tmp_path / "brain_ones.csv"
    np.savetxt(file_input, data_input, fmt="%d", delimiter=",")

    # Expected: all averages should be 1
    expected = np.ones(10)

    # Run function
    file_output = tmp_path / "brain_ones_average.csv"
    run_averages(file_input=str(file_input), file_output=str(file_output))

    # Load and compare
    result = np.loadtxt(file_output, delimiter=",")
    np.testing.assert_array_equal(result, expected)
