# **Receipt Processor API**  

A FastAPI-based web service for processing receipts and calculating points based on predefined rules.

---

## **Setting Up the Project Locally**  

### **1️. Clone the Repository**  
```sh
git clone <your-github-repo-url>
```

### **2. Navigate into the Project Directory**  
```sh
cd receipt_processor
```

### **3. Create a Virtual Environment**  
```sh
python -m venv venv
```

### **4️. Activate the Virtual Environment**  
#### **For Windows (CMD)**
```sh
venv\Scripts\activate
```

### **5️. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **6️. Run the FastAPI Server**  
```sh
uvicorn app.main:app --reload
```

### **7️. Open the API in a Browser**  
Once the server starts, open:  
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**  
> **Note:** This URL serves as the base for the API but does not display any content directly. If you open it in a browser, you will see a message:  
> ```json
> {"detail":"Not Found"}
> ```
> This is expected, as the API does not have a default home route. To interact with the API, see point 8 or send requests using tools like **Postman** or `curl`.

### **8️. Open Swagger UI for API Documentation**  
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  
You can interact with the API and test endpoints on this url.

---

## **API Endpoints**  

### **1️. Process a Receipt**  
- **Endpoint:** `POST /receipts/process`  
- **Description:** Submits a receipt for processing and returns a unique receipt ID.  
- **Example Request:**
```json
{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
        {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
        {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
    ],
    "total": "35.35"
}
```
- **Example Response:**
```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```

---

### **2️. Get Points for a Receipt**  
- **Endpoint:** `GET /receipts/{id}/points`  
- **Description:** Retrieves the points awarded for a submitted receipt.  
- **Example Request:**  
```sh
GET http://127.0.0.1:8000/receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points
```
- **Example Response:**
```json
{
  "points": 32
}
```

---

### **3️. (Optional) Retrieve All Stored Receipts**  
> This endpoint is for **debugging purposes only**.
- **Endpoint:** `GET /receipts`
- **Description:** Returns all stored receipts along with their calculated points. You can use this endpoint by uncommenting the 
/receipts API endpoint in app/routes.py file.

---

## **Walkthrough: Using Swagger UI to Test the API**  

**Swagger UI** provides an interactive way to test your API **without needing external tools** like Postman. This guide walks you through how to use Swagger UI to send requests and see responses.  

---

### **1. Open Swagger UI**  

Once your FastAPI server is running (`uvicorn app.main:app --reload`), open:  
- **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  

You should see a **list of API endpoints**, each with an **"Try it out"** button.
![image](https://github.com/user-attachments/assets/1d54b4c8-ba92-4ca8-b6ff-882f02ee6ab8)
![image](https://github.com/user-attachments/assets/519657b1-0372-4214-99cd-6ef658e3019d)

---

### **2. Submit a Receipt (`POST /receipts/process`)**  

1️) Scroll down to the **`POST /receipts/process`** section.  
2️) Click on **"Try it out"** (top right of the section).  
3️) You will see an editable **JSON input box**.  
4️) Replace the default JSON with a **sample receipt**:  

```json
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```

![image](https://github.com/user-attachments/assets/0a4f1d2e-69ad-44eb-818a-24b5a1b31358)

5️) Click **"Execute"**.  
6️) In the response section, you will see a **generated receipt ID**:  

```json
{
  "id": "db31755f-fbe8-4ba7-87f0-86af6d6b2657"
}
```

> **Note:**: Save the **ID**, as you’ll need it for the next step.

![image](https://github.com/user-attachments/assets/deb01a52-2064-4c74-b334-db8aee5b862e)

---

### **3. Retrieve Points (`GET /receipts/{id}/points`)**  

1️) Scroll to **`GET /receipts/{id}/points`**.  
2️) Click **"Try it out"**.  
3️) In the **`id` field**, enter the ID you received from the previous step (`7fb1377b-b223-49d9-a31a-5a02701dd310`).  
4️) Click **"Execute"**.  
5️) The API will return the **points** for that receipt:  

```json
{
  "points": 109
}
```
![image](https://github.com/user-attachments/assets/e29758a1-9541-414d-bfe8-ab60119c83da)

---

### **4. (Optional) Retrieve All Stored Receipts (`GET /receipts`)**  

> **Note:** This endpoint is for debugging purposes only.

1️) Scroll to **`GET /receipts`**  
2️) Click **"Try it out"** → **"Execute"**.  
3️) You will see a response containing all receipts stored in memory:

```json
{
  "7fb1377b-b223-49d9-a31a-5a02701dd310": {
    "receipt": {
      "retailer": "Target",
      "purchaseDate": "2022-01-01",
      "purchaseTime": "13:01",
      "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"}
      ],
      "total": "9.84"
    }
  }
}
```
![image](https://github.com/user-attachments/assets/00abd1a5-7a2c-4bb2-9c98-fce9c7af0cd6)

---

## **5. Handling Errors in Swagger UI**

### **1. Missing or Incorrect Field Types (400 Bad Request)**
- **Missing Required Field:**  
  If you forget to include a required field (for example, omitting `retailer`), the API will respond with:
  ```json
  {
    "detail": "The receipt is invalid."
  }
  ```
  🔹 **Fix:** Ensure all required fields (`retailer`, `purchaseDate`, `purchaseTime`, `items`, and `total`) are provided.

- **Incorrect Field Type:**  
  If a field is provided but its type does not match the expected format (for example, passing a number instead of a string for `total`), the API will also respond with:
  ```json
  {
    "detail": "The receipt is invalid."
  }
  ```
  🔹 **Fix:** Double-check that each field uses the correct type (e.g., `total` must be a string matching the pattern `^\d+\.\d{2}$`).

### **2. Invalid JSON Input (422 Unprocessable Entity)**
- If the JSON input itself is malformed or not valid JSON (for example, missing quotes around string values), FastAPI will automatically throw a 422 error with details on the JSON decoding error.
  ```json
  {
    "detail": [
      {
        "loc": ["body"],
        "msg": "Expecting value: line 1 column 1 (char 0)",
        "type": "value_error.jsondecode"
      }
    ]
  }
  ```
  🔹 **Fix:** Ensure your request body is valid JSON. For example, string values must be enclosed in double quotes.

---

### **3. Invalid Receipt ID (404 Not Found)**  
- If you enter an **invalid** receipt ID in `GET /receipts/{id}/points`, you'll see:

```json
{
  "detail": "No receipt found for that ID."
}
```
🔹 **Fix:** Use the correct **receipt ID** from `POST /receipts/process`.

--- 
## **Running Tests**  

### **1️. Run All Tests**
```sh
pytest tests/
```

### **2️. Run Tests with Detailed Output**
```sh
pytest -v
```

---

## **Additional Notes**
- The application **stores data in memory**, meaning all receipts will be lost when the server restarts.
- This project uses **Swagger UI** to interact with the API without needing external tools like Postman.

---
