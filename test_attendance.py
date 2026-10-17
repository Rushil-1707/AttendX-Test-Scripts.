
def mark_attendance(student_id, present):
    if not student_id:
        return "Invalid Student ID"
    if present:
        return "Attendance Marked"
    return "Attendance Not Marked"


def test_mark_present():
    assert mark_attendance("ST101", True) == "Attendance Marked"


def test_mark_absent():
    assert mark_attendance("ST101", False) == "Attendance Not Marked"


def test_empty_student_id():
    assert mark_attendance("", True) == "Invalid Student ID"
