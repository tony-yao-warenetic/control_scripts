import requests
import time
import cv2
import numpy as np
import base64

server_url = "https://no-more-waiting-4-lunch-atest20061206.replit.app/get_img/"

test_url = "https://80755081-e125-4a75-b806-06998c36e03c-00-s7c32woc0kef.worf.replit.dev/get_img/"

def fetch_image_from_server(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "image" not in data:
            print("No image field in response.")
            return None

        image_data = base64.b64decode(data["image"])
        np_arr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        return image
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except Exception as e:
        print("Unexpected error:", e)
    return None

def main():
    while True:
        image = fetch_image_from_server(str(server_url+"1"))
        image2 = fetch_image_from_server(str(server_url+"2"))
        image3 = fetch_image_from_server(str(server_url+"3"))
        image4 = fetch_image_from_server(str(server_url+"4"))
        image5 = fetch_image_from_server(str(server_url+"5"))
        if image is not None:
            cv2.imshow("Image Feed", image)
            cv2.imshow("Image Feed 2", image2)
            cv2.imshow("Image Feed 3", image3)
            cv2.imshow("Image Feed 4", image4)
            print("Refreshed")
        else:
            print("Failed to load image.")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(2)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
