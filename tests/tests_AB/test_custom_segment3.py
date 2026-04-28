def test_create_custom_segment(page):
    from pages.custom_segment_page import CustomSegmentPage

    page.set_default_timeout(10000)

    segment_page = CustomSegmentPage(page)

    segment_page.navigate()
    segment_page.click_custom_segments()
    segment_page.click_new_custom_segment()

    name = segment_page.enter_segment_name()
    print("Created Segment:", name)

    segment_page.click_create()

    # -------- Group 1 --------
    segment_page.add_group()
    segment_page.add_segment("Workspace A", "Race_Indian")
    segment_page.add_segment("Workspace B", "Life_Stage_Young_Professional")

    # -------- Group 2 --------
    segment_page.add_group()
    segment_page.click_and()
    segment_page.add_segment("Workspace A", "Race_Indian")
    segment_page.add_segment("Workspace B", "Life_Stage_Early_Family")

    # -------- Group 3 --------
    segment_page.add_group()
    segment_page.click_and()
    segment_page.add_segment("Workspace A", "Race_Indian")
    segment_page.add_segment("Workspace B", "Life_Stage_Established_Family")

    # -------- Group 4 --------
    segment_page.add_group()
    segment_page.click_and()
    segment_page.add_segment("Workspace A", "Race_Indian")
    segment_page.add_segment("Workspace B", "Life_Stage_Empty_Nester")

    # -------- Filter Section --------
    segment_page.add_filter_section()
    segment_page.add_group_to_filter()
    segment_page.add_segment("Workspace E", "Premium_Subscribers")

    segment_page.save_version()
    segment_page.activate_segment()
