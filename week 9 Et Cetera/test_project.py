from project import add_item, update_item, delete_item, mark_done, mark_undone, display_checklist, display_done_items, display_undone_items




def test_add_item():
     assert add_item("laundry") == None


def test_update_item():
     assert update_item(1,"laundry") == None


def test_delete_item():
     assert delete_item(1) == None


def test_mark_done():
     assert mark_done(1) == None


def test_mark_done():
     assert mark_undone(1) == None


def test_display_checklist():
     assert display_checklist() == None


def test_display_done_items():
     assert display_done_items() == None


def test_display_undone_items():
     assert display_undone_items() == None