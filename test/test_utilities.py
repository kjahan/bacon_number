import sys
import os
import json
import pytest

path = os.getcwd()

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, os.path.join(path, "src"))

from utilities import cleanup_json

def test_clean_json():
    dirty_json_1 = "[{'cast_id': 14, 'character': 'Woody (voice)', 'credit_id': '52fe4284c3a36847f8024f95', 'gender': 2, 'id': 31, 'name': 'Tom Hanks', 'order': 0, 'profile_path': '/pQFoyx7rp09CJTAb932F2g8Nlho.jpg'}]"
    clean_json_1 = cleanup_json(dirty_json_1)
    try:
        data_1 = json.loads(clean_json_1)
    except json.JSONDecodeError:
        pytest.fail("Unexpected JSONDecodeError on the first dirty json.")
    dirty_json_2 = "[{'cast_id': 15, 'character': 'Buzz Lightyear (voice)', 'credit_id': '52fe4284c3a36847f8024f99', 'gender': 2, 'id': 12898, 'name': 'Tim Allen', 'order': 1, 'profile_path': None}]"
    clean_json_2 = cleanup_json(dirty_json_2)
    try:
        data_2 = json.loads(clean_json_2)
    except json.JSONDecodeError:
        pytest.fail("Unexpected JSONDecodeError on the second dirty string.")