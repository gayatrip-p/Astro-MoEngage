from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Launch the browser in headed mode to see the actions visually
    # Added slow_mo=1000 to slow down actions by 1 second each
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the target application
    page.goto("http://localhost:5173/")

    # 1. Click on "Custom Segments"
    page.get_by_text("Custom Segments", exact=True).first.click()

    # 2. Click on "New Custom Segment"
    page.get_by_role("button", name="New Custom Segment").click()

    # 3. Enter the Custom segment name as "TestSegment Datetime start time"
    # Assuming there's a text input for the name. We use get_by_role("textbox")
    # as a generic locator. If there are multiple textboxes, you might need to use
    # page.get_by_placeholder("Segment Name") or a specific selector.
    name_input = page.get_by_role("textbox").first
    from datetime import datetime

    segment_name = "TestSegment_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    name_input.fill(segment_name)
    print("Created Segment:", segment_name)

    # 4. Click on "Create"
    page.get_by_role("button", name="Create").click()

    # 5. Click on "Add Group"
    # The '+ ' is an SVG, so the text is just "Add Group"
    page.wait_for_selector("text=Add Group")
    page.get_by_role("button", name="Add Group").first.click()

    # Wait a bit for the next section to appear
    page.wait_for_selector("text=Add Segment", timeout=5000)

    # 6. Click on "Add Segment"
    page.get_by_role("button", name="Add Segment").first.click()

    # 7. Select Workspace A
    # Based on the UI, selecting SELECT A WORKSPACE opens the dropdown to pick Workspace A
    page.wait_for_selector("text=SELECT A WORKSPACE")
    page.get_by_text("SELECT A WORKSPACE").first.click()
    page.get_by_text("Workspace A").first.click()

    # 8. Add the specific race segments
    # Wait for the lists to populate or become visible
    page.wait_for_selector("text=Race_Chinese")
    page.get_by_text("Race_Chinese").first.click()

    # Wait a bit for the next section to appear
    page.wait_for_selector("text=Add Segment", timeout=5000)

    # 6. Click on "Add Segment"
    page.get_by_role("button", name="Add Segment").first.click()

    # 7. Select Workspace A
    # The text is "SELECT A WORKSPACE" meaning "select *any* workspace", not "Workspace A"
    page.wait_for_selector("text=SELECT A WORKSPACE")
    page.get_by_text("SELECT A WORKSPACE").first.click()
    page.get_by_text("Workspace B").first.click()

    # 8. Add the specific race segments
    # Wait for the lists to populate or become visible

    page.wait_for_selector("text=Life_Stage_Early_Family")
    page.get_by_text("Life_Stage_Early_Family").first.click()

    # --- NEW GROUP ---
    # 9. Click on Add Group to make the second group
    page.wait_for_selector("text=Add Group")
    page.get_by_role("button", name="Add Group").click()

    # 10. Click on the AND operator
    page.wait_for_selector("text=AND")
    # Using exact match since 'AND' is a very generic word
    page.get_by_text("AND", exact=True).first.click()

    # 11. Add Race_Chinese to the second group
    page.wait_for_selector("text=Add Segment", timeout=5000)
    # Target the last Add Segment button (the one inside our newly created group)
    page.get_by_role("button", name="Add Segment").last.click(force=True)

    page.locator("button", has_text="Workspace A").click()

    page.get_by_role("button", name="Race_Chinese").click()

    # 12. Add Life_Stage_Young_Professional to the second group
    page.wait_for_selector("text=Add Segment")
    page.get_by_role("button", name="Add Segment").last.click(force=True)

    page.get_by_role("button", name="Workspace B").click()

    page.get_by_role("button", name="Life_Stage_Young_Professional").click()

    page.get_by_role("button", name="Add Filter Section (Optional)").click()
    page.get_by_role("button", name="Add Group").nth(1).click()
    add_segment_btn = page.get_by_role("button", name="Add Segment").last
    add_segment_btn.click()
    page.get_by_role("button", name="Workspace C").click()
    page.get_by_role("button", name="Income_High").click()
    page.get_by_role("button", name="Save Version").click()
    page.get_by_role("button", name="Activate").click()

    # # Wait for a few seconds to visually confirm the action before closing
    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
