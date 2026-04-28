from datetime import datetime

class CustomSegmentPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("http://localhost:5173/")

    def click_custom_segments(self):
        self.page.get_by_text("Custom Segments", exact=True).click()

    def click_new_custom_segment(self):
        self.page.get_by_role("button", name="New Custom Segment").click()

    def enter_segment_name(self):
        segment_name = "TestSegment_" + datetime.now().strftime("%Y%m%d_%I%M%S")
        self.page.get_by_role("textbox").first.fill(segment_name)
        print("Segment Name:", segment_name)
        return segment_name

    def click_create(self):
        self.page.get_by_role("button", name="Create").click()

    def add_group(self):
        """Add a group to the main section (before filter section)"""
        self.page.get_by_role("button", name="Add Group").first.click()

    def add_group_to_filter(self):
        """Add a group to the filter section (after filter section is created)"""
        self.page.get_by_role("button", name="Add Group").nth(1).click()

    def add_segment(self, workspace, segment):
        """Add a segment with specified workspace and segment name"""
        self.page.get_by_role("button", name="Add Segment").last.click()
        self.page.get_by_role("button", name=workspace).click()
        self.page.get_by_role("button", name=segment).click()

    def click_and(self):
        """Click the AND operator to connect groups"""
        self.page.wait_for_selector("text=AND")
        self.page.get_by_text("AND", exact=True).first.click()

    def add_filter_section(self):
        """Add a filter section (optional) to the segment"""
        self.page.get_by_role("button", name="Add Filter Section (Optional)").click()



    def save_version(self):
        """Save the segment version"""
        self.page.get_by_role("button", name="Save Version").click()

    def activate_segment(self):
        """Activate the segment"""
        self.page.get_by_role("button", name="Activate").click()






