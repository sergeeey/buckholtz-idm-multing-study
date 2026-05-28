"""
Test Table A1 extraction validation.

Purpose: Validate that manually extracted Table A1 CSV meets quality requirements.

IMPORTANT: These tests will FAIL until user manually transcribes Table A1.
This is expected — tests are templates for post-extraction validation.
"""

import csv
from pathlib import Path

import pytest

# Path to extracted CSV
TABLE_A1_PATH = Path(__file__).parent.parent / "data" / "table_a1_raw.csv"


def is_comment_or_empty(row: list[str]) -> bool:
    """Check if row is a comment (starts with #) or empty."""
    return not row or (row[0].startswith("#") if row else False)


def read_table_a1() -> tuple[list[str], list[list[str]]]:
    """
    Read Table A1 CSV, skipping comments and empty lines.

    Returns:
        (headers, data_rows)
    """
    if not TABLE_A1_PATH.exists():
        pytest.skip(f"Table A1 CSV not found: {TABLE_A1_PATH}")

    with open(TABLE_A1_PATH, encoding="utf-8") as f:
        reader = csv.reader(f)
        all_rows = list(reader)

    # Skip comments and empty lines
    non_comment_rows = [row for row in all_rows if not is_comment_or_empty(row)]

    if len(non_comment_rows) == 0:
        pytest.skip(
            "Table A1 CSV contains only comments/empty lines (awaiting manual transcription)"
        )

    headers = non_comment_rows[0]
    data_rows = non_comment_rows[1:]

    if len(data_rows) == 0:
        pytest.skip("Table A1 CSV contains only headers (awaiting manual transcription)")

    return headers, data_rows


def test_table_a1_file_exists():
    """Table A1 CSV file must exist."""
    assert TABLE_A1_PATH.exists(), (
        f"Table A1 CSV not found: {TABLE_A1_PATH}. "
        "Create file by manually transcribing manuscript Table A1."
    )


def test_table_a1_has_headers():
    """Table A1 CSV must have header row."""
    headers, _ = read_table_a1()

    assert len(headers) > 0, "Table A1 CSV must have at least one column"
    assert len(headers) >= 8, (
        f"Table A1 CSV must have at least 8 columns (got {len(headers)}). "
        "Expected: row_id, z, time, H_obs, H_obs_unc, H_FLRW, H_MULT, sigma_MULT"
    )


def test_table_a1_has_data():
    """Table A1 CSV must have at least one data row."""
    _, data_rows = read_table_a1()

    assert len(data_rows) > 0, (
        "Table A1 CSV must have at least one data row. "
        "Manually transcribe data from manuscript Table A1."
    )


def test_table_a1_column_consistency():
    """All rows must have same number of columns as header."""
    headers, data_rows = read_table_a1()

    num_cols_expected = len(headers)

    for i, row in enumerate(data_rows, start=2):  # Start=2 because row 1 is headers
        assert len(row) == num_cols_expected, (
            f"Row {i} has {len(row)} columns, expected {num_cols_expected}. "
            f"Check for missing commas or extra commas in CSV."
        )


def test_table_a1_required_columns():
    """Table A1 must contain expected column names (exact or provisional)."""
    headers, _ = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    # Required columns (flexible matching)
    required_keywords = {
        "z": ["z", "redshift"],
        "time": ["time", "gyr", "age"],
        "H_FLRW": ["h_flrw", "flrw", "lambda", "lcdm"],
        "H_MULT": ["h_mult", "mult", "multing", "idm"],
        "sigma": ["sigma", "deviation", "error"],
    }

    missing_columns = []
    for col_name, keywords in required_keywords.items():
        found = any(any(kw in h for kw in keywords) for h in headers_lower)
        if not found:
            missing_columns.append(col_name)

    assert len(missing_columns) == 0, (
        f"Table A1 CSV missing required columns: {missing_columns}. "
        f"Current headers: {headers}. "
        "Ensure CSV contains z, time, H_FLRW, H_MULT, sigma_MULT columns."
    )


