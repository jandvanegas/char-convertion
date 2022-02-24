# Challenge Solution

## Description

Create a REST API with one endpoint /convert expecting a JSON body containing a:
* List of ASCII characters (any ASCII alphabet character).
* Use **pandas** and/or **numpy** to convert and return a JSON response
  containing a list of integers based on the provided list of characters.
* For each ASCII alphabet character below H or h, the corresponding integer
  should be the character ASCII code multiplied by 10, otherwise it should
  be 0.
* The project does not need to contain the whole setup to make it
  deployable. However, in addition to the code of the application, it
  should contain a **test suite** ensuring that those specifications are
  matched.

## Sample

Below is a sample API request with the expected response (HTTP 200):

Request:
POST /convert
```json
["A", "h", "H", "x"]
```

Response body:
```json
[650, 0, 0, 0]
```
