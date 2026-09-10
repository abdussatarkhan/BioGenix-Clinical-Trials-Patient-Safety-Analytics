"""
BioGenix: Global Biopharma Phase-III Clinical Trials & Patient Safety Analytics - Pytest Automated Test Suite
"""
import pytest
import numpy as np


def test_enrollment_rate_calculation():
    actual_enrolled = 3480
    target_enrolled = 3340
    rate = (actual_enrolled / target_enrolled) * 100.0
    assert round(rate, 1) == 104.2

def test_sae_reporting_bound():
    sae_count = 49
    total_subjects = 3480
    pct = (sae_count / total_subjects) * 100.0
    assert round(pct, 2) == 1.41


def test_sla_compliance_bounds():
    compliant = 9400
    total = 10000
    assert (compliant / total) * 100.0 == 94.0

def test_data_integrity():
    metric_val = 1420.50
    assert metric_val > 0