def test_table_a1_numeric_columns_parse():
    """Numeric columns (z, H_FLRW, H_MULT) must parse as float or NA."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    # Identify numeric column indices (heuristic: z, H_*, sigma_*, time)
    numeric_keywords = ["z", "h_", "sigma", "time", "gyr"]
    numeric_col_indices = [
        i for i, h in enumerate(headers_lower) if any(kw in h for kw in numeric_keywords)
    ]

    if len(numeric_col_indices) == 0:
        pytest.skip("No numeric columns identified (check column names)")

    parse_errors = []

    for row_idx, row in enumerate(data_rows, start=2):
        for col_idx in numeric_col_indices:
            if col_idx >= len(row):
                continue  # Column missing in this row (handled by column_consistency test)

            value = row[col_idx].strip()

            # Allow NA, empty, or valid float
            if value in ("", "NA", "N/A", "nan"):
                continue

            try:
                float(value)
            except ValueError:
                parse_errors.append(
                    f"Row {row_idx}, column {headers[col_idx]}: '{value}' not a valid number"
                )

    assert len(parse_errors) == 0, (
        "Numeric parsing errors found:\n"
        + "\n".join(parse_errors[:5])  # Show first 5
        + (f"\n... and {len(parse_errors) - 5} more" if len(parse_errors) > 5 else "")
    )


def test_table_a1_z_values_monotonic():
    """z (redshift) values should be monotonic (increasing or decreasing)."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    # Find z column index
    z_col_idx = None
    for i, h in enumerate(headers_lower):
        if "z" in h and "redshift" not in h:  # Match "z" but not "redshift z"
            z_col_idx = i
            break

    if z_col_idx is None:
        pytest.skip("z column not identified (check column names)")

    z_values = []
    for row in data_rows:
        if z_col_idx >= len(row):
            continue

        value = row[z_col_idx].strip()
        if value in ("", "NA", "N/A", "nan"):
            continue

        try:
            z_values.append(float(value))
        except ValueError:
            continue  # Handled by numeric_columns_parse test

    if len(z_values) < 2:
        pytest.skip("Not enough valid z values to check monotonicity")

    # Check monotonicity (either increasing or decreasing)
    is_increasing = all(z_values[i] <= z_values[i + 1] for i in range(len(z_values) - 1))
    is_decreasing = all(z_values[i] >= z_values[i + 1] for i in range(len(z_values) - 1))

    assert is_increasing or is_decreasing, (
        f"z values are not monotonic. "
        f"First few z values: {z_values[:10]}. "
        "Check for data entry errors or duplicate rows."
    )


def test_table_a1_z_range_cosmological():
    """z values should be within cosmological range (0 <= z <= ~10)."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    z_col_idx = None
    for i, h in enumerate(headers_lower):
        if "z" in h and "redshift" not in h:
            z_col_idx = i
            break

    if z_col_idx is None:
        pytest.skip("z column not identified")

    out_of_range = []

    for row_idx, row in enumerate(data_rows, start=2):
        if z_col_idx >= len(row):
            continue

        value = row[z_col_idx].strip()
        if value in ("", "NA", "N/A", "nan"):
            continue

        try:
            z = float(value)
        except ValueError:
            continue

        if z < 0 or z > 10:  # Cosmological range: 0 <= z <= ~10
            out_of_range.append(f"Row {row_idx}: z={z}")

    assert len(out_of_range) == 0, (
        "z values out of cosmological range (0 <= z <= 10):\n" + "\n".join(out_of_range[:5])
    )


def test_table_a1_time_range_physical():
    """Time after Big Bang should be 0 < t < 13.8 Gyr (age of universe)."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    time_col_idx = None
    for i, h in enumerate(headers_lower):
        if "time" in h or "gyr" in h or "age" in h:
            time_col_idx = i
            break

    if time_col_idx is None:
        pytest.skip("time column not identified")

    out_of_range = []

    for row_idx, row in enumerate(data_rows, start=2):
        if time_col_idx >= len(row):
            continue

        value = row[time_col_idx].strip()
        if value in ("", "NA", "N/A", "nan"):
            continue

        try:
            t = float(value)
        except ValueError:
            continue

        if t <= 0 or t > 13.8:  # Age of universe: 0 < t < 13.8 Gyr
            out_of_range.append(f"Row {row_idx}: time={t} Gyr")

    assert len(out_of_range) == 0, (
        "Time values out of physical range (0 < t < 13.8 Gyr):\n" + "\n".join(out_of_range[:5])
    )


