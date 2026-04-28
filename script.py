from playwright.sync_api import expect

def test_login(page):

    # Open URL with Basic Auth
    page.context.set_http_credentials({
        "username": "Admin",
        "password": "Password123"
    })

    page.goto("http://iash-app-dev.spurtreetech.com:8080/")

    # Login
    page.wait_for_selector("text=Sign in to Sprint", timeout=15000)
    print("✅ Basic Auth handled")

    page.get_by_role("button", name="Sign in to Sprint").click()

    # Companies
    page.locator("span:has-text('Companies')").first.click()
    print("✅ Clicked Companies")

    COMPANY_NAME = "1210 Investments L.P."

    # Search
    search_box = page.locator("input[placeholder='Company Name']:visible").first
    search_box.wait_for()
    search_box.fill(COMPANY_NAME)

    page.wait_for_selector("mat-option")
    page.locator("mat-option", has_text=COMPANY_NAME).first.click()

    print(f"✅ Selected company: {COMPANY_NAME}")

    # Tabs
    page.wait_for_selector(".mat-tab-group")

    # Bank Details
    page.get_by_role("tab", name="Bank Details").click()

    active_tab = page.locator(".mat-tab-body-active")
    active_tab.wait_for()

    page.wait_for_timeout(2000)

    rows = active_tab.locator(".mat-row").count()
    print("Rows:", rows)

    if rows == 0:
        if active_tab.locator("text=No Data").is_visible():
            raise Exception("❌ No bank data available")
        else:
            raise Exception("❌ Bank tab not loaded")

    # Delete
    delete_btn = active_tab.locator("//span[@title='delete']").first
    expect(delete_btn).to_be_visible()
    delete_btn.click()

    print("✅ Delete clicked")