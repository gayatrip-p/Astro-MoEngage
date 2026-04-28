import pytest

@pytest.fixture(scope="function", autouse=True)
def take_screenshot_on_failure(page, request):
    yield
    if request.node.rep_call.failed:
        screenshot_path = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

@pytest.fixture
def context_args(context_args):
    # Add HTTP credentials for the context
    return {
        **context_args,
        "http_credentials": {
            "username": "Admin",
            "password": "Password123"
        }
    }
