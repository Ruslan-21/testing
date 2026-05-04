from shooters_qa_test.pages.main_page import MainPage



def test_filter_affects_api_request(browser_page):
   filter_api = MainPage(browser_page)

   filter_api.login()

   response = filter_api.filter_affect_request()

   print("STATUS:", response.status)
   print("URL:", response.url)
   print("BODY:", response.text())