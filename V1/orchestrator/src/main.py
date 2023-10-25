import httpx
import asyncio


async def send_file(url, file):
    async with httpx.AsyncClient() as client:
        try:
            # Send a GET request to the API endpoint
            response = await client.post(url=url, files=file)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse and work with the API response data
                data = response.json()
                return data

            # Handle errors or non-200 status codes here
            print(f"Request failed with status code {response.status_code}")
            return None

        except httpx.RequestError as e:
            # Handle request errors (e.g., connection issues)
            print(f"Request error: {e}")
            return None
        except httpx.HTTPStatusError as e:
            # Handle unexpected HTTP status codes
            print(f"HTTP status error: {e}")
            return None


def retrieve_data(file_name, file_path):
    # This function retrieves data from the common storage location

    return {"file": (file_name, open(file_path, "rb"))}


if __name__ == "__main__":
    # Retrieve data once for the purpose of the demonstration
    file_name = "sample.zip"
    file_path = "../data/{}".format(file_name)
    file = retrieve_data(file_name, file_path)

    # Run the pipeline
    endpoints = [
        "8080/unzip/",
        "8081/convert/",
        "8082/split/",
        "8083/transform/",
        "8084/arango/",
    ]

    for endpoint in endpoints:
        # Contact the service
        response = asyncio.run(send_file("http://0.0.0.0:{}".format(endpoint), file))

        if response["response"] == "ok":
            print(
                "Service {} succeeded ... Continuing pipeline ...".format(
                    endpoint.split("/")[1]
                )
            )
            continue
        else:
            # Handle errors or failures here
            print(
                "Service {} failed its execution ... Aborting pipeline ...".format(
                    endpoint.split("/")[1]
                )
            )
            break

    print("Pipeline execution succeeded!")
