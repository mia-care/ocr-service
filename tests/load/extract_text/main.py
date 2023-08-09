from locust import HttpUser, task, between


class User(HttpUser):
    """
    TODO
    """
    wait_time = between(1, 1.5)

    @task
    def extract_text_from_hello_world_sample(self):
        sample1 = open('assets/images/ocr-hello-world-sample.png', 'rb')
        files = {
            'file': ('ocr-hello-world-sample.png', sample1, 'image/png')
        }

        with self.client.post(
            "/extract-text",
            files=files,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Wrong statusCode")

    @task
    def extract_text_from_multilingual_sample(self):
        sample1 = open('assets/images/ocr-multilingual-sample.png', 'rb')
        files = {
            'file': ('ocr-multilingual-sample.png', sample1, 'image/png')
        }

        with self.client.post(
            "/extract-text",
            files=files,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Wrong statusCode")

    @task
    def extract_text_from_sales_quote_sample(self):
        sample1 = open('assets/images/ocr-sales-quote-sample.png', 'rb')
        files = {
            'file': ('ocr-sales-quote-sample.png', sample1, 'image/png')
        }

        with self.client.post(
            "/extract-text",
            files=files,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Wrong statusCode")