def test_table_a1_H_values_positive():
    """Hubble parameter values (H_FLRW, H_MULT) must be positive."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    # Find H_* column indices
    h_col_indices = [i for i, h in enumerate(headers_lower) if "h_" in h or h.startswith("h")]

    if len(h_col_indices) == 0:
        pytest.skip("No H_* columns identified")

    negative_values = []

    for row_idx, row in enumerate(data_rows, start=2):
        for col_idx in h_col_indices:
            if col_idx >= len(row):
                continue

            value = row[col_idx].strip()
            if value in ("", "NA", "N/A", "nan"):
                continue

            try:
                h = float(value)
            except ValueError:
                continue

            if h <= 0:
                negative_values.append(
                    f"Row {row_idx}, column {headers[col_idx]}: H={h} (must be > 0)"
                )

    assert len(negative_values) == 0, (
        "Negative or zero Hubble parameter values found:\n" + "\n".join(negative_values[:5])
    )


def test_table_a1_sigma_nonnegative():
    """sigma_MULT values must be non-negative (deviation metric)."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    sigma_col_idx = None
    for i, h in enumerate(headers_lower):
        if "sigma" in h:
            sigma_col_idx = i
            break

    if sigma_col_idx is None:
        pytest.skip("sigma column not identified")

    negative_values = []

    for row_idx, row in enumerate(data_rows, start=2):
        if sigma_col_idx >= len(row):
            continue

        value = row[sigma_col_idx].strip()
        if value in ("", "NA", "N/A", "nan"):
            continue

        try:
            sigma = float(value)
        except ValueError:
            continue

        if sigma < 0:
            negative_values.append(f"Row {row_idx}: sigma_MULT={sigma} (must be >= 0)")

    assert len(negative_values) == 0, "Negative sigma_MULT values found:\n" + "\n".join(
        negative_values[:5]
    )


def test_table_a1_no_duplicate_z_values():
    """z values should be unique (no duplicate redshifts)."""
    headers, data_rows = read_table_a1()

    headers_lower = [h.lower().strip() for h in headers]

    z_col_idx = None
    for i, h in enumerate(headers_lower):
        if "z" in h and "redshift" not in h:
            z_col_idx = i
            break

    if z_col_idx is None:
        pytest.skip("z column not identified")

    z_values = []
    for row in data_rows:
        if z_col_idx >= len(row):
            continue

        value = row[z_col_idx].strip()
        if value in ("", "NA", "N/A", "nan"):
            continue

        try:
            z_values.append(float(value))
        except ValueError:
            continue

    duplicates = [z for z in set(z_values) if z_values.count(z) > 1]

    assert len(duplicates) == 0, (
        f"Duplicate z values found: {duplicates}. "
        "Check for data entry errors or intentional duplicate rows."
    )


def test_table_a1_row_count_reasonable():
    """Table A1 should have a reasonable number of rows (5-100 typical for cosmology H(z) tables)."""
    _, data_rows = read_table_a1()

    row_count = len(data_rows)

    assert 1 <= row_count <= 200, (
        f"Table A1 has {row_count} data rows. "
        "Expected: 5-100 for typical cosmology H(z) table. "
        "If correct, update test threshold. If not, check transcription."
    )


def test_table_a1_beta_values_present():
    """Verify beta_d=4.5 and beta_q=18.0 are referenced in context (not necessarily in table rows)."""
    # This test checks the extraction log, not the CSV itself
    log_path = TABLE_A1_PATH.parent / "table_a1_extraction_log.md"

    if not log_path.exists():
        pytest.skip("Extraction log not found")

    with open(log_path, encoding="utf-8") as f:
        log_content = f.read()

    assert (
        "beta_d = 4.5" in log_content or "beta_d=4.5" in log_content
    ), "Extraction log must document beta_d=4.5 from manuscript context"

    assert (
        "beta_q = 18.0" in log_content or "beta_q=18.0" in log_content
    ), "Extraction log must document beta_q=18.0 from manuscript context"
